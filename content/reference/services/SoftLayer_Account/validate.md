---
title: "validate"
description: "This method will validate the following account fields. Included are the allowed characters for each field.<br> <strong>... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/validate"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::validate

Validate a SoftLayer customer account.


## Overview 
This method will validate the following account fields. Included are the allowed characters for each field.<br> <strong>Email Address<sup>*</sup>:</strong> letters, numbers, space, period, dash, parenthesis, exclamation point, at sign, ampersand, colon, comma, underscore, apostrophe, octothorpe.<br><br> <strong>Company Name<sup>*</sup>:</strong> alphabet, numbers, space, period, dash, octothorpe, forward slash, backward slash, comma, colon, at sign, ampersand, underscore, apostrophe, parenthesis, exclamation point. (Note: may not contain an email address)<br> <strong>First Name<sup>*</sup>:</strong> alphabet, space, period, dash, comma, apostrophe.<br> <strong>Last Name<sup>*</sup>:</strong> alphabet, space, period, dash, comma, apostrophe.<br> <strong>Address 1<sup>*</sup>:</strong> alphabet, numbers, space, period, dash, octothorpe, forward slash, backward slash, comma, colon, at sign, ampersand, underscore, apostrophe.<br> <strong>Address 2:</strong> alphabet, numbers, space, period, dash, octothorpe, forward slash, backward slash, comma, colon, at sign, ampersand, underscore, apostrophe.<br> <strong>City<sup>*</sup>:</strong> alphabet, space, period, dash, apostrophe.<br> <strong>State<sup>*</sup>:</strong> Required if country is US or Canada. Must be valid Alpha-2 ISO 3166-1 state code for that country.<br> <strong>Postal Code<sup>*</sup>:</strong> alphabet, numbers, dash, space.<br> <strong>Country<sup>*</sup>:</strong> alphabet, numbers. Must be valid Alpha-2 ISO 3166-1 country code.<br> <strong>Office Phone<sup>*</sup>:</strong> alphabet, numbers, space, period, dash, parenthesis, plus sign.<br> <strong>Alternate Phone:</strong> alphabet, numbers, space, period, dash, parenthesis, plus sign.<br> <strong>Fax Phone:</strong> alphabet, numbers, space, period, dash, parenthesis, plus sign.<br> 
* denotes a required field.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|account| <a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>| |


### Required Headers
* authenticate

### Optional Headers

### Return Values
array of strings

