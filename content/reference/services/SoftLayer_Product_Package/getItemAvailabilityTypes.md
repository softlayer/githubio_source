---
title: "getItemAvailabilityTypes"
description: "Returns a collection of SoftLayer_Product_Item_Attribute_Type objects.  These item attribute types specifically deal wit... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package"
---
# SoftLayer_Product_Package::getItemAvailabilityTypes
## Overview 
Returns a collection of SoftLayer_Product_Item_Attribute_Type objects.  These item attribute types specifically deal with when an item, SoftLayer_Product_Item, from the product catalog may no longer be available.  The keynames for these attribute types start with 'UNAVAILABLE_AFTER_DATE_*', where the '*' may represent any string.  For example, 'UNAVAILABLE_AFTER_DATE_NEW_ORDERS', signifies that the item is not available for new orders.  There is a catch all attribute type, 'UNAVAILABLE_AFTER_DATE_ALL'.  If an item has one of these availability attributes set, the value should be a valid date in MM/DD/YYYY, indicating the date after which the item will no longer be available. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Product_PackageObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Product_Item_Attribute_Type'>SoftLayer_Product_Item_Attribute_Type[] </a>

