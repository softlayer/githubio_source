---
title: "setOsPasswordFromEncrypted"
description: "The setOsPasswordFromEncrypted method is used to set the operating system password from a key/pair encrypted password signed by SoftLayer. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Resource"
classes:
    - "SoftLayer_Resource_Configuration"
type: "reference"
layout: "method"
mainService : "SoftLayer_Resource_Configuration"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Resource_Configuration/{SoftLayer_Resource_ConfigurationID}/setOsPasswordFromEncrypted'
```
