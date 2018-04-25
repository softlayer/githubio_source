---
title: "reload_current_operating_system_configuration.rb"
description: "reload_current_operating_system_configuration.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Provisioning_Version"
tags:
    - "virtualservers"
---


```
# Create a transaction to perform an OS reload
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/reloadCurrentOperatingSystemConfiguration
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction
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

  provisioning_version1_transaction = virtual_guest_service.object_with_id(virtual_guest_id)
                                                           .reloadCurrentOperatingSystemConfiguration
  ap provisioning_version1_transaction
rescue StandardError => e
  p 'Error when executing the script...'
  $stdout.print(e.inspect)
end



```
