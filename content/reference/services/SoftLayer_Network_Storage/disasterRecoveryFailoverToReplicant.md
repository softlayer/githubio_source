---
title: "disasterRecoveryFailoverToReplicant"
description: "If a volume (with replication) becomes inaccessible due to a disaster event, this method can be used to immediately failover to an available replica in another location. This method does not allow for fail back via the API. To fail back to the original volume after using this method, open a support ticket. To test failover, use [SoftLayer_Network_Storage::failoverToReplicant](reference/datatypes/$1/#$2) instead. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage"
---
