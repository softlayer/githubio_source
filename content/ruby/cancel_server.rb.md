---
title: "cancel_server.rb"
description: "cancel_server.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Item_Hardware"
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
# Cancel servers from a list of IPs
#
# This script looks for a server with a determinate IP address and delete it.
#
# It makes a single call to the cancelItem() method in the
# SoftLayer_Billing_Item API service
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Item_Hardware
# http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelItem
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc.<sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The list of IPs from the servers you wish cancel
ips_to_cancel = ['1.1.1.1', '2.2.2.2']

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)

# Declare a new API service objects for:
# SoftLayer_Account
# SoftLayer_Billing_Item
account_client = client.service_named('SoftLayer_Account')
billing_item_client = client.service_named('SoftLayer_Billing_Item')

# Add an object mask to retrieve our billing items related to the servers
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# for a list of the relational properties you can retrieve along with hardware.
object_mask = 'mask[billingItem]'

begin
  # Make the call to retrieve our hardware records along with their billing item.
  servers = account_client.object_mask(object_mask).getHardware
rescue StandardError => exception
  puts "Unable to retrieve the list of servers: #{exception}"
end

# We are looking for the server which has the desired IP to delete it.
begin
  ips_to_cancel.each do |ip_to_cancel|
    servers.each do |server|
      if server.key?('primaryIpAddress')
        if (server['primaryIpAddress'] == ip_to_cancel)
          if server.key?('billingItem')
            billing_id = server['billingItem']['id']
            result = billing_item_client.object_with_id(billing_id).cancelItem(false,false,"No longer needed","Api test")
            pp result
          end
        end
      end
    end
  end
rescue StandardError => exception
  puts "Unable to cancel the server: #{exception}"
end

```
