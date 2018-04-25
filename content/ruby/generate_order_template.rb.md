---
title: "generate_order_template.rb"
description: "generate_order_template.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Product_Order"
tags:
    - "virtualservers"
---


```
# Generates an order template.
#
# Obtain an order container that can be sent to verifyOrder or placeOrder.
# This is primarily useful when there is a necessity to confirm the price which will be charged for an order.
# See createObject for specifics on the requirements of the template object parameter.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'
require 'awesome_print'

virtual_guest = {
    hostname: 'host1',
    domain: 'example.com',
    startCpus: 1,
    maxMemory: 1024,
    datacenter: {
        name: 'dal05'
    },
    hourlyBillingFlag: true,
    localDiskFlag: true,
    operatingSystemReferenceCode: 'UBUNTU_LATEST'
}

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME,
                               api_key: SL_API_KEY)

virtual_guest_service = client['SoftLayer_Virtual_Guest']

begin

  order_template = virtual_guest_service.generateOrderTemplate(virtual_guest)
  ap order_template
rescue StandardError => e
  p 'Error when executing the script...'
  $stdout.print(e.inspect)
end



```
