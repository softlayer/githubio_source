---
title: "createObject"
description: "createObject creates a new domain resource record. The ''host'' property of the templateObject parameter is scrubbed to... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord"
---
# SoftLayer_Dns_Domain_ResourceRecord::createObject
## Overview 
createObject creates a new domain resource record. The ''host'' property of the templateObject parameter is scrubbed to remove all non-alpha numeric characters except for "@", "_", ".", "*", and "-". The ''data'' property of the templateObject parameter is scrubbed to remove all non-alphanumeric characters for "." and "-". Creating a resource record updates the serial number of the domain the resource record is associated with. 

''createObject'' returns Boolean ''true'' on successful create or ''false'' if it was unable to create a resource record. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord </a>| The SoftLayer_Dns_Domain_ResourceRecord object that you wish to create.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Dns_Domain_ResourceRecordObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord </a>
