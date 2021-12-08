---
title: "updateDomainMapping"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Configuration_Mapping"
aliases:
    - "/reference/services/softlayer_network_cdnmarketplace_configuration_mapping/updateDomainMapping"
---
# [SoftLayer_Network_CdnMarketplace_Configuration_Mapping](/reference/services/SoftLayer_Network_CdnMarketplace_Configuration_Mapping)::updateDomainMapping


SOAP API will update the Domain Mapping identified by the Unique Id. Following fields are allowed to be changed: originHost, HttpPort/HttpsPort, RespectHeaders, ServeStale 

Additionally, bucketName and fileExtension if OriginType is Object Store 


## Overview 


-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|input| <a href='/reference/datatypes/SoftLayer_Container_Network_CdnMarketplace_Configuration_Input'>SoftLayer_Container_Network_CdnMarketplace_Configuration_Input </a>| |


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_CdnMarketplace_Configuration_Mapping'>SoftLayer_Container_Network_CdnMarketplace_Configuration_Mapping[] </a>




