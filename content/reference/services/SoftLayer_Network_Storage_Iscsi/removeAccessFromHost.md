---
title: "removeAccessFromHost"
description: "This method is used to modify the access control list for this Storage volume.  The [[SoftLayer_Hardware|SoftLayer_Virtual_Guest|SoftLayer_Network_Subnet|SoftLayer_Network_Subnet_IpAddress]] objects which have been allowed access to this storage will be listed in the [[allowedHardware|allowedVirtualGuests|allowedSubnets|allowedIpAddresses]] property of this storage volume. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Iscsi"
---

# [REST Example](#removeAccessFromHost-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeAccessFromHost-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Iscsi/{SoftLayer_Network_Storage_IscsiID}/removeAccessFromHost'
```
