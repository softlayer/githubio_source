---
title: "get_order_template.rb"
description: "get_order_template.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Item_Price"
tags:
    - "virtualservers"
---


```
# Retrieve an order container.
#
# Obtain an order container that is ready to be sent to the
# SoftLayer_Product_Order#placeOrder|SoftLayer_Product_Order::placeOrder method.
# This container will include all services that the selected computing instance has.
# If desired you may remove prices which were returned.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getOrderTemplate
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'
require 'awesome_print'

virtual_guest_id = 6032256
# either MONTHLY or HOURLY
billing_type = 'MONTHLY'
# This is a list of prices that could replace options that are normally selected by matching
# the items to the existing virtual server.
product_item_price = [
    { id: 50367 },
    { id: 1640  },
    { id: 2202  },
    { id: 2302  },
    { id: 55    },
    { id: 57    },
    { id: 13947 },
    { id: 273   },
    { id: 21    },
    { id: 1644  },
    { id: 905   },
    { id: 58    },
    { id: 420   },
    { id: 418   }
]

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME,
                               api_key: SL_API_KEY)

virtual_guest_service = client['SoftLayer_Virtual_Guest']

begin
  container_product_order = virtual_guest_service.object_with_id(virtual_guest_id)
                                                 .getOrderTemplate(billing_type, product_item_price)
  ap container_product_order
rescue StandardError => e
  p 'Error when executing the script...'
  $stdout.print(e.inspect)
end


```
