---
title: "get_dedicated_host_to_migrate.rb"
description: "get_dedicated_host_to_migrate.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
    - "SoftLayer_Virtual_DedicatedHost"
tags:
    - "dedicatedhosts"
---


```
# Get valid dedicated host for migration.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getDedicatedHosts
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_DedicatedHost
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getDedicatedHost
# http://sldn.softlayer.com/article/object-masks
# http://sldn.softlayer.com/article/object-filters
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'softlayer_api'
require 'json'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Id of virtual guest you want to migrate
virtual_guest_id = 37117661

# Create a SoftLayer API client object
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
account_service = client['SoftLayer_Account']
virtual_guest_service = client['SoftLayer_Virtual_Guest']

# Object-mask to know backend router of current dedicated host associated to virtual guest
mask = 'mask[backendRouter]'

begin
  # Get associated dedicated host from virtual guest
  dedicated_host = virtual_guest_service.object_with_id(virtual_guest_id).object_mask(mask).getDedicatedHost

  filter = SoftLayer::ObjectFilter.new do |filter|
    filter.set_criteria_for_key_path(
        'dedicatedHosts.backendRouter',
        :id => { :operation => dedicated_host['backendRouter']['id']}
    )
  end

  # Retrieve all dedicated host with same backend router.
  hosts_to_migrate = account_service.object_filter(filter).getDedicatedHosts

  hosts_to_migrate.each do |host|
    puts JSON.generate(host)
  end

rescue StandardError => exception
  puts "Unable to get the dedicated hosts: #{exception}"
end

```
