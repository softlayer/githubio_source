---
title: "validatePersonForAllRegistrars"
description: "Validates this person detail against all supported external registrars (APNIC/ARIN/RIPE). The validation uses the most r... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Regional_Registry_Detail"
aliases:
    - "/reference/services/softlayer_account_regional_registry_detail/validatePersonForAllRegistrars"
---
# [SoftLayer_Account_Regional_Registry_Detail](/reference/services/SoftLayer_Account_Regional_Registry_Detail)::validatePersonForAllRegistrars

Validate an existing person detail object.


## Overview 
Validates this person detail against all supported external registrars (APNIC/ARIN/RIPE). The validation uses the most restrictive rules ensuring that any person detail passing this validation would be acceptable to any supported registrar. 

The person detail properties are validated against - Non-emptiness - Minimum length - Maximum length - Maximum words - Supported characters - Format of data 

If the person detail validation succeeds, then an empty list is returned indicating no errors were found and that this person detail would work against all three registrars during a subnet registration. 

If the person detail validation fails, then an array of validation errors (SoftLayer_Container_Message[]) is returned. Each message container contains error messages grouped by property type and a message type indicating the person detail property type object which failed validation. It is possible to create a subnet registration using a person detail which does not pass this validation, but at least one registrar would reject it for being invalid. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Account_Regional_Registry_DetailInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Message'>SoftLayer_Container_Message[] </a>




