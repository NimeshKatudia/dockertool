from flask import Flask, render_template, jsonify
import docker
import json
import os
import threading
import time

app = Flask(__name__)
client = docker.from_env()

stats_lock = threading.Lock()
container_stats = {}

@app.route('/')
def index():
    return render_template('container_stats.html')

@app.route('/stats')
def get_stats():
    update_container_stats()
    return jsonify(container_stats)

def get_container_stats():
    containers = client.containers.list()
    stats = {}

    for container in containers:
        container_stats = container.stats(stream=False)
        container_id = container_stats['id']

        cpu_stats = container_stats['cpu_stats']
        percpu_usage = cpu_stats['cpu_usage']['percpu_usage']

        # Detailed CPU stats per process
        cpu_per_process = {}
        for i, cpu_usage in enumerate(percpu_usage):
            cpu_per_process[f"CPU_{i + 1}"] = {
                "total_usage": cpu_usage,
                "usage_in_kernelmode": cpu_stats['cpu_usage']['usage_in_kernelmode'],
                "usage_in_usermode": cpu_stats['cpu_usage']['usage_in_usermode'],
            }

        stats[container_id] = {
            "name": container.name,
            "cpu_stats": {
                "per_process": cpu_per_process,
                "total_usage": sum(percpu_usage),
                "usage_in_kernelmode": cpu_stats['cpu_usage']['usage_in_kernelmode'],
                "usage_in_usermode": cpu_stats['cpu_usage']['usage_in_usermode'],
            },
            "memory_stats": {
                "total_usage": container_stats['memory_stats']['usage'],
                "max_usage": container_stats['memory_stats']['max_usage'],
                "limit": container_stats['memory_stats']['limit'],
            }
        }

    return stats

def update_container_stats():
    global container_stats
    with stats_lock:
        container_stats = get_container_stats()

if __name__ == '__main__':
    # Periodically update container stats in the background
    def update_stats_background():
        while True:
            update_container_stats()
            time.sleep(2)

    background_thread = threading.Thread(target=update_stats_background)
    background_thread.start()

    # Start the Flask app without threading
    app.run(debug=True)
