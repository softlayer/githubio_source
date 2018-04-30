---
title: "getPendingCreditCardChangeRequestData"
description: "Before being approved for general use, a credit card must be approved by a SoftLayer agent. Once a credit card change re... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/getPendingCreditCardChangeRequestData"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::getPendingCreditCardChangeRequestData

Retrieve details of all credit card change requests which have not been processed by a SoftLayer agent.


## Overview 
Before being approved for general use, a credit card must be approved by a SoftLayer agent. Once a credit card change request has been either approved or denied, the change request will no longer appear in the list of pending change requests. This method will return a list of all pending change requests as well as a portion of the data from the original request. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Account_Payment_Method_CreditCard'>SoftLayer_Container_Account_Payment_Method_CreditCard[] </a>

