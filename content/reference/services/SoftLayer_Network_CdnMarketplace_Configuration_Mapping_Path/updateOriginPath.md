---
title: "updateOriginPath"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path"
aliases:
    - "/reference/services/softlayer_network_cdnmarketplace_configuration_mapping_path/updateOriginPath"
---
# [SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path)::updateOriginPath

SOAP API will update Origin Path for an existing mapping and for a particular customer. 

When passing the $input object as a parameter, it will expect the following properties to be set: $oldPath $uniqueId $originType, $path, $origin, $httpPort, $httpsPort, and if the path's origin type is object storage, the $bucketName and the $fileExtension. 

Out of the properties listed above only the following path properties are allowed to be changed: $path, $origin, $httpPort, $httpsPort These properties may not be changed: $originType 


## Overview 


-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|input| <a href='/reference/datatypes/SoftLayer_Container_Network_CdnMarketplace_Configuration_Input'>SoftLayer_Container_Network_CdnMarketplace_Configuration_Input </a>| |


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_CdnMarketplace_Configuration_Mapping_Path'>SoftLayer_Container_Network_CdnMarketplace_Configuration_Mapping_Path[] </a>




