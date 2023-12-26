---
title: "editObject"
description: "Edit the object by passing in a modified instance of the object "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Authentication_Saml"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Authentication_Saml"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Authentication_Saml]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Authentication_Saml/{SoftLayer_Account_Authentication_SamlID}/editObject'
```
