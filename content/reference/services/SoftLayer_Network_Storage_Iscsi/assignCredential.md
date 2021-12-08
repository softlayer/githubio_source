---
title: "assignCredential"
description: "This method will assign an existing credential to the current volume. The credential must have been created using the 'a... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
aliases:
    - "/reference/services/softlayer_network_storage_iscsi/assignCredential"
---
# [SoftLayer_Network_Storage_Iscsi](/reference/services/SoftLayer_Network_Storage_Iscsi)::assignCredential


This method will assign an existing credential to the current volume.


## Overview 
This method will assign an existing credential to the current volume. The credential must have been created using the 'addNewCredential' method. The volume type must support an additional credential. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|username| string| A username assigned to a different volume.|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_IscsiInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Network_Storage_AssignCredential 

> "Problem assigning a credential to the volume. The network storage type is not supported for credential assigning in this manner." 

* SoftLayer_Exception_Network_Storage_Iscsi_EqualLogic_Version3_AssignCredential_DuplicateDesignation 

> "Username is already assigned to volume." 

* SoftLayer_Exception_Network_Storage_Iscsi_EqualLogic_Version3_AssignCredential_ConsoleError 

> "A console error was encountered when trying to remove username from Iscsi volume, please contact development." 



