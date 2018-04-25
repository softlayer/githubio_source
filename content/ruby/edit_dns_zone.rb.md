---
title: "edit_dns_zone.rb"
description: "edit_dns_zone.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain_ResourceRecord"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns_domain"
---


```
# Edit a DNS Zone.
# This script edits an existing domain resource record.
#
# Important manual pages:
# see http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getResourceRecords
#      http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/editObject
#
# license <http://sldn.softlayer.com/article/License>
# author SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'

# Set the domain id that you want to edit.
dns_id = 1559414

responsible_person = 'root.mcruzeditedd07.com'

# TTL values:
#          900 (15 Min)
#          3600 (1 Hour)
#          86400 (1 Day)
#          604800 (1 Week)
ttl = 900

# Your SoftLayer API username.
SL_API_USERNAME = 'set me'

# Your SoftLayer API key.
SL_API_KEY = 'set me'

softlayer_client = SoftLayer::Client.new(username: SL_API_USERNAME,
                                         api_key: SL_API_KEY)

dns_domain_service = softlayer_client.service_named('Dns_Domain')

# Create a filter to get "SOA" information which is associated to the Domain
# Note: Just some data is available to be edited and they are associated to "SOA"
filter_instance = SoftLayer::ObjectFilter.new
filter_instance.set_criteria_for_key_path('resourceRecords.type', operation: 'soa')

begin
  resource_records = dns_domain_service.object_with_id(dns_id)
                                       .object_filter(filter_instance)
                                       .getResourceRecords                                
                                    
  puts 'Process finished successfully'
  resource_record_id = resource_records[0]['id']

  # Editing the "responsiblePerson" and "ttl".
  object_template = {
      responsiblePerson: responsible_person,
      ttl: ttl
  }

  domain_service = softlayer_client.service_named('Dns_Domain_ResourceRecord')
  edit_result = domain_service.object_with_id(resource_record_id)
                              .editObject(object_template)

  p edit_result
rescue StandardError => e
  p 'Error when executing the script...'

  $stdout.print(e.inspect)
end

```
