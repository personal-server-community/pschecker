import os

from pschecker.helpers import (
    get_first_line_from_command,
    get_lines_from_command
)

name = "Servers should not listen 0.0.0.0"
description = """Servers should not listen 0.0.0.0 except reverse proxy and
SSH server."""

UNKNOWN_PORT_LIMIT = 1024
EVERY_IPS = ["0.0.0.0", ":::"]
XMPP_PORTS = [5222, 5223, 5269, 5298]


def run_check(config):
    lines = get_lines_from_command("sudo netstat -pltn | grep 0.0.0.0")
    lines = lines + get_lines_from_command("sudo netstat -pltn | grep 0\ :::")

    unexpected_open_ports = []

    for line in lines:
        column = str(line).split()
        host = column[3]
        port = 0

        if host[:3] == ":::":
            port = int(host[3:])
            host = ":::"
        elif len(host.split(":")) > 1:
            port = int(host.split(":")[1])
            host = host.split(":")[0]

        name = ""
        if len(column) > 6:
            name = column[6].split("/")[1]

        if port > UNKNOWN_PORT_LIMIT \
           and port not in XMPP_PORTS \
           and host in EVERY_IPS:
            unexpected_open_ports.append("%s (%s)" % (name, str(port)))

    if len(unexpected_open_ports) == 0:
        return {
            "status": "SUCCESS"
        }
    else:
        return {
            "status": "FAILURE",
            "message": "Some of your servers listen to the 0.0.0.0 host:"
                       " %s " % ", ".join(unexpected_open_ports)
        }
