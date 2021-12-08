---
title: "transferNow"
description: "Force a secondary DNS zone transfer by setting it's status 'Transfer Now'.  A zone transfer will be initiated within a m... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Secondary"
aliases:
    - "/reference/services/softlayer_dns_secondary/transferNow"
---
# [SoftLayer_Dns_Secondary](/reference/services/SoftLayer_Dns_Secondary)::transferNow


Initiate a zone transfer for a secondary DNS record.


## Overview 
Force a secondary DNS zone transfer by setting it's status "Transfer Now".  A zone transfer will be initiated within a minute of receiving this API call. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Dns_SecondaryInitParameters


### Return Values
* boolean




