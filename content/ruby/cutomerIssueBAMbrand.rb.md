---
title: "cutomerIssueBAMbrand.rb"
description: "cutomerIssueBAMbrand.rb"
date: "2018-04-25"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Brand"
tags:
    - "brands"
---


```
require 'softlayer_api'
require 'pp'
puts "INFO: connecting...."

account_service = SoftLayer::Service.new("SoftLayer_Account",
:username => "",
:api_key => "apikey_goes_here")

brand_service = SoftLayer::Service.new("SoftLayer_Brand",
:username => "",
:api_key => "apikey_goes_here")

brands = account_service.getOwnedBrands()
puts "INFO: printing brands...."
pp (brands)
puts "INFO: printing customers for the brands...."
for brand in brands
  accounts = brand_service.object_with_id(brand['id']).getAllOwnedAccounts()
  pp (accounts)
end

```
