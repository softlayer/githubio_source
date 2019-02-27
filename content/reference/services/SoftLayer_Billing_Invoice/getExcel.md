---
title: "getExcel"
description: "Retrieve a Microsoft Excel spreadsheet of a SoftLayer invoice. You must have a Microsoft Excel reader installed in order... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice"
aliases:
    - "/reference/services/softlayer_billing_invoice/getExcel"
---
# [SoftLayer_Billing_Invoice](/reference/services/SoftLayer_Billing_Invoice)::getExcel

Retrieve a Microsoft Excel copy of an invoice.


## Overview 
Retrieve a Microsoft Excel spreadsheet of a SoftLayer invoice. You must have a Microsoft Excel reader installed in order to view these invoice files. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Billing_InvoiceInitParameters


### Return Values
* binary data

### External Links


* [Microsoft Excel at Wikipedia](http://en.wikipedia.org/wiki/Microsoft_Excel)




### Error Handling

* SoftLayer_Exception. 

> Throw the exception "Excel workbook does not exist: invoice has not yet been closed." when trying to retrieve an open invoice. This service is not design to generate spreadsheet for open invoices. 



