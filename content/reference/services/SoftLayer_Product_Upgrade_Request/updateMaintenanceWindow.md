---
title: "updateMaintenanceWindow"
description: "In case an upgrade cannot be performed, the maintenance window needs to be updated to a future date."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Upgrade_Request"
aliases:
    - "/reference/services/softlayer_product_upgrade_request/updateMaintenanceWindow"
---
# [SoftLayer_Product_Upgrade_Request](/reference/services/SoftLayer_Product_Upgrade_Request)::updateMaintenanceWindow

Updates the maintenance window


## Overview 
In case an upgrade cannot be performed, the maintenance window needs to be updated to a future date. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|maintenanceStartTime| dateTime| A maintenance window starting time in ISO 8601 format.|
|maintenanceWindowId| integer| |


### Required Headers
* authenticate
* SoftLayer_Product_Upgrade_RequestInitParameters

### Optional Headers

### Return Values
boolean

