import os

from . import root_password


check_runners = [
    root_password
]


if os.getenv("DEBUG", False):
    from . import fail
    from . import success
    from . import warning
    check_runners += [fail, success, warning]
