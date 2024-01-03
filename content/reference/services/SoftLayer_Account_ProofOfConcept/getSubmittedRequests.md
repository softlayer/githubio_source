---
title: "getSubmittedRequests"
description: "Allows authorized IBMer to retrieve a list summarizing all previously submitted proof of concept requests. 

Note that the proof of concept system is for internal IBM employees only and is not applicable to users outside the IBM organization. "
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

# [REST Example](#getSubmittedRequests-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getSubmittedRequests-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_ProofOfConcept/getSubmittedRequests'
```
