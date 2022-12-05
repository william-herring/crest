#!/usr/local/bin/python3
import typer
import shutil
import os
from rich import print
import webbrowser

app = typer.Typer()


@app.command()
def create(title: str):
    """
    Create a new Crest app
    """
    working_directory = os.getcwd()
    shutil.copytree(f'{os.path.dirname(os.path.realpath(__file__))}/resources/app_template', working_directory + '/app_template')
    os.rename('app_template', title)
    print(f'Created [bold green]{title}[/bold green] at {working_directory + "/" + title}')


@app.command()
def docs():
    """
    View the Crest documentation
    """
    webbrowser.open('https://github.com/william-herring/crest/tree/main/docs')


if __name__ == "__main__":
    app()
