import docker


client = docker.from_env()

for container in client.containers.list(ignore_removed=True):
    print(container.name)
    diffs = container.diff()
    if diffs is None:
        continue
    container.reload()
    print("\t", container.attrs['GraphDriver']['Data'])
    volumes = [m['Destination'] for m in container.attrs['Mounts'] if m['Type'] == 'bind']
    print("\t", volumes)
    for diff in diffs:
        print("\t", diff)


