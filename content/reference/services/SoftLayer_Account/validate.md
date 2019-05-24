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

Validates SoftLayer account information. Will return an error if any field is not valid.


## Overview 
This method will validate the following account fields. Included are the allowed characters for each field.<br> <strong>Company Name (required):</strong> alphabet, numbers, space, period, dash, octothorpe, forward slash, backward slash, comma, colon, at sign, ampersand, underscore, apostrophe, parenthesis, exclamation point. (Note: may not contain an email address)<br> <strong>First Name (required):</strong> alphabet, space, period, dash, comma, apostrophe.<br> <strong>Last Name (required):</strong> alphabet, space, period, dash, comma, apostrophe.<br> <strong>Email (required):</strong> Validates e-mail addresses against the syntax in RFC 822.<br> <strong>Address 1 (required):</strong> alphabet, numbers, space, period, dash, octothorpe, forward slash, backward slash, comma, colon, at sign, ampersand, underscore, apostrophe, parentheses.<br> <strong>Address 2 (required):</strong> alphabet, numbers, space, period, dash, octothorpe, forward slash, backward slash, comma, colon, at sign, ampersand, underscore, apostrophe, parentheses.<br> <strong>City (required):</strong> alphabet, space, period, dash, apostrophe, forward slash.<br> <strong>State (required):</strong> Required if country is US, Brazil, Canada or India. Must be valid Alpha-2 ISO 3166-1 state code for that country.<br> <strong>Postal Code (required):</strong> alphabet, numbers, dash, space.<br> <strong>Country (required):</strong> alphabet, numbers. Must be valid Alpha-2 ISO 3166-1 country code.<br> <strong>Office Phone (required):</strong> alphabet, numbers, space, period, dash, parenthesis, plus sign.<br> <strong>Alternate Phone:</strong> alphabet, numbers, space, period, dash, parenthesis, plus sign.<br> <strong>Fax Phone:</strong> alphabet, numbers, space, period, dash, parenthesis, plus sign.<br> 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|account| <a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>| |


### Required Headers
* authenticate


### Return Values
* array of strings




