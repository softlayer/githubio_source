---
title: "lookupDomain"
description: "The lookupDomain method checks whether a specified domain name is available for registration in TLD's, and suggests othe... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Registration"
---
# SoftLayer_Dns_Domain_Registration::lookupDomain
## Overview 
The lookupDomain method checks whether a specified domain name is available for registration in TLD's, and suggests other similar domain names, and checks whether they are available as well. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|domainName| string| The domain name (i.e. example.com).|


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Dns_Domain_Registration_Lookup'>SoftLayer_Container_Dns_Domain_Registration_Lookup[] </a>
