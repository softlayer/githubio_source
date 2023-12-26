---
title: "addNsRecord"
description: "The global load balancer service has been deprecated and is no longer available. 

If your globally load balanced domain is hosted on the SoftLayer nameservers this method will add the required NS resource record to your DNS zone file and remove any A records that match the host portion of a global load balancer account hostname. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Global_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LoadBalancer_Global_Account"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LoadBalancer_Global_Account/{SoftLayer_Network_LoadBalancer_Global_AccountID}/addNsRecord'
```
