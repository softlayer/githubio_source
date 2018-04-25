---
title: "create_customer.py"
description: "create_customer.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Brand"
tags:
    - "brands"
---


```
'''
Create a customer.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Brand/createCustomerAccount
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
'''

import SoftLayer.API
import json

USERNAME = 'set me'
API_KEY = 'set me'

template = {
    'address1': '8200 Warden Ave',
    'city': 'Markham',
    'companyName': 'My company',
    'email': 'email@softlayer.com',
    'firstName': 'FirstName',
    'lastName': 'Surename',
    'officePhone': 'number',
    'postalCode': 'L6G 1C7',
    'state': 'TX',
    'brandId': 4,
    'country': 'CA'
}

client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)
brandService = client['SoftLayer_Brand']

try:
    result = brandService.createCustomerAccount(template)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create the customer. "
          % (e.faultCode, e.faultString))

```
