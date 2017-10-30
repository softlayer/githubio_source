---
title: "Create a new virtual server and attach Security Groups"
description: "Creates a new virtual server (VSI) aand attach the public and private interfaces to respective Security Groups."
date: "2017-10-30"
classes:
  - "SoftLayer_Virtual_Guest"
tags:
  - "vsis"
  - "create"
  - "securitygroups"
---

To get a list of Security Groups you can attach to a Virtual Guest you can run the following code:

```ruby
require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)

getGroups = client['Network_SecurityGroup'].getAllObjects

pp getGroups
```

Once you have the Security Group IDs you would like to use you can plug them in to the following example:

```ruby
require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)

productOrder = {
    	'hostname' => 'rubysectest',
    	'domain' => 'cde.services',
    	'datacenter' => {'name' => 'dal05'},
    	'startCpus' => 2, # 2 x 2.0 GHz Cores
    	'maxMemory' => 2048, # 4GB RAM
    	'private_network_only' => false,
    	'dedicated_host_only' => false,
    	'operatingSystemReferenceCode' => 'UBUNTU_LATEST_64', # Latest Ubuntu LTS
    	'localDiskFlag' => false, # Use a SAN disk
    	'public_security_groups' => [43507],
    	'private_security_groups' => [43511],
    	'hourly' => false # Charge me for hourly use, rather than monthly.
}

order = client['Virtual_Guest'].createObject(productOrder)

pp order

```