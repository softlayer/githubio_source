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
---
# SoftLayer_Account::getDomainsWithoutSecondaryDnsRecords
## Overview 
Retrieve the DNS domains associated with an account that were not created as a result of a secondary DNS zone transfer.

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
<a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain[] </a>
