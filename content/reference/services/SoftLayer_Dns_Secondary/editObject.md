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
aliases:
    - "/reference/services/softlayer_dns_secondary/editObject"
---
# [SoftLayer_Dns_Secondary](/reference/services/SoftLayer_Dns_Secondary)::editObject


Edit a secondary DNS record.


## Overview 
Edit the properties of a secondary DNS record by passing in a modified instance of a SoftLayer_Dns_Secondary object. You may only edit the ''masterIpAddress'' and ''transferFrequency'' properties of your secondary DNS record. ''ZoneName'' may not be altered after a secondary DNS record has been created.  Please remove and re-create the record if you need to make changes to your zone name. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Dns_Secondary'>SoftLayer_Dns_Secondary </a>| A skeleton SoftLayer_Dns_Secondary object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_Dns_SecondaryInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "The zone name may not be edited after the secondary DNS record is created." if you are trying to edit the zone name. 

* SoftLayer_Exception_Public 

> Throw the exception "The master IP address is not a valid IP address." if the supplied master IP address is not in a valid IP format. 

* SoftLayer_Exception_Public 

> Throw the exception "The transfer frequency must be numeric." if the transfer frequency is blank or not a valid number. 



