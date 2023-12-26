---
title: "resendEmail"
description: "A Certificate Authority sends out various emails to your domain administrator or your technical contact. Use this service to have these emails re-sent. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Certificate_Request"
type: "reference"
layout: "method"
mainService : "SoftLayer_Security_Certificate_Request"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Security_Certificate_Request/{SoftLayer_Security_Certificate_RequestID}/resendEmail'
```
