---
title: "createObject"
description: "createObject creates a new SRV record. The ''host'' property of the templateObject parameter is scrubbed to remove all n... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord_SrvType"
---
# SoftLayer_Dns_Domain_ResourceRecord_SrvType::createObject
## Overview 
createObject creates a new SRV record. The ''host'' property of the templateObject parameter is scrubbed to remove all non-alpha numeric characters except for "@", "_", ".", "*", and "-". The ''data'' property of the templateObject parameter is scrubbed to remove all non-alphanumeric characters for "." and "-". Creating an SRV record updates the serial number of the domain the resource record is associated with. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_SrvType'>SoftLayer_Dns_Domain_ResourceRecord_SrvType </a>| The SoftLayer_Dns_Domain_ResourceRecord_SrvType object that you wish to create.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Dns_Domain_ResourceRecord_SrvTypeObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord_SrvType'>SoftLayer_Dns_Domain_ResourceRecord_SrvType </a>


### associatedMethods

*  [SoftLayer_Dns_Domain_ResourceRecord::createObject](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/createObject )
*  [SoftLayer_Dns_Domain_ResourceRecord::createObjects](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/createObjects )
*  [SoftLayer_Dns_Domain_ResourceRecord_SrvType::createObjects](/reference/services/SoftLayer_Dns_Domain_ResourceRecord_SrvType/createObjects )

