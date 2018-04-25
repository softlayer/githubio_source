---
title: "order_vsi_simplified_form.rb"
description: "order_vsi_simplified_form.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Product_Order"
tags:
    - "dedicatedhosts"
---


```
# Order a virtual server in a dedicated host.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate
# http://developer.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions
#
#License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'softlayer_api'
require 'json'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Build the skeleton of SoftLayer_Container_Product_Order object
# containing the order you wish to place.
template_order = {
    :hostname => 'vsi-dedicated',
    :domain => 'softlayer.com',
    :dedicatedHost => {
        :id => 9301
    },
    :datacenter => {
        :name => 'mex01'
    },
    :blockDevices => [
        {
            :device => '0',
            :diskImage => { :capacity => 25 }
        }
    ],
    :localDiskFlag => true,
    :startCpus => 8,
    :maxMemory => 8192,
    :operatingSystemReferenceCode => 'UBUNTU_LATEST'
}

# Create a SoftLayer API client object
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
service = client['SoftLayer_Virtual_Guest']

begin
  # Use generateOrderTemplate() method to create a order template that can be used with verifyOrder()
  # or placeOrder() methods. Replace generateOrderTemplate() with createObject() when you are ready
  # to create the virtual guest.
  receipt = service.generateOrderTemplate template_order

  puts JSON.pretty_generate(receipt)

rescue StandardError => exception
  puts "Unable to place order: #{exception}"
end
```
