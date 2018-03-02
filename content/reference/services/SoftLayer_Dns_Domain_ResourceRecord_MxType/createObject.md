---
title: "createObject"
description: "createObject creates a new MX record. The ''host'' property of the templateObject parameter is scrubbed to remove all no... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord_MxType"
---
# SoftLayer_Dns_Domain_ResourceRecord_MxType::createObject
## Overview 
createObject creates a new MX record. The ''host'' property of the templateObject parameter is scrubbed to remove all non-alpha numeric characters except for "@", "_", ".", "*", and "-". The ''data'' property of the templateObject parameter is scrubbed to remove all non-alphanumeric characters for "." and "-". Creating an MX record updates the serial number of the domain the resource record is associated with. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_MxType'>SoftLayer_Dns_Domain_ResourceRecord_MxType </a>| The SoftLayer_Dns_Domain_ResourceRecord_MxType object that you wish to create.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Dns_Domain_ResourceRecord_MxTypeObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_MxType'>SoftLayer_Dns_Domain_ResourceRecord_MxType </a>


### associatedMethods

*  [SoftLayer_Dns_Domain_ResourceRecord::createObject](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/createObject )
*  [SoftLayer_Dns_Domain_ResourceRecord::createObjects](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/createObjects )
*  [SoftLayer_Dns_Domain_ResourceRecord_MxType::createObjects](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_MxType/createObjects )

