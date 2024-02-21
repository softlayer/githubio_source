#!python

import click
import os
import logging
import requests
import json
from pprint import pprint as pp
# from http.client import HTTPConnection
from rich.console import Console

def printIssues(issues):
    for issue in issues:
        fields = issue.get('fields')
        print(f"{issue.get('key')} {fields.get('summary')}")


class JiraAPI():
    def __init__(self, apitoken):
        self.apitoken = apitoken
        self.jira_url = 'https://jira.softlayer.local/rest/api/2'
        self.headers = {"Authorization": f"Bearer {self.apitoken}", "Content-Type": "application/json"}
        self.console = Console()

    def getReleaseJiras(self):
        jql_project = """project = JIRA"""
        jql_type = """type = "Production Release" """
        jql_start = """ "Release Estimated Start Time" >= startOfDay(-7d) """
        jql_orderby = """ORDER BY "Release Estimated Start Time" DESC"""
        jql_status = """status = Resolved"""
        jql = f"{jql_project} AND {jql_type} AND {jql_start} AND {jql_status} {jql_orderby}"
        apirequest = f"{self.jira_url}/search?jql={jql}"
        result = requests.get(apirequest, headers=self.headers, verify=False)
        if result.status_code == 200:
            raw_json = result.json()
            self.console.print_json(data=raw_json)
            return raw_json
            # printIssues(raw_json.get('issues', []))
        else:
            print(f"ERROR {result.status_code}: {result.text}")
        return None

# Color Chart: https://rich.readthedocs.io/en/stable/appendix/colors.html#appendix-colors
@click.command()
@click.option('--debug', default=False, is_flag=True, help="Show debug level output")
def cli(debug):
    """CLI entrypoint"""

    apitoken = os.getenv('SL_JIRA_TOKEN')
    if not apitoken:
        raise click.UsageError("APITOKEN env variable is not set")

    j_api = JiraAPI(apitoken)
    releases = j_api.getReleaseJiras()
    printIssues(releases.get('issues'))

    

if __name__ == "__main__":
    cli()
