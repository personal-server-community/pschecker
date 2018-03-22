
name = "Fail"
description = "It always fails."

def run_check(config):
    return {
        "status": "FAILURE",
        "message": description
    }
