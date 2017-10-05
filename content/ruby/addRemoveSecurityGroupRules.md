---
title: "Add and remove rules in a Security group"
description: "Example for adding and removing rules in a Security Group."
date: "2017-08-09"
classes:
    - "SoftLayer_Network_SecurityGroup"
tags:
    - "objectTemplate"
---

### Adding Rules

```ruby

=begin
@author Ryan Tiffany
=end

require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)
secGroupId = 84301

# Create an object template to create the item.
objectTemplate = {
	'direction' => 'ingress',
	'protocol' => 'tcp',
	'portRangeMin' => 22,
	'portRangeMax' => 22,
	'ethertype' => 'IPv4',
	'remoteIp' => '0.0.0.0/0'
}

newRules = client['SoftLayer_Network_SecurityGroup'].object_with_id(secGroupId).addRules([objectTemplate])
pp newRules
```

### Removing rules

```ruby

=begin
@author Ryan Tiffany
=end

require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)
secGroupId = 45101

# Create an object template to create the item.
objectTemplate = [ 48501, 48401 ]

remove = client['SoftLayer_Network_SecurityGroup'].object_with_id(secGroupId).removeRules(objectTemplate)
pp remove
```
