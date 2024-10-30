#!python

import click
# from prettytable import PrettyTable
import json
import requests
import os
import shutil
from string import Template
import re


METAURL = 'https://api.softlayer.com/metadata/v3.1'


class OpenAPIGen():

    def __init__(self, outdir: str) -> None:
        self.outdir = outdir
        if not os.path.isdir(self.outdir):
            print(f"Creating directory {self.outdir}")
            os.mkdir(self.outdir)
        self.metajson = None
        self.metapath = f'{self.outdir}/sldn_metadata.json'
        self.openapi = {
            "openapi": '3.0.3',
            "info": {
                "title": "SoftLayer API - OpenAPI 3.0",
                "description": "SoftLayer API Definitions in a swagger format",
                "termsOfService": "https://cloud.ibm.com/docs/overview?topic=overview-terms",
                "version": "1.0.0"
            },
            "externalDocs": {
                "description": "SLDN",
                "url": "https://sldn.softlayer.com"
            },
            "servers": [
                {"url": "https://api.softlayer.com"},
                {"url": "https://api.service.softlayer.com"}
            ],
            "paths": {},
            "components": {
                "schemas": {},
                "requestBodies": {},
                "securitySchemes": {
                    "api_key": {
                        "type": "apiKey",
                        "name": "api_key",
                        "in": "header"
                    }
                }
            }
        }

    def getMetadata(self, url: str) -> dict:
        """Downloads metadata from SLDN"""
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"{url} returned \n{response.text}\nHTTP CODE: {response.status_code}")

        self.metajson = response.json()
        return self.metajson

    def saveMetadata(self) -> None:
        """Saves metadata to a file"""
        print(f"Writing SLDN Metadata to {self.metapath}")
        with open(self.metapath, 'w') as f:
            json.dump(self.metajson, f, indent=4)

    def getLocalMetadata(self) -> dict:
        """Loads metadata from local data folder"""
        with open(self.metapath, "r", encoding="utf-8") as f:
            metadata = f.read()
        self.metajson = json.loads(metadata)
        return self.metajson

    def addInORMMethods(self):
        for serviceName, service in self.metajson.items():
            # noservice means datatype only.
            if service.get('noservice', False) == False:
                for propName, prop in service.get('properties', {}).items():
                    if prop.get('form', '') == 'relational':
                        # capitlize() sadly lowercases the other letters in the string
                        ormName = f"get{propName[0].upper()}{propName[1:]}"
                        ormMethod = {
                            'doc': prop.get('doc', ''),
                            'docOverview': "",
                            'name': ormName,
                            'type': prop.get('type'),
                            'typeArray': prop.get('typeArray', None),
                            'ormMethod': True,
                            'maskable': True,
                            'filterable': True,
                            'deprecated': prop.get('deprecated', False)
                        }
                        if ormMethod['typeArray']:
                            ormMethod['limitable'] = True
                        self.metajson[serviceName]['methods'][ormName] = ormMethod
        return self.metajson

    def addInChildMethods(self):
        for serviceName, service in self.metajson.items():
            self.metajson[serviceName]['methods'] = self.getBaseMethods(serviceName, 'methods')
            self.metajson[serviceName]['properties'] = self.getBaseMethods(serviceName, 'properties')


    def getBaseMethods(self, serviceName, objectType):
        """Responsible for pulling in properties or methods from the base class of the service requested"""
        service = self.metajson[serviceName]
        methods = service.get(objectType, {})
        if service.get('base', "SoftLayer_Entity") != "SoftLayer_Entity":
            
            baseMethods = self.getBaseMethods(service.get('base'), objectType)
            for bName, bMethod in baseMethods.items():
                if not methods.get(bName, False):
                    methods[bName] = bMethod
        return methods 

    def generate(self) -> None:
        print("OK")
        for serviceName, service in self.metajson.items():
            print(f"Working on {serviceName}")
            # Writing the check this way to be more clear to myself when reading it
            # This service has methods
            if service.get('noservice', False) == False:
                for methodName, method in service.get('methods', {}).items():
                    self.openapi['paths'].update(self.genPath(serviceName, methodName, method))


        with open(f"{self.outdir}/sl_openapi.json", "w") as outfile:
            json.dump(self.openapi, outfile, indent=4)

    def genPath(self, serviceName: str, methodName: str, method: dict) -> dict:
        http_method = "get"
        if method.get('parameters', False):
            http_method = "post"
        init_param = ''
        if not method.get('static', False):
            init_param = f"{{{serviceName}ID}}/"

        schema = method.get('type')
        new_path = {
            f"{serviceName}/{init_param}{methodName}": {
                http_method: {
                    "description": method.get('doc'),
                    "summary": method.get('docOverview', ''),
                    "externalDocs": f"https://sldn.softlayer.com/reference/services/{serviceName}/{methodName}/",
                    "operationId": f"{serviceName}::{methodName}",
                    "responses": {
                        "200": {
                            "description": "Successful operation",
                            "content": {
                                "application/json": {
                                    "schema": self.getSchema(method)
                                }
                            }
                        }
                    },
                    "security": [
                        {"api_key": []}
                    ]
                }
            }
        }
        return new_path

    def getSchema(self, method: dict) -> dict:
        """Gets a formatted schema object from a method"""
        is_array = method.get('typeArray', False)
        sl_type = method.get('type', "null")
        ref = {}
        if sl_type.startswith("SoftLayer_"):
            ref = {"$ref": f"#/components/schemas/{sl_type}"}
        else:
            ref = {"type": sl_type}
        if is_array:
            schema = {"type": "array", "items": ref}
        else:
            schema = ref
        return schema
        


@click.command()
@click.option('--download', default=False, is_flag=True)
@click.option('--clean', default=False, is_flag=True, help="Removes the services and datatypes directories so they can be built from scratch")
def main(download: bool, clean: bool):
    cwd = os.getcwd()
    outdir = f'{cwd}/openapi'
    if not cwd.endswith('githubio_source'):
        raise Exception(f"Working Directory should be githubio_source, is currently {cwd}")

    if clean:
        print(f"Removing {outdir}")
        try:
            shutil.rmtree(f'{outdir}')
        except FileNotFoundError:
            print("Directory doesnt exist...")

    generator = OpenAPIGen(outdir)
    if download:
        try:
            metajson = generator.getMetadata(url = METAURL)
            generator.addInChildMethods()
            generator.addInORMMethods()
            generator.saveMetadata()
        except Exception as e:
            print("========== ERROR ==========")
            print(f"{e}")
            print("========== ERROR ==========")
    else:
        metajson = generator.getLocalMetadata()

    print("Generating OpenAPI....")
    generator.generate()


if __name__ == "__main__":
    main()