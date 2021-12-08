---
title: "configureMetadataDisk"
description: "Creates a transaction to configure the guest's metadata disk. If the guest has user data associated with it, the transac... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/configureMetadataDisk"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::configureMetadataDisk


Configures the guest's metadata disk.


## Overview 
Creates a transaction to configure the guest's metadata disk. If the guest has user data associated with it, the transaction will create a small virtual drive and write the metadata to a file on the drive; if the drive already exists, the metadata will be rewritten. If the guest has no user data associated with it, the transaction will remove the virtual drive if it exists. 

WARNING: The transaction created by this service will shut down the guest while the metadata disk is configured. The guest will be turned back on once this process is complete. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters


### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>




