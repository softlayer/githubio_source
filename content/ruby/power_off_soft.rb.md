---
title: "power_off_soft.rb"
description: "power_off_soft.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualservers"
---


```
# Power off a VSI.
#
# Important manual pages:
# https://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
# https://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/powerOffSoft
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY, timeout: 180)

virtual_guest_service = client.service_named('SoftLayer_Virtual_Guest')
virtual_guest_id = 614_303_8

begin
  result = virtual_guest_service.object_with_id(virtual_guest_id).powerOffSoft
  pp result
rescue StandardError => exception
  puts "Unable to power off the VSI: #{exception}"
end

```
