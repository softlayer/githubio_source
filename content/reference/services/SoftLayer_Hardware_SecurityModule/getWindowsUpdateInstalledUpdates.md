---
title: "getWindowsUpdateInstalledUpdates"
description: "Retrieve a list of Windows updates installed on a server as reported by the local SoftLayer Windows Server Update Servic... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/getWindowsUpdateInstalledUpdates"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::getWindowsUpdateInstalledUpdates


Retrieve a list of Windows updates installed on a server.


## Overview 
Retrieve a list of Windows updates installed on a server as reported by the local SoftLayer Windows Server Update Services (WSUS) server. Windows servers provisioned by SoftLayer are configured to use the local WSUS server via the private network by default. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModuleInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem'>SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem[] </a>

### External Links


* [Windows Server Update Services (WSUS) Home](http://technet.microsoft.com/en-us/wsus/default.aspx)




### Error Handling

* SoftLayer_Exception 

> Throw the exception "This server does not run the Microsoft Windows operating system" when trying to run this method on a server that doesn't run Microsoft Windows. 



