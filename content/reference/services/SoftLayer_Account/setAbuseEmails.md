---
title: "setAbuseEmails"
description: "Set this account's abuse emails. Takes an array of email addresses as strings. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---

# [REST Example](#setAbuseEmails-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#setAbuseEmails-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/setAbuseEmails'
```
