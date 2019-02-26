---
title: "getBandwidthImage"
description: "Use this method when needing a bandwidth image for a single server.  It will gather the correct input parameters for the... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/getBandwidthImage"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::getBandwidthImage

Retrieve a bandwidth image and textual description of that image for this server.


## Overview 
Use this method when needing a bandwidth image for a single server.  It will gather the correct input parameters for the generic graphing utility automatically based on the snapshot specified.  Use the $draw flag to suppress the generation of the actual binary PNG image. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|networkType| string| <ul type="xsd:string"> <li title="public">public</li> <li title="private">private</li> </ul>|
|snapshotRange| string| <ul type="xsd:string"> <li title="day">day</li> <li title="week">week</li> <li title="30day">30day</li> <li title="previous_calendar_month">previous_calendar_month</li> <li title="current_calendar_month">current_calendar_month</li> <li title="current_billing_cycle">current_billing_cycle</li> <li title="previous_billing_cycle">previous_billing_cycle</li> <li title="specified_day">specified_day</li> <li title="specified_range">specified_range</li> </ul>|
|draw| boolean| TRUE to generate binary image otherwise just return text|
|dateSpecified| dateTime| Include this parameter when snapshot is 'specified_day' or 'specified_range'.  Needs to be formatted as: 'MM/DD/YYYY'|
|dateSpecifiedEnd| dateTime| Include this parameter when snapshotRange is 'specified_range'.  Also formatted as 'MM/DD/YYYY'.|


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModule750InitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputs'>SoftLayer_Container_Bandwidth_GraphOutputs </a>




