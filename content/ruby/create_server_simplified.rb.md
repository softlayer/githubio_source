---
title: "create_server_simplified.rb"
description: "create_server_simplified.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware"
tags:
    - "baremetalservers"
---


```
# Create Bare Metal server simplified way.
#
# The script creates a Bare Metal using the simplified way
# it makes a single call to the SoftLayer_Hardware::createObject method.
# For more information see below
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware/createObject/
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware/getCreateObjectOptions/
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware/generateOrderTemplate/
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc.<sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# To get the configuration options to create the server
# call the SoftLayer_Hardware::getCreateObjectOptions method.
# e.g.
# createOptions = hardwareServerService.getCreateObjectOptions()
# print (createOptions)
# Creating our server template with the configuration options that we want.
hardware_object = {
  'hostname' => 'host1',  # The name of the server
  'domain' => 'example.com', # The domain for the server
  'processorCoreAmount' => 2, # The number of logical CPU cores to allocate
  'memoryCapacity' => 2, # The amount of memory to allocate in gigabytes.
  'hourlyBillingFlag' => true, # Specifies the billing type for the server.
  'operatingSystemReferenceCode' => 'UBUNTU_LATEST', # An identifier for the operating system to provision the server with.
  'datacenter' => { # Specifies which datacenter the server is to be provisioned in.
    'name' => 'dal05'
  }
}

# Declare the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
hardware_server_service = client['SoftLayer_Hardware']

begin
  # To test the input parameters call the SoftLayer_Hardware::generateOrderTemplate method
  # when you are ready to create the server call the SoftLayer_Hardware::createObject method.
  receipt = hardware_server_service.generateOrderTemplate(hardware_object)
  print receipt
rescue StandardError => exception
  puts "There was an error in your order: #{exception}"
end

```
