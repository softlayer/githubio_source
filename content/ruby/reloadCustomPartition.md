---
title: "Reloading a server with a custom partition scheme"
description: "The script will issue an OS reload on your Bare Metal server with a custom partition scheme."
date: "2017-03-31"
classes: ["Hardware_Server"]
tags:
    - "reloadoperatingsystem"
---

The following code allows you to reload a Bare Metal server with a custom partitioning scheme. You simply need to change the serverId and the partitions to suit your needs. Note that one partition must be marked as the 'grow' partition.

```ruby
require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)
server_id = 1154505

config = { 

    'upgradeHardDriveFirmware' => 0,
        'upgradeBios' => 0,
        'hardDrives' => [
            {
                'complexType' => "SoftLayer_Hardware_Component_HardDrive",
                'partitions' => [
                    { 'name' => { "/" => { "minimumSize" => "100"} } },
                    { 'name' => { "/boot" => { "minimumSize" => ".25" } } },
                    { 'name' => { "/swap0" => { "minimumSize" => "32"} } },
                    { 'name' => { "/tmp" => { "minimumSize" => "100"} } },
                    { 'name' => { "/var" => { "minimumSize" => "100"} } },
                    { 'name' => { "/remove" => { "minimumSize" => "1", "grow" => "1" } } } 
                ]
            }
        ]
     }

setclient = client['Hardware_Server']
reload = setclient.object_with_id(server_id).reloadOperatingSystem('FORCE', config)

pp reload

```