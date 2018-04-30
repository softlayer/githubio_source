---
title: "create_record.rb"
description: "create_record.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain_ResourceRecord"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns_domain"
---


```
# Create Resource Record.
# This script creates a new domain resource record.
#
# Important manual pages:
# see http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getResourceRecords
#      http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/createObject
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

resource_record_service = softlayer_client.service_named('Dns_Domain_ResourceRecord')

object_template = {
    domainId: '1801053',
    data: '127.1.1.1',
    host: '@',
    type:  'a'
}

begin
  result = resource_record_service.createObject(object_template)
  puts 'The resource record was created successfully'
  puts result.inspect

rescue StandardError => e
  puts 'Error when executing the script...'

  $stdout.print(e.inspect)
end

```
