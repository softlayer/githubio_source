---
title: "addNsRecord"
description: "The global load balancer service has been deprecated and is no longer available. 

If your globally load balanced domain... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Global_Account"
aliases:
    - "/reference/services/softlayer_network_loadbalancer_global_account/addNsRecord"
---
# [SoftLayer_Network_LoadBalancer_Global_Account](/reference/services/SoftLayer_Network_LoadBalancer_Global_Account)::addNsRecord

[Deprecated] Add the required nameserver resource record for a global load balancer account.


## Overview 
The global load balancer service has been deprecated and is no longer available. 

If your globally load balanced domain is hosted on the SoftLayer nameservers this method will add the required NS resource record to your DNS zone file and remove any A records that match the host portion of a global load balancer account hostname. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_LoadBalancer_Global_AccountInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Deprecated 

> Throw the exception "Operation addNsRecord has been deprecated and will be removed in API version 3.2." when attempting to invoke this function. 



