---
title: "editObjects"
description: "Edit multiple MX records on a domain. This follows the same logic as ''createObject'. The serial number of the domain as... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord_MxType"
---
# SoftLayer_Dns_Domain_ResourceRecord_MxType::editObjects
## Overview 
Edit multiple MX records on a domain. This follows the same logic as ''createObject'. The serial number of the domain associated with this MX record is updated upon creation. 

''createObjects'' returns Boolean ''true'' on successful creation or ''false'' if it was unable to create a resource record. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord[] </a>| An array of skeleton SoftLayer_Dns_Domain_ResourceRecord_MxType objects with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Dns_Domain_ResourceRecord::editObject](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/editObject )
*  [SoftLayer_Dns_Domain_ResourceRecord::editObjects](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/editObjects )
*  [SoftLayer_Dns_Domain_ResourceRecord_MxType::editObject](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_MxType/editObject )

