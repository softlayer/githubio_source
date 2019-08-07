---
title: "createCustomerAccount"
description: "Create a new customer account record. By default, the newly created account will be associated to a platform (PaaS) acco... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Brand"
classes:
    - "SoftLayer_Brand"
aliases:
    - "/reference/services/softlayer_brand/createCustomerAccount"
---
# [SoftLayer_Brand](/reference/services/SoftLayer_Brand)::createCustomerAccount

Create a new customer account record.


## Overview 
Create a new customer account record. By default, the newly created account will be associated to a platform (PaaS) account. To skip the automatic creation and linking to a new platform account, set the <em>bluemixLinkedFlag</em> to <strong>false</strong> on the account template. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|account| <a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>| The template of the account object to be created.|
|bypassDuplicateAccountCheck| boolean| Bypass validation for duplicate account(s).|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_BrandObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>




