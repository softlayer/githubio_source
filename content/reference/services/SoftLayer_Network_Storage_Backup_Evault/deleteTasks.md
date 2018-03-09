---
title: "deleteTasks"
description: "This method can be used to help maintain the storage space on a vault.  When a job is removed from the Webcc, the task a... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::deleteTasks

Delete task(s)


## Overview 
This method can be used to help maintain the storage space on a vault.  When a job is removed from the Webcc, the task and stored usage still exists on the vault. This method can be used to delete the associated task and its usage. 

All that is required for the use of the method is to pass in an integer array of task(s). 



### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|tasks| array of integers| Array of tasks to be deleted.|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Backup_EvaultInitParameters

### Optional Headers

### Return Values
boolean

