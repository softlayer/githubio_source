---
title: "create_server_from_another.rb"
description: "create_server_from_another.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Billing_Order"
    - "SoftLayer_Container_Product_Order_Hardware_Server"
    - "SoftLayer_Product_Order"
tags:
    - "virtualservers"
---


```
# Create a server from another.
#
# The script looks for a server with a determinate IP address  ,then
# gathers the order information from that server and build a new order
#
# Important manual pages:
# https://sldn.softlayer.com/reference/services/SoftLayer_Account
# https://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
# https://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order
# https://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
# https://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

USERNAME = 'set me'
API_KEY = 'set me'
ip_address_server_to_copy = '50.97.205.198'

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)

product_order_service = client.service_named('SoftLayer_Product_Order')
account_service = client.service_named('SoftLayer_Account')
billing_order_service = client.service_named('SoftLayer_Billing_Order')

object_mask_get_order_and_package = 'mask[billingItem[package, orderItem]]'
object_mask_get_prices = 'mask[items[itemPrice]]'

begin
  # Getting the orderId
  orders_item = account_service.object_mask(object_mask_get_order_and_package).getHardware
  order_item_to_copy = 0
  package_to_copy = 0
  orders_item.each do |order_item|
    if (order_item['primaryIpAddress'] == ip_address_server_to_copy)
      order_item_to_copy = order_item['billingItem']['orderItem']['order']['id']
      package_to_copy = order_item['billingItem']['package']['id']
    end
  end

  # Getting the prices for the order
  prices_id_list = []
  prices = billing_order_service.object_mask(object_mask_get_prices).object_with_id(order_item_to_copy).getObject
  prices['items'].each do |item|
    # Build a skeleton SoftLayer_Product_Item_Price objects. These objects contain
    # much more than ids, but SoftLayer's ordering system only needs the price's id
    # to know what you want to order.
    price_id = {}
    price_id['id'] = item['itemPrice']['id']
    prices_id_list.push(price_id)
  end

  # Build a skeleton SoftLayer_Container_Product_Order_Hardware_Server object
  # containing the order you wish to place.
  order_template = {
    'packageId' => package_to_copy,
    # Where you'd like your new server provisioned.
    # This can either be the id of the datacenter you wish your new server to be
    # provisioned in or the string
    # Location id 3     = Dallas
    # Location id 18171 = Seattle
    # Location id 37473 = Washington, D.C.
    'location' => 'AMSTERDAM',
    'prices' => prices_id_list,
    'quantity' => 1, # The number of servers you wish to order in this configuration.
    # Build a skeleton SoftLayer_Hardware_Server object to model the hostname and
    # domain we want for our server. If you set quantity greater than 1 then you
    # need to define one hostname/domain pair per server you wish to order.
    'hardware' => [
      {
        'hostname' => 'newServer', # The hostname of the server you wish to order.
        'domain' => 'example.org' # The domain name of the server you wish to order.
      }
    ]
  }

  # verifyOrder() will check your order for errors. Replace this with a call to
  # placeOrder() when you're ready to order. Both calls return a receipt object
  # that you can use for your records.
  #
  # Once your order is placed it'll go through SoftLayer's provisioning process.
  # When it's done you'll have a new SoftLayer_Virtual_Guest object and CCI ready
  # to use
  receipt = product_order_service.verifyOrder(order_template)
  pp receipt
rescue StandardError => exception
  puts "Unable to create the VSI: #{exception}"
end

```
