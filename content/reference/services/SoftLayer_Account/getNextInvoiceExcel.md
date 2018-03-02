---
title: "getNextInvoiceExcel"
description: "Return an account's next invoice in a Microsoft excel format. The 'next invoice' is what a customer will be billed on th... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
---
# SoftLayer_Account::getNextInvoiceExcel
## Overview 
Return an account's next invoice in a Microsoft excel format. The "next invoice" is what a customer will be billed on their next invoice, assuming no changes are made. Currently this does not include Bandwidth Pooling charges.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|documentCreateDate| dateTime| Retrieves Excel on file created after this date. (optional)|


### Required Headers
* authenticate

### Optional Headers

### Return Values
binary data

