---
title: "getRegionalInternetRegistryHandle"
description: "The RIR handle that this registration object belongs to. This field may not be populated until the registration is complete."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Registration"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet_Registration"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_Registration/{SoftLayer_Network_Subnet_RegistrationID}/getRegionalInternetRegistryHandle'
```
