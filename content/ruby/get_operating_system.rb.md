---
title: "get_operating_system.rb"
description: "get_operating_system.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Software_Component_OperatingSystem"
tags:
    - "virtualservers"
---


```
# Retrieve the operating system of a virtual guest object.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getOperatingSystem
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Software_Component_OperatingSystem
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
  software_component_operating_system = virtual_guest_service.object_with_id(virtual_guest_id)
                                                             .getOperatingSystem
  ap software_component_operating_system
rescue StandardError => e
  p 'Error when executing the script...'
  $stdout.print(e.inspect)
end


```
