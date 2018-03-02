---
title: "getHardwareWithEvaultFirst"
description: "Retrieve a list of hardware associated with a SoftLayer customer account, placing all hardware with associated EVault st... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
---
# SoftLayer_Network_Storage_Backup_Evault::getHardwareWithEvaultFirst
## Overview 
Retrieve a list of hardware associated with a SoftLayer customer account, placing all hardware with associated EVault storage accounts at the beginning of the list. The return type is SoftLayer_Hardware_Server[] contains the results; the number of items returned in the result will be returned in the soap header (totalItems). ''getHardwareWithEvaultFirst'' is useful in situations where you wish to search for hardware and provide paginated output. 





Results are only returned for hardware belonging to the account of the user making the API call. 

This method drives the backup page of the SoftLayer customer portal. It serves a very specific function, but we have exposed it as it may prove useful for API developers too. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|option| string| The field you wish to search on. This can be set to either "Servername" or "Username". If set to Servername then this will search for the value specified in the criteria parameter on your hardware's hostname and domain name. If set to Username then it will search on the EVault webcc username of the server's associated user account. If option is not set then it will search for hardware based on the hardware's associated EVault user's password. This parameter is only used when the mode parameter is set to "search".|
|exactMatch| boolean| How you wish to search through hardware. Set this to either 'true' for an exact match of your search criteria or false if you wish search for part of a server name. This parameter is only used when the mode parameter is set to "search" and defaults to true.|
|criteria| string| The value you wish to search for. This is only used when mode is set to "search".|
|mode| string| How you wish you gather your hardware list. Mode can either equal "normal" or "search". Normal mode will return all of your hardware, while search mode filters your hardware by the values you specify for the option, type, and criteria parameters.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_Storage_Backup_EvaultObjectMask
* SoftLayer_ObjectMask
* resultLimit

### Return Values
<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>

### External Links


* [Backup management on the SoftLayer customer portal](http://maange.softlayer.com/backup/index.html)


