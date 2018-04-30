---
title: "reload_operating_system.rb"
description: "reload_operating_system.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Hardware_Server_Configuration"
tags:
    - "virtualservers"
---


```
# Reloads current operating system configuration.
#
# This service has a confirmation protocol for proceeding with the reload. To proceed with the reload
# without confirmation, simply pass in 'FORCE' as the token parameter. To proceed with the reload with confirmation,
# simply call the service with no parameter. A token string will be returned by this service.
# The token will remain active for 10 minutes. Use this token as the parameter
# to confirm that a reload is to be performed for the server.
# As a precaution, we strongly recommend backing up all data before reloading the operating system.
# The reload will format the primary disk and will reconfigure the computing instance
# to the current specifications on record.
# If reloading from an image template, we recommend first getting the list
# of valid private block device template groups, by calling the getOperatingSystemReloadImages method.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/reloadOperatingSystem
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Hardware_Server_Configuration
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

  result = virtual_guest_service.object_with_id(virtual_guest_id)
                                .reloadOperatingSystem
  ap result
rescue StandardError => e
  p 'Error when executing the script...'
  $stdout.print(e.inspect)
end



```
