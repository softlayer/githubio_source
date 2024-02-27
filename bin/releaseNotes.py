#!python

import click
import os
import logging
import requests
import json
import re
from datetime import date
from pprint import pprint as pp
# from http.client import HTTPConnection
from rich.console import Console




class JiraAPI():
    def __init__(self, apitoken):
        self.apitoken = apitoken
        self.jira_url = 'https://jira.softlayer.local/rest/api/2'
        self.headers = {"Authorization": f"Bearer {self.apitoken}", "Content-Type": "application/json"}
        self.console = Console()
        self.releases = []
        self.internal =  re.compile(r"internal", re.I)

    def getReleaseJiras(self):
        jql_project = """project = JIRA"""
        jql_type = """type = "Production Release" """
        jql_start = """ "Release Estimated Start Time" >= startOfDay(-7d) """
        jql_orderby = """ORDER BY "Release Estimated Start Time" DESC"""
        jql_status = """status = Resolved"""
        jql = f"{jql_project} AND {jql_type} AND {jql_start} AND {jql_status} {jql_orderby}"
        apirequest = f"{self.jira_url}/search?jql={jql}"
        result = requests.get(apirequest, headers=self.headers, verify=True)

        return self.jiraToJson(result)

    def getNotes(self, jira_issue):
        result = requests.get(jira_issue, headers=self.headers, verify=True)
        json = self.jiraToJson(result)
        return json.get('fields', {}).get('customfield_10113', 'NONE')


    def processReleases(self, releases):
        r_issues = releases.get('issues', [])
        for issue in r_issues:
            fileds  = issue.get('fields', {})
            this_issue = {
                "key": issue.get('key'),
                "resolution": fileds.get('resolution', {}).get('name', 'None'),
                "summary": fileds.get('summary'),
                "issues": []
            }
            for sub_issue in fileds.get('issuelinks', []):
                outward_issue = sub_issue.get('outwardIssue')
                released = {
                    "key": outward_issue.get('key'),
                    "self": outward_issue.get('self'),
                    "summary": outward_issue.get('fields').get('summary'),
                    "notes": self.getNotes(outward_issue.get('self'))
                }
                this_issue['issues'].append(released)

            self.releases.append(this_issue)
        return self.releases


    def jiraToJson(self, result):
        if result.status_code == 200:
            raw_json = result.json()
            # self.console.print_json(data=raw_json)
            return raw_json
        else:
            raise Exception(f"ERROR {result.status_code}: {result.text}")

    def printIssues(self, issues):
        for issue in issues:
            self.console.print(f"[orange3]{issue['key']}, {issue['summary']}, {issue['resolution']}", highlight=False)
            for sub_issue in issue.get('issues'):
                notes = sub_issue.get('notes')
                color = "green"
                isInternal = self.internal.search(notes)
                if isInternal:
                    color = "red"
                self.console.print(f"\t[{color}]{sub_issue.get('key')}, {notes}, {sub_issue.get('summary')}", highlight=False)

    def printReleaseNotes(self, issues):
        today = date.today()
        template = f"""---
title: "Release notes: {today.strftime('%B %d, %Y')}"
date: "{today.isoformat()}"
tags:
    - "release notes"
---

#### API
"""
        self.console.print(template)
        for issue in issues:
            for sub_issue in issue.get('issues'):
                notes = sub_issue.get('notes')
                isInternal = self.internal.search(notes)
                if isInternal is None:
                    self.console.print(f"- {notes}. {sub_issue.get('summary')} {sub_issue.get('key')}")


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
    parsed = j_api.processReleases(releases)
    j_api.printIssues(parsed)
    j_api.printReleaseNotes(parsed)

    

if __name__ == "__main__":
    cli()
