---
title: "checkItemAvailabilityForImageTemplate"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
aliases:
    - "/reference/services/softlayer_product_order/checkItemAvailabilityForImageTemplate"
---
# [SoftLayer_Product_Order](/reference/services/SoftLayer_Product_Order)::checkItemAvailabilityForImageTemplate





## Overview 


-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|imageTemplateId| integer| The image template id for which to check the availability of items.|
|accountId| integer| The account number for which to check for a restricted item price.|
|packageId| integer| The package id of the package to which the template will be deployed.|
|availabilityTypeKeyNames| array of strings| An array of keynames for which to check for item availability types.|


### Required Headers
* authenticate


### Return Values
* boolean




