---
title: "create_portal_user.rb"
description: "create_portal_user.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
tags:
    - "users"
---


```
#
# Create Portal User.
# This script will create a new portal user based in the values set into a SoftLayer_User_Customer
# template object and then it will pass to SoftLayer_User_Customer::createObject method.
# Check below references for more details.
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/createObject
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer
# @License: http://sldn.softlayer.com/article/License
# @Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
#
require 'rubygems'
require 'softlayer_api'
require 'pp'

# Set API user account credentials
SL_API_USERNAME =  'set me'
SL_API_KEY =  'set me'

# Set the password for the new  user
usr_password =  'Password!123 '
# Set the vpn password for the new user
vpn_password =  'Password!123 '

#
# The userTemplate contains general information relating to a single SoftLayer customer portal user.
# Personal information in this type such as names, addresses,
# and phone numbers are not necessarily associated with the customer account the user is assigned to.
#
user_template = {
  'address1' =>  '315 Capitol Street',
  'city' =>  'Dallas',
  'companyName' =>  'company name',
  'country' =>  'US',
  'email' =>  'test@softlayer.local',
  'firstName' =>  'myFirstName',
  'lastName' =>  'myLastName',
  'officePhone' =>  444_44,
  'postalCode' =>  770_02,
  'state' =>  'TX',
  'timezoneId' =>  114,
  'userStatusId' =>  1001,
  'username' =>  'myUsername'
}
# Create a client instance.
client = SoftLayer::Client.new(username: SL_API_USERNAME, api_key: SL_API_KEY)
begin
  # Create a new portal user
  result = client['User_Customer'].createObject(user_template, usr_password, vpn_password)
  pp(result)
rescue => error_reason
  puts "Error creating the user #{error_reason}"
end

```
