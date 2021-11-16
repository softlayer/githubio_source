---
title: "disasterRecoveryFailoverToReplicant"
description: "If a volume (with replication) becomes inaccessible due to a disaster event, this method can be used to immediately fail... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
aliases:
    - "/reference/services/softlayer_network_storage/disasterRecoveryFailoverToReplicant"
---
# [SoftLayer_Network_Storage](/reference/services/SoftLayer_Network_Storage)::disasterRecoveryFailoverToReplicant


Failover an inaccessible block/file volume to its available replicant volume.


## Overview 
If a volume (with replication) becomes inaccessible due to a disaster event, this method can be used to immediately failover to an available replica in another location. This method does not allow for fail back via the API. To fail back to the original volume after using this method, open a support ticket. To test failover, use [SoftLayer_Network_Storage::failoverToReplicant]({{<ref "reference/services/SoftLayer_Network_Storage/failoverToReplicant">}}) instead. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|replicantId| integer| Replicant ID to failover to|


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters


### Return Values
* boolean




