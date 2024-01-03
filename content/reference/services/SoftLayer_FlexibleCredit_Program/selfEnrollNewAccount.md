---
title: "selfEnrollNewAccount"
description: ""
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "FlexibleCredit"
classes:
    - "SoftLayer_FlexibleCredit_Program"
type: "reference"
layout: "method"
mainService : "SoftLayer_FlexibleCredit_Program"
---

# [REST Example](#selfEnrollNewAccount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#selfEnrollNewAccount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_FlexibleCredit_Program/{SoftLayer_FlexibleCredit_ProgramID}/selfEnrollNewAccount'
```
