import os

from pschecker.helpers import (
    get_first_line_from_command,
    get_lines_from_command
)

name = "Root must not use password"
description = "Your root user should not be able to log in with a password."


def run_check(config):
    first_line = get_first_line_from_command("passwd -S")
    if "NP" in first_line:
        return {"status": "SUCCESS"}
    else:
        lines = get_lines_from_command("cat /root/.ssh/authorized_keys")
        if os.path.exists("/root/.ssh/authorized_keys") and len(lines) > 0:
            return {
                "status": "FAILURE",
                "message": "Your root user should not be able to log in with "
                           "password, only SSH login should be allowed."
            }
        else:
            return {
                "status": "WARNING",
                "message": "Your root user can connect only with root password."
                           " That's fine but you should consider having a "
                           "strong password and think about allowing SSH "
                           "access only."
            }
