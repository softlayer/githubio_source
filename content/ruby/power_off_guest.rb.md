---
title: "power_off_guest.rb"
description: "power_off_guest.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
tags:
    - "virtualservers"
---


```
# Power off a VSI.
#
# Important manual pages:
# https://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
# https://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/powerOffSoft
# https://sldn.softlayer.com/reference/services/SoftLayer_Account
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY, timeout: 180)

# The VSI data
hostname = 'test' # Set this with the hostname of the machine you want
domain = 'softlayer.local' # Set this with the domain of the machine you want

account_service = client.service_named('SoftLayer_Account')
virtual_guest_service = client.service_named('SoftLayer_Virtual_Guest')

# Adding a filter to filter the VSI we want.
object_filter = SoftLayer::ObjectFilter.new do |filter|
  filter.accept('virtualGuests.hostname').when_it is(hostname)
  filter.accept('virtualGuests.domain').when_it is(domain)
end

begin
  # It will return only the virtual machine which have the specified hostname and domain
  virtual_guest = account_service.object_filter(object_filter).getVirtualGuests
  result = virtual_guest_service.object_with_id(virtual_guest[0]['id']).powerOffSoft
  pp result
rescue StandardError => exception
  puts "Unable to power off the VSI: #{exception}"
end

```
