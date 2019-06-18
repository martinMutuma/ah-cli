import click
import json as jsonPkg
from utils import fetch, files


@click.command()
@click.option('--export', is_flag=True, default=False)
@click.option('--json', is_flag=True, default=False)
@click.option('--csv', is_flag=True, default=False)
@click.argument('article', default="this-is-the-article-title-1")
def view(article, export, json, csv):
    """This is a command that returns a single article to
    Arguments:
        article {[string or id]} -- [unique identifier for the article]
    """
    response = fetch.get('articles/{}/'. format(article))
    article = response.json().get('article', {})
    click.echo(jsonPkg.dumps(article, indent=0))
    if export:
        filename = article['slug']
        if json:
            files.export_to_json(filename=filename, data=article)
        if csv:
            files.export_to_csv(filename=filename, data=article)
