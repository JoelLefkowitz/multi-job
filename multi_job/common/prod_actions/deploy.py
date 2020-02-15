from random import random

from paramiko import sshclient
from scp import scpclient

from multi_job.utils.functions import get_from_context, step, success_msg


def main(path: str, context: dict) -> str:
    (
        image_name,
        version,
        deploy_target,
        remote_user,
        docker_compose_file,
    ) = get_from_context(
        [
            "image_name",
            "version",
            "deploy_target",
            "remote_user",
            "docker_compose_file",
        ],
        context,
    )

    tagged_image_name = f"{image_name}:{version}"
    image_ref = image_name + str(random()) + ".tar.gz"

    # save docker image
    step(["docker", "save", "-o", image_ref, tagged_image_name], path)

    ssh = sshclient()
    ssh.load_system_host_keys()
    ssh.connect(deploy_target, username=remote_user)

    with scpclient(ssh.get_transport()) as scp:

        # scp docker compose file
        scp.put(docker_compose_file, "docker-compose.yml")

        # scp docker image file
        scp.put(image_ref, image_ref)

    # load docker image on the remote
    stdin, stdout, stderr = ssh.exec_command(
        " ".join(["docker", "load", "-i", image_ref])
    )
    stdin, stdout, stderr = ssh.exec_command(
        " ".join(["docker-compose", "up", "--force-recreate", "-d"])
    )
    ssh.close()
    return success_msg
