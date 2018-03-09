---
title: "getBandwidthData"
description: "This method returns bandwidth data for a given time range.  It returns an array of [[SoftLayer_Container_Network_Content... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::getBandwidthData

Returns bandwidth data for a time range


## Overview 
This method returns bandwidth data for a given time range.  It returns an array of [[SoftLayer_Container_Network_ContentDelivery_Bandwidth_Summary|bandwidth summary]] objects. [[SoftLayer_Container_Network_ContentDelivery_Bandwidth_Summary|Bandwidth summary]] object contains a beginning time, ending time, and bandwidth in bytes. 

A Beginning and ending date parameters have to be a timestamp in "yyyy-mm-dd HH24:mi:ss" format and it assumes the time is in Central Standard Time (CST) or Central Daylight Time (CDT) time zone. CDN bandwidth data is stored in Greenwich Mean Time (GMT) internally and converts a beginning and ending time to GMT before querying. 

Unlike server bandwidth, CDN bandwidth returns total bytes consumed within an hour. For example, if you pass "2008-10-10 00:00:00" for a beginning time and "2008-10-10 05:00:00" for an ending time, your return value will have 6 elements of bandwidth summary objects. The first bandwidth summary object will have the total bytes consumed between 2008-10-10 00:00:00 and 2008-10-10 05:00:00. And the last object will have the bandwidth consumed between 2008-10-10 05:00:00 and 2008-10-10 00:59:59. The bandwidth data is updated at 10 minutes after every hour.  The queried data is on a two hour time delay. The two hour delay is required to gather bandwidth data from each POP and that is the minimum delay required to create a feasible graph. It usually takes about 8 hours to reconcile all the data from every CDN POP. This hourly data is corrected after 24 hours if necessary.  If you consume a large amount of bandwidth, your bandwidth data will be updated the next day. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|beginDateTime| dateTime| time|
|endDateTime| dateTime| time|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_Bandwidth_Summary'>SoftLayer_Container_Network_ContentDelivery_Bandwidth_Summary[] </a>

