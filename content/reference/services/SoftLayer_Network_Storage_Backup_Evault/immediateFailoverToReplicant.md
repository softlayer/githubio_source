---
title: "immediateFailoverToReplicant"
description: "Immediate Failover to a volume replicant.  During the time which the replicant is in use the local nas volume will not b... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
aliases:
    - "/reference/services/softlayer_network_storage_backup_evault/immediateFailoverToReplicant"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::immediateFailoverToReplicant


Immediate Failover to a volume replicant.


## Overview 
Immediate Failover to a volume replicant.  During the time which the replicant is in use the local nas volume will not be available. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|replicantId| integer| Replicant ID to failover to|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Backup_EvaultInitParameters


### Return Values
* boolean




