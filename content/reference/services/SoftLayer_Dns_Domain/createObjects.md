---
title: "createObjects"
description: "Create multiple domains on the SoftLayer name servers. Each domain record passed to ''createObjects'' follows the logic... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain"
aliases:
    - "/reference/services/softlayer_dns_domain/createObjects"
---
# [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain)::createObjects

Create multiple domains at once.


## Overview 
Create multiple domains on the SoftLayer name servers. Each domain record passed to ''createObjects'' follows the logic in the SoftLayer_Dns_Domain ''createObject'' method. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain[] </a>| An array of SoftLayer_Dns_Domain objects that you wish to create.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Dns_DomainObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Dns_Domain'>SoftLayer_Dns_Domain[] </a>


### associatedMethods

*  [SoftLayer_Dns_Domain::createObject](/reference/services/SoftLayer_Dns_Domain/createObject )

