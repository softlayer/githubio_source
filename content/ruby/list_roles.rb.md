---
title: "list_roles.rb"
description: "list_roles.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_User_Permission_Role"
tags:
    - "brands"
---


```
# List roles.
#
# The script retrieves all the roles in a brand account.
# It displays the same result like in https://agent.softlayer.com/administration/role/list
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getPermissionRoles
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Permission_Role
# http://sldn.softlayer.com/article/Object-Masks
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'softlayer_api'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
account_service = client['SoftLayer_Account']
object_mask = 'mask[userCount]'

begin
  result = account_service.object_mask(object_mask).getPermissionRoles
  print result
rescue StandardError => exception
  puts "Unable to list the roles.: #{exception}"
end

```
