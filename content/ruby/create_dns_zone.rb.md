---
title: "create_dns_zone.rb"
description: "create_dns_zone.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain"
tags:
    - "dns_domain"
---


```
# Create a DNS Zone.
# It creates a new domain (zone) on the SoftLayer name servers.
#
# Important manual pages:
# see http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/createObject
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

dns_domain_service = softlayer_client.service_named('Dns_Domain')

# Creating a template to configure our new DNS Zone.
object_template = {
  name: 'mydomain.com',
  resourceRecords: [
    {
      data: '127.0.0.1',
      host: '@',
      type:  'a'
    }
  ]
}

begin
  result = dns_domain_service.createObject(object_template)
  puts 'Process finished successfully'
  puts result.inspect

rescue StandardError => e
  puts 'Error when executing the script...'

  $stdout.print(e.inspect)
end

```
