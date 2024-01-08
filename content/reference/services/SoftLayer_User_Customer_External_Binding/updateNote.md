---
title: "updateNote"
description: "Update the note of an external binding.  The note is an optional property that is used to store information about a binding. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_External_Binding"
---

### [REST Example](#updateNote-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateNote-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_External_Binding/{SoftLayer_User_Customer_External_BindingID}/updateNote'
```
