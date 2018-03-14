---
title: "initiateBareMetalRestore"
description: "Evault Bare Metal Restore is a special version of Rescue Kernel designed specifically for making full system restores ma... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
aliases:
    - "/reference/services/softlayer_network_storage_backup_evault/initiateBareMetalRestore"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::initiateBareMetalRestore

Initiate a bare metal restore for the server tied to the EVault account


## Overview 
Evault Bare Metal Restore is a special version of Rescue Kernel designed specifically for making full system restores made with Evault's BMR backup. This process works very similar to Rescue Kernel, except only the Evault restore program is available. The process takes approximately 10 minutes. Once completed you will be able to access your server to do a restore through VNC or your servers KVM-over-IP. IP information and credentials can be found on the hardware page of the customer portal. The Evault Application will be running automatically upon startup, and will walk you through the restore process. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Backup_EvaultInitParameters

### Optional Headers

### Return Values
boolean

