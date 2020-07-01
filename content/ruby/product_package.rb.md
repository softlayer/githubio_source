---
title: "Working with Product package"
description: "A few examples on interacting with product package"

date: "2020-07-01"
classes: 
    - "SoftLayer_Product_Package"    
tags:
    - "Product_Package"
---

[Product_Package](https://https://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/)

### Product package examples

#### Some examples use the most important methods.

```ruby
require 'softlayer_api'
require 'json'

class ProductPackage


  def initialize(username, apikey)
    client = SoftLayer::Client.new(username: username,
                                   api_key: apikey,)
    @package_service = client['SoftLayer_Product_Package']
  end

  def getAllObject()
    return @package_service.getAllObjects()
  end

  def getActivePreset(packageId)
    return @package_service.object_with_id(packageId).getActivePreset()
  end

  def getItemPrices(packageId)
    return @package_service.object_with_id(packageId).getItemPrices()
    end
  def getItemsConflicts(packageId)
    return @package_service.object_with_id(packageId).getItemsConflicts()
  end

  def getLocations(packageId)
    return @package_service.object_with_id(packageId).getLocations()
  end

  def getObject(packageId)
    return @package_service.object_with_id(packageId).getObject()
  end

  def getRegions(packageId)
    return @package_service.object_with_id(packageId).getRegions()
  end

  def getType(packageId)
    return @package_service.object_with_id(packageId).getType()
  end

end

user = 'set - me'
key = 'set -  me'
product = ProductPackage.new(user, key)

pp product.getAllObject

pp product.getItemPrices(200)





``` 