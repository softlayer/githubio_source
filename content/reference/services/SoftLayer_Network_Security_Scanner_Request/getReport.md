---
title: "getReport"
description: "Get the vulnerability report for a scan request, formatted as HTML string. Previous scan reports are held indefinitely."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Security_Scanner_Request"
aliases:
    - "/reference/services/softlayer_network_security_scanner_request/getReport"
---
# [SoftLayer_Network_Security_Scanner_Request](/reference/services/SoftLayer_Network_Security_Scanner_Request)::getReport

Get the vulnerability report for a scan request.


## Overview 
Get the vulnerability report for a scan request, formatted as HTML string. Previous scan reports are held indefinitely. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Security_Scanner_RequestInitParameters


### Return Values
* string



### Error Handling

* SoftLayer_Exception_Network_Security_Scanner_Request_ReportNotFound 

> Throws the error "The selected vulnerability report could not be found." when the report file could not be located. 



