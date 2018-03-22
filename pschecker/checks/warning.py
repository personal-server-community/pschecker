name = "Warning"
description = "Always warning"

def run_check(config):
    return {
        "status": "WARNING",
        "message": description
    }
