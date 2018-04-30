---
title: "list_instances.rb"
description: "list_instances.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "virtualservers"
---


```
# List Virtual Guests.
# It retrieves an account's associated virtual guest objects.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'rubygems'
require 'softlayer_api'

# Your SoftLayer API username.
SL_API_USERNAME = 'set me'

# Your SoftLayer API key.
SL_API_KEY = 'set me'

virtual_account = SoftLayer::Service.new('SoftLayer_Account',
                                         :username => SL_API_USERNAME,
                                         :api_key => SL_API_KEY)

begin
  # Declare an object filter to retrieve valid virtual guests.
  object_filter = SoftLayer::ObjectFilter.new
  object_filter.set_criteria_for_key_path('virtualGuests.host','operation' => 'not null')

  result = virtual_account.object_filter(object_filter).getVirtualGuests
  puts result.inspect
rescue => e
  $stdout.print(e.inspect)
end

```
