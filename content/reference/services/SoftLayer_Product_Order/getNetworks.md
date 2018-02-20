---
title: "getNetworks"
description: "This method returns a collection of [[SoftLayer_Container_Product_Order_Network]] objects. This will contain the availab... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
---
# SoftLayer_Product_Order::getNetworks
## Overview 
This method returns a collection of [[SoftLayer_Container_Product_Order_Network]] objects. This will contain the available networks that can be used when ordering services. 

If a location id is supplied, the list of networks will be trimmed down to only those that are available at that particular datacenter. 

If a package id is supplied, the list of public VLANs and subnets will be trimmed down to those that are available for that particular package. 

The account id is for internal use only and will be ignored when supplied by customers. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|locationId| integer| The id of the [[SoftLayer_Location|datacenter]] to filter the networks.|
|packageId| integer| This id of the [[SoftLayer_Product_Package|package]] to filter the public VLANs and subnets.|
|accountId| integer| The id of the [[SoftLayer_Account|account]] to pull networks. This is ignored for customer requests.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Product_Order_Network'>SoftLayer_Container_Product_Order_Network[] </a>
