---
title: "editObject"
description: "Update a ssh key. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Ssh_Key"
type: "reference"
layout: "method"
mainService : "SoftLayer_Security_Ssh_Key"
---

# [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Security_Ssh_Key]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Security_Ssh_Key/{SoftLayer_Security_Ssh_KeyID}/editObject'
```
