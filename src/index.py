import click
from .view_article import view


@click.group()
def ah():
    "The ah command input"
    pass


ah.add_command(view)
