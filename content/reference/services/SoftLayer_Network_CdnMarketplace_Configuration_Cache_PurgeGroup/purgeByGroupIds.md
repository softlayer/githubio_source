---
title: "purgeByGroupIds"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup"
aliases:
    - "/reference/services/softlayer_network_cdnmarketplace_configuration_cache_purgegroup/purgeByGroupIds"
---
# [SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup)::purgeByGroupIds

This method purges the content from purge groups. 


## Overview 


-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|uniqueId| string| Domain mapping uniqueID|
|groupUniqueIds| array of strings| Array of purge group uniqueID|


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroupHistory'>SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroupHistory[] </a>



### Error Handling

* SoftLayer_Exception<<< 

> EOT 



