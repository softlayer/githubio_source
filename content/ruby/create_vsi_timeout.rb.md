---
title: "create_vsi_timeout.rb"
description: "create_vsi_timeout.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Order"
tags:
    - "virtualservers"
---


```
# Create a VSI with a timeout to wait the transaction.
#
# Important manual pages:
# https://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
# https://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
# https://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate
# https://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY, timeout: 500)
virtual_guest_service = client['SoftLayer_Virtual_Guest']
product_order = client['SoftLayer_Product_Order']

template = {
  'hostname' => 'host1',
  'domain' => 'mydomain.com',
  'datacenter' => {
    'name' => 'wdc01'
  },
  'startCpus' => 1,
  'maxMemory' => 1,
  'localDiskFlag' => false,
  'hourlyBillingFlag' => true,
  'operatingSystemReferenceCode' => 'UBUNTU_LATEST',
  'privateNetworkOnlyFlag' => true,
  'primaryBackendNetworkComponent' => {
    'networkVlan' => {
      'id' => 123_45
    }
  },
  'networkComponent' => {
    'max_speed' => 10
  }
}

begin
  puts 'Verifying: ' + template
  order = virtual_guest_service.generateOrderTemplate(template)
  product_order.verifyOrder(order)
  puts 'The server order verified successfully'
rescue Interrupt
  puts '\nExiting..'
  exit
rescue StandardError => e
  puts "ERROR: Order of Virtual Server failed with Exception -- #{e}"
  puts e.backtrace.join("\n")
  exit 1
end

```
