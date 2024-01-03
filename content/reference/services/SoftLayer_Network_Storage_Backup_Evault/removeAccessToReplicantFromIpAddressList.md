---
title: "removeAccessToReplicantFromIpAddressList"
description: "This method is used to modify the access control list for this Storage volume's replica.  The SoftLayer_Network_Subnet_IpAddress objects which have been allowed access to this storage volume's replica will be listed in the allowedReplicationIpAddresses property of this storage volume. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Backup_Evault"
---

# [REST Example](#removeAccessToReplicantFromIpAddressList-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#removeAccessToReplicantFromIpAddressList-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Subnet_IpAddress]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage_Backup_Evault/{SoftLayer_Network_Storage_Backup_EvaultID}/removeAccessToReplicantFromIpAddressList'
```
