---
title: "addNsRecord"
description: "If your globally load balanced domain is hosted on the SoftLayer nameservers this method will add the required NS resour... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Global_Account"
---
# SoftLayer_Network_LoadBalancer_Global_Account::addNsRecord
## Overview 
If your globally load balanced domain is hosted on the SoftLayer nameservers this method will add the required NS resource record to your DNS zone file and remove any A records that match the host portion of a global load balancer account hostname.  A NS resource record is required to be able to use your SoftLayer global load balancer account. Please make sure the zone file for the hostname listed on your SoftLayer global load balancer account is setup prior to using this method.  If your globally load balanced domain is hosted on any other nameservers this method will not be able to add the required NS record. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_LoadBalancer_Global_AccountInitParameters

### Optional Headers

### Return Values
boolean
