---
title: "removeNsRecord"
description: "If your globally load balanced domain is hosted on the SoftLayer nameservers this method will remove the NS resource rec... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Global_Account"
---
# [SoftLayer_Network_LoadBalancer_Global_Account](/reference/services/SoftLayer_Network_LoadBalancer_Global_Account)::removeNsRecord

Remove the required nameserver resource record for a global load balancer account.


## Overview 
If your globally load balanced domain is hosted on the SoftLayer nameservers this method will remove the NS resource record from your DNS zone file. Removing the NS resource record will basically disable your global load balancer account since no DNS requests will be forwarded to the global load balancers. Any A records that were removed when the NS resource record was added will not be created for you.  If your globally load balanced domain is hosted on any other nameservers this method will not be able to remove the required NS record. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_LoadBalancer_Global_AccountInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Network_LoadBalancer_Global_Account::addNsRecord](/reference/services/SoftLayer_Network_LoadBalancer_Global_Account/addNsRecord )

