from flask import Flask

app = Flask(__name__)

@app.route('/')
def display_docker_stats():
    import subprocess

    # Execute 'docker stats' command and get the output
    output = subprocess.check_output(['docker', 'stats']).decode('utf-8')

    return output

