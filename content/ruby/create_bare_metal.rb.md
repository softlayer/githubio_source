---
title: "create_bare_metal.rb"
description: "create_bare_metal.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Container_Product_Order_Hardware_Server"
    - "SoftLayer_Product_Order"
tags:
    - "baremetalservers"
---


```
# Order a Bare Metal Server.
#
# Build a SoftLayer_Container_Product_Order object for a new
# server order and pass it to the SoftLayer_Product_Order API service to order
# it. In this care we'll order a Xeon 3460 server with 2G RAM, 100mbit NICs,
# 2000GB bandwidth, a 500G SATA drive, CentOS 5 32-bit, and default server
# order options. See below for more details.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc.<sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'
require 'json'

# Your SoftLayer API username.
USERNAME = 'set me'

# Your SoftLayer API key.
API_KEY = 'set me'

# The number of servers you wish to order in this configuration.
quantity = 1

# Where you'd like your new server provisioned.
# This can either be the id of the datacenter you wish your new server to be
# provisioned in or the string 'FIRST_AVAILABLE' if you have no preference
# where your server is provisioned.
# Location id 3     = Dallas
# Location id 18171 = Seattle
# Location id 37473 = Washington, D.C.
location = 'AMSTERDAM'

# The id of the SoftLayer_Product_Package you wish to order.
# In this case the Intel Xeon 3460's package id is 145.
package_id = 146

# Build a skeleton SoftLayer_Hardware_Server object to model the hostname and
# domain we want for our server. If you set quantity greater then 1 then you
# need to define one hostname/domain pair per server you wish to order.
hardware = [
  {
    'hostname' => 'test', # The hostname of the server you wish to order.
    'domain' => 'example.org' # The domain name of the server you wish to order.
  }
]

# Build a skeleton SoftLayer_Product_Item_Price objects. These objects contain
# much more than ids, but SoftLayer's ordering system only needs the price's id
# to know what you want to order.

# Every item in SoftLayer's product catalog is assigned an id. Use these ids
# to tell the SoftLayer API which options you want in your new server. Use
# the getActivePackages() method in the SoftLayer_Account API service to get
# a list of available item and price options per available package.
prices = [
  { 'id' => 172_32 }, # Single Processor Quad Core Xeon 1270 - 3.40GHz  (Sandy Bridge) - 1 x 8MB cache w/HT
  { 'id' => 637 }, # RAM 2 GB DDR2 667
  { 'id' => 682 }, # CentOS 5.x (32 bit)
  { 'id' => 876 }, # Disk Controller
  { 'id' => 20 }, # 500 GB SATA II
  { 'id' => 342 }, # 20000 GB Bandwidth
  { 'id' => 273 }, # 100 Mbps Public & Private Network Uplinks
  { 'id' => 55 }, # Host Ping
  { 'id' => 58 }, # Automated Notification
  { 'id' => 420 }, # Unlimited SSL VPN Users & 1 PPTP VPN User per account
  { 'id' => 418 }, # Nessus Vulnerability Assessment & Reporting
  { 'id' => 21 }, # 1 IP Address
  { 'id' => 57 }, # Email and Ticket
  { 'id' => 906 } # Reboot / KVM over IP
]

# Build a skeleton SoftLayer_Container_Product_Order_Hardware_Server object
# containing the order you wish to place.
order_template = {
  'quantity' => quantity,
  'location' => location,
  'packageId' => package_id,
  'prices' => prices,
  'hardware' => hardware
}

# Declare the API client to use the SoftLayer_Product_Order API service
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
product_order_service = client.service_named('SoftLayer_Product_Order')

# verifyOrder() will check your order for errors. Replace this with a call to
# placeOrder() when you're ready to order. Both calls return a receipt object
# that you can use for your records.
#
# Once your order is placed it'll go through SoftLayer's provisioning process.
# When it's done you'll have a new SoftLayer_Virtual_Guest object and CCI ready
# to use.

begin
  receipt = product_order_service.verifyOrder(order_template)
  puts receipt
rescue StandardError => exception
  puts "There was an error in your order: #{exception}"
end

```
