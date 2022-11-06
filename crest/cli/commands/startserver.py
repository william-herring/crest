from crest.cli.commands import BaseCommand
from crest.servers import devserver


class StartServer(BaseCommand):
    def handle(self):
        super(StartServer, self).handle()
        devserver.start()
