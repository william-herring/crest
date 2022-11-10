from crest.cli.commands.createapp import CreateApp
from crest.cli.commands.startserver import StartServer

commands = {
    'startserver': StartServer(),
    'createapp': CreateApp()
}


def run_command(command):
    try:
        commands[command].run()
    except KeyError:
        raise Exception(f"Command '{command}' not found")
