import os

from pschecker.helpers import (
    get_first_line_from_command,
    get_lines_from_command
)

name = "Root must not use password"
description = "Your root user should not be able to log in with a password."


def run_check(config):
    first_line = get_first_line_from_command(
        "cat /etc/ssh/sshd_config | grep PermitRootLogin"
    )
    if "without-password" in first_line:
        return {"status": "SUCCESS"}
    else:
        return {
            "status": "FAILURE",
            "message": "Your root user should not be able to log in with "
                       "password, only SSH login should be allowed."
            }
