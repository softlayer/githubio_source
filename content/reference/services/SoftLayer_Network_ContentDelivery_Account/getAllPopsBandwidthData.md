---
title: "getAllPopsBandwidthData"
description: "This method returns bandwidth data for each POP. [[SoftLayer_Container_Network_ContentDelivery_Bandwidth_PointsOfPresenc... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::getAllPopsBandwidthData

Returns bandwidth data for each POP


## Overview 
This method returns bandwidth data for each POP. [[SoftLayer_Container_Network_ContentDelivery_Bandwidth_PointsOfPresence_Summary|POP Bandwidth]] object contains a starting time, ending time, total bytes, POP name and bandwidth unit. 

POP bandwidth data is updated everyday at 22:50 CST (or CDT). It queries and stores POP data from the day before. It is a more resource intensive process than a regular CDN bandwidth update thus we run this once a day. Since the POP bandwidth data is delayed for a day, there is no correction process for POP data. The POP bandwidth is not associated with any billing process and is mainly used to generate a POP bandwidth graph. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|beginDateTime| dateTime| beginning time|
|endDateTime| dateTime| Ending time|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_Bandwidth_PointsOfPresence_Summary'>SoftLayer_Container_Network_ContentDelivery_Bandwidth_PointsOfPresence_Summary[] </a>


### associatedMethods

*  [SoftLayer_Network_ContentDelivery_Account::getBandwidthData](/reference/services/SoftLayer_Network_ContentDelivery_Account/getBandwidthData )

