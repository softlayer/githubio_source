---
title: "get_user_status.rb"
description: "get_user_status.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
tags:
    - "users"
---


```
#
# Get User status.
# This script will list the status of sub-users similar to the view displayed at
# https://control.softlayer.com/account/users
# it calls to SoftLayer_User_Customer::getChildUsers
# method to retrieve the user list.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getUsers
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer
# @License: http://sldn.softlayer.com/article/License
# @Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
#

require 'rubygems'
require 'softlayer_api'
require 'pp'

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME, api_key: SL_API_KEY)
# Get current user
begin
  current_user = client['Account'].getCurrentUser
rescue => error_reason
  puts "Cannot get current user, #{error_reason}"
end

begin
  child_users = client['SoftLayer_User_Customer'].object_with_id(current_user['id']).getChildUsers
  print "+------------+------------+----------------------+------------+------------+\n"
  print "| Last Name  | First Name |    User Name         | Status     | VPN Access |\n"
  print "+------------+------------+----------------------+------------+------------+\n"
  child_users.each do |child_user|
    printf('| %-10s ', child_user['lastName'])
    printf('| %-10s ', child_user['firstName'])
    printf('| %-20s ', child_user['userName'])
    printf('| %-10s ', child_user['userStatusId'])
    printf("| %-10s |\n", child_user['sslVpnAllowedFlag'])
  end
  print "+------------+------------+----------------------+------------+------------+\n"
rescue => error_reason
  puts "Error getting child users details #{error_reason}"
end

```
