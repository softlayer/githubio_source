#!python

import click
# from prettytable import PrettyTable
import json
import requests
import os
from string import Template


METAURL = 'https://api.softlayer.com/metadata/v3.1'

SERVICEMARKDOWN = """---
title: "$service"
description: "$documentation"
date: "2018-02-12"
tags:
    - "service"
    - "sldn"
    - "$serviceType"
classes:
    - "$service"
type: "reference"
layout: "service"
---
"""

class SLDNgenerator():

    def __init__(self):
        pass

    def getMetadata(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"{url} returned \n{response.text}\nHTTP CODE: {response.status_code}")

        return response.json()

    def getLocalMetadata(self, filename='data/sldn_metadata.json'):
        with open(filename, "r", encoding="utf-8") as f:
            metadata = f.read()
        return json.loads(metadata)

    def saveMetadata(self, metajson, filename='data/sldn_metadata.json'):
        print(f"Writing SLDN Metadata to {filename}")
        with open(filename, 'w') as f:
            json.dump(metajson, f, indent=4)


    def generateServices(self, metajson):
        for name, service in metajson.items():
            print(f"Working on: {name}")
            # noservice means datatype only.
            if service.get('noservice', False) == True:
                continue
            else:
                self.writeServiceMarkdown(service)

    def writeServiceMarkdown(self, serviceJson):
        service_dir = f"./content/reference/services/{serviceJson.get('name')}/"
        if not (os.path.isdir(service_dir)):
            os.mkdir(service_dir)
        template = Template(SERVICEMARKDOWN)
        # Needed to get the category of the service.
        service_parts = serviceJson.get('name').split('_')

        substitions = {
            'service': serviceJson.get('name'),
            'documentation': serviceJson.get('serviceDoc', '').replace('"', "'"),
            'serviceType': service_parts[1]
        }
        with open(f"{service_dir}/_index.md", "w", encoding="utf-8") as f:
            f.write(template.substitute(substitions))
        


@click.command()
@click.option('--download', default=False)
def main(download):
    generator = SLDNgenerator()
    if download:
        try:
            metajson = generator.getMetadata(url = METAURL)
            generator.saveMetadata(metajson)
        except Exception as e:
            print("========== ERROR ==========")
            print(f"{e}")
            print("========== ERROR ==========")
    else:
        metajson = generator.getLocalMetadata()

    print("Generating Services....")
    # print(metajson)
    generator.generateServices(metajson)


if __name__ == "__main__":
    main()