---
title: "getStatisticsGraphImage"
description: "Retrieve a graph of a SoftLayer datacenter's last 48 hours of network activity. Statistics graphs show traffic outbound... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Datacenter"
aliases:
    - "/reference/services/softlayer_location_datacenter/getStatisticsGraphImage"
---
# [SoftLayer_Location_Datacenter](/reference/services/SoftLayer_Location_Datacenter)::getStatisticsGraphImage

Retrieve a graph of a SoftLayer datacenter's last 48 hours of network activity.


## Overview 
Retrieve a graph of a SoftLayer datacenter's last 48 hours of network activity. Statistics graphs show traffic outbound from a datacenter on top and inbound traffic on the bottom followed by a legend of the network services tracked in the graph. getStatisticsGraphImage returns a PNG image of variable width and height depending on the number of services reported in the image. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Location_DatacenterInitParameters

### Optional Headers

### Return Values
binary data

### External Links


* [Portable Network Graphics at Wikipedia](http://en.wikipedia.org/wiki/Portable_Network_Graphics)


