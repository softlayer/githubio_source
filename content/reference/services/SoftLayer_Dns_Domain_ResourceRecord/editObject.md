---
title: "editObject"
description: "editObject edits an existing domain resource record. The ''host'' property of the templateObject parameter is scrubbed t... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord"
aliases:
    - "/reference/services/softlayer_dns_domain_resourcerecord/editObject"
---
# [SoftLayer_Dns_Domain_ResourceRecord](/reference/services/SoftLayer_Dns_Domain_ResourceRecord)::editObject

Edit a domain's resource record.


## Overview 
editObject edits an existing domain resource record. The ''host'' property of the templateObject parameter is scrubbed to remove all non-alpha numeric characters except for "@", "_", ".", "*", and "-". The ''data'' property of the templateObject parameter is scrubbed to remove all non-alphanumeric characters for "." and "-". Editing a resource record updates the serial number of the domain the resource record is associated with. 

''editObject'' returns Boolean ''true'' on a successful edit or ''false'' if it was unable to edit the resource record. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord'>SoftLayer_Dns_Domain_ResourceRecord </a>| A skeleton SoftLayer_Dns_Domain_ResourceRecord object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_Dns_Domain_ResourceRecordInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Dns_ResourceRecord::editObjects](/reference/services/SoftLayer_Dns_ResourceRecord/editObjects )

