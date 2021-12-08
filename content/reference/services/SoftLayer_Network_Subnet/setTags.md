---
title: "setTags"
description: "Tag a subnet by passing in one or more tags separated by a comma. Any existing tags you wish to keep should be included... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
aliases:
    - "/reference/services/softlayer_network_subnet/setTags"
---
# [SoftLayer_Network_Subnet](/reference/services/SoftLayer_Network_Subnet)::setTags





## Overview 
Tag a subnet by passing in one or more tags separated by a comma. Any existing tags you wish to keep should be included in the set of tags, as any missing tags will be removed. To remove all tags from the subnet, send an empty string. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|tags| string| Comma separated list of tags|


### Required Headers
* authenticate
* SoftLayer_Network_SubnetInitParameters


### Return Values
* boolean




