---
title: "getObject"
description: "getObject returns a SoftLayer_Network_Firewall_Template object. You can retrieve all available firewall templates. getAl... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Template"
aliases:
    - "/reference/services/softlayer_network_firewall_template/getObject"
---
# [SoftLayer_Network_Firewall_Template](/reference/services/SoftLayer_Network_Firewall_Template)::getObject

Retrieve a SoftLayer_Network_Firewall_Template record.


## Overview 
getObject returns a SoftLayer_Network_Firewall_Template object. You can retrieve all available firewall templates. getAllObjects returns an array of all available SoftLayer_Network_Firewall_Template objects. You can use these templates to generate a [[SoftLayer Network Firewall Update Request]]. 

@SLDNDocumentation Service See Also SoftLayer_Network_Firewall_Update_Request 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Firewall_TemplateInitParameters
* authenticate


### Optional Headers
* SoftLayer_Network_Firewall_TemplateObjectMask
* SoftLayer_Network_Firewall_TemplateObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Firewall_Template'>SoftLayer_Network_Firewall_Template </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throw the error "Unable to find object with id of {id}." if the given initialization parameter has an invalid id field. 

* SoftLayer_Exception_AccessDenied 

> Throw the error "Access Denied." if the given initialization parameter id field is not the account id of the user making the API call. 



