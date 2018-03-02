---
title: "failoverToReplicant"
description: "Failover to a volume replicant.  During the time which the replicant is in use the local nas volume will not be availabl... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
---
# SoftLayer_Network_Storage_Iscsi::failoverToReplicant
## Overview 
Failover to a volume replicant.  During the time which the replicant is in use the local nas volume will not be available. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|replicantId| integer| Replicant ID to failover to|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_IscsiInitParameters

### Optional Headers

### Return Values
boolean

### External Links


* [In depth details on storage replication at Wikipedia](http://en.wikipedia.org/wiki/Storage_replication#Disk_storage_replication)


