---
title: "forceRebuildvSRXCluster"
description: "Purpose is to rebuild the target Gateway cluster with the specified OS price id. Method will remove the current OS and a... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway"
aliases:
    - "/reference/services/softlayer_network_gateway/forceRebuildvSRXCluster"
---
# [SoftLayer_Network_Gateway](/reference/services/SoftLayer_Network_Gateway)::forceRebuildvSRXCluster


Rebuild HA GAteway


## Overview 
Purpose is to rebuild the target Gateway cluster with the specified OS price id. Method will remove the current OS and apply the default vSRX configuration settings. This will result in an extended OUTAGE!! Any custom configuration settings must be re-applied after the forced rebuild is completed. This is a DESTRUCTIVE action, use with caution. 



-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|osPriceId| integer| Price Id of the OS to use for rebuild|


### Required Headers
* authenticate
* SoftLayer_Network_GatewayInitParameters


### Return Values
* boolean




