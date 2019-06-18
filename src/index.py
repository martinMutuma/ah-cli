import click
from .view_article import view
from .list_articles import list_articles


@click.group()
def ah():
    "The ah command input"
    pass


ah.add_command(view)
ah.add_command(list_articles, name='list')
