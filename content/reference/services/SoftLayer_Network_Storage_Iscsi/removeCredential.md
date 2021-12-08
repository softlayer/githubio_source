---
title: "removeCredential"
description: "This method will remove a credential from the current volume. The credential must have been created using the 'addNewCre... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
aliases:
    - "/reference/services/softlayer_network_storage_iscsi/removeCredential"
---
# [SoftLayer_Network_Storage_Iscsi](/reference/services/SoftLayer_Network_Storage_Iscsi)::removeCredential


This method will remove a credential from the current volume.


## Overview 
This method will remove a credential from the current volume. The credential must have been created using the 'addNewCredential' method. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|username| string| A username assigned to the current storage volume|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_IscsiInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Network_Storage_RemoveCredential 

> "Problem removing a credential from the volume. The network storage type is not supported for credential removal in this manner." 

* SoftLayer_Exception_Network_Storage_Iscsi_EqualLogic_Version3_RemoveCredential_CredentialRequired 

> "Username could not be removed from Iscsi volume because it is required to identify the volume" 



