---
title: "delete_user.rb"
description: "delete_user.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
tags:
    - "users"
---


```
#
# Delete user.
# This scripts allows to delete a given user, it retrieves the SoftLayer_User_Customer object
# by the SoftLayer_User_Customer::getObject method and changes the status of user to deleted.
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer
# http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/editObject
# @License: http://sldn.softlayer.com/article/License
# @Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
#

require 'rubygems'
require 'softlayer_api'
require 'pp'

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME, api_key: SL_API_KEY)

# Set the user ID of the user you want to delete, yo can get it using
# The  SoftLayer_Account::getUsers method.
user_id = 111_922
user_to_delete = client['User_Customer'].object_with_id(user_id).getObject
# Set the user status to delete, these are the possible status for user
# 1001 = Active; 1002 = Disable; 1003 = Inactive; 1021 = Delete ; 1022 = VPN Only
user_to_delete['userStatusId'] = 102_1
begin
  # Define the connection to SoftLayer_User_Customer
  result = client['User_Customer'].object_with_id(user_id).editObject(user_to_delete)
  pp(result)
rescue => error_reason
  puts "Error deleting the user  #{error_reason}"
end

```
