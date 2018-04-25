---
title: "get_accounts_brands.py"
description: "get_accounts_brands.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Brand"
tags:
    - "brands"
---


```
'''
Get owned account

The script retrieves all the owned accounts for an arbitrary brand,
the script makes a call to getOwnedBrands() method to retrieve
the brands where the account belongs, then it calls the getAllOwnedAccounts()
method to get the owned accounts for every brand.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getOwnedBrands
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getAllOwnedAccounts
http://sldn.softlayer.com/reference/services/SoftLayer_Brand
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Brand

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
'''
import SoftLayer.API

USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)

accountService = client['SoftLayer_Account']
brandService = client['SoftLayer_Brand']

# Getting the brands
brands = accountService.getOwnedBrands()
for brand in brands:
    brandId = brand['id']
    # Getting the owned Accounts
    accounts = brandService.getAllOwnedAccounts(id=brandId)
    for account in accounts:
        print(account['companyName'])

```
