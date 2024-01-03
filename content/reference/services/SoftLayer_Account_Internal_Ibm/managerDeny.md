---
title: "managerDeny"
description: "Denies a pending request and prevents additional requests from the same applicant for as long as the manager remains the same. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Internal_Ibm"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Internal_Ibm"
---

# [REST Example](#managerDeny-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#managerDeny-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Internal_Ibm/managerDeny'
```
