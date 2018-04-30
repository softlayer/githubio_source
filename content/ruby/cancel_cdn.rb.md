---
title: "cancel_cdn.rb"
description: "cancel_cdn.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Item_Cancellation_Request"
tags:
    - "cdn"
---


```
# Cancel CDN.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item_Cancellation_Request/createObject
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account/
# http://sldn.softlayer.com/article/Object-Filters
# http://sldn.softlayer.com/article/Object-Masks
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
#

require 'softlayer_api'
require 'pp'

# Your SoftLayer API key and username.
USERNAME = 'set me'
API_KEY = 'set me'

# The name of the CDN to cancel.
cdn_account_name = 'C308'
immediate_cancellation = true

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
billing_service = client['SoftLayer_Billing_Item_Cancellation_Request']
account_service = client['SoftLayer_Account']

# Set an object mask to get the billing item associated to the CDNN.
object_mask = 'mask[billingItem]'

object_filter = SoftLayer::ObjectFilter.new { |f| f.accept('cdnAccounts.cdnAccountName').when_it is(cdn_account_name) }

begin
  # Getting the CDN to delete
  cdns = account_service.object_mask(object_mask).object_filter(object_filter).getCdnAccounts
  if cdns.length == 0
    print 'The configured CDN: ' + cdn_account_name + ' does not exist in the account'
    exit
  end
  template = {
    'accountId' => cdns[0]['accountId'],
    'items' => [
      {
        'billingItemId' => cdns[0]['billingItem']['id'],
        'immediateCancellationFlag' => immediate_cancellation
      }
    ]
  }
  result = billing_service.createObject(template)
  print result
rescue StandardError => exception
  puts "Unable to create the cancel request. : #{exception}"
end

```
