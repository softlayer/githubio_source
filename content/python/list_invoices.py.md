---
title: "list_invoices.py"
description: "list_invoices.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Invoice"
tags:
    - "brands"
---


```
'''
List invoices.

The script retrieves all the invoices in a brand account.
It displays the same result like in https://agent.softlayer.com/administration/invoice/list

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getInvoices
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Invoice
http://sldn.softlayer.com/article/Object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
'''

import SoftLayer.API
import json

USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)

accountService = client['SoftLayer_Account']
objectMask = "mask[id, modifyDate, createDate, amount, payment, typeCode, statusCode, purchaseOrderNumber]"

try:
    result = accountService.getInvoices(mask=objectMask)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the invoices. "
          % (e.faultCode, e.faultString))

```
