---
title: "allowAccessToReplicantFromSubnet"
description: "This method is used to modify the access control list for this Storage replicant volume.  The SoftLayer_Network_Subnet o... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
aliases:
    - "/reference/services/softlayer_network_storage/allowAccessToReplicantFromSubnet"
---
# [SoftLayer_Network_Storage](/reference/services/SoftLayer_Network_Storage)::allowAccessToReplicantFromSubnet

Allow access to this replicant volume from multiple SoftLayer_Network_Subnet objects.


## Overview 
This method is used to modify the access control list for this Storage replicant volume.  The SoftLayer_Network_Subnet objects which have been allowed access to this storage will be listed in the allowedHardware property of this storage replicant volume. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|subnetObjectTemplate| <a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>| |


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters


### Return Values
* boolean




