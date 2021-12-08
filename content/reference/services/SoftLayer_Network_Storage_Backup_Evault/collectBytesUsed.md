---
title: "collectBytesUsed"
description: "{{CloudLayerOnlyMethod}} 

collectBytesUsed() retrieves the number of bytes capacity currently in use on a Storage accou... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
aliases:
    - "/reference/services/softlayer_network_storage_backup_evault/collectBytesUsed"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::collectBytesUsed


Retrieve the number of bytes capacity currently in use on a Storage account.


## Overview 
{{CloudLayerOnlyMethod}} 

collectBytesUsed() retrieves the number of bytes capacity currently in use on a Storage account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Backup_EvaultInitParameters


### Return Values
* unsigned long



### Error Handling

* SoftLayer_Exception 

> Throw the exception "The <nasType> Storage type is not supported for bytes used collection.  Please contact development." if the storage volume's type does not support usage collection. Currently, only Virtual Server storage is supported. 



