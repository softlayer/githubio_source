---
title: "validateHostsAccess"
description: "This method is used to validate if the hosts are behind gateway or not from [SoftLayer_Network_Subnet|SoftLayer_Network_Subnet_IpAddress] objects. This returns [SoftLayer_Container_Network_Storage_HostsGatewayInformation] object containing the host details along with a boolean attribute which indicates if it's behind the gateway or not. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage"
---

# [REST Example](#validateHostsAccess-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#validateHostsAccess-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Network_Storage_Host]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage/{SoftLayer_Network_StorageID}/validateHostsAccess'
```
