from random import random

from multi_job.utils.functions import get_from_context, step
from paramiko import SSHClient
from scp import SCPClient


def main(path: str, context: dict) -> str:
    (
        IMAGE_NAME,
        IMAGE_VERSION,
        SSH_TARGET,
        REMOTE_USER,
        DOCKER_COMPOSE_FILE,
    ) = get_from_context(
        [
            "image_name",
            "image_version",
            "ssh_target",
            "remote_user",
            "docker_compose_file",
        ],
        context,
    )

    TAGGED_IMAGE_NAME = f"{IMAGE_NAME}:{IMAGE_VERSION}"
    IMAGE_REF = IMAGE_NAME + str(random()) + ".tar.gz"

    # Save docker image
    step(["docker", "save", "-o", IMAGE_REF, TAGGED_IMAGE_NAME], path)

    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(SSH_TARGET, username=REMOTE_USER)

    with SCPClient(ssh.get_transport()) as scp:

        # Scp docker compose file
        scp.put(DOCKER_COMPOSE_FILE, "docker-compose.yml")

        # Scp docker image file
        scp.put(IMAGE_REF, IMAGE_REF)

    # Load docker image on the remote
    stdin, stdout, stderr = ssh.exec_command(
        " ".join(["docker", "load", "-i", IMAGE_REF])
    )
    stdin, stdout, stderr = ssh.exec_command(" ".join(["docker-compose", "up", "-d"]))
    ssh.close()
