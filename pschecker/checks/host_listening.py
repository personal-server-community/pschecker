import os

from pschecker.helpers import (
    get_first_line_from_command,
    get_lines_from_command
)

name = "Servers should not listen 0.0.0.0"
description = """Servers should not listen 0.0.0.0 except reverse proxy and
SSH server."""

UNKNOWN_PORT_LIMIT = 1024
EVERY_IP = "0.0.0.0"


def run_check(config):
    lines = get_lines_from_command("netstat -ltn | grep 0.0.0.0")

    unexpected_open_ports = []

    for line in lines:
        column = str(line).split()
        host = column[3]
        port = int(host.split(":")[1])
        if port > UNKNOWN_PORT_LIMIT and EVERY_IP in host:
            unexpected_open_ports.append(str(port))

    if len(unexpected_open_ports) == 0:
        return {
            "status": "SUCCESS"
        }
    else:
        return {
            "status": "FAILURE",
            "message": "Some of your servers listen to the 0.0.0.0 host."
                       "(ports: %s)" % ", ".join(unexpected_open_ports)
        }
