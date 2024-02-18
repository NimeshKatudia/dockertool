import docker
import json

# Connect to the Docker daemon
client = docker.from_env()

def get_container_stats():
    container_stats = []
    containers = client.containers.list()

    for container in containers:
        container_stats.append(container.stats(stream=False))

    return container_stats

def save_stats_to_file(stats):
    with open('log.json', 'w') as file:
        json.dump(stats, file)

if __name__ == '__main__':
    stats = get_container_stats()
    save_stats_to_file(stats)
