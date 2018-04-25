---
title: "edit_record.rb"
description: "edit_record.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain_ResourceRecord"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns_domain_resource_record"
---


```
# Edit Resource Records.
# This script edits an existing domain resource record.
#
# Important manual pages:
# see http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/editObject
#
# license <http://sldn.softlayer.com/article/License>
# author SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'

# Set a Resource Record Id
# To get Resource Record information: http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getResourceRecords
resource_id = 56876637

# Your SoftLayer API username.
SL_API_USERNAME = 'set me'

# Your SoftLayer API key.
SL_API_KEY = 'set me'

softlayer_client = SoftLayer::Client.new(username: SL_API_USERNAME,
                                         api_key: SL_API_KEY)

dns_domain_ResourceRecord_service = softlayer_client.service_named('Dns_Domain_ResourceRecord')
domain_ref = dns_domain_ResourceRecord_service.object_with_id(resource_id)

# Create an object template with new configuration for Resource Record.
# TTL values:
#          900 (15 Min)
#          3600 (1 Hour)
#          86400 (1 Day)
#          604800 (1 Week)

object_template = {
	data: '127.4.0.1',
	host: '@',
	ttl: 900
}


begin
  result = domain_ref.editObject(object_template)
  puts 'The resource record was edited successfully'
  puts result.inspect

rescue StandardError => e
  puts 'Error when executing the script...'

  $stdout.print(e.inspect)
end

```
