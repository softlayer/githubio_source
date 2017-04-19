---
title: "Reload with SSH keys"
description: "Reloads a server with an image template and some ssh keys"
date: "2017-04-02"
classes: ["SoftLayer_Hardware_Server"]
tags:
    - "reloadOperatingSystem"
    - "reload"
    - "server"
---


```ruby
require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)

imageId = 1234567
sshKey1 = 876543
sshKey2 = 456789
serverId = 1154265
        config = {
            'imageTemplateId'=> imageId, 
            'sshKeyIds' => [sshKey1, sshKey2]
        }

setclient = client['Hardware_Server']
reload = setclient.object_with_id(serverId).reloadOperatingSystem('FORCE', config)
pp reload	        
```
