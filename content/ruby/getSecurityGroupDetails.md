---
title: "Get Security Group Details"
description: "Get the rules and associated servers in a Security Group."
date: "2017-08-09"
classes:
    - "SoftLayer_Network_SecurityGroup"
tags:
    - "getAllObjects"
---

The Security Group offering is currently in Beta. The use of this feature is restricted to select users. When the Beta period is over, security groups will be available for all users. Contact sgbeta@us.ibm.com using ‘Security Groups’ in the subject line with any questions.

```ruby

=begin
@author Ryan Tiffany
=end

require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)
secGroupId = 70501

getAll = client['SoftLayer_Network_SecurityGroup'].object_with_id(secGroupId).getAllObjects
pp getAll
```