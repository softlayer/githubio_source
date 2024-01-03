---
title: "getSubmittedRequest"
description: "Allows authorized IBMer to pull all the details of a single proof of concept account request. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_ProofOfConcept"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_ProofOfConcept"
---

# [REST Example](#getSubmittedRequest-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getSubmittedRequest-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_ProofOfConcept/getSubmittedRequest'
```
