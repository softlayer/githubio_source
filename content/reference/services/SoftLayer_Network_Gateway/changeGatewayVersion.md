---
title: "changeGatewayVersion"
description: "Used to create a transaction to upgrade or rollback the vSRX version for Juniper gateway."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway"
aliases:
    - "/reference/services/softlayer_network_gateway/changeGatewayVersion"
---
# [SoftLayer_Network_Gateway](/reference/services/SoftLayer_Network_Gateway)::changeGatewayVersion

Change Juniper vSRX version on a Gateway


## Overview 
Used to create a transaction to upgrade or rollback the vSRX version for Juniper gateway. 



### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|versionId| integer| Version Id found in SoftLayer_Network_Gateway_ServiceVariables|


### Required Headers
* authenticate
* SoftLayer_Network_GatewayInitParameters

### Optional Headers

### Return Values
boolean

