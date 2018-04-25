---
title: "delete_record.rb"
description: "delete_record.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain_ResourceRecord"
tags:
    - "dns_domain_resource_record"
---


```
# Delete Resource Record.
# This script deletes a domain's resource record.
#
# Important manual pages:
# see http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/deleteObject
#
# license <http://sldn.softlayer.com/article/License>
# author SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'

# Set the id of item to delete
record_id = 58935105

# Your SoftLayer API username.
SL_API_USERNAME = 'set me'

# Your SoftLayer API key.
SL_API_KEY = 'set me'

# Create a client to the API service
softlayer_client = SoftLayer::Client.new(username: SL_API_USERNAME,
                                         api_key: SL_API_KEY)

resource_record_service = softlayer_client.service_named('Dns_Domain_ResourceRecord')
record_ref = resource_record_service.object_with_id(record_id)

begin
	result = record_ref.deleteObject
	puts 'The resource record was deleted successfully'
	p result
rescue StandardError => e
	puts "Error when executing the script...  #{e}"
end

```
