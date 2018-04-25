---
title: "find_by_ip_address.rb"
description: "find_by_ip_address.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualservers"
---


```
# Retrieve a virtual guest object.
#
# Find CCI by only its primary public or private IP address. IP addresses within secondary subnets tied to the CCI
# will not return the CCI. If no CCI is found, no errors are generated and no data is returned.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'
require 'awesome_print'

ip_address = '184.173.20.162'

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME,
                               api_key: SL_API_KEY)

virtual_guest_service = client['SoftLayer_Virtual_Guest']

begin
  virtual_guest = virtual_guest_service.findByIpAddress(ip_address)
  ap virtual_guest
rescue StandardError => e
  p 'Error when executing the script...'
  $stdout.print(e.inspect)
end


```
