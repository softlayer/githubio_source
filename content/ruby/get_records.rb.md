---
title: "get_records.rb"
description: "get_records.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns_domain_resource_record"
---


```
# Get Resource Records.
# This script retrieves the individual records contained within a domain record.
#
# Important manual pages:
# see http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getResourceRecords
#
# license <http://sldn.softlayer.com/article/License>
# author SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'

# Set the domain id to get the associated records
# To get Domain information: http://sldn.softlayer.com/reference/services/SoftLayer_Account/getDomains
domain_id = 1801053

# Your SoftLayer API username.
SL_API_USERNAME = 'set me'

# Your SoftLayer API key.
SL_API_KEY = 'set me'

softlayer_client = SoftLayer::Client.new(username: SL_API_USERNAME,
                                         api_key: SL_API_KEY)

dns_domain__service = softlayer_client.service_named('SoftLayer_Dns_Domain')
domain_ref = dns_domain__service.object_with_id(domain_id)

begin
  # Display the Resource Records list
  result = domain_ref.getResourceRecords
  p 'The resource records are displayed successfully'
  p result
rescue StandardError => e
  p "Error when executing the script...  #{e}"
end

```
