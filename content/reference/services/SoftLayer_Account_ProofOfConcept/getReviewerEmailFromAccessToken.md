---
title: "getReviewerEmailFromAccessToken"
description: "Finds a reviewer's email using the access token "
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

### [REST Example](#getReviewerEmailFromAccessToken-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getReviewerEmailFromAccessToken-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_ProofOfConcept/getReviewerEmailFromAccessToken'
```
