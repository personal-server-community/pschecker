import os

from . import (
    firewall,
    host_listening,
    root_password,
    last_update,
    domain_names
)


check_runners = [
    root_password,
    host_listening,
    firewall,
    last_update,
    domain_names
]


if os.getenv("DEBUG", False):
    from . import fail
    from . import success
    from . import warning
    check_runners += [fail, success, warning]
