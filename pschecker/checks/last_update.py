from datetime import datetime, timedelta

from pschecker.helpers import get_first_line_from_command

name = "Last system update was done recently"
description = "Fails if your last update is older than 2 weeks."

def run_check(config):
    date_command = "stat -c %y /var/lib/apt/"
    date_string = get_first_line_from_command(date_command)
    date = datetime.strptime(date_string[:10], "%Y-%m-%d")
    now = datetime.now()
    limit = now - timedelta(days=14)

    if date > limit:
        return {"status": "SUCCESS"}
    else:
        return {
            "status": "FAILURE",
            "message": "Your last OS update is older than 2 weeks."
        }
