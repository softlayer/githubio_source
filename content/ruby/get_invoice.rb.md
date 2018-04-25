---
title: "get_invoice.rb"
description: "get_invoice.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Invoice"
tags:
    - "billing"
---


```
# Retrieve the invoice information.
#
# This script makes a single call to the getInvoices() method in the
# SoftLayer_Account API service and uses a object mask to get more
# information about the invoices.
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getInvoices
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Invoice
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API key and username.
USERNAME = 'set me'
API_KEY = 'set me'

# Declaring the object mask to get more information about the invoices.
object_mask = 'mask[payment,amount,invoiceTotalOneTimeAmount,invoiceTotalRecurringAmount,invoiceTotalOneTimeTaxAmount,invoiceTotalRecurringTaxAmount]'

# Declare the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
hardware_account = client['SoftLayer_Account']

begin
  # Retrieve the invoices for the account.
  invoices = hardware_account.object_mask(object_mask).getInvoices
  print invoices
rescue StandardError => exception
  puts "Unable to retrieve the invoices. : #{exception}"
end

```
