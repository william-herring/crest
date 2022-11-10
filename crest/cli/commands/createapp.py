import os
from distutils.dir_util import copy_tree
from crest.cli.commands import BaseCommand


class CreateApp(BaseCommand):
    def handle(self):
        super(CreateApp, self).handle()
        copy_tree('../resources/app_template', os.getcwd())

