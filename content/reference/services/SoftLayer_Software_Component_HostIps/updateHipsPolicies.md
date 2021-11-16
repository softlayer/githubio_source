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
aliases:
    - "/reference/services/softlayer_software_component_hostips/updateHipsPolicies"
---
# [SoftLayer_Software_Component_HostIps](/reference/services/SoftLayer_Software_Component_HostIps)::updateHipsPolicies


Update the Host IPS policies.


## Overview 
Update the Host IPS policies. To retrieve valid policy options you must use the provided relationships. 

-----

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


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Software_Component_Mcafee_AntivirusPolicyUpdateInProgress 

> Throws the error "A host ips policy update may only take place if a previous anti-virus/spyware policy update has finished." 

* SoftLayer_Exception_Software_Component_Mcafee_InvalidPolicyUpdateResponseCode 

> Throws the error "The host ips policy update page returned a failed response code." 

* SoftLayer_Exception_Software_Component_Mcafee_PolicyUpdateFailure 

> Throws the error "The host ips policies could not be updated at this time." 



