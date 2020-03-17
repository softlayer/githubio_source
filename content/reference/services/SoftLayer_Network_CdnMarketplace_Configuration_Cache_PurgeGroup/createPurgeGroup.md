---
title: "createPurgeGroup"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup"
aliases:
    - "/reference/services/softlayer_network_cdnmarketplace_configuration_cache_purgegroup/createPurgeGroup"
---
# [SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup)::createPurgeGroup

This method creates a purge group record in the table, and also initiates the purge action based on the input option value. The unsaved groups will be deleted after 15 days if no purge actions executed. The possible input option value can be: 1: (Default) Only purge the paths in the group, don't save the group as favorite. 2: Only save the group as favorite, don't purge the paths. 3: Save the group as favorite and also purge the paths in the group. 


## Overview 


-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|uniqueId| string| Domain mapping uniqueID|
|groupName| string| Name of purge group|
|paths| array of strings| Array of paths|
|option| integer| |


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup'>SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup </a>



### Error Handling

* SoftLayer_Exception 

> <<< EOT 



