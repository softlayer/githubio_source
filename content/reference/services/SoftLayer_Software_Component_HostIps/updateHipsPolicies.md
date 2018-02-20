---
title: "updateHipsPolicies"
description: "Update the Host IPS policies. To retrieve valid policy options you must use the provided relationships."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component_HostIps"
---
# SoftLayer_Software_Component_HostIps::updateHipsPolicies
## Overview 
Update the Host IPS policies. To retrieve valid policy options you must use the provided relationships. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|newIpsMode| string| IPS mode setting to be updated.|
|newIpsProtection| string| IPS protection setting to be updated|
|newFirewallMode| string| Firewall mode setting to be updated|
|newFirewallRuleset| string| Firewall rule set setting to be updated|
|newApplicationMode| string| Application mode setting to be updated|
|newApplicationRuleset| string| Application rule set setting to be updated|
|newEnforcementPolicy| string| Enforcement policy setting to be updated|


### Required Headers
* authenticate
* SoftLayer_Software_Component_HostIpsInitParameters

### Optional Headers

### Return Values
boolean
