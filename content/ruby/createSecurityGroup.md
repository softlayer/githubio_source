---
title: "Create a Security group"
description: "Example for creating a Security Group."
date: "2017-08-09"
classes:
    - "SoftLayer_Network_SecurityGroup"
tags:
    - "objectTemplate"
---

The Security Group offering is currently in Beta. The use of this feature is restricted to select users. When the Beta period is over, security groups will be available for all users. Contact sgbeta@us.ibm.com using ‘Security Groups’ in the subject line with any questions.

```ruby 

=begin
@author Ryan Tiffany
=end

require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)
objectTemplate = { 
	'name' => 'rubyExampleCreation',
    	'description' => 'Sec Group created via ruby'
}

createGroup = client['SoftLayer_Network_SecurityGroup'].createObjects([objectTemplate])

pp createGroup
```