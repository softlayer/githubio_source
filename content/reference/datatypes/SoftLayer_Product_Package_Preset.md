---
title: "SoftLayer_Product_Package_Preset"
description: "Package presets are used to simplify ordering by eliminating the need for price ids when submitting orders. 

Orders submitted with a preset id defined will use the prices included in the package preset. Prices submitted on an order with a preset id will replace the prices included in the package preset for that prices category. If the package preset has a fixed configuration flag <em>(fixedConfigurationFlag)</em> set then the prices included in the preset configuration cannot be replaced by prices submitted on the order. The only exception to the fixed configuration flag would be if a price submitted on the order is an account-restricted price for the same product item. "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package_Preset"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_Product_Package_Preset"
---
