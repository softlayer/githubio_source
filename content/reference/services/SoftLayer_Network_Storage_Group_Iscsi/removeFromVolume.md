---
title: "removeFromVolume"
description: "Use this method to remove a SoftLayer_Network_Storage volume from this group.  This will automatically disable access to... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Group_Iscsi"
aliases:
    - "/reference/services/softlayer_network_storage_group_iscsi/removeFromVolume"
---
# [SoftLayer_Network_Storage_Group_Iscsi](/reference/services/SoftLayer_Network_Storage_Group_Iscsi)::removeFromVolume


Remove a SoftLayer_Network_Storage volume from this group


## Overview 
Use this method to remove a SoftLayer_Network_Storage volume from this group.  This will automatically disable access to this volume for any SoftLayer_Network_Storage_Allowed_Host objects currently attached to this group. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|volume| <a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>| |


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Group_IscsiInitParameters


### Return Values
* boolean




