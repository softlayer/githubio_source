---
title: "list_event_logs.rb"
description: "list_event_logs.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Event_Log"
tags:
    - "eventlogs"
---


```
# List all event logs.
#
# This assumes the SoftLayer API Ruby client
# <https://github.com/softlayer/softlayer-ruby> is installed.
#
# Important manual pages:
# http://sldn.softlayer.com/article/ruby
# http://sldn.softlayer.com/reference/services/SoftLayer_Event_Log
# http://sldn.softlayer.com/reference/services/SoftLayer_Event_Log/getAllObjects
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Creating a SoftLayer API client object
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
event_log_service = client['SoftLayer_Event_Log']

# Calling the getAllObjects method
objects = event_log_service.getAllObjects
pp objects

begin
  # Calling the getAllObjects method
  objects = event_log_service.getAllObjects
  pp objects
rescue StandardException => exception
  puts "Unable to get the logs.  #{exception}"
end

```
