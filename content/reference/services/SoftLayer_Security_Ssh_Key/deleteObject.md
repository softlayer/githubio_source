---
title: "deleteObject"
description: "Remove a ssh key from your account. "
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

### [REST Example](#deleteObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Security_Ssh_Key/{SoftLayer_Security_Ssh_KeyID}/deleteObject'
```
