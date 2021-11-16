---
title: "createObject"
description: "Create a new vulnerability scan request. New scan requests are picked up every five minutes, and the time to complete an... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Security_Scanner_Request"
aliases:
    - "/reference/services/softlayer_network_security_scanner_request/createObject"
---
# [SoftLayer_Network_Security_Scanner_Request](/reference/services/SoftLayer_Network_Security_Scanner_Request)::createObject


Create a new vulnerability scan request.


## Overview 
Create a new vulnerability scan request. New scan requests are picked up every five minutes, and the time to complete an actual scan may vary. Once the scan is finished, it can take up to another five minutes for the report to be generated and accessible. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network_Security_Scanner_Request'>SoftLayer_Network_Security_Scanner_Request </a>| The SoftLayer_Network_Security_Scanner_Request object that you wish to create.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_Security_Scanner_RequestObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Security_Scanner_Request'>SoftLayer_Network_Security_Scanner_Request </a>




