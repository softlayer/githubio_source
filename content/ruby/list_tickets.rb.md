---
title: "list_tickets.rb"
description: "list_tickets.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Brand"
    - "SoftLayer_Notification_Occurrence_Event"
tags:
    - "brands"
---


```
#
# List tickets.
#
# The script retrieves all the tickets in a brand account.
# It displays the same result like in https://agent.softlayer.com/support/ticket/list
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Notification_Occurrence_Event/getAllObjects
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Notification_Occurrence_Event
# http://sldn.softlayer.com/article/Object-Filters
# http://sldn.softlayer.com/article/Object-Masks
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
#

require 'softlayer_api'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

brandId = 4

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
brand_service = client['SoftLayer_Brand']

object_mask = 'mask[group[name], status[name], statusId, id, createDate, title, assignedUser[username], attachedFileCount, totalUpdateCount, modifyDate, lastEditType, newUpdatesFlag, attachedHardwareCount, attachedVirtualGuestCount, priority, account[companyName, accountStatus[name]], assignedAgents[username], state[stateType], scheduledActions[transactionGroup, ticketScheduledActionReference] ]'
object_filter = SoftLayer::ObjectFilter.new
object_filter.set_criteria_for_key_path('tickets.status.name',           'operation' => 'in',
                                                                         'options' => [{
                                                                           'name' => 'data',
                                                                           'value' => %w(Open Assigned)
                                                                         }])

begin
  result = brand_service.object_with_id(brandId).object_mask(object_mask).object_filter(object_filter).getTickets
  print result
rescue StandardError => exception
  puts "Unable to list the tickets.: #{exception}"
end

```
