---
title: "getPdfDetailed"
description: "Return an account's next invoice detailed portion in PDF format."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice_Next"
---
# [SoftLayer_Billing_Invoice_Next](/reference/services/SoftLayer_Billing_Invoice_Next)::getPdfDetailed

Retrieve the next billing period's detailed invoice as a PDF.


## Overview 
Return an account's next invoice detailed portion in PDF format.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|documentCreateDate| dateTime| Retrieves PDF Details on file created after this date. (optional)|


### Required Headers
* authenticate
* SoftLayer_Billing_Invoice_NextInitParameters

### Optional Headers

### Return Values
binary data

