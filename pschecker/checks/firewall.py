import os

from pschecker.helpers import (
    get_first_line_from_command,
    get_lines_from_command
)

name = "A firewall should be up and running"
description = """We expect that a firewall limits access for sensitive part of
the server."""

FIREWALL_NAMES = ["iptables", "ufw"]


def run_check(config):
    is_firewall_up = False
    for firewall_name in FIREWALL_NAMES:
        lines = get_lines_from_command("ps -ef | grep %s" % firewall_name)
        if len(lines) > 2:
            is_firewall_up = True

    if is_firewall_up:
        return {
            "status": "SUCCESS"
        }
    else:
        return {
            "status": "FAILURE",
            "message": "No firewall is running."
        }
