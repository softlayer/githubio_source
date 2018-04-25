---
title: "place_quote_order.rb"
description: "place_quote_order.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Virtual_Server"
    - "SoftLayer_Container_Product_Order_Virtual_Guest"
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Order_Quote"
tags:
    - "quote"
---


```
#
# Order from account's quote.
# This script creates an order from a account's quote presented
# in the SoftLayer Customer Portal's (https://control.softlayer.com/account/quotes)
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getQuotes
# http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote/getRecalculatedOrderContainer
# http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote/placeOrder
# @License: http://sldn.softlayer.com/article/License
# @Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
#

require 'rubygems'
require 'softlayer_api'
require 'pp'

# Set API user name
SL_API_USERNAME = 'set me'
# Set API key
SL_API_KEY = 'set me'

# Create a client instance
client = SoftLayer::Client.new(username: SL_API_USERNAME, api_key: SL_API_KEY)

# Set the quote id
quote_id = 124_280_2
# Get the order data by using SoftLayer_Billing_Order_Quote::getRecalculatedOrderContainer method
order_templates = client['SoftLayer_Billing_Order_Quote'].object_with_id(quote_id).getRecalculatedOrderContainer

# For this example we are retrieving the data from a quote which
# contains configuration to order a single virtual server.

order = order_templates['orderContainers'][0]
# Set template information for the new order.
# First, declare the template as a
# SoftLayer_Container_Product_Order_Virtual_Server type, so the API knows
# you're trying to place an order for a virtual guest.
order['complexType'] = 'SoftLayer_Container_Product_Order_Virtual_Guest'
# We want to order one CCI.
order['quantity'] = 1

# Set the hostname and domain for our new CCI. If ordering more
# than one CCI then define another hostname/domain pair accordingly.
order['virtualGuests'] = [{ 'hostname' => 'server01', 'domain' => 'example.com' }]

begin
  # Verify the order container is right. If this returns an error
  # then fix your order container and re-submit. Once ready then place
  # your order with the placeOrder() method.
  receipt = client['SoftLayer_Billing_Order_Quote'].object_with_id(quote_id).verifyOrder(order)
  pp(receipt)
rescue => error_reason
  puts "The order could not be verified  #{error_reason}"
end

```
