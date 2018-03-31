import os

from . import root_password, host_listening, firewall


check_runners = [
    root_password,
    host_listening,
    firewall
]


if os.getenv("DEBUG", False):
    from . import fail
    from . import success
    from . import warning
    check_runners += [fail, success, warning]
