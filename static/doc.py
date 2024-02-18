from flask import Flask, render_template, jsonify
import docker
import json
import os

app = Flask(__name__)
client = docker.from_env()

@app.route('/')
def index():
    return render_template('container_stats.html')

@app.route('/stats')
def get_stats():
    container_stats = get_container_stats()

    # Save container stats to a JSON file
    save_stats_to_file(container_stats)

    return jsonify(container_stats)

def get_container_stats():
    containers = client.containers.list()
    stats = {}

    for container in containers:
        container_stats = container.stats(stream=False)
        container_id = container_stats['id']

        io_stats = container_stats['blkio_stats'].get('io_service_bytes_recursive', [])

        stats[container_id] = {
            "name": container.name,
            "cpu_stats": {
                "total_usage": container_stats['cpu_stats']['cpu_usage']['total_usage'],
                "usage_in_kernelmode": container_stats['cpu_stats']['cpu_usage']['usage_in_kernelmode'],
                "usage_in_usermode": container_stats['cpu_stats']['cpu_usage']['usage_in_usermode'],
            },
            "memory_stats": {
                "total_usage": container_stats['memory_stats']['usage'],
                "max_usage": container_stats['memory_stats']['max_usage'],
                "limit": container_stats['memory_stats']['limit'],
            },
            "network_stats": {
                "rx_bytes": container_stats['networks']['eth0']['rx_bytes'],
                "tx_bytes": container_stats['networks']['eth0']['tx_bytes'],
            },
            "io_stats": {
                "read_bytes": io_stats[0]['value'] if io_stats else 0,
                "write_bytes": io_stats[1]['value'] if len(io_stats) > 1 else 0,
            }
        }

    return stats

def save_stats_to_file(stats):
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, 'container_stats.json')

    with open(file_path, 'w') as file:
        json.dump(stats, file)

if __name__ == '__main__':
    app.run(debug=True)
