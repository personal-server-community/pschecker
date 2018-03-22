import os

from . import root_password, host_listening


check_runners = [
    root_password,
    host_listening
]


if os.getenv("DEBUG", False):
    from . import fail
    from . import success
    from . import warning
    check_runners += [fail, success, warning]
