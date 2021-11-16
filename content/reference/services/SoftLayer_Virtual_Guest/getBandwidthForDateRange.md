---
title: "getBandwidthForDateRange"
description: "Retrieve a collection of bandwidth data from an individual public or private network tracking object. Data is ideal if y... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/getBandwidthForDateRange"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::getBandwidthForDateRange


Retrieve bandwidth data from a tracking object.


## Overview 
Retrieve a collection of bandwidth data from an individual public or private network tracking object. Data is ideal if you with to employ your own traffic storage and graphing systems. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDate| dateTime| |
|endDate| dateTime| |


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data'>SoftLayer_Metric_Tracking_Object_Data[] </a>




