---
title: "get_available_network_storages.rb"
description: "get_available_network_storages.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Network_Storage"
tags:
    - "virtualservers"
---


```
# Retrieve a list of Network Storage volumes.
#
# This method retrieves a list of SoftLayer_Network_Storage volumes that can be authorized
# to this SoftLayer_Virtual_Guest.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getAvailableNetworkStorages
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Storage
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'
require 'awesome_print'

virtual_guest_id = 6032256
# Either 'ISCSI', 'NAS', or '*' for both
nas_type = '*'

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME,
                               api_key: SL_API_KEY)

virtual_guest_service = client['SoftLayer_Virtual_Guest']

begin
  network_storage = virtual_guest_service.object_with_id(virtual_guest_id)
                                         .getAvailableNetworkStorages(nas_type)
  ap network_storage
rescue StandardError => e
  p 'Error when executing the script...'
  $stdout.print(e.inspect)
end






```
