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
import concurrent.futures as cf
import time



class JiraAPI():
    def __init__(self, apitoken, debug=False):
        self.apitoken = apitoken
        self.jira_url = 'https://jira.softlayer.local/rest/api/2'
        self.headers = {"Authorization": f"Bearer {self.apitoken}", "Content-Type": "application/json"}
        self.console = Console(highlight=None)
        self.releases = []
        self.internal =  re.compile(r"internal", re.I)
        self.debug = debug
        #self.verify = '/etc/ssl/certs/allCAbundle.pem'
        self.verify = False

    def getReleaseJiras(self, days=7):
        jql_project = """project = JIRA"""
        jql_type = """type = "Production Release" """
        jql_start = f""" "Release Estimated Start Time" >= startOfDay(-{days}d) """
        jql_orderby = """ORDER BY "Release Estimated Start Time" DESC"""
        jql_status = """status = Resolved"""
        jql = f"{jql_project} AND {jql_type} AND {jql_start} AND {jql_status} {jql_orderby}"
        apirequest = f"{self.jira_url}/search?jql={jql}"
        self.printDebug(f"Calling {apirequest}")
        result = requests.get(apirequest, headers=self.headers, verify=self.verify)
        # sleep a bit so we don't get rate limited
        time.sleep(0.2)
        return self.jiraToJson(result)

    def getNotes(self, jira_issue):
        self.printDebug(f"Getting JIRA: {jira_issue}")
        result = requests.get(jira_issue, headers=self.headers, verify=self.verify)
        json = self.jiraToJson(result)
        return json.get('fields', {}).get('customfield_10113', 'NONE')


    def processReleases(self, releases):
        r_issues = releases.get('issues', [])
        for issue in r_issues:
            # Slow things down otherwise we get rate limited
            time.sleep(0.5)
            fileds  = issue.get('fields', {})
            this_issue = {
                "key": issue.get('key'),
                "resolution": fileds.get('resolution', {}).get('name', 'None'),
                "summary": fileds.get('summary'),
                "issues": []
            }
            for sub_issue in fileds.get('issuelinks', []):
                released = self.processSubIssue(sub_issue)
                this_issue['issues'].append(released)

            self.releases.append(this_issue)
        return self.releases

    def processReleasesWithThreads(self, releases):
        """does processReleases, but uses threads. for some reason it seems slower than doing 1 at a time"""
        r_issues = releases.get('issues', [])
        for issue in r_issues:
            fileds  = issue.get('fields', {})
            this_issue = {
                "key": issue.get('key'),
                "resolution": fileds.get('resolution', {}).get('name', 'None'),
                "summary": fileds.get('summary'),
                "issues": []
            }
            with cf.ThreadPoolExecutor(max_workers=10) as executor:
                issueLinks = fileds.get('issuelinks', [])
                self.printDebug(f"{this_issue.get('key')} has {len(issueLinks)} sub issues")
                futures = {executor.submit(self.processSubIssue, sub_issue): sub_issue for sub_issue in issueLinks}
                for future in cf.as_completed(futures):                
                    this_issue['issues'].append(future.result())

            self.releases.append(this_issue)
        return self.releases

    def processSubIssue(self, sub_issue={}):
        outward_issue = sub_issue.get('outwardIssue', {})
        if not outward_issue:
            self.printDebug(f"{sub_issue} is empty???")
            return {"key": "", "self": "", "summary": "", "notes": ""}
        released = {
            "key": outward_issue.get('key'),
            "self": outward_issue.get('self'),
            "summary": outward_issue.get('fields').get('summary'),
            "notes": self.getNotes(outward_issue.get('self'))
        }
        return released     

    def jiraToJson(self, result):
        if result.status_code == 200:
            raw_json = result.json()
            # self.console.print_json(data=raw_json)
            return raw_json
        else:
            raise Exception(f"ERROR {result.status_code}: {result.text}")

    def printIssues(self, issues):
        for issue in issues:
            self.console.print(f"[orange3]{issue['key']}, {issue['summary']}, {issue['resolution']}")
            for sub_issue in issue.get('issues'):
                notes = sub_issue.get('notes')
                color = "green"
                isInternal = self.internal.search(notes)
                if isInternal:
                    color = "red"
                self.console.print(f"\t[{color}]{sub_issue.get('key')}, {notes}, {sub_issue.get('summary')}")

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
        self.console.print(template, highlight=False)
        for issue in issues:
            for sub_issue in issue.get('issues'):
                notes = sub_issue.get('notes')
                isInternal = self.internal.search(notes)
                if isInternal is None:
                    self.console.print(f"- {notes}. {sub_issue.get('summary')} {sub_issue.get('key')}")

    def printDebug(self, message):
        if self.debug:
            self.console.print(f"[gold3][[DEBUG]] {message}", highlight=False)


# Color Chart: https://rich.readthedocs.io/en/stable/appendix/colors.html#appendix-colors
@click.command()
@click.option('--debug', default=False, is_flag=True, help="Show debug level output")
@click.option('--days', default=7, help="How many days in the past to search for issues.")
def cli(debug, days):
    """CLI entrypoint"""

    apitoken = os.getenv('SL_JIRA_TOKEN')
    # I'm not sure why this has to be set along with verify, but it works this way.
    os.environ['SSL_CERT_FILE'] = '/etc/ssl/certs/allCAbundle.pem'
    if not apitoken:
        raise click.UsageError("APITOKEN env variable is not set")

    j_api = JiraAPI(apitoken, debug)
    releases = j_api.getReleaseJiras(days)
    #parsed = j_api.processReleasesWithThreads(releases)
    parsed = j_api.processReleases(releases)
    j_api.printIssues(parsed)
    j_api.printReleaseNotes(parsed)

    

if __name__ == "__main__":
    cli()
