import os

import root_password


check_runners = [
    root_password
]


if os.getenv("DEBUG", False):
    import fail
    import success
    check_runners += [fail, success]
