---
title: "dns_zone_details.rb"
description: "dns_zone_details.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain"
tags:
    - "dns_domain"
---


```
# DNS Zone Details.
# It retrieves the SoftLayer_Dns_Domain object whose ID number corresponds to
# the ID number of the init parameter passed to the SoftLayer_Dns_Domain service.
#
# Important manual pages:
# see http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getObject
#
# license <http://sldn.softlayer.com/article/License>
# author SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'

# Set the domain id that you want to get details.
dns_id = 1846857

# Your SoftLayer API username.
SL_API_USERNAME = 'set me'

# Your SoftLayer API key.
SL_API_KEY = 'set me'

softlayer_client = SoftLayer::Client.new(username: SL_API_USERNAME,
                                         api_key: SL_API_KEY)

domain_service = softlayer_client.service_named('Dns_Domain')
domain_ref = domain_service.object_with_id(dns_id)

# You can use getObject method to get details too (but there is less information than getResourceRecords)
# result = domain_ref.getObject

# Create a mask to get specific data
mask_string = 'mask[id,name,resourceRecords]'

begin
  result = domain_ref.object_mask(mask_string).getObject
  puts 'The DNS Zone details display successfully'
  puts result.inspect

rescue StandardError => e
  puts 'Error when executing the script...'

  $stdout.print(e.inspect)
end

```
