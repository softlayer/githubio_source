---
title: "deleteSoftwareComponentPasswords"
description: "Delete software component passwords. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Server"
---

# [REST Example](#deleteSoftwareComponentPasswords-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteSoftwareComponentPasswords-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Software_Component_Password]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Server/{SoftLayer_Hardware_ServerID}/deleteSoftwareComponentPasswords'
```
