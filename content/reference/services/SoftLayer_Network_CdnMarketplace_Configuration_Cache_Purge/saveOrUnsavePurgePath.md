---
title: "saveOrUnsavePurgePath"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge"
aliases:
    - "/reference/services/softlayer_network_cdnmarketplace_configuration_cache_purge/saveOrUnsavePurgePath"
---
# [SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge)::saveOrUnsavePurgePath

Creates a new saved purge if a purge path is saved. Deletes a saved purge record if the path is unsaved. 


## Overview 


-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|uniqueId| string| |
|path| string| |
|saveOrUnsave| integer| |


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_Purge'>SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_Purge[] </a>



### Error Handling

* SoftLayer_Exception 

> <<< EOT 



