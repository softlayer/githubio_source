---
title: "get_power_state.rb"
description: "get_power_state.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Virtual_Guest_Power_State"
tags:
    - "virtualservers"
---


```
# Retrieve the current power state of a virtual guest.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getPowerState
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Power_State
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
  virtual_guest_power_state = virtual_guest_service.object_with_id(virtual_guest_id)
                                                   .getPowerState
  ap virtual_guest_power_state
rescue StandardError => e
  p 'Error when executing the script...'
  $stdout.print(e.inspect)
end


```
