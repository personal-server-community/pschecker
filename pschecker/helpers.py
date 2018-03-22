import subprocess


def get_lines_from_command(command):
    result = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    return result.stdout.readlines()


def get_first_line_from_command(command):
    return str(get_lines_from_command(command)[0])
