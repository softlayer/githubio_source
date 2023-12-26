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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_ProofOfConcept/getReviewerEmailFromAccessToken'
```
