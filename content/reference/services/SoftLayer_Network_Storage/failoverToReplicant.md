---
title: "failoverToReplicant"
description: "Failover to a volume replicant.  During the time which the replicant is in use the local nas volume will not be availabl... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
---
# SoftLayer_Network_Storage::failoverToReplicant
## Overview 
Failover to a volume replicant.  During the time which the replicant is in use the local nas volume will not be available. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|replicantId| integer| Replicant ID to failover to|


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters

### Optional Headers

### Return Values
boolean
