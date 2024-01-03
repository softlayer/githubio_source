---
title: "isCurrentReviewer"
description: "Determines if the user is one of the reviewers currently able to act "
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

# [REST Example](#isCurrentReviewer-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#isCurrentReviewer-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_ProofOfConcept/isCurrentReviewer'
```
