import requests
import click
import sys

partial_url = "http://ah-premier-staging.herokuapp.com/api/"


def get(url):
    full_url = partial_url+url

    try:
        response = requests.get(full_url, timeout=3)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as e:
        click.secho("Http Error:" + str(e), fg="red")
    except requests.exceptions.ConnectionError as e:
        click.secho("Error Connecting:"+str(e), fg="red")
    except requests.exceptions.Timeout as e:
        click.secho("Timeout Error:" + str(e), fg="red")
    except requests.exceptions.RequestException as e:
        click.secho("OOps: Somethhing went wrong"+str(e), fg="red")
    sys.exit(1)
