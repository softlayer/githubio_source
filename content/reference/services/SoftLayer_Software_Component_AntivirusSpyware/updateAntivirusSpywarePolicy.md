---
title: "updateAntivirusSpywarePolicy"
description: "Update an anti-virus/spyware policy. The policy options that it accepts are the following: 
*1 - Minimal
*2 - Relaxed
*3... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component_AntivirusSpyware"
---
# SoftLayer_Software_Component_AntivirusSpyware::updateAntivirusSpywarePolicy
## Overview 
Update an anti-virus/spyware policy. The policy options that it accepts are the following: 
*1 - Minimal
*2 - Relaxed
*3 - Default
*4 - High
*5 - Ultimate

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|newPolicy| string| The new anti-virus policy.|
|enforce| boolean| Enforce the updated policy|


### Required Headers
* authenticate
* SoftLayer_Software_Component_AntivirusSpywareInitParameters

### Optional Headers

### Return Values
boolean
