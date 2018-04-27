import subprocess


def get_lines_from_command(command):
    result = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    lines = result.stdout.readlines()
    lines = [line.decode() if isinstance(line, bytes) else line for line in lines]
    return lines


def get_first_line_from_command(command):
    return str(get_lines_from_command(command)[0])
