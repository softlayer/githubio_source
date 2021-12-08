---
title: "allowAccessToReplicantFromHardwareList"
description: "This method is used to modify the access control list for this Storage volume's replica.  The SoftLayer_Hardware objects... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
aliases:
    - "/reference/services/softlayer_network_storage_backup_evault/allowAccessToReplicantFromHardwareList"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::allowAccessToReplicantFromHardwareList


allow access to this volume's replica from multiple SoftLayer_Hardware objects.


## Overview 
This method is used to modify the access control list for this Storage volume's replica.  The SoftLayer_Hardware objects which have been allowed access to this storage volume's replica will be listed in the allowedReplicationHardware property of this storage volume. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareObjectTemplates| <a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>| |


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Backup_EvaultInitParameters


### Return Values
* boolean




