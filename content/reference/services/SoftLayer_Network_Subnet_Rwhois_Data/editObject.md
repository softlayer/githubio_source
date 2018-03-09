---
title: "editObject"
description: "Edit the RWHOIS record by passing in a modified version of the record object.  All fields are editable."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Rwhois_Data"
---
# [SoftLayer_Network_Subnet_Rwhois_Data](/reference/services/SoftLayer_Network_Subnet_Rwhois_Data)::editObject

Edit the RWHOIS record by passing in a modified version of the record object. All fields are editable. The fields are as follows: 
* companyName
* firstName
* lastName
* city
* country
* postalCode
* abuseEmail
* address1


## Overview 
Edit the RWHOIS record by passing in a modified version of the record object.  All fields are editable.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network_Subnet_Rwhois_Data'>SoftLayer_Network_Subnet_Rwhois_Data </a>| A skeleton SoftLayer_Network_Subnet_Rwhois_Data object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_Network_Subnet_Rwhois_DataInitParameters

### Optional Headers

### Return Values
boolean

