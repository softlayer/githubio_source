---
title: "editObject"
description: "Edit the properties of a secondary DNS record by passing in a modified instance of a SoftLayer_Dns_Secondary object. You may only edit the ''masterIpAddress'' and ''transferFrequency'' properties of your secondary DNS record. ''ZoneName'' may not be altered after a secondary DNS record has been created.  Please remove and re-create the record if you need to make changes to your zone name. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Secondary"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Secondary"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Dns_Secondary]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Secondary/{SoftLayer_Dns_SecondaryID}/editObject'
```
