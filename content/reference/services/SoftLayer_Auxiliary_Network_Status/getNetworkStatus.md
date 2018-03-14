---
title: "getNetworkStatus"
description: "Return the current network status of and latency information for a given target from numerous points around the world. V... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Auxiliary"
classes:
    - "SoftLayer_Auxiliary_Network_Status"
aliases:
    - "/reference/services/softlayer_auxiliary_network_status/getNetworkStatus"
---
# [SoftLayer_Auxiliary_Network_Status](/reference/services/SoftLayer_Auxiliary_Network_Status)::getNetworkStatus

return current network status for a given target.


## Overview 
Return the current network status of and latency information for a given target from numerous points around the world. Valid Targets: 
* ALL
* NETWORK_DALLAS
* NETWORK_SEATTLE
* NETWORK_PUBLIC
* NETWORK_PUBLIC_DALLAS
* NETWORK_PUBLIC_SEATTLE
* NETWORK_PUBLIC_WDC
* NETWORK_PRIVATE
* NETWORK_PRIVATE_DALLAS
* NETWORK_PRIVATE_SEATTLE
* NETWORK_PRIVATE_WDC

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|target| string| <ul type="xsd:string"> <li title="All">ALL</li> <li title="Dallas Network">NETWORK_DALLAS</li> <li title="Seattle Network">NETWORK_SEATTLE</li> - <li title="Public Network">NETWORK_PUBLIC</li> <li title="Dallas, TX - Public Network">NETWORK_PUBLIC_DALLAS</li> <li title="Seattle, WA - Public Network">NETWORK_PUBLIC_SEATTLE</li> <li title="Washington, DC - Public Network">NETWORK_PUBLIC_WDC</li> - <li title="Private Network">NETWORK_PRIVATE</li> <li title="Dallas, TX - Private Network">NETWORK_PRIVATE_DALLAS</li> <li title="Seattle, WA - Private Network">NETWORK_PRIVATE_SEATTLE</li> <li title="Washington, DC - Private Network">NETWORK_PRIVATE_WDC</li> </ul>|


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Auxiliary_Network_Status_Reading'>SoftLayer_Container_Auxiliary_Network_Status_Reading[] </a>

