---
title: "getAdministratorEmailDomains"
description: "Gets the email domains that can be used to validate a certificate to a domain. "
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

### [REST Example](#getAdministratorEmailDomains-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAdministratorEmailDomains-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Security_Certificate_Request/getAdministratorEmailDomains'
```
