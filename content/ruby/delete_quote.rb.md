---
title: "delete_quote.rb"
description: "delete_quote.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Order_Quote"
tags:
    - "quote"
---


```
#
# Delete quote.
# This script deletes a presented quote in the SoftLayer Customer Portal's
# (https://control.softlayer.com/account/quotes) using a single
# API call to SoftLayer_Billing_Order_Quote::deleteQuote method passing the ID of the quote to be deleted.
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote
# http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote/deleteQuote
# @License: http://sldn.softlayer.com/article/License
# @Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
#

require 'rubygems'
require 'softlayer_api'

# We can set the default client to be our client and that way
# we can avoid supplying it later
SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'
client = SoftLayer::Client.new(
  username: SL_API_USERNAME,
  api_key: SL_API_KEY)

# Set the id of quote you want to delete, you may use SoftLayer::getQuotes method
# to get a list of quotes available in the account
quote_id = 123_456
begin
  result = client['SoftLayer_Billing_Order_Quote'].object_with_id(quote_id).deleteQuote
  pp(result)
rescue => error_reason
  puts error_reason
end

```
