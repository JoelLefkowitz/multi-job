import os, re
from random import random

from paramiko import SSHClient
from scp import scpclient

from multi_job.utils.functions import (
    get_optional_from_context,
    get_required_from_context,
    step,
    success_msg,
)


def main(path: str, context: dict) -> str:

    image_name, version, deploy_target = get_required_from_context(
        ["image_name", "version", "deploy_target"], context
    )
    remote_user, docker_compose_file = get_optional_from_context(
        ["remote_user", "docker_compose_file"], context
    )

    if not remote_user:
        remote_user = "root"

    if not docker_compose_file:
        remote_user = "docker-compose.yml"

    tagged_image_name = f"{image_name}:{version}"

    re_match_str = f"^{tagged_image_name}-.*\.tar\.gz$"
    re_sub_str = f"^{tagged_image_name}-|\.tar\.gz$"

    # Increment built binary suffix
    old_build_suffixes = [
        re.sub(re_sub_str, "", file)
        for file in os.listdir(path)
        if re.match(re_match_str, file)
    ]
    old_build_numbers = [
        int(suffix) for suffix in old_build_suffixes if suffix.isdigit()
    ]
    build_number = str(max(old_build_numbers) + 1) if old_build_numbers else "1"
    image_file = tagged_image_name + "-" + build_number + ".tar.gz"

    step(["docker", "save", "-o", image_file, tagged_image_name], path)

    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(deploy_target, username=remote_user)

    with scpclient(ssh.get_transport()) as scp:
        scp.put(docker_compose_file, docker_compose_file)
        scp.put(image_file, image_file)

    ssh.exec_commands(
        [f"docker load -i {image_file}", "docker-compose up --force-recreate -d"]
    )
    ssh.close()

    return success_msg
