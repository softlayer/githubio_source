---
title: "createObjects"
description: "Create Softlayer portal user VPN overrides."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Service_Vpn_Overrides"
aliases:
    - "/reference/services/softlayer_network_service_vpn_overrides/createObjects"
---
# [SoftLayer_Network_Service_Vpn_Overrides](/reference/services/SoftLayer_Network_Service_Vpn_Overrides)::createObjects


Create Softlayer portal user VPN overrides.


## Overview 
Create Softlayer portal user VPN overrides. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Network_Service_Vpn_Overrides'>SoftLayer_Network_Service_Vpn_Overrides[] </a>| An array of SoftLayer_Network_Service_Vpn_Overrides objects that you wish to create.|


### Required Headers
* authenticate


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Network_Service_Vpn_Overrides::createObject](/reference/services/SoftLayer_Network_Service_Vpn_Overrides/createObject )



### Error Handling

* SoftLayer_Exception_NotFound 

> Thrown if the requested user or subnet records could not be retrieved. 

* SoftLayer_Exception_NotSupported 

> <<<EOT 

* SoftLayer_Exception_NotSupported 

> Thrown if subnet is ineligible for manual route assignments. 



