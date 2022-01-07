#!python

import click
# from prettytable import PrettyTable
import json
import requests
import os
from string import Template
import re


METAURL = 'https://api.softlayer.com/metadata/v3.1'

SERVICEMARKDOWN = """---
title: "$service"
description: "$documentation"
date: "2018-02-12"
tags:
    - "$layoutType"
    - "sldn"
    - "$serviceType"
classes:
    - "$mainService"
type: "reference"
layout: "$layoutType"
mainService : "$mainService"
---
"""

LISTMARKDOWN = """---
title: "$type"
description: "List of $type"
date: "2018-02-12"
type: reference
layout: $listType
url: /reference/$type/list.html
---
"""

def wikiToMarkdownFilter(text):
    # Remove double quotes, because hugo will complain about that.
    text = text.replace('"', "'")
    # Even if they are escaped.
    text = text.replace('\\"', "'")
    # [[SoftLayer_Account]] -> reference/datatypes/SoftLayer_Account
    text = re.sub(r'\[\[(?P<one>\w+)( \(type\))?(\|.*)?\]\]', "[\g<one>](reference/datatypes/\g<one>)", text)
    # [[SoftLayer_Account/getObject]] -> reference/services/SoftLayer_Account/getObject
    text = re.sub(r'\[\[(?P<one>\w+)\/(?P<two>\w+)(\|.*)?\]\]', "[\g<one>::\g<two>](reference/services/\g<one>/\g<two>')", text)
    # [[SoftLayer_Account::id]] -> reference/datatypes/SoftLayer_ACccount/#id
    text = re.sub(r'\[\[(?P<one>\w+)::(?P<two>\w+)(\|.*)?\]\]', "[\g<one>::\g<two>](reference/datatypes/$1/#$2)", text)
    return text


class SLDNgenerator():

    def __init__(self):
        cwd = os.getcwd()
        if not cwd.endswith('githubio_source'):
            raise Exception(f"Working Directory should be githubio_source, is currently {cwd}")
        # Make sure required directories exist
        if not os.path.isdir(f'{cwd}/content/reference/datatypes'):
            os.mkdir(f'{cwd}/content/reference/datatypes')
            substitions = {
                "type": "datatypes",
                "listType": "datatypelist"
            }
            template = Template(LISTMARKDOWN)
            with open(f"{cwd}/content/reference/datatypes/list.md", "w", encoding="utf-8") as f:
                f.write(template.substitute(substitions))
        if not os.path.isdir(f'{cwd}/content/reference/services'):
            os.mkdir(f'{cwd}/content/reference/services')
            substitions = {
                "type": "services",
                "listType": "servicelist"
            }
            template = Template(LISTMARKDOWN)
            with open(f"{cwd}/content/reference/services/list.md", "w", encoding="utf-8") as f:
                f.write(template.substitute(substitions))
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


    def generateMarkdown(self, metajson):
        for serviceName, service in metajson.items():
            print(f"Working on: {serviceName}")
            # noservice means datatype only.
            if service.get('noservice', False) == False:
                self.writeServiceMarkdown(service)
                for methodName, method in service.get('methods', {}).items():
                    self.writeMethodMarkdown(method, serviceName=serviceName)
            self.writeDatatypeMarkdown(service)

    def writeServiceMarkdown(self, serviceJson):
        service_dir = f"./content/reference/services/{serviceJson.get('name')}/"
        if not (os.path.isdir(service_dir)):
            os.mkdir(service_dir)
        template = Template(SERVICEMARKDOWN)
        # Needed to get the category of the service.
        service_parts = serviceJson.get('name').split('_')
        documentation = serviceJson.get('serviceDoc', '')

        substitions = {
            'service': serviceJson.get('name'),
            'documentation': wikiToMarkdownFilter(documentation),
            'serviceType': service_parts[1],
            'layoutType' : 'service',
            'mainService': serviceJson.get('name')
        }
        with open(f"{service_dir}/_index.md", "w", encoding="utf-8") as f:
            f.write(template.substitute(substitions))
        
    def writeDatatypeMarkdown(self, serviceJson):
        service_dir = f"./content/reference/datatypes/{serviceJson.get('name')}.md"
        # if not (os.path.isdir(service_dir)):
        #     os.mkdir(service_dir)
        template = Template(SERVICEMARKDOWN)
        # Needed to get the category of the service.
        service_parts = serviceJson.get('name').split('_')

        # For datatypes, docs will either be in one of these 2 fields.
        documentation = serviceJson.get('typeDoc', '')
        if documentation == '':
            documentation = serviceJson.get('serviceDoc', '')

        substitions = {
            'service': serviceJson.get('name'),
            'documentation': wikiToMarkdownFilter(documentation),
            'serviceType': service_parts[1],
            'layoutType' : 'datatype',
            'mainService': serviceJson.get('name')
        }
        with open(f"{service_dir}", "w", encoding="utf-8") as f:
            f.write(template.substitute(substitions))

    def writeMethodMarkdown(self, serviceJson, serviceName):
        service_dir = f"./content/reference/services/{serviceName}/"
        if not (os.path.isdir(service_dir)):
            os.mkdir(service_dir)
        template = Template(SERVICEMARKDOWN)
        # Needed to get the category of the service.
        service_parts = serviceName.split('_')
        documentation = serviceJson.get('doc', '')
        if documentation == '':
            documentation = serviceJson.get('docOverview', '')

        substitions = {
            'service': serviceJson.get('name'),
            'documentation': wikiToMarkdownFilter(documentation),
            'serviceType': service_parts[1],
            'layoutType' : 'method',
            'mainService': serviceName
        }
        with open(f"{service_dir}/{serviceJson.get('name','')}.md", "w", encoding="utf-8") as f:
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

    print("Generating Markdown....")
    # print(metajson)
    generator.generateMarkdown(metajson)


if __name__ == "__main__":
    main()