---
title: "editObject"
description: "Edit the properties of a data transfer request record by passing in a modified instance of a SoftLayer_Account_Media_Data_Transfer_Request object. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Media_Data_Transfer_Request"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Media_Data_Transfer_Request"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Media_Data_Transfer_Request]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Media_Data_Transfer_Request/{SoftLayer_Account_Media_Data_Transfer_RequestID}/editObject'
```
