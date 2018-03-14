---
title: "getFrontendBandwidthByHour"
description: "This method recurses through all servers on a Bandwidth Pool for 24 hour time span starting at a given date/time. To get... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
aliases:
    - "/reference/services/softlayer_network_bandwidth_version1_allotment/getFrontendBandwidthByHour"
---
# [SoftLayer_Network_Bandwidth_Version1_Allotment](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment)::getFrontendBandwidthByHour

return a collection of public usage objects that contain hourly incoming and outgoing network traffic amounts for a 24 hour period. 


## Overview 
This method recurses through all servers on a Bandwidth Pool for 24 hour time span starting at a given date/time. To get the public data set for all servers on a Bandwidth Pool from midnight Feb 1st, 2008 to 23:59 on Feb 1st, you would pass a parameter of '02/01/2008 0:00'.  The ending date / time is calculated for you to prevent requesting data from the server for periods larger than 24 hours as this method requires processing a lot of data records and can get slow at times. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|date| dateTime| The date at which you wish to start a 24 hour snapshot formatted as 'MM/DD/YYYY HH:00'.|


### Required Headers
* authenticate
* SoftLayer_Network_Bandwidth_Version1_AllotmentInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Network_Bandwidth_Version1_Usage'>SoftLayer_Container_Network_Bandwidth_Version1_Usage[] </a>

