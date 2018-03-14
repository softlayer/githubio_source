---
title: "getWindowsUpdateStatus"
description: "Retrieve a list of an account's hardware's Windows Update status. This list includes which servers have available update... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/getWindowsUpdateStatus"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::getWindowsUpdateStatus

Retrieve a list of an account's hardware's Windows Update status.


## Overview 
Retrieve a list of an account's hardware's Windows Update status. This list includes which servers have available updates, which servers require rebooting due to updates, which servers have failed retrieving updates, and which servers have failed to communicate with the SoftLayer private Windows Software Update Services server. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_Status'>SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_Status[] </a>


### associatedMethods

*  [SoftLayer_Hardware::getWindowsUpdateStatus](/reference/services/SoftLayer_Hardware/getWindowsUpdateStatus )

