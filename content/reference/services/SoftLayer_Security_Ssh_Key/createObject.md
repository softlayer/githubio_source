---
title: "createObject"
description: "Add a ssh key to your account for use during server provisioning and os reloads. "
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

# [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Security_Ssh_Key]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Security_Ssh_Key/createObject'
```
