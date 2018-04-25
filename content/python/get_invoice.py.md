---
title: "get_invoice.py"
description: "get_invoice.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Invoice"
tags:
    - "billing"
---


```
"""
Retrieve the invoice information.

This script makes a single call to the getInvoices() method in the
SoftLayer_Account API service and uses a object mask to get more
information about the invoices.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getInvoices
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Invoice

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

"""
Client configuration
Your SoftLayer API username and key.
"""
USERNAME = 'set me'
API_KEY = 'set me'

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

# Declaring the object mask to get information about the invoices.
objectMask = "mask[payment,amount,invoiceTotalOneTimeAmount,invoiceTotalRecurringAmount,invoiceTotalOneTimeTaxAmount,invoiceTotalRecurringTaxAmount]"

try:
    # Retrieve the invoices for the account.
    invoices = accountService.getInvoices(mask=objectMask)
    print(invoices)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the invoices. " % (e.faultCode, e.faultString))
    exit(1)

```
