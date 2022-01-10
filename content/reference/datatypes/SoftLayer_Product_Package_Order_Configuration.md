---
title: "SoftLayer_Product_Package_Order_Configuration"
description: "This datatype describes the item categories that are required for each package to be ordered. For instance, for package 2, there will be many required categories. When submitting an order for a server, there must be at most 1 price for each category whose 'isRequired' is set. Examples of required categories: - server - ram - bandwidth - disk0 

There are others, but these are the main ones. For each required category, a SoftLayer_Product_Item_Price must be chosen that is valid for the package. 

"
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package_Order_Configuration"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_Product_Package_Order_Configuration"
---
