---
title: "getBandwidthImage"
description: "This method recurses through all servers on a Bandwidth Pool for a given snapshot range, gathers the necessary parameter... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
---
# SoftLayer_Network_Bandwidth_Version1_Allotment::getBandwidthImage
## Overview 
This method recurses through all servers on a Bandwidth Pool for a given snapshot range, gathers the necessary parameters, and then calls the bandwidth graphing server.  The return result is a container that includes the min and max dates for all servers to be used in the query, as well as an image in PNG format.  This method uses the new and improved drawing routines which should return in a reasonable time frame now that the new backend data warehouse is used. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|networkType| string| <ul type="xsd:string"> <li title="public">public</li> <li title="private">private</li> </ul>|
|snapshotRange| string| <ul type="xsd:string"> <li title="day">day</li> <li title="week">week</li> <li title="30day">30day</li> <li title="previous_calendar_month">previous_calendar_month</li> <li title="current_calendar_month">current_calendar_month</li> <li title="current_billing_cycle">current_billing_cycle</li> <li title="previous_billing_cycle">previous_billing_cycle</li> <li title="specified_day">specified_day</li> <li title="specified_range">specified_range</li> </ul>|
|draw| boolean| TRUE to generate binary image otherwise just return text.  Deprecated, images return fast enough now.|
|dateSpecified| dateTime| Include this parameter when snapshot is 'specified_day' or 'specified_range'.  Needs to be formatted as: 'MM/DD/YYYY'|
|dateSpecifiedEnd| dateTime| Include this parameter when snapshotRange is 'specified_range'.  Also formatted as 'MM/DD/YYYY'|


### Required Headers
* authenticate
* SoftLayer_Network_Bandwidth_Version1_AllotmentInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputs'>SoftLayer_Container_Bandwidth_GraphOutputs </a>
