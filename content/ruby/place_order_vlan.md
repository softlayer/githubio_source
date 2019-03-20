---
title: "Order a Vlan"
description: "Order a Network Vlan"
date: "2019-03-18"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_Vlan"
tags:
    - "vlans"
    - "order"
---

This example uses `verifyOrder` method to check the order for errors, replace it by
`placeOrder` method when you are ready to order.
```ruby
require 'softlayer_api'
require 'pp'

class Network

    def initialize(username, apikey)        
        client = SoftLayer::Client.new(username: username, api_key: apikey)
        @package_service = client["Product_Package"]
        @order_service = client["Product_Order"]
    end

    def get_package_id(keyname)
        obj_filter = SoftLayer::ObjectFilter.new do |filter|
            filter.accept("type.keyName").when_it is(keyname)
        end
    
        package = @package_service.object_filter(obj_filter).getAllObjects()
        return package[0]["id"]
    end

    def get_price_id(package_id, item_keyname)        
        obj_filter = SoftLayer::ObjectFilter.new do |filter|
            filter.accept("items.keyName").when_it is(item_keyname)
        end

        items = @package_service.object_filter(obj_filter).object_with_id(package_id).getItems()
        
        price = items[0]["prices"].detect{|p| p["locationGroupId"] == ""}
        return price["id"]
    end

    def order_vlan(package, location, item_keyname, name: nil)
        packageId = get_package_id(package)        
        priceId = get_price_id(packageId, item_keyname)

        orderData = {
            "complexType": "SoftLayer_Container_Product_Order_Network_Vlan",
            "packageId": packageId,
            "location": location,
            "prices": [{"id": priceId}],
            "quantity": 1, # for vlans each configuration quantity is restricted to 1
            "name": name
        }

        begin
            # verifyOrder will check your order for errors. Replace this with a call
            # to placeOrder() when you're ready to order.
            return @order_service.verifyOrder(orderData)
        rescue StandardError => exception
            puts "Unable to place the order : #{exception}"
        end
    end
end

# Running the example
USERNAME = 'set me'
APIKEY = 'set me'

package = "ADDITIONAL_SERVICES_NETWORK_VLAN"
location = "AMSTERDAM"

# set PRIVATE_NETWORK_VLAN if you want a private vlan
network_type = "PUBLIC_NETWORK_VLAN"
vlan_name = "A vlan Name"

# Initialize the class
network = Network.new(USERNAME, APIKEY)

# The new Vlan comes with a primary subnet which have 8 ip addresses
receipt = network.order_vlan(package, location, network_type, name: vlan_name)
pp(receipt)

```
