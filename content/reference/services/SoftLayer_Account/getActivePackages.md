---
title: "getActivePackages"
description: "This method will return the [SoftLayer_Product_Package]({{<ref 'reference/datatypes/SoftLayer_Product_Package'>}}) objec... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/getActivePackages"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::getActivePackages

Retrieve the active [SoftLayer_Product_Package]({{<ref "reference/datatypes/SoftLayer_Product_Package">}}) objects from which you can order a server, service or software. 


## Overview 
This method will return the [SoftLayer_Product_Package]({{<ref "reference/datatypes/SoftLayer_Product_Package">}}) objects from which you can order a bare metal server, virtual server, service (such as CDN or Object Storage) or other software. Once you have the package you want to order from, you may query one of various endpoints from that package to get specific information about its products and pricing. See [SoftLayer_Product_Package::getCategories]({{<ref "reference/services/SoftLayer_Product_Package/getCategories">}}) for more information. 

Packages that have been retired will not appear in this result set. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_AccountObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package[] </a>




