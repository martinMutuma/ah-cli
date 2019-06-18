import click
from .view_article import view
from .list_articles import list_articles
from .search_articles import search_articles


@click.group()
def ah():
    "The ah command input"
    pass


ah.add_command(view)
ah.add_command(list_articles, name='list')
ah.add_command(search_articles, name='search')
