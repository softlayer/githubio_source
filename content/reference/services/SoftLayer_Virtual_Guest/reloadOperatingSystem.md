---
title: "reloadOperatingSystem"
description: "Reloads current operating system configuration. 

This service has a confirmation protocol for proceeding with the reloa... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# SoftLayer_Virtual_Guest::reloadOperatingSystem
## Overview 
Reloads current operating system configuration. 

This service has a confirmation protocol for proceeding with the reload. To proceed with the reload without confirmation, simply pass in 'FORCE' as the token parameter. To proceed with the reload with confirmation, simply call the service with no parameter. A token string will be returned by this service. The token will remain active for 10 minutes. Use this token as the parameter to confirm that a reload is to be performed for the server. 

As a precaution, we strongly  recommend backing up all data before reloading the operating system. The reload will format the primary disk and will reconfigure the computing instance to the current specifications on record. 

If reloading from an image template, we recommend first getting the list of valid private block device template groups, by calling the getOperatingSystemReloadImages method. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|token| string| The token returned by this service as a confirmation to proceed with the reload.|
|config| <a href='/reference/datatypes/SoftLayer_Container_Hardware_Server_Configuration'>SoftLayer_Container_Hardware_Server_Configuration </a>| The new cloud configuration for the reload.|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters

### Optional Headers

### Return Values
string


### associatedMethods

*  [SoftLayer_Account::getOperatingSystemReloadImages](/reference/services/SoftLayer_Account/getOperatingSystemReloadImages )

