---
title: "edit_user.rb"
description: "edit_user.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
tags:
    - "users"
---


```
#
# Edit User.
# Account master users and sub-users who have the User Manage permission in the SoftLayer customer portal
# can update other user's information. Use editObject() if you wish to edit a single user account.
# Users who do not have the User Manage permission can only update their own information.
# Important manual Pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/editObject
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer
# @License: http://sldn.softlayer.com/article/License
# @Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
#

require 'rubygems'
require 'softlayer_api'
require 'pp'
#
# Your SoftLayer API username and key.
# Generate an API key at the SoftLayer Customer Portal
#
SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

# Set the id of user to edit, use the SoftLayer_Account::getUsers method
# to get a list of users
user_id = 123_456
#
# userTemplate contains general information relating to a single SoftLayer customer portal user.
# Personal information in this type such as names, addresses,
# and phone numbers are not necessarily associated with the customer account the user is assigned to.
#
user_template_object = {
  'address1' => '315 Capitol Street',
  'city' => 'Dallas',
  'companyName' => 'company name',
  'country' => 'US',
  'email' => 'test@softlayer.local',
  'firstName' => 'myFirstName',
  'lastName' => 'myLastName',
  'officePhone' => 444_44,
  'postalCode' => 770_02,
  'state' => 'TX',
  'timezoneId' => 114,
  'userStatusId' => 100_1,
  'username' => 'myUsername'
}
# Create a client instance to connect to the API service.
client = SoftLayer::Client.new(username: SL_API_USERNAME, api_key: SL_API_KEY)
begin
  result = client['User_Customer'].object_with_id(user_id).editObject(user_template_object)
  print 'User information updated'
  pp(result)
rescue => error_reason
  puts "Unable to edit user information, #{error_reason}"
end

```
