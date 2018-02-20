---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_Security_Scanner_Request object whose ID number corresponds to the ID number o... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Security_Scanner_Request"
---
# SoftLayer_Network_Security_Scanner_Request::getObject
## Overview 
getObject retrieves the SoftLayer_Network_Security_Scanner_Request object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Network_Security_Scanner_Request service. You can only retrieve requests and reports that are assigned to your SoftLayer account. 

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
<a href='/reference/datatypes/SoftLayer_Network_Security_Scanner_Request'>SoftLayer_Network_Security_Scanner_Request </a>
