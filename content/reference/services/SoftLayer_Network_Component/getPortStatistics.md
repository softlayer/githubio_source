---
title: "getPortStatistics"
description: "**DEPRECATED - This operation will cease to function after April 4th, 2016 and will be removed from v3.2**
Retrieve vari... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component"
---
# SoftLayer_Network_Component::getPortStatistics
## Overview 

**DEPRECATED - This operation will cease to function after April 4th, 2016 and will be removed from v3.2**
Retrieve various network statistics.  The network statistics are retrieved from the network device using snmpget. Below is a list of statistics retrieved: 
* Administrative Status
* Operational Status
* Maximum Transmission Unit
* In Octets
* Out Octets
* In Unicast Packets
* Out Unicast Packets
* In Multicast Packets
* Out Multicast Packets

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_ComponentInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Network_Port_Statistic'>SoftLayer_Container_Network_Port_Statistic </a>
