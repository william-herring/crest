import typer
import shutil
import os

app = typer.Typer()


@app.command()
def create(title: str):
    working_directory = os.getcwd()
    shutil.copytree('/resources/app_template', working_directory)
    os.rename('app_template', title)


if __name__ == "__main__":
    app()
