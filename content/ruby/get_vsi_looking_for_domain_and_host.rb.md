---
title: "get_vsi_looking_for_domain_and_host.rb"
description: "get_vsi_looking_for_domain_and_host.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "virtualservers"
---


```
# Get a VSI looking for Hostname and Domain
#
# Important manual pages:
# https://sldn.softlayer.com/reference/services/SoftLayer_Account
# https://sldn.softlayer.com/reference/datatypes/SoftLayer_Account/getVirtualGuests
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
#
require 'softlayer_api'
require 'pp'

USERNAME = 'set me'
API_KEY = 'set me'

# The virtual machine data
# Set this with the hostname of the machine you want
hostname = 'ProvisionApiTest'
# Set this with the domain of the machine you want
domain = 'mydomain.com'

# Creating a filter to get the specific VSI we are seeking.
object_filter = SoftLayer::ObjectFilter.new do |filter|
  filter.accept('virtualGuests.hostname').when_it is(hostname)
  filter.accept('virtualGuests.domain').when_it is(domain)
end

account_service = SoftLayer::Service.new('SoftLayer_Account', username: USERNAME, api_key: API_KEY)

begin
  # It will return only the virtual machine which have the specified hostname and domain
  virtual_guest = account_service.object_filter(object_filter).getVirtualGuests
  pp virtual_guest[0]['id']
rescue StandardError => exception
  puts "Unable to  get the VSI: #{exception}"
end

```
