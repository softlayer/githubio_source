---
title: "delete_quote.py"
description: "delete_quote.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Order_Quote"
tags:
    - "quotes"
---


```
"""
Delete quote.
This script delete a presented quote in the SoftLayer Customer Portal's
(https://control.softlayer.com/account/quotes) using a single
API call to SoftLayer_Billing_Order_Quote::deleteQuote method passing the ID of the quote to be deleted.
Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote/deleteQuote
@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
# So we can talk to the SoftLayer API:
import SoftLayer
"""
Your SoftLayer API username and key.
Generate an API key at the SoftLayer Customer Portal
"""

API_USERNAME = 'set-me'
API_KEY = 'set-me'
"""
Set quote id you want to delete, you may use the SoftLayer_Account::getQuotes
to get the id of quotes available in the account.
"""
quoteId = 1181568
# Create a client instance
try:
    client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
    result = client['SoftLayer_Billing_Order_Quote'].deleteQuote(id=quoteId)
    print("Quote deleted!")
except SoftLayer.SoftLayerAPIError as e:
    print("Error to delete the quote faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
