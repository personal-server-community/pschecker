#!/usr/bin/env python
import re
import click

from terminaltables import SingleTable
from pschecker import checks


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
@click.option(
    "--domains",
    default="",
    help="Domain names that targets your server."
)
def cli(distribution, domains):
    config = build_config(distribution, domains)
    display_introduction(config)
    run_diagnostic(config)


def build_config(distribution, domains):
    domain_names = []
    if len(domains) > 0:
        domain_names = domains.split(",")
    return {
        "distribution": distribution,
        "domains": domain_names
    }


def display_introduction(config):
    print("Running the audit of your personal server...")
    print("")
    print("Context:")
    print("- Distribution: %s" % config["distribution"])
    print("- Domain names: %s" % ", ".join(config["domains"]))
    print("")
    print("Processing tests:")


def run_diagnostic(config):
    table_rows = [["Name", "Result", "Infos"]]
    for check_runner in checks.check_runners:
        result = check_runner.run_check(config)
        if result["status"] != "EMPTY":
            print(check_runner.name + ": done")
            table_rows.append(build_check_result_row(
                check_runner.name,
                result
            ))

    table = SingleTable(
        table_rows,
        title="Your personal server diagnostic"
    )

    print("")
    print(table.table)


def build_check_result_row(name, result):
    message = re.sub(
        "(.{32})",
        "\\1\n",
        result.get("message", ""),
        0,
        re.DOTALL
    )  # Make sure that message is not too wide for display
    if result["status"] == "SUCCESS":
        return [name, GREEN + "OK" + ENDC, ""]
    elif result["status"] == "WARNING":
        return [name, ORANGE + "WARN" + ENDC, message]
    else:
        return [name, RED + BOLD + "KO" + ENDC, message]


if __name__ == '__main__':
    cli()
