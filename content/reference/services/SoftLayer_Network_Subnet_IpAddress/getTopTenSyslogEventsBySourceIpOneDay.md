---
title: "getTopTenSyslogEventsBySourceIpOneDay"
description: "Retrieve top Ten network datacenter syslog events, grouped by source ip address, for the last 24 hours"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_IpAddress"
aliases:
    - "/reference/services/softlayer_network_subnet_ipaddress/getTopTenSyslogEventsBySourceIpOneDay"
---
# [SoftLayer_Network_Subnet_IpAddress](/reference/services/SoftLayer_Network_Subnet_IpAddress)::getTopTenSyslogEventsBySourceIpOneDay

Retrieve top Ten network datacenter syslog events, grouped by source ip address, for the last 24 hours


## Overview 
Retrieve top Ten network datacenter syslog events, grouped by source ip address, for the last 24 hours

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Subnet_IpAddressInitParameters
* authenticate


### Optional Headers
* SoftLayer_Network_Subnet_IpAddressObjectMask
* SoftLayer_Network_Subnet_IpAddressObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>




