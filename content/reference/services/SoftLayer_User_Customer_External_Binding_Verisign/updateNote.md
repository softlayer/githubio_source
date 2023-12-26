---
title: "updateNote"
description: "Update the note of an external binding.  The note is an optional property that is used to store information about a binding. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_External_Binding_Verisign/{SoftLayer_User_Customer_External_Binding_VerisignID}/updateNote'
```
