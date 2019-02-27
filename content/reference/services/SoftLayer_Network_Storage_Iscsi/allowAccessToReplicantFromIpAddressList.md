---
title: "allowAccessToReplicantFromIpAddressList"
description: "This method is used to modify the access control list for this Storage volume.  The SoftLayer_Network_Subnet_IpAddress o... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
aliases:
    - "/reference/services/softlayer_network_storage_iscsi/allowAccessToReplicantFromIpAddressList"
---
# [SoftLayer_Network_Storage_Iscsi](/reference/services/SoftLayer_Network_Storage_Iscsi)::allowAccessToReplicantFromIpAddressList

allow access to this volume from multiple SoftLayer_Network_Subnet_IpAddress objects.


## Overview 
This method is used to modify the access control list for this Storage volume.  The SoftLayer_Network_Subnet_IpAddress objects which have been allowed access to this storage will be listed in the allowedVirtualGuests property of this storage volume. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|ipAddressObjectTemplates| <a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>| |


### Required Headers
* authenticate
* SoftLayer_Network_Storage_IscsiInitParameters


### Return Values
* boolean




