#!/usr/local/bin/python3.10
import typer
import shutil
import os
from rich import print

app = typer.Typer()


@app.command()
def create(title: str):
    working_directory = os.getcwd()
    shutil.copytree(f'{os.path.dirname(os.path.realpath(__file__))}/resources/app_template', working_directory + '/app_template')
    os.rename('app_template', title)
    print(f'Created [bold green]{title}[/bold green] at {working_directory + "/" + title}')


# Will be used to migrate schema changes once database module is fully implemented
@app.command()
def migrate(hi: int):
    pass


if __name__ == "__main__":
    app()
