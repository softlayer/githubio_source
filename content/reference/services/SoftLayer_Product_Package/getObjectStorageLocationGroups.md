---
title: "getObjectStorageLocationGroups"
description: "This method will return a collection of [[SoftLayer_Container_Product_Order_Network_Storage_ObjectStorage_LocationGroup]... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package"
---
# SoftLayer_Product_Package::getObjectStorageLocationGroups
## Overview 
This method will return a collection of [[SoftLayer_Container_Product_Order_Network_Storage_ObjectStorage_LocationGroup]] objects which contain a location group and all the associated active usage rate prices where object storage is available. This method is really only applicable to the object storage additional service package which has a [[SoftLayer_Product_Package_Type]] of '''ADDITIONAL_SERVICES_OBJECT_STORAGE'''. This information is useful so that you can see the "pay as you go" rates per location group. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Product_PackageInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_ObjectStorage_LocationGroup'>SoftLayer_Container_Product_Order_Network_Storage_ObjectStorage_LocationGroup[] </a>

