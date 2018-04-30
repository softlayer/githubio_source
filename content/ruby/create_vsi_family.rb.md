---
title: "create_vsi_family.rb"
description: "create_vsi_family.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Package"
tags:
    - "virtualservers"
---


```
# Create a Virtual Guest - Compute flavor.
#
# This example shows how to create a Virtual Guest device which is part of new VSI Families.
# On this case we will create a Compute VSI with the following configuration:
#          2 x 2.0 GHz Cores, 2 GB RAM, and primary disk of 25 GB (SAN).
#
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getActivePresets
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc.<sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'
require 'json'

# Your SoftLayer API username and API Key.
USERNAME = 'set me'
API_KEY = 'set me'

# Build the skeleton of SoftLayer_Virtual_Guest object.
# The method SoftLayer_Product_Package::getActivePresets list all available flavors you can use,
# check the keyName values to know which are Balanced, Compute,etc., they should start with:
#       B1   is for "Balanced"
#       BL1  is for "Balanced Local Storage"
#       BL2  is for "Balanced Local Storage - SSD"
#       C1   is for "Compute"
#       M1   is for "Memory"
# These characters are followed by a short description of VSI configuration as following:
#       C1_2X2X100    which is for Compute VSI with "2 x 2.0 GHz Cores x 2 GB x 100 GB (SAN)"
#       B1_1X2X25     which is for Balanced VSI with "8 x 2.0 GHz Cores x 8 GB x 25 GB (SAN)"
# Following configuration will use the keyName C1_2X2X25 in order to create a Compute VSI with
# 2 x 2.0 GHz Cores, 2 GB RAM, and primary disk of 25 GB (SAN)
virtual_guest = {
    hostname: 'compute-vsi',
    domain: 'softlayer.local',        
    datacenter: { name: 'dal05' },
    supplementalCreateObjectOptions: {
        flavorKeyName: "C1_2X2X25"
    },
    hourlyBillingFlag: false,        
    operatingSystemReferenceCode: 'UBUNTU_LATEST',
    blockDevices: [
        {
          "device": "2",
          "diskImage": { "capacity": 25	}
        }
		],
    networkComponents: [
        { maxSpeed: 100}
    ]
}

# Declare the API client to use the SoftLayer_Virtual_Guest API service
client = SoftLayer::Client.new(username: USERNAME,  api_key: API_KEY)
virtual_guest_service = client['SoftLayer_Virtual_Guest']

begin
  # generateOrderTemplate() will create an order container that can be used with methods
  # verifyOrder and  placeOrder. Replace this with createObject() when you're ready to order.
  virtual_guest = virtual_guest_service.generateOrderTemplate(virtual_guest)
  puts JSON.pretty_generate(virtual_guest)
rescue StandardError => exception
  puts "There was an error in your order: #{exception}"
end

```
