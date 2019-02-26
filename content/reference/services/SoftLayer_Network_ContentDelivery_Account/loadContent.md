---
title: "loadContent"
description: "Whether you are using Origin Pull or POP Pull, your content will be transferred and cached on CDN POP (node) on the init... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_account/loadContent"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::loadContent

Loads content to all CDN nodes


## Overview 
Whether you are using Origin Pull or POP Pull, your content will be transferred and cached on CDN POP (node) on the initial request. If you wish to load your content to all CDN POPs, you may use this service to accomplish that. Please keep in mind, it will take about 10 to 15 minutes to load content to all CDN POPs depending on the load. 

You can only specify 5 URLs at a time. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|objectUrls| array of strings| |


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters


### Return Values
* boolean




