---
title: "getParameterConfigurationsForCustomerView"
description: "All of the IPSec VPN tunnel's configurations will be returned.  It will list all of phase one and two negotiation parame... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
aliases:
    - "/reference/services/softlayer_network_tunnel_module_context/getParameterConfigurationsForCustomerView"
---
# [SoftLayer_Network_Tunnel_Module_Context](/reference/services/SoftLayer_Network_Tunnel_Module_Context)::getParameterConfigurationsForCustomerView

Build and returns IPsec VPN tunnel configurations


## Overview 
All of the IPSec VPN tunnel's configurations will be returned.  It will list all of phase one and two negotiation parameters.  Both remote and local subnets will be provided as well.  This is useful when the configurations need to be passed on to another team and/or company for internal network configuration. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Tunnel_Module_ContextInitParameters


### Return Values
* string


### Associated Methods

*  [SoftLayer_Network_Tunnel_Module_Context::downloadParameterConfigurations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/downloadParameterConfigurations )




