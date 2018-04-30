---
title: "list_portal_storages.rb"
description: "list_portal_storages.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "portablestorages"
---


```
# List portal storages
#
# The script lists all portable storages, it makes a single call to the
# SoftLayer_Account::getPortableStorageVolumes method.
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getPortableStorageVolumes
#
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Declaring the API client to use the SoftLayer_Account API service
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)

account_service = client.service_named('SoftLayer_Account')

object_mask = 'mask[id,name,description,capacity,units,blockDevices[id,guest[fullyQualifiedDomainName]]]'

begin
  result = account_service.object_mask(object_mask).getPortableStorageVolumes
  pp result
rescue StandardError => exception
  puts "Unable to list the portable storages.  #{exception}"
end

```
