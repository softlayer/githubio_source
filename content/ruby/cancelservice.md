---
title: "Cancel an item or service"
description: "Use cancelService to cancel am item or service"
date: "2016-01-29"
classes: ["SoftLayer_Billing_Item"]
tags:
    - "billing"
    - "cancelService"
---

```ruby
require 'softlayer_api' # Requires softlayer_api >= 3.2
require 'pp' # used to display results

# Create a client
client = SoftLayer::Client.new

# add your servers' id, can be found with the following script: https://softlayer.github.io/ruby/list_instances/
id_of_virtual_server_to_cancel = FILL_IN_YOUR_SERVERS_ID
begin
   # Substitute :Virtual_Guest for :Hardware_Server if you want to cancel a bare metal server
   item = client[:Virtual_Guest].object_mask("mask[billingItem[id]]").object_with_id(id_of_virtual_server_to_cancel).getObject
   rescue XMLRPC::FaultException # error will be triggered if item doesn't exist
   item = false
end
#
# # Then invoke [cancelService](http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService) or [cancelItem](http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelItem)
if item and item['billingItem'] and client[:Billing_Item].object_with_id(item['billingItem']['id']).cancelService()
   puts "Cancelled service of #{id_of_virtual_server_to_cancel}"
 else
   puts "#{id_of_virtual_server_to_cancel} Doesn't exist or is already cancelled"
 end
```
