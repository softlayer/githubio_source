---
title: "getPresets"
description: "A transcode preset is a configuration that defines a certain media output. This method returns an array of transcoding p... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Media_Transcode_Account"
aliases:
    - "/reference/services/softlayer_network_media_transcode_account/getPresets"
---
# [SoftLayer_Network_Media_Transcode_Account](/reference/services/SoftLayer_Network_Media_Transcode_Account)::getPresets


Returns an array of transcoding preset objects


## Overview 
A transcode preset is a configuration that defines a certain media output. This method returns an array of transcoding preset objects supported by SoftLayer's Transcode server. Each [SoftLayer_Container_Network_Media_Transcode_Preset]({{<ref "reference/datatypes/SoftLayer_Container_Network_Media_Transcode_Preset">}}) contains a GUID property. You will need a GUID string when you create a new transcode job. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Media_Transcode_AccountInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_Media_Transcode_Preset'>SoftLayer_Container_Network_Media_Transcode_Preset[] </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throw an exception if connection to a Transcode server fails. 



