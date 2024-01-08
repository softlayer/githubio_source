---
title: "verifyReviewer"
description: "Verifies that a potential reviewer is an approved internal IBM employee "
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

### [REST Example](#verifyReviewer-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#verifyReviewer-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_ProofOfConcept/verifyReviewer'
```
