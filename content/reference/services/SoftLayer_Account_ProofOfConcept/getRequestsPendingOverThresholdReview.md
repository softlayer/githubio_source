---
title: "getRequestsPendingOverThresholdReview"
description: "Retrieves a list of requests that are pending over threshold review "
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

### [REST Example](#getRequestsPendingOverThresholdReview-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRequestsPendingOverThresholdReview-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_ProofOfConcept/getRequestsPendingOverThresholdReview'
```
