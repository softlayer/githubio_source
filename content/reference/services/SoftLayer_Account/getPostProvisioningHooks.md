---
title: "getPostProvisioningHooks"
description: "Customer specified URIs that are downloaded onto a newly provisioned or reloaded server. If the URI is sent over https it will be executed directly on the server."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getPostProvisioningHooks'
```
