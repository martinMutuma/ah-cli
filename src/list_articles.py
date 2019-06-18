import click
import json as jsonPkg
from utils import fetch, files


@click.command()
@click.option('--export', is_flag=True, default=False)
@click.option('--json', is_flag=True, default=False)
@click.option('--csv', is_flag=True, default=False)
@click.option('--limit', type=int, default=5)
def list_articles(limit, export, json, csv):
    """This is a command that returns a list of articles to
    Arguments:
        article {[string or id]} -- [unique identifier for the article]
    """
    response = fetch.get('articles?page_size={}'.format(limit))
    articles = response.json().get('articles', {})
    click.echo(jsonPkg.dumps(articles, indent=4))
    if export:
        filename = "all_articles"
        if json:
            files.export_to_json(filename=filename, data=articles)
        if csv:
            files.export_to_csv(filename=filename, data=articles)
