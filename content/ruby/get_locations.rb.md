---
title: "get_locations.rb"
description: "get_locations.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
tags:
    - "package"
---


```
#
# Get package location
#
# This script will retrieve a collection of valid locations for this package.
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getLocations
#
# @License: http://sldn.softlayer.com/article/License
# @Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'rubygems'
require 'softlayer_api'
require 'pp'

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME, api_key: SL_API_KEY)
# Set the ID of the package to retrieve the information
package_id = 46
locations = client['SoftLayer_Product_Package'].object_with_id(package_id).getLocations
print "+------------+---------------------------+------------+\n"
print "| ID         | Location description      | Status ID  |\n"
print "+------------+---------------------------+------------+\n"
locations.each do |location|
  printf('| %-10s ', location['id'])
  printf('| %-25s ', location['longName'])
  printf("| %-10s | \n", location['statusId'])
end
print "+------------+---------------------------+------------+\n"

```
