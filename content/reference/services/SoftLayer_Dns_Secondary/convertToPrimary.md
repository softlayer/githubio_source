---
title: "convertToPrimary"
description: "A secondary DNS record may be converted to a primary DNS record. By converting a secondary DNS record, the SoftLayer nam... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Secondary"
aliases:
    - "/reference/services/softlayer_dns_secondary/convertToPrimary"
---
# [SoftLayer_Dns_Secondary](/reference/services/SoftLayer_Dns_Secondary)::convertToPrimary

Convert a secondary DNS record into a primary DNS record.


## Overview 
A secondary DNS record may be converted to a primary DNS record. By converting a secondary DNS record, the SoftLayer name servers will be the authoritative nameserver for this domain and will be directly editable in the SoftLayer API and Portal. 

Primary DNS record conversion performs the following steps: 
* The SOA record is updated with SoftLayer's primary name server.
* All NS records are removed and replaced with SoftLayer's NS records.
* The secondary DNS record is removed.


After the DNS records are converted, the following restrictions will apply to the new domain record: 
* You will need to manage the zone record using the [[SoftLayer_Dns_Domain]] service.
* You may not edit the SOA or NS records.
* You may only edit the following resource records: A, AAAA, CNAME, MX, TX, SRV.


This change can not be undone, and the record can not be converted back into a secondary DNS record once the conversion is complete. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Dns_SecondaryInitParameters

### Optional Headers

### Return Values
boolean

