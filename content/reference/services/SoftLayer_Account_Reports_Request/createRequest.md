---
title: "createRequest"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Reports_Request"
---
# SoftLayer_Account_Reports_Request::createRequest
## Overview 


### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|contact| <a href='/reference/datatypes/SoftLayer_Account_Contact'>SoftLayer_Account_Contact </a>| The external party for which the request may be created|
|reason| string| The reason the external party is requesting the report|
|reportType| string| type of the report customer is requesting|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Account_Reports_RequestObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Account_Reports_Request'>SoftLayer_Account_Reports_Request </a>
