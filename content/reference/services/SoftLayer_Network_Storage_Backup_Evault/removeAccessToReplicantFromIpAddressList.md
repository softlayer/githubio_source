---
title: "removeAccessToReplicantFromIpAddressList"
description: "This method is used to modify the access control list for this Storage volume's replica.  The SoftLayer_Network_Subnet_I... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
aliases:
    - "/reference/services/softlayer_network_storage_backup_evault/removeAccessToReplicantFromIpAddressList"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::removeAccessToReplicantFromIpAddressList


Remove access to this replica volume's replica from multiple SoftLayer_Network_Subnet_IpAddress objects.


## Overview 
This method is used to modify the access control list for this Storage volume's replica.  The SoftLayer_Network_Subnet_IpAddress objects which have been allowed access to this storage volume's replica will be listed in the allowedReplicationIpAddresses property of this storage volume. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|ipAddressObjectTemplates| <a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>| |


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Backup_EvaultInitParameters


### Return Values
* boolean




