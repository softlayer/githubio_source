---
title: "getExchangeRate"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Currency_ExchangeRate"
aliases:
    - "/reference/services/softlayer_billing_currency_exchangerate/getExchangeRate"
---
# [SoftLayer_Billing_Currency_ExchangeRate](/reference/services/SoftLayer_Billing_Currency_ExchangeRate)::getExchangeRate




## Overview 


### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|to| string| Short Name of the currency to exchange to|
|from| string| Short Name of the base currency, optional, using default funding currency if none given|
|effectiveDate| dateTime| Effective Date to look up currency from, defaults to current date if none given|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Billing_Currency_ExchangeRateObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Currency_ExchangeRate'>SoftLayer_Billing_Currency_ExchangeRate </a>

