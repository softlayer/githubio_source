#!python

import click
import os
import logging
import requests
import json
from pprint import pprint as pp
# from http.client import HTTPConnection

# Color Chart: https://rich.readthedocs.io/en/stable/appendix/colors.html#appendix-colors
jira_url = 'https://jira.softlayer.local/rest/api/2'
# https://jira.softlayer.local/issues/?filter=26578&jql=project%20%3D%20JIRA%20AND%20type%20%3D%20"Production%20Release"%20AND%20created%20>%3D%20startOfDay(-90d)%20ORDER%20BY%20"Release%20Estimated%20Start%20Time"%20DESC
@click.command()
@click.option('--debug', default=False, is_flag=True, help="Show debug level output")
def cli(debug):
    """CLI entrypoint"""

    apitoken = os.getenv('SL_JIRA_TOKEN')
    if not apitoken:
        raise click.UsageError("APITOKEN env variable is not set")
    else:
        print(f"APITOKEN={apitoken}")

    print("Ok Doing the thing")
    jql = """project%20%3D%20JIRA%20AND%20type%20%3D%20"Production%20Release"%20AND%20created%20>%3D%20startOfDay(-90d)%20ORDER%20BY%20"Release%20Estimated%20Start%20Time"%20DESC"""
    apirequest = f"{jira_url}/search?jql={jql}"
    headers = {"Authorization": f"Bearer {apitoken}", "Content-Type": "application/json"}
    result = requests.get(apirequest, headers=headers, verify=False)
    if result.status_code == 200:
        print("OK THIS WORKS")
        pp(result.json())
    else:
        print(f"ERROR: {result.text}")
    

if __name__ == "__main__":
    cli()
