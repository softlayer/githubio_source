---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_Customer_Subnet object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Network_Customer_Subnet service. You can only retrieve the subnet whose account matches the account that your portal user is assigned to. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Customer_Subnet"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Customer_Subnet"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Customer_Subnet/{SoftLayer_Network_Customer_SubnetID}/getObject'
```
