---
title: "editObject"
description: "Edit the properties of a secondary DNS record by passing in a modified instance of a SoftLayer_Dns_Secondary object. You... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Secondary"
---
# SoftLayer_Dns_Secondary::editObject
## Overview 
Edit the properties of a secondary DNS record by passing in a modified instance of a SoftLayer_Dns_Secondary object. You may only edit the ''masterIpAddress'' and ''transferFrequency'' properties of your secondary DNS record. ''ZoneName'' may not be altered after a secondary DNS record has been created.  Please remove and re-create the record if you need to make changes to your zone name. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Dns_Secondary'>SoftLayer_Dns_Secondary </a>| A skeleton SoftLayer_Dns_Secondary object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_Dns_SecondaryInitParameters

### Optional Headers

### Return Values
boolean
