---
title: "Migrating a VSI from SAN to Local Storage and vice-versa"
description: "Example on how to call verifyOrder / placeOrder via REST to migrate a Virtual_Guest from SAN to Local storage and vice-versa."
date: "2016-11-07"
classes: ["SoftLayer_Product_Order"]
tags:
    - "placeOrder"
    - "verifyOrder"
    - "upgrade"
---

You can use the following [ruby example](https://softlayer.github.io/ruby/list_packages/) to get a list of all the available priceId's for the Virtual_Guest package. You need to change the second to last line from main.getPackage(126) to main.getPackage(46). The priceId you need will depend on if you are moving to or from Local Storage and the size of the current primary drive.


```ruby

require 'softlayer_api'
require 'pp'

softlayer_client = SoftLayer::Client.new(:timeout => 120)
client = softlayer_client.service_named('Product_Order')

# The package for Virtual Guests
packageId = 46

# The price item id for a 25GB Local Primary Drive.
prices = [
{
  'id' => 13899,
    'categories' => [
       {
           'categoryCode' => 'guest_disk0',
           'id' => 81,
           'name' => 'First Disk'
       }
   ]
  }
]

# Maintenance Window time. The migration requires downtime
properties = [
  {
      'name' => 'MAINTENANCE_WINDOW',
      'value' => 'now'
  }
]

productOrder = {
  'complexType' => 'SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade',
  'packageId' => packageId,
  'prices' => prices,
  'properties' => properties,
  'virtualGuests' => [ {'id' => '25367125'} ]
}

begin
 # verifyOrder() will check your order for errors. Replace this with a call to
 # placeOrder() when you're ready to order. Both calls return a receipt object
 # that you can use for your records.
 #
 # Once your order is placed it'll go through SoftLayer's provisioning process.

 receipt = client.verifyOrder(productOrder)
 puts receipt
rescue Exception => exception
 puts "There is an error in the order: #{exception}"
end
```
