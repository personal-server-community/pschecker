import click

from . import checks

GREEN = '\033[92m'
ORANGE = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
ENDC = '\033[0m'


@click.command()
@click.option(
    "--distribution",
    default="debian",
    help="Distribution your server is running on. Choose between debian, " + \
         "ubuntu or arch."
)
def pschecker(distribution):
    config = build_config(distribution)
    display_introduction(config)
    run_diagnostic(config)


def build_config(distribution):
    return {
        "distribution": distribution
    }


def display_introduction(config):
    print("Welcome to Personal Server Checker!")
    print("Your personal server diagnostic is:")
    print("Distribution: %s" % config["distribution"])


def run_diagnostic(config):
    for check_runner in checks.check_runners:
        display_check_result(
            check_runner.name,
            check_runner.run_check(config)
        )


def display_check_result(name, result):
    if result["status"] == "SUCCESS":
        print("%s: %s" % (name, GREEN + "OK" + ENDC))
    else:
        print("%s: %s" % (name, RED + BOLD + "KO" + ENDC))
        print("* %s" % result["message"])


if __name__ == "__main__":
    pschecker()
