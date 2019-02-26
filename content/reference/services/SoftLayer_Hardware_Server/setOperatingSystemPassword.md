---
title: "setOperatingSystemPassword"
description: "Changes the password that we have stored in our database for a servers' Operating System"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/setOperatingSystemPassword"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::setOperatingSystemPassword

Changes the password stored in our system for a servers' Operating System


## Overview 
Changes the password that we have stored in our database for a servers' Operating System

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|newPassword| string| The password to be set for the administrator/root of the operating system.|


### Required Headers
* authenticate
* SoftLayer_Hardware_ServerInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception 'No operating system could be found for this server.' When there is no operating system installed on a server. 



