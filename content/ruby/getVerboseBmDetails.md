---
title: "Get verbose details about a Bare Metal Server"
description: "Retrieve the packages, categories and items associated with a Bare Metal Server."
date: "2016-12-29"
classes: ["SoftLayer_Hardware"]
tags:
    - "objectmask"
    - "getobject"
---

This script will get the Packages, Categories, and items associated with a Bare Metal Server. 

```ruby

require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)

hardware_id = 26961063
object_mask = 'mask[id,fullyQualifiedDomainName,billingItem[id,item[id,description],category[name,id],children[id,item[id,description],category[name,id]]]]'

getDetails = client['SoftLayer_Hardware'].object_mask(object_mask).object_with_id(hardware_id).getObject
pp getDetails

```