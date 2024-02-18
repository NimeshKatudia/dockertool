import re
import docker
from flask import Flask, render_template, request

app = Flask(__name__)
client = docker.from_env()

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/create-container', methods=['POST'])
def create_container():
    cpu_quota = int(request.form['cpu_quota'])
    memory_limit = int(request.form['memory_limit'])
    existing_container_id = request.form['existing_container_id']
    
    if cpu_quota < 1:
        return "CPU quota cannot be less than 1ms (i.e. 1000)"

    container_params = {
        'cpu_quota': cpu_quota,
        'mem_limit': memory_limit,
    }
    
    if re.match(r'^[a-f0-9]{64}$', existing_container_id):
        try:
            container = client.containers.get(existing_container_id)
            container_params['image'] = f'{container.image.tags[0]}:{container.image.tags[1]}' if container.image.tags else None
        except docker.errors.NotFound:
            return f"Container with ID {existing_container_id} does not exist."
    else:
        container_params['image'] = existing_container_id

    try:
        new_container = client.containers.create(**container_params)
        new_container.start()
        return f"Container '{new_container.name}' created and started successfully!"
    except docker.errors.APIError as e:
        if "CPU cfs quota can not be less than 1ms" in str(e):
            return "Error: CPU quota cannot be less than 1ms (i.e. 1000)"
        else:
            return f"Error: {e}"
    
if __name__ == '__main__':
    app.run(debug=True)
