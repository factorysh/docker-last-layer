import docker


client = docker.from_env()

for container in client.containers.list(ignore_removed=True):
    print(container.name)
    diffs = container.diff()
    if diffs is None:
        continue
    container.reload()
    print("\t", container.attrs['GraphDriver']['Data'])
    volumes = set(m['Destination'] for m in container.attrs['Mounts'] if m['Type'] == 'bind')
    print("\t", volumes)
    for diff in diffs:
        if diff['Kind'] != 1: # not a file ?
            continue
        if diff['Path'] in volumes:
            continue
        print("\t", diff['Path'])


