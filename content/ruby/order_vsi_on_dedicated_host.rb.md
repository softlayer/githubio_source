---
title: "order_vsi_on_dedicated_host.rb"
description: "order_vsi_on_dedicated_host.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Virtual_Guest"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "dedicatedhosts"
---


```
# Order Virtual Guest on Dedicated Host.
#
# This script shows how to order a vsi on an customer's dedicated host.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'softlayer_api'
require 'json'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Declare the hostId, packageId and quantity for the virtual guest you wish to order.
host_id = 9301
package_id = 46
quantity = 1

# Skeleton of SoftLayer_Virtual_Guest object to model the hostname,
# domain and the router that we want for our dedicated host.
virtualGuests = [
    {
        :domain => 'softlayer.com',
        :hostname => 'vsi-dedicated',
        :primaryBackendNetworkComponent => {
            :networkVlan => {
                :id => 1404269,
                :primarySubnet => 1314283
            }
        },
        :primaryNetworkComponent => {
            :networkVlan => {
                :id => 1404267,
                :primarySubnet => 1319803
            }
        }
    }
]

# Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
# prices for the package use the SoftLayer_Product_Package:getItemPrices method.
prices = [
    { :id => 200313 },        # 4 x 2.0 GHz Cores (Dedicated Host)
    { :id => 200397 },        # 100 GB (Local Disk - Dedicated Host)
    { :id => 45456 },         # CentOS 7.x - LAMP Install (64 bit)
    { :id => 200365 },        # 32 GB (RAM - Dedicated Host)
    { :id => 1800 },          # 0 GB Bandwidth
    { :id => 55 },            # Host Ping
    { :id => 57 },            # Email and Ticket
    { :id => 273 },           # 100 Mbps Public & Private Network Uplinks
    { :id => 21 },            # 1 IP Address
    { :id => 905 },           # Reboot / Remote Console
    { :id => 58 },            # Automated Notification
    { :id => 420 },           # Unlimited SSL VPN Users & 1 PPTP VPN User per account
    { :id => 418 }            # Nessus Vulnerability Assessment & Reporting
]

# Build the skeleton of SoftLayer_Container_Product_Order object
# containing the order you wish to place.
template_order = {
    :orderContainers => [
        :complexType => 'SoftLayer_Container_Product_Order_Virtual_Guest',
        :hostId => host_id,
        :packageId => package_id,
        :virtualGuests => virtualGuests,
        :prices => prices,
        :quantity => quantity
    ]
}

# Create a SoftLayer API client object
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
service = client['SoftLayer_Product_Order']

begin
  # Use verifyOrder() method to check for errors. Replace this with placeOrder() when
  # you are ready to order.
  receipt = service.verifyOrder template_order

  puts JSON.pretty_generate(receipt)

rescue StandardError => exception
  puts "Unable to place order: #{exception}"
end
```
