---
title: "getWindowsUpdateStatus"
description: "This method returns an update status record for this server.  That record will specify if the server is missing updates,... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/getWindowsUpdateStatus"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::getWindowsUpdateStatus

Retrieve a server's Windows update synchronization status


## Overview 
This method returns an update status record for this server.  That record will specify if the server is missing updates, or has updates that must be reinstalled or require a reboot to go into affect. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModuleInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_Status'>SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_Status </a>

### External Links


* [Windows Server Update Services (WSUS) Home](http://technet.microsoft.com/en-us/wsus/default.aspx)




### Error Handling

* SoftLayer_Exception 

> Throw the exception "This server does not run the Microsoft Windows operating system" when trying to run this method on a server that doesn't run Microsoft Windows. 



