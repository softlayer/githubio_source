---
title: "testRaidAlertService"
description: "Test the RAID Alert service by sending the service a request to store a test email for this server. The server must have... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/testRaidAlertService"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::testRaidAlertService


Tests the RAID Alert service.


## Overview 
Test the RAID Alert service by sending the service a request to store a test email for this server. The server must have an account ID and MAC address.  A RAID controller must also be installed. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_ServerInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception 'Missing required property: ...' when the server is missing an account ID, MAC address, or RAID controller. 

* SoftLayer_Exception_Public 

> Throws the exception 'API request failed.' when there is an unrecoverable error communication with the RAID Alert service. 



