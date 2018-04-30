---
title: "list_dedicated_host.rb"
description: "list_dedicated_host.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Virtual_DedicatedHost"
tags:
    - "dedicatedhosts"
---


```
# List the dedicated hosts in the account.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getDedicatedHosts
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_DedicatedHost
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'softlayer_api'
require 'json'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Create a SoftLayer API client object
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
service = client['SoftLayer_Account']

begin
  # getDedicatedHosts() will get all the Virtual Dedicated Hosts in the account.
  dedicated_hosts = service.getDedicatedHosts

  dedicated_hosts.each do |host|
    puts JSON.generate(host)
  end

rescue StandardError => exception
  puts "Unable to get dedicated hosts: #{exception}"
end

```
