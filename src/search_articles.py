import click
import json as jsonPkg
from utils import fetch, files
import sys


@click.command()
@click.option('--export', is_flag=True, default=False)
@click.option('--json', is_flag=True, default=False)
@click.option('--csv', is_flag=True, default=False)
@click.option('--limit', type=int, default=5)
@click.option('--page', type=int, default=1)
@click.argument('query', default="")
@click.pass_context
def search_articles(ctx, query, limit, export, json, csv, page):
    """Search through the articles
    """
    response = fetch.get(
        'articles?page_size={}&title={}&page={}'.format(limit, query, page))

    articles = response.json().get('articles', {})
    click.echo(jsonPkg.dumps(articles, indent=4))
    if export:
        filename = "search_"+query.replace(' ', '_')
        if json:
            files.export_to_json(filename=filename, data=articles)
        if csv:
            files.export_to_csv(filename=filename, data=articles)
    next_q = click.prompt(
        "Use [n] to go next page or [q] to exit", default='q')
    if next_q.lower() == 'n':
        ctx.invoke(search_articles, query=query,
                   limit=limit, export=False, page=page+1)
    sys.exit(0)
