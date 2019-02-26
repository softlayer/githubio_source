---
title: "getRequestorOwnedFlag"
description: "Retrieve flag whether the requestor owns the hardware the scan was run on. This flag will  return for hardware servers o... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Security_Scanner_Request"
aliases:
    - "/reference/services/softlayer_network_security_scanner_request/getRequestorOwnedFlag"
---
# [SoftLayer_Network_Security_Scanner_Request](/reference/services/SoftLayer_Network_Security_Scanner_Request)::getRequestorOwnedFlag

Retrieve flag whether the requestor owns the hardware the scan was run on. This flag will  return for hardware servers only, virtual servers will result in a null return even if you have  a request out for them.


## Overview 
Retrieve flag whether the requestor owns the hardware the scan was run on. This flag will  return for hardware servers only, virtual servers will result in a null return even if you have  a request out for them.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Security_Scanner_RequestInitParameters
* authenticate


### Optional Headers
* SoftLayer_Network_Security_Scanner_RequestObjectMask
* SoftLayer_Network_Security_Scanner_RequestObjectFilter
* SoftLayer_ObjectMask

### Return Values
* boolean




