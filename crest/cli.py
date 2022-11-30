import typer
import shutil
import os

app = typer.Typer()


@app.command()
def create(title: str):
    working_directory = os.getcwd()
    shutil.copytree(f'{os.path.dirname(os.path.realpath(__file__))}/resources/app_template', working_directory + '/app_template')
    os.rename('app_template', title)


# Will be used to migrate schema changes once database module is fully implemented
@app.command()
def migrate(hi: int):
    pass


if __name__ == "__main__":
    app()
