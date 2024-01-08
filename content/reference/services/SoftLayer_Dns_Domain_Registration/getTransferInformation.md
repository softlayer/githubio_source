---
title: "getTransferInformation"
description: "The getTransferInformation method checks to see if the domain can be transferred and also can be used to check the status of the last transfer request. "
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

### [REST Example](#getTransferInformation-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getTransferInformation-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_Registration/getTransferInformation'
```
