---
title: "list_agents.rb"
description: "list_agents.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
tags:
    - "brands"
---


```
# List agents.
#
# The script retrieves all the agents in a brand account.
# It displays the same result like in https://agent.softlayer.com/administration/user/list
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getUsers
# http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'softlayer_api'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
account_service = client['SoftLayer_Account']
object_mask = 'mask[id, firstName, lastName, username, email, userStatus[name]]'

begin
  result = account_service.setObjectMask(object_mask).getUsers
  print result
rescue StandardError => exception
  puts "Unable to list the agents.: #{exception}"
end

```
