---
title: "getPdfFileSize"
description: "Retrieve the size of a PDF record of a SoftLayer invoice. SoftLayer keeps PDF records of all closed invoices for custome... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice"
aliases:
    - "/reference/services/softlayer_billing_invoice/getPdfFileSize"
---
# [SoftLayer_Billing_Invoice](/reference/services/SoftLayer_Billing_Invoice)::getPdfFileSize

Retrieve the size of a PDF copy of an invoice.


## Overview 
Retrieve the size of a PDF record of a SoftLayer invoice. SoftLayer keeps PDF records of all closed invoices for customer retrieval from the portal and API. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Billing_InvoiceInitParameters


### Return Values
* integer

### External Links


* [Portable Document Format at Wikipedia](http://en.wikipedia.org/wiki/Portable_Document_Format)




### Error Handling

* SoftLayer_Exception. 

> Throw the exception "PDF does not exist: invoice has not yet been closed." when trying to retrieve an open invoice. Open invoices do not have PDF records. 

* SoftLayer_Exception. 

> Throw the exception "PDF does not exist: file not found" if the API is unable to locate the PDF File for the invoice. 

* SoftLayer_Exception. 

> Throw the exception "Unable to load a valid invoice PDF." if the PDF for this invoice is a corrupted. 



