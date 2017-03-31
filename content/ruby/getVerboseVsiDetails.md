---
title: "Get verbose details about a Virtual Guest"
description: "Retrieve the packages, categories and items associated with a Virtual Guest."
date: "2016-12-29"
classes: ["SoftLayer_Virtual_Guest"]
tags:
    - "objectMask"
    - "getObject"
---

This script will get the Packages, Categories, and items associated with a Virtual Guest. 

```ruby
require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)

virtual_server_id = 26961063
object_mask = 'mask[id,fullyQualifiedDomainName,billingItem[id,item[id,description],category[name,id],children[id,item[id,description],category[name,id]]]]'

getDetails = client['SoftLayer_Virtual_Guest'].object_mask(object_mask).object_with_id(virtual_server_id).getObject
pp getDetails
```