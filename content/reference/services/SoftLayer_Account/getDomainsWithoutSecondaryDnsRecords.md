---
title: "getDomainsWithoutSecondaryDnsRecords"
description: "Retrieve the DNS domains associated with an account that were not created as a result of a secondary DNS zone transfer."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/getDomainsWithoutSecondaryDnsRecords"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::getDomainsWithoutSecondaryDnsRecords

Retrieve the DNS domains associated with an account that were not created as a result of a secondary DNS zone transfer.


## Overview 
Retrieve the DNS domains associated with an account that were not created as a result of a secondary DNS zone transfer.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_AccountObjectMask
* SoftLayer_AccountObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain[] </a>




