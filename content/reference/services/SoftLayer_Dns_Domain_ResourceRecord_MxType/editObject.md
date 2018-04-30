---
title: "editObject"
description: "editObject edits an existing MX resource record. The ''host'' property of the templateObject parameter is scrubbed to re... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord_MxType"
aliases:
    - "/reference/services/softlayer_dns_domain_resourcerecord_mxtype/editObject"
---
# [SoftLayer_Dns_Domain_ResourceRecord_MxType](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_MxType)::editObject

Edit a domain's MX record.


## Overview 
editObject edits an existing MX resource record. The ''host'' property of the templateObject parameter is scrubbed to remove all non-alpha numeric characters except for "@", "_", ".", "*", and "-". The ''data'' property of the templateObject parameter is scrubbed to remove all non-alphanumeric characters for "." and "-". Editing an MX record updates the serial number of the domain the record is associated with. 

''editObject'' returns Boolean ''true'' on a successful edit or ''false'' if it was unable to edit the resource record. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_MxType'>SoftLayer_Dns_Domain_ResourceRecord_MxType </a>| A skeleton SoftLayer_Dns_Domain_ResourceRecord_MxType object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_Dns_Domain_ResourceRecord_MxTypeInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Dns_Domain_ResourceRecord::editObject](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/editObject )
*  [SoftLayer_Dns_Domain_ResourceRecord::editObjects](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/editObjects )
*  [SoftLayer_Dns_Domain_ResourceRecord_MxType::editObjects](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_MxType/editObjects )

