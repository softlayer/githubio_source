---
title: "get_quote_details.py"
description: "get_quote_details.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "quotes"
---


```
"""
Retrieve an account's quote information.

This script retrieves the data presented in the SoftLayer Customer Portal's
(https://control.softlayer.com/account/quotes) using an API call to SoftLayer_Account::getQuotes method.
Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getQuotes
@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
# So we can talk to the SoftLayer API:
import SoftLayer

# For nice output:
from prettytable import PrettyTable
"""
Your SoftLayer API username and key.
Generate an API key at the SoftLayer Customer Portal
"""
API_USERNAME = 'set-me'
API_KEY = 'set-me'

# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)

# Get the quotes available in the account.
try:
    quotes = client['Account'].getQuotes()
except SoftLayer.SoftLayerAPIError as e:
    print("Error getting quote information, faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

table = []
# Let's to iterate through the list of quotes to get the details of each one.
for quote in quotes:
    table.append([quote['id'], quote['name'], quote['quoteKey'], quote['status'], quote['completedPurchaseDataId'],
                  quote['createDate'], quote['expirationDate'], quote['modifyDate']])

quoteDetail = PrettyTable(
    ["ID", "Name", "Quote Key", "Status", "Completed Purchase Data Id", "Create Date", "Expiration Date",
     "Modify Date"])
quoteDetail.align["ID"] = "l"
quoteDetail.padding_width = 1
for row in table:
    quoteDetail.add_row([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])
print(quoteDetail)

```
