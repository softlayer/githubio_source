---
title: "set_user_data_vsi.rb"
description: "set_user_data_vsi.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualservers"
---


```
# Create VSI with metadata.
#
# Important manual pages:
# https://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
# https://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

USERNAME = 'set me'
API_KEY = 'set me'
ENDPOINT = 'set me'

client = SoftLayer::Client.new(endpoint_url: ENDPOINT, username: USERNAME, api_key: API_KEY)
virtual_guest_service = client['SoftLayer_Virtual_Guest']

template = {
  'hostname' => 'host1',
  'domain' => 'example.com',
  'startCpus' => 1,
  'maxMemory' => 1024,
  'hourlyBillingFlag' => true,
  'localDiskFlag' => true,
  'operatingSystemReferenceCode' => 'CENTOS_6_64',
  'userData' => [
    {
      'value' => 'someValue'
    }
  ],
  'datacenter' => {
    'name' => 'dal06'
  }
}

begin
  result = virtual_guest_service.createObject(template)
  puts result
rescue StandardError => exception
  puts "Unable to create the VSI: #{exception}"
end

```
