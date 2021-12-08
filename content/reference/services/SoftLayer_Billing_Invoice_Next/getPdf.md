---
title: "getPdf"
description: "Return an account's next invoice in PDF format."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice_Next"
aliases:
    - "/reference/services/softlayer_billing_invoice_next/getPdf"
---
# [SoftLayer_Billing_Invoice_Next](/reference/services/SoftLayer_Billing_Invoice_Next)::getPdf


Retrieve the next billing period's invoice as a PDF.


## Overview 
Return an account's next invoice in PDF format.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|documentCreateDate| dateTime| Retrieves PDF on file created after this date. (optional)|


### Required Headers
* authenticate
* SoftLayer_Billing_Invoice_NextInitParameters


### Return Values
* binary data




