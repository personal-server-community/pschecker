import os

from . import (
    firewall,
    host_listening,
    root_password,
    last_update
)


check_runners = [
    root_password,
    host_listening,
    firewall,
    last_update
]


if os.getenv("DEBUG", False):
    from . import fail
    from . import success
    from . import warning
    check_runners += [fail, success, warning]
