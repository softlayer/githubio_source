---
title: "editObject"
description: "The global load balancer service has been deprecated and is no longer available. 

Edit the properties of a global load... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Global_Account"
aliases:
    - "/reference/services/softlayer_network_loadbalancer_global_account/editObject"
---
# [SoftLayer_Network_LoadBalancer_Global_Account](/reference/services/SoftLayer_Network_LoadBalancer_Global_Account)::editObject

[Deprecated] Edit a global load balancer account and the hosts that make up the load balancing pool.


## Overview 
The global load balancer service has been deprecated and is no longer available. 

Edit the properties of a global load balancer account by passing in a modified instance of the object. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Global_Account'>SoftLayer_Network_LoadBalancer_Global_Account </a>| A skeleton SoftLayer_Network_LoadBalancer_Global_Account object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_Network_LoadBalancer_Global_AccountInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Deprecated 

> Throw the exception "Operation editObject has been deprecated and will be removed in API version 3.2." when attempting to invoke this function. 



