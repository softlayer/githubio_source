---
title: "getSshKeys"
description: "SSH keys to be installed on the server during provisioning or an OS reload."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component_Password"
type: "reference"
layout: "method"
mainService : "SoftLayer_Software_Component_Password"
---

### [REST Example](#getSshKeys-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getSshKeys-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Software_Component_Password/{SoftLayer_Software_Component_PasswordID}/getSshKeys'
```
