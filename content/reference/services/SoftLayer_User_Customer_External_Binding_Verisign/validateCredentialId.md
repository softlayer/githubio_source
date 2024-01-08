---
title: "validateCredentialId"
description: "Validate the user id and VeriSign credential id used to create an external authentication binding. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding_Verisign"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_External_Binding_Verisign"
---

### [REST Example](#validateCredentialId-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#validateCredentialId-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_External_Binding_Verisign/validateCredentialId'
```
