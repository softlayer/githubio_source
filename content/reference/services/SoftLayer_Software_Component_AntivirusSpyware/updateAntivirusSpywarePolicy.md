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
aliases:
    - "/reference/services/softlayer_software_component_antivirusspyware/updateAntivirusSpywarePolicy"
---
# [SoftLayer_Software_Component_AntivirusSpyware](/reference/services/SoftLayer_Software_Component_AntivirusSpyware)::updateAntivirusSpywarePolicy


Update an anti-virus/spyware policy.


## Overview 
Update an anti-virus/spyware policy. The policy options that it accepts are the following: 
*1 - Minimal
*2 - Relaxed
*3 - Default
*4 - High
*5 - Ultimate

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|newPolicy| string| The new anti-virus policy.|
|enforce| boolean| Enforce the updated policy|


### Required Headers
* authenticate
* SoftLayer_Software_Component_AntivirusSpywareInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Software_Component_Mcafee_InvalidPolicyUpdateResponseCode 

> Throws the error "The host ips policy update page returned a failed response code." 

* SoftLayer_Exception_Software_Component_Mcafee_PolicyUpdateFailure 

> Throws the error "The host ips policies could not be updated at this time." 



