---
title: "getTaxCalculationResult"
description: "Sometimes taxes cannot be calculated immediately, so we start the calculations and let them run in the background. This... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
aliases:
    - "/reference/services/softlayer_product_order/getTaxCalculationResult"
---
# [SoftLayer_Product_Order](/reference/services/SoftLayer_Product_Order)::getTaxCalculationResult

Get the results of a tax calculation.


## Overview 
Sometimes taxes cannot be calculated immediately, so we start the calculations and let them run in the background. This method will return the current progress and information related to a specific tax calculation, which allows real-time progress updates on tax calculations. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|orderHash| string| <<< EOT|


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Tax_Cache'>SoftLayer_Container_Tax_Cache </a>

