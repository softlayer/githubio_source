---
title: "add_portal_permissions.rb"
description: "add_portal_permissions.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
    - "SoftLayer_User_Customer_CustomerPermission_Permission"
tags:
    - "users"
---


```
#
# Add user permission.
# This script adds a single permission to an user.
# Use the SoftLayer_User_Customer_CustomerPermission_Permission::getAllObjects method
# to retrieve a list of all permissions available in the SoftLayer.
# Important manual Pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/addPortalPermission
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission
# @License: http://sldn.softlayer.com/article/License
# @Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
#
require 'rubygems'
require 'softlayer_api'
require 'pp'

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME, api_key: SL_API_KEY)

# Set the user ID of the user you want to add permissions, yo can get them using
# The method SoftLayer_Account::getUsers.
user_id = 282_220

# In this example we are going to add permissions to the user
# to add tickets using SoftLayer_User_Customer::addPortalPermission method.
permission_template = {
  'keyName' => 'TICKET_ADD'
}

begin
  # Define the connection to SoftLayer_User_Customer
  result = client['User_Customer'].object_with_id(user_id).addPortalPermission(permission_template)
  pp(result)
rescue => error_reason
  puts "Error adding permission to the user #{error_reason}"
end

```
