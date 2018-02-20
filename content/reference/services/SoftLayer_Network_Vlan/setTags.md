---
title: "setTags"
description: "Tag a VLAN by passing in one or more tags separated by a comma. Tag references are cleared out every time this method is... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
---
# SoftLayer_Network_Vlan::setTags
## Overview 
Tag a VLAN by passing in one or more tags separated by a comma. Tag references are cleared out every time this method is called. If your VLAN is already tagged you will need to pass the current tags along with any new ones. To remove all tag references pass an empty string. To remove one or more tags omit them from the tag list. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|tags| string| Comma separated list of tags|


### Required Headers
* authenticate
* SoftLayer_Network_VlanInitParameters

### Optional Headers

### Return Values
boolean
