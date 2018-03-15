
name = "Fail"
description = "Always fails"

def run_check(config):
    return {
        "status": "FAILURE",
        "message": "It always fails."
    }
