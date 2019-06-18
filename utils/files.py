import click
import json
import os
import random
import csv
import logging


def create_imports_folder():
    if not os.path.isdir('./imports'):
        os.mkdir("./imports", 755)


def export_to_json(filename="ah_cli", data={}):
    create_imports_folder()
    file_name = "./imports/"+filename+'.json'
    if os.path.isfile(file_name):
        return export_to_json(filename + str(random.randint(1, 101)), data)

    click.secho("Exporting data to json file ...", fg="blue")
    with click.open_file(file_name, "w") as exportFile:
        exportFile.write(json.dumps(data, indent=4))
        click.secho("success open: {}".format(file_name), fg="green")


def export_to_csv(filename="ah_cli", data={}):
    create_imports_folder()
    file_name = "./imports/"+filename+'.csv'
    if os.path.isfile(file_name):
        return export_to_csv(filename + str(random.randint(1, 101)), data)

    click.secho("Exporting data to csv file ...", fg="blue")
    if isinstance(data, list):
        try:
            headers = data[0].keys()
            with click.open_file(file_name, "w") as exportFile:
                csvFile = csv.DictWriter(exportFile, headers)
                csvFile.writeheader()
                csvFile.writerows(data)
        except Exception as error:
            logging.error(error)
    if isinstance(data, dict):
        headers = data.keys()
        with click.open_file(file_name, "w") as exportFile:
            csvFile = csv.DictWriter(exportFile, headers)
            csvFile.writeheader()
            csvFile.writerow(data)
    click.secho("success open: {}".format(file_name), fg="green")
