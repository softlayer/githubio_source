---
title: "getCategories"
description: "Retrieve this is a collection of categories ([SoftLayer_Product_Item_Category]({{<ref 'reference/datatypes/SoftLayer_Pro... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package"
aliases:
    - "/reference/services/softlayer_product_package/getCategories"
---
# [SoftLayer_Product_Package](/reference/services/SoftLayer_Product_Package)::getCategories


Retrieve this is a collection of categories ([SoftLayer_Product_Item_Category]({{<ref "reference/datatypes/SoftLayer_Product_Item_Category">}})) associated with a package which can be used for ordering. These categories have several objects prepopulated which are useful when determining the available products for purchase. The categories contain groups ([SoftLayer_Product_Package_Item_Category_Group]({{<ref "reference/datatypes/SoftLayer_Product_Package_Item_Category_Group">}})) that organize the products and prices by similar features. For example, operating systems will be grouped by their manufacturer and virtual server disks will be grouped by their disk type (SAN vs. local). Each group will contain prices ([SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}})) which you can use determine the cost of each product. Each price has a product ([SoftLayer_Product_Item]({{<ref "reference/datatypes/SoftLayer_Product_Item">}})) which provides the name and other useful information about the server, service or software you may purchase.


## Overview 
Retrieve this is a collection of categories ([SoftLayer_Product_Item_Category]({{<ref "reference/datatypes/SoftLayer_Product_Item_Category">}})) associated with a package which can be used for ordering. These categories have several objects prepopulated which are useful when determining the available products for purchase. The categories contain groups ([SoftLayer_Product_Package_Item_Category_Group]({{<ref "reference/datatypes/SoftLayer_Product_Package_Item_Category_Group">}})) that organize the products and prices by similar features. For example, operating systems will be grouped by their manufacturer and virtual server disks will be grouped by their disk type (SAN vs. local). Each group will contain prices ([SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}})) which you can use determine the cost of each product. Each price has a product ([SoftLayer_Product_Item]({{<ref "reference/datatypes/SoftLayer_Product_Item">}})) which provides the name and other useful information about the server, service or software you may purchase.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Product_PackageInitParameters
* authenticate


### Optional Headers
* SoftLayer_Product_PackageObjectMask
* SoftLayer_Product_PackageObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category[] </a>




