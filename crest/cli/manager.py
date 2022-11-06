# Default commands
from crest.cli.commands.startserver import StartServer

commands = {
    'startserver': StartServer()
}


def run_command(command):
    try:
        commands[command].run()
    except KeyError:
        raise Exception(f"Command '{command}' not found")
