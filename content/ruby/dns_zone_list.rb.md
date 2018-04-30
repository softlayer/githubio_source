---
title: "dns_zone_list.rb"
description: "dns_zone_list.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "dns_domain"
---


```
# List Zones.
# It retrieves the DNS domains associated with an account.
#
# Important manual pages:
# see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getDomains
#
# license <http://sldn.softlayer.com/article/License>
# author SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'

# Your SoftLayer API username.
SL_API_USERNAME = 'set me'

# Your SoftLayer API key.
SL_API_KEY = 'set me'

softlayer_client = SoftLayer::Client.new(username: SL_API_USERNAME,
                                         api_key: SL_API_KEY)

server = SoftLayer::Account.account_for_client(softlayer_client)

begin
  # Display the DNS Zone list
  result = server.service.getDomains
  puts 'Process finished successfully'
  p result
rescue StandardError => e
  puts 'Error when executing the script...  #{e}'
end

```
