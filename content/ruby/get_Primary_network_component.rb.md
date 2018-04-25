---
title: "get_Primary_network_component.rb"
description: "get_Primary_network_component.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Virtual_Guest_Network_Component"
tags:
    - "virtualservers"
---


```
# Retrieve a guest's primary public network component.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getPrimaryNetworkComponent
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component
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
  virtual_guest_network_component = virtual_guest_service.object_with_id(virtual_guest_id)
                                                         .getPrimaryNetworkComponent
  ap virtual_guest_network_component
rescue StandardError => e
  p 'Error when executing the script...'
  $stdout.print(e.inspect)
end


```
