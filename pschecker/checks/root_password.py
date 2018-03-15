import subprocess

name = "Root can use password"
description = "Your root user should not be able to log in with a password."

def run_check(config):
    result = subprocess.Popen(
        'passwd -S',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    first_line = result.stdout.readlines()[0]

    if "NP" in first_line:
        return {"status": "SUCCESS"}
    else:
        return {
            "status": "FAILURE",
            "message": "Your root user should not be able to log in with "
                       "password, only SSH login should be allowed."
        }

