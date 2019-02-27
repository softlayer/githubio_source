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
aliases:
    - "/reference/services/softlayer_virtual_guest/reloadOperatingSystem"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::reloadOperatingSystem

Reloads operating system configuration.


## Overview 
Reloads current operating system configuration. 

This service has a confirmation protocol for proceeding with the reload. To proceed with the reload without confirmation, simply pass in 'FORCE' as the token parameter. To proceed with the reload with confirmation, simply call the service with no parameter. A token string will be returned by this service. The token will remain active for 10 minutes. Use this token as the parameter to confirm that a reload is to be performed for the server. 

As a precaution, we strongly  recommend backing up all data before reloading the operating system. The reload will format the primary disk and will reconfigure the computing instance to the current specifications on record. 

If reloading from an image template, we recommend first getting the list of valid private block device template groups, by calling the getOperatingSystemReloadImages method. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|token| string| The token returned by this service as a confirmation to proceed with the reload.|
|config| <a href='/reference/datatypes/SoftLayer_Container_Hardware_Server_Configuration'>SoftLayer_Container_Hardware_Server_Configuration </a>| The new cloud configuration for the reload.|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters


### Return Values
* string


### Associated Methods

*  [SoftLayer_Account::getOperatingSystemReloadImages](/reference/services/SoftLayer_Account/getOperatingSystemReloadImages )



### Error Handling

* SoftLayer_Exception_Hardware_Server_OperatingSystemReloadPermissionDenied 

> Throws the exception 'You do not have permission to this service.' when a user does not have permission to Issue OS Reloads. 

* SoftLayer_Exception_Hardware_Server_ActiveTransactionExists 

> Throws the exception 'There is currently an outstanding transaction for this server.' when a server has a currently running transaction. 

* SoftLayer_Exception_Hardware_Server_InvalidReloadToken 

> Throws the exception 'Invalid token provided.' when a token that is either expired or invalid is provided. 

* SoftLayer_Exception_Hardware_Server_MissingBillingItem 

> Throws the exception 'Couldn't find BillingItem for this server.' when there is no billing item that exists for a server. 

* SoftLayer_Exception_Public 

> Throws the exception 'Unable to cancel current billing item.  Please contact support.' when a billing item for software that is not being reloaded can not be cancelled. 

* SoftLayer_Exception_Public 

> Throws the exception 'Partitions provided are to large for the servers primary hard drive.' when the partition configuration provided exceeds the size of the drive. 



