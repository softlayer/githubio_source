---
title: "get_billing_item.rb"
description: "get_billing_item.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Billing_Item_Virtual_Guest"
tags:
    - "virtualservers"
---


```
# Retrieve the billing item for a CloudLayer Compute Instance.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getBillingItem
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Item_Virtual_Guest
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'
require 'awesome_print'

virtual_guest_id = 6032256

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME,
                               api_key: SL_API_KEY)

virtual_guest_service = client['SoftLayer_Virtual_Guest']

begin
  billing_item_virtual_guest = virtual_guest_service.object_with_id(virtual_guest_id)
                                                    .getBillingItem
  ap billing_item_virtual_guest
rescue StandardError => e
  p 'Error when executing the script...'
  $stdout.print(e.inspect)
end






```
