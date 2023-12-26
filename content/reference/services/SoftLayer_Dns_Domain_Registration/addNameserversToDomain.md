---
title: "addNameserversToDomain"
description: "The addNameserversToDomain method adds nameservers to a domain for a domain that already has nameservers assigned to it. This method does not create a nameserver; the nameserver must already exist. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Registration"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Domain_Registration"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_Registration/{SoftLayer_Dns_Domain_RegistrationID}/addNameserversToDomain'
```
