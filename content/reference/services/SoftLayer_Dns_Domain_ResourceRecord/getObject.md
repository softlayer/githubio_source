---
title: "getObject"
description: "getObject retrieves the SoftLayer_Dns_Domain_ResourceRecord object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Dns_Domain_ResourceRecord service. You can only retrieve resource records belonging to domains that are assigned to your SoftLayer account. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Domain_ResourceRecord"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_ResourceRecord/{SoftLayer_Dns_Domain_ResourceRecordID}/getObject'
```
