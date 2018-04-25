---
title: "order_vsi_family.rb"
description: "order_vsi_family.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Item_Price"
tags:
    - "virtualservers"
---


```
# Order a Virtual Guest - Compute flavor.
#
# This example shows how to order a Virtual Guest device which is part of new VSI Families.
# On this case we will order Compute VSI with the following configuration:
#          2 x 2.0 GHz Cores, 2 GB RAM, and primary disk of 25 GB (SAN).
#
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getActivePresets
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc.<sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'
require 'json'

# Your SoftLayer API username and API Key.
USERNAME = 'set me'
API_KEY = 'set me'

# Location where server will be provisioned.
location = 'AMSTERDAM03'

# The id of the SoftLayer_Product_Package, use the 835 for VSI Families.
package_id = 835

# To specify the configuration you must to use the presetId parameter, so in order to get the
# list of available preset ids use the method SoftLayer_Product_Package::getActivePresets.
# Check the keyName values to know which are Balanced, Memory, etc., they should start with:
#       B1   is for "Balanced"
#       BL1  is for "Balanced Local Storage"
#       BL2  is for "Balanced Local Storage - SSD"
#       C1   is for "Compute"
#       M1   is for "Memory"
# These characters are followed by a short description of VSI configuration as following:
#       C1_2X2X100    which is for Compute VSI with "2 x 2.0 GHz Cores x 2 GB x 100 GB (SAN)"
#       B1_1X2X25     which is for Balanced VSI with "8 x 2.0 GHz Cores x 8 GB x 25 GB (SAN)"
# Following is the preset id used to complete this example. 
preset_id = 295   # C1_2X2X25  (2 x 2.0 GHz Cores, 2 GB RAM, and primary disk of 25 GB)

# The number of servers you wish to order in this configuration.
quantity = 1

# Build a skeleton SoftLayer_Virtual_Guest object. If you set quantity greater than 1 then you
# need to define one hostname/domain per server you wish to order.
virtual_guest = [
    {
        'hostname' => 'compute-vsi', 
        'domain' => 'softlayer.local'
    }
]

# Build a skeleton SoftLayer_Product_Item_Price objects. Note that you don't need to specify
# the item price for cpus, ram, and primary disk, and take into account that “Balanced Local Storage”
# and “Balanced Local Storage - SSD” requires a second disk, the system will select one if you
# don’t specify it. 
prices = [
    { 'id' => 45456 },  # CentOS 7.x - LAMP Install (64 bit)
    { 'id' => 2255 },   # 10 GB (SAN) - As second Disk
    { 'id' => 50367 },  # 250 GB Bandwidth
    { 'id' => 273 },    # 100 Mbps Public & Private Network Uplinks
    { 'id' => 55 },     # Host Ping
    { 'id' => 58 },     # Automated Notification
    { 'id' => 420 },    # Unlimited SSL VPN Users & 1 PPTP VPN User per account
    { 'id' => 418 },    # Nessus Vulnerability Assessment & Reporting    
    { 'id' => 21 },     # 1 IP Address
    { 'id' => 57 },     # Email and Ticket
    { 'id' => 905 },    # Reboot and Remote Console
]

# Build a skeleton SoftLayer_Container_Product_Order object containing the order
# you wish to place.
order_template = {
    'quantity' => quantity,
    'location' => location,
    'packageId' => package_id,
    'presetId' => preset_id,
    'prices' => prices,
    'virtual_guest' => virtual_guest
}

# Declare the API client to use the SoftLayer_Product_Order API service
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
product_order_service = client.service_named('SoftLayer_Product_Order')

begin
  # verifyOrder() will check your order for errors. Replace this with placeOrder()
  # when you're ready to order. 
  receipt = product_order_service.verifyOrder(order_template)
  puts JSON.pretty_generate(receipt)
rescue StandardError => exception
  puts "There was an error in your order: #{exception}"
end

```
