---
title: "get_accounts_brands.rb"
description: "get_accounts_brands.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Brand"
tags:
    - "brands"
---


```
# Get owned account
#
# The script retrieves all the owned accounts for an arbitrary brand,
# the script makes a call to getOwnedBrands() method to retrieve
# the brands where the account belongs, then it calls the getAllOwnedAccounts()
# method to get the owned accounts for every brand.
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getOwnedBrands
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getAllOwnedAccounts
# http://sldn.softlayer.com/reference/services/SoftLayer_Brand
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Brand
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'softlayer_api'

USERNAME = 'set me'
API_KEY = 'set me'

# Creating a SoftLayer API client object
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
account_service = client['SoftLayer_Account']
brand_service = client['SoftLayer_Brand']

begin
  brands = account_service.getOwnedBrands
  brands.each do |brand|
    brand_id = brand['id']
    accounts = brand_service.object_with_id(brand_id).getAllOwnedAccounts
    accounts.each do |account|
      print account
    end
  end
rescue StandardError => exception
  puts "Unable to retrieve the accounts in the brand. : #{exception}"
end

```
