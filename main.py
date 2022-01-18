import typer
import os

app = typer.Typer()


@app.command()
def dbconnect(conname: str, contype: str, dbtype: str, dbconfig: str):
    print(f'conname: {conname}, contype: {contype}, dbtyoe: {dbtype}, dbconfig: {dbconfig}')


@app.command()
def dbviewer():
    print('goodbye')


if __name__ == '__main__':
    typer.run(dbviewer)
