---
title: "getGraphImage"
description: "Retrieve a graph of a SoftLayer backbone's last 24 hours of activity. getGraphImage returns a PNG image measuring 827 pi... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Backbone"
aliases:
    - "/reference/services/softlayer_network_backbone/getGraphImage"
---
# [SoftLayer_Network_Backbone](/reference/services/SoftLayer_Network_Backbone)::getGraphImage

Retrieve a graph of a SoftLayer backbone's last 24 hours of activity.


## Overview 
Retrieve a graph of a SoftLayer backbone's last 24 hours of activity. getGraphImage returns a PNG image measuring 827 pixels by 293 pixels.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_BackboneInitParameters


### Return Values
* binary data

### External Links


* [Portable Network Graphics at Wikipedia](http://en.wikipedia.org/wiki/Portable_Network_Graphics)




### Error Handling

* SoftLayer_Exception 

> Throw the exception "Unable to load the image for the <backbone name> backbone graph" if the API is unable to retrieve a valid PNG image for the backbone. 



