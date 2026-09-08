import subprocess

def execute(command: str):
    return subprocess.run(command, shell=True)