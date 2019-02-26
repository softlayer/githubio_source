---
title: "collectBandwidth"
description: "{{CloudLayerOnlyMethod}} 

collectBandwidth() Retrieve the bandwidth usage for the current billing cycle."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
aliases:
    - "/reference/services/softlayer_network_storage_iscsi/collectBandwidth"
---
# [SoftLayer_Network_Storage_Iscsi](/reference/services/SoftLayer_Network_Storage_Iscsi)::collectBandwidth

Retrieve the bandwidth usage for the current billing cycle.


## Overview 
{{CloudLayerOnlyMethod}} 

collectBandwidth() Retrieve the bandwidth usage for the current billing cycle. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|type| string| The bandwidth type to collect usage for (upload, download)|
|startDate| dateTime| The starting date of the range of data you wish to collect.|
|endDate| dateTime| The ending date of the range of data you wish to collect.|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_IscsiInitParameters


### Return Values
* unsigned long



### Error Handling

* SoftLayer_Exception 

> Throw the exception "The <nasType> Storage type is not supported for bandwidth used collection.  Please contact development." 



