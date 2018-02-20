---
title: "getNextInvoicePdf"
description: "Return an account's next invoice in PDF format. The 'next invoice' is what a customer will be billed on their next invoi... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
---
# SoftLayer_Account::getNextInvoicePdf
## Overview 
Return an account's next invoice in PDF format. The "next invoice" is what a customer will be billed on their next invoice, assuming no changes are made. Currently this does not include Bandwidth Pooling charges.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|documentCreateDate| dateTime| Retrieves PDF on file created after this date. (optional)|


### Required Headers
* authenticate

### Optional Headers

### Return Values
binary data
