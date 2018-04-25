---
title: "reset_portal_user_password.rb"
description: "reset_portal_user_password.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
tags:
    - "users"
---


```
#
# Reset portal user password.
# This script resets the password of a portal user by SoftLayer_User_Customer::updatePassword method
# need to define the new password and pass it to updatePassword() method.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer
# http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/updatePassword
# @License: http://sldn.softlayer.com/article/License
# @Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
#

require 'rubygems'
require 'softlayer_api'

#
# Your SoftLayer API username and key.
# Generate an API key at the SoftLayer Customer Portal
#
SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'
# Set the user id to reset the portal user password, use the
# SoftLayer_Account::getUsers method to get a list of users available in the account.
user_customer_id = 152_188
new_password = 'newPassword123!'
# Create a client object to connect to API services
client = SoftLayer::Client.new(username: SL_API_USERNAME, api_key: SL_API_KEY)
begin
  client['SoftLayer_User_Customer'].object_with_id(user_customer_id).updatePassword(new_password)
  print 'Password updated!'
rescue => error_reason
  puts "Unable to reset the user password, #{error_reason}"
end

```
