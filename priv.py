import docker
import time
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)
client = docker.from_env()

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/create-container', methods=['POST'])
def create_container():
    cpu_quota = request.form['cpu_quota']
    memory_limit = request.form['memory_limit']
    existing_container_id = request.form['existing_container_id']

    # Get the existing container
    container = client.containers.get(existing_container_id)

    # Define the container parameters
    container_params = {
        'image': f'{container.image.tags[0]}:{container.image.tags[1]}',
        'name': f'my_container_{int(time.time())}',
        'cpu_period': 100000,
        'cpu_quota': int(cpu_quota),
        'mem_limit': f'{memory_limit}b',
        'healthcheck': {
            'test': ['CMD', 'python', '-c', 'import sys; sys.exit(0)'],
            'interval': 30000000000,
            'retries': 3,
            'start_period': 30000000000,
            'timeout': 30000000000
        }
    }

    # Create the Docker container
    new_container = client.containers.create(**container_params)

    # Start the container
    new_container.start()

    return jsonify({
        'message': f'Container created with CPU quota {cpu_quota}% and memory limit {memory_limit} bytes',
        'container_id': new_container.id
    })

if __name__ == '__main__':
    app.run(debug=True)
