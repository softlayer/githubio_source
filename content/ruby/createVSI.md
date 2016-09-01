---
title: "Create a new virtual server with all options"
description: "Creates a new virtual server (VSI) and demonstrates the many options that can be used to customize the creation."
date: "2016-09-01"
classes:
  - "SoftLayer_Virtual_Guest"
tags:
  - "vsis"
  - "create"
---

When you are ready to place the order change `verifyOrder(productOrder)` to `placeOrder(productOrder)`.



```ruby

require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)

productOrder = {
  'virtualGuests' => [{
     'hostname' => 'testRuby',
     'domain'   => 'example.com',
     'primaryBackendNetworkComponent' => { 'networkVlan' => { 'id' => 1286783 } }
  }],
  'location' => 1441195,
  'packageId' => 46,
  'operatingSystemReferenceCode' => 'CENTOS_6_64', 
  'useHourlyPricing' => false,
  'prices' => [
     {'id' => 1640 }, # 1 x 2.0 GHz Core
     {'id' => 1644 }, # 1 GB RAM
     {'id' => 13945 }, # CENTOS_6_64
     {'id' => 1639 }, # 100 GB (SAN) First Disk
     {'id' => 2277 }, # 100 GB (SAN) Second Disk
     {'id' => 50367 }, # 250 GB Bandwidth
     {'id' => 274 }, # 1 Gbps Public & Private Network Uplinks
     {'id' => 21 }, # 1 IP Address
     {'id' => 420 }, # Unlimited SSL VPN Users & 1 PPTP VPN User per account
     {'id' => 56 }, # Host Ping and TCP Service Monitoring
     {'id' => 57 }, # Email and Ticket
     {'id' => 418 }, # NESSUS_VULNERABILITY_ASSESSMENT_REPORTING
     {'id' => 905 }, # REBOOT_REMOTE_CONSOLE
     {'id' => 58 }  # AUTOMATED_NOTIFICATION
  ]
}

order = client['Product_Order'].verifyOrder(productOrder)

pp order

```
