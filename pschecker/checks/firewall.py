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
    is_firewall_up = check_ufw()

    if is_firewall_up:
        return {
            "status": "SUCCESS"
        }
    else:
        return {
            "status": "FAILURE",
            "message": "No firewall is running."
        }


def check_ufw():
    lines = get_lines_from_command("sudo ufw status")
    return len(lines) > 2 and \
        "Status" in lines[0] and \
        "inactive" not in lines[0]
