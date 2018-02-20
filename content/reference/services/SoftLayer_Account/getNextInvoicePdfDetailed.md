---
title: "getNextInvoicePdfDetailed"
description: "Return an account's next invoice detailed portion in PDF format. The 'next invoice' is what a customer will be billed on... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
---
# SoftLayer_Account::getNextInvoicePdfDetailed
## Overview 
Return an account's next invoice detailed portion in PDF format. The "next invoice" is what a customer will be billed on their next invoice, assuming no changes are made. Currently this does not include Bandwidth Pooling charges.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|documentCreateDate| dateTime| Retrieves PDF Details on file created after this date. (optional)|


### Required Headers
* authenticate

### Optional Headers

### Return Values
binary data
