---
title: "list_invoices.rb"
description: "list_invoices.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Invoice"
tags:
    - "brands"
---


```
# List invoices.
#
# The script retrieves all the invoices in a brand account.
# It displays the same result like in https://agent.softlayer.com/administration/invoice/list
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getInvoices
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Invoice
# http://sldn.softlayer.com/article/Object-Masks
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'softlayer_api'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
account_service = client['SoftLayer_Account']
object_mask = 'mask[id, modifyDate, createDate, amount, payment, typeCode, statusCode, purchaseOrderNumber]'

begin
  result = account_service.object_mask(object_mask).getInvoices
  print result
rescue StandardError => exception
  puts "Unable to list the invoices.: #{exception}"
end

```
