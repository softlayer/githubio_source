---
title: "get_object.rb"
description: "get_object.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualservers"
---


```
# Retrieve a virtual guest object.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getObject
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
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
  virtual_guest = virtual_guest_service.object_with_id(virtual_guest_id)
                                       .getObject
  ap virtual_guest
rescue StandardError => e
  p 'Error when executing the script...'
  $stdout.print(e.inspect)
end

```
