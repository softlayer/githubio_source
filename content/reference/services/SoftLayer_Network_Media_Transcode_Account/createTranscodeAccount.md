---
title: "createTranscodeAccount"
description: "With this method, you can create a transcode account.  Individual SoftLayer account can have a single Transcode account.... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Media_Transcode_Account"
aliases:
    - "/reference/services/softlayer_network_media_transcode_account/createTranscodeAccount"
---
# [SoftLayer_Network_Media_Transcode_Account](/reference/services/SoftLayer_Network_Media_Transcode_Account)::createTranscodeAccount


Creates a new transcode account


## Overview 
With this method, you can create a transcode account.  Individual SoftLayer account can have a single Transcode account. You have to pass your SoftLayer account id as a parameter. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception if a SoftLayer account is inactive or disabled. 

* SoftLayer_Exception_Public 

> Throw the exception if a user already has a Transcode account. 



