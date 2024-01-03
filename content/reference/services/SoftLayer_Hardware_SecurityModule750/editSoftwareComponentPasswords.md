---
title: "editSoftwareComponentPasswords"
description: "Edit the properties of a software component password such as the username, password, and notes. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_SecurityModule750"
---

# [REST Example](#editSoftwareComponentPasswords-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editSoftwareComponentPasswords-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Software_Component_Password]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule750/{SoftLayer_Hardware_SecurityModule750ID}/editSoftwareComponentPasswords'
```
