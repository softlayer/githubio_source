---
title: "activatePartner"
description: "This service enables a partner account that has been created but is currently inactive. This restricted service is only available for certain accounts. Please contact support for questions. "
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

### [REST Example](#activatePartner-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#activatePartner-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/activatePartner'
```
