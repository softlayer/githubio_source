---
title: "getMainStatistics"
description: "This method returns the attack statistics for the current user's account and for the entire SoftLayer network.  These at... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_TippingPointReporting"
aliases:
    - "/reference/services/softlayer_network_tippingpointreporting/getMainStatistics"
---
# [SoftLayer_Network_TippingPointReporting](/reference/services/SoftLayer_Network_TippingPointReporting)::getMainStatistics

Returns the main statistics for the entire SoftLayer network, as well as your particular account.


## Overview 
This method returns the attack statistics for the current user's account and for the entire SoftLayer network.  These attacks are recorded and monitored at the entry point to the network, and represent attacks in both directions. 

The data returned is: 
* Top attacks (by attack name) on datacenter Dal01 in the last hour (and last 24 hours)
* Top attacks (by attack name) on IPs you own in the last hour (and last 24 hours)
* Top IPs attacking IPs you own in the last hour (and last 24 hours)
Each one of these lists can contain any number of items, the default is 5.  The usable limit is less than 10, but setting the limit to an abnormally high value will effectively return all records. 

The data is returned as a collection of SoftLayer_Container_Network_IntrusionProtection_Statistics objects. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|numberOfAttacks| integer| (optional) number of rows to show for each statistic.  Default is 5|


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Network_IntrusionProtection_Statistics'>SoftLayer_Container_Network_IntrusionProtection_Statistics[] </a>

