---
title: "getBandwidthDataWithTypes"
description: "This method returns bandwidth data for a given time range.  It returns an array of [[SoftLayer_Container_Network_Content... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_account/getBandwidthDataWithTypes"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::getBandwidthDataWithTypes

Returns bandwidth data for a time range, separated by types and regions


## Overview 
This method returns bandwidth data for a given time range.  It returns an array of [[SoftLayer_Container_Network_ContentDelivery_Report_Usage|bandwidth usage report]] objects. 

These will be first sorted by timestamp, and there will be one entry with that timestamp for each enabled region. The region type 'NONE' is provided only when non-region-specific data is returned. [[SoftLayer_Container_Network_ContentDelivery_Report_Usage|bandwidth usage report]] objects with a region will never contain non-region-specific data. Non-region-specific values are standardTotal and sslTotal; standardTotal is computed by adding the HTTP Large, Windows Media, Flash and Application Delivery Network bandwidth. The sslTotal is computed by adding the HTTP Large SSL bandwidth and the Application Delivery Network SSL bandwidth. 

A Beginning and ending date parameters have to be a timestamp in "yyyy-mm-dd HH24:mi:ss" format and it assumes the time is in Central Standard Time (CST) or Central Daylight Time (CDT) time zone. CDN bandwidth data is stored in Greenwich Mean Time (GMT) internally and converts a beginning and ending time to GMT before querying. 

Unlike server bandwidth, CDN bandwidth returns total bytes consumed within an hour. For example, if you pass "2008-10-10 00:00:00" for a beginning time and "2008-10-10 05:00:00" for an ending time, your return value will have 6 elements of bandwidth summary objects. The first bandwidth summary object will have the total bytes consumed between 2008-10-10 00:00:00 and 2008-10-10 05:00:00. And the last object will have the bandwidth consumed between 2008-10-10 05:00:00 and 2008-10-10 00:59:59. The bandwidth data is updated at 10 minutes after every hour.  The queried data is on a two hour time delay. The two hour delay is required to gather bandwidth data from each POP and that is the minimum delay required to create a feasible graph. It usually takes about 8 hours to reconcile all the data from every CDN POP. This hourly data is corrected after 24 hours if necessary.  If you consume a large amount of bandwidth, your bandwidth data will be updated the next day. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|beginDateTime| dateTime| time|
|endDateTime| dateTime| time|
|period| string| to summarize, auto|hourly|daily|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_Report_Usage'>SoftLayer_Container_Network_ContentDelivery_Report_Usage[] </a>

