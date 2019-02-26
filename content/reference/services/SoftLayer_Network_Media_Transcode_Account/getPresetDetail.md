---
title: "getPresetDetail"
description: "This method returns an array of [[SoftLayer_Container_Network_Media_Transcode_Preset_Element|preset element]] objects. E... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Media_Transcode_Account"
aliases:
    - "/reference/services/softlayer_network_media_transcode_account/getPresetDetail"
---
# [SoftLayer_Network_Media_Transcode_Account](/reference/services/SoftLayer_Network_Media_Transcode_Account)::getPresetDetail

Returns details on a transcode output preset


## Overview 
This method returns an array of [[SoftLayer_Container_Network_Media_Transcode_Preset_Element|preset element]] objects. Each preset has its own collection of preset elements such as encoder, frame rate, aspect ratio and so on. Each element object has a default value for itself and an array of [[SoftLayer_Container_Network_Media_Transcode_Preset_Element_Option|element option]] objects. For example, "Frame Rate" element for "Windows Media 9 - Download - 1 Mbps - NTSC - Constrained VBR" preset has 19 element options. 15.0 frame rate is selected by default.  Currently, you are not able to change the default value. Customizing these values may be possible in the future. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|guid| string| The unique id of a preset|


### Required Headers
* authenticate
* SoftLayer_Network_Media_Transcode_AccountInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_Media_Transcode_Preset_Element'>SoftLayer_Container_Network_Media_Transcode_Preset_Element[] </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throw an exception if connection to a Transcode server fails. 



