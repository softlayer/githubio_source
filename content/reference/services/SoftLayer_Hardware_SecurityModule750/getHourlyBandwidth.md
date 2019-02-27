---
title: "getHourlyBandwidth"
description: "The '''getHourlyBandwidth''' method retrieves all bandwidth updates hourly for the specified hardware. Because the poten... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/getHourlyBandwidth"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::getHourlyBandwidth

Retrieves bandwidth hourly over a 24-hour period for the specified hardware.


## Overview 
The '''getHourlyBandwidth''' method retrieves all bandwidth updates hourly for the specified hardware. Because the potential number of data points can become excessive, the method limits the user to obtain data in 24-hour intervals. The required ''dateTime'' parameter is used as the starting point for the query and will be calculated for the 24-hour period starting with the specified date and time. For example, entering a parameter of 

'02/01/2008 0:00' 

results in a return of all bandwidth data for the entire day of February 1, 2008, as 0:00 specifies a midnight start date. Please note that the time entered should be completed using a 24-hour clock (military time, astronomical time). 

For data spanning more than a single 24-hour period, refer to the getBandwidthData function on the metricTrackingObject for the piece of hardware. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|mode| string| Specifies the 'public' or 'private' port for this server.|
|day| dateTime| A date and time formatted as 'MM/DD/YYYY HH:00'|


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModule750InitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data'>SoftLayer_Metric_Tracking_Object_Data[] </a>




