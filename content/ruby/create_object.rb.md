---
title: "create_object.rb"
description: "create_object.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualservers"
---


```
# Create a virtual guest object.
#
# createObject() enables the creation of computing instances on an account. This
# method is a simplified alternative to interacting with the ordering system directly.
# In order to create a computing instance, a template object must be sent in with a few required values.
# When this method returns an order will have been placed for a computing instance of the specified configuration.
# To determine when the instance is available you can poll the instance via getObject, with an object mask requesting
# the provisionDate relational property. When provisionDate is not null, the instance will be ready.
# Warning: Computing instances created via this method will incur charges on your account. For testing input parameters
# see generateOrderTemplate.
# Input - SoftLayer_Virtual_Guest
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'
require 'awesome_print'

virtual_guest = {
        hostname: 'vs574DC',
        domain: 'softlayer.local',
        startCpus: 1,
        maxMemory: 1024,
        datacenter: {
            name: 'dal05'
        },
        hourlyBillingFlag: true,
        localDiskFlag: true,
        operatingSystemReferenceCode: 'UBUNTU_LATEST'
}

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME,
                               api_key: SL_API_KEY)

virtual_guest_service = client['SoftLayer_Virtual_Guest']

begin
  virtual_guest = virtual_guest_service.createObject(virtual_guest)
  ap virtual_guest
rescue StandardError => e
  p 'Error when executing the script...'
  $stdout.print(e.inspect)
end


```
