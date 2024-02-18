import docker
client = docker.from_env()

def get_container_stats(container_id):
    container = client.containers.get(container_id)
    stats = container.stats(stream=False)
    return stats

# Example: Get stats for a container with ID 'container_id'
container_id = '6993a0b90a81'
container_stats = get_container_stats(container_id)

# Extract relevant metrics from the container stats
cpu_stats = container_stats['cpu_stats']
memory_stats = container_stats['memory_stats']
network_stats = container_stats['networks']  # Updated key to access network stats
print(cpu_stats)

# Process and utilize the metrics as needed