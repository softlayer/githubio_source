---
title: "Using fog-softlayer for Managing Global IP Addresses"
description: "In [part six]( http://sldn.softlayer.com/blog/matteldridge/Using-fog-softlayer-Managing-Networks-VLANs) of this series w"
date: "2014-08-01"
author: "matt.eldridge"
tags:
    - "blog"
---

In [part six]( http://sldn.softlayer.com/blog/matteldridge/Using-fog-softlayer-Managing-Networks-VLANs) of this series we explored using [fog-softlayer](https://github.com/softlayer/fog-softlayer) for managing your SoftLayer VLANs.

In this installment, we’ll cover creating and routing [global IP addresses](http://blog.softlayer.com/2012/global-ip-addresses-what-are-they-and-how-do-they-work).

You can follow [this link](http://blog.softlayer.com/2012/global-ip-addresses-what-are-they-and-how-do-they-work) for details  on  what SoftLayer global IP addresses are and how they work.

In short, with SoftLayer global IP addresses you can route a public IPv4 or IPv6 address to any server, on any (public) VLAN, in any SoftLayer data center.

They're similar to "Elastic IPs" offered by some other public clouds. The only difference is that global IPs are more flexible, powerful, and useful.

This post will cover basic management of global IP addresses with [fog-softlayer](https://github.com/fog/fog-softlayer). Before we get into that, there's one <em>IMPORTANT ITEM TO NOTE: before a global IP will work properly certain minor configuration changes must be made on the target host</em>. Please read [this article](http://knowledgelayer.softlayer.com/learning/global-ip-addresses) for information on the configuration changes.


##### Network Examples

These examples all assume you have `~/.fog`, which contains the following:


   <code>
default:
  softlayer_username: example-username
  softlayer_api_key: 1a1a1a1a1a1a1a1a1a11a1a1a1a1a1a1a1a1a1 
  </code>

##### Create a Connection to the SoftLayer Network

<ruby>
require 'fog/softlayer'
@sl = Fog::Network[:softlayer]
</ruby>

##### The Same, But Different

[Part six](http://sldn.softlayer.com/blog/matteldridge/Using-fog-softlayer-Managing-Networks-VLANs) of this series covered using the `Network` service to manage your VLANs. The service comprises a handful of models including `Fog::Network::Softlayer::Network`, `Fog::Network::Softlayer::Subnet`, and `Fog::Network::Softlayer::Ip`.

Global IP addresses are accessed through the `Fog::Network::Softlayer::Ip` model. Unlike "normal" IP addresses, they can be specifically created and destroyed, while non-global IP addresses are created and destroyed via a subnet.

This example lists all IPs on the SoftLayer account and selects those that are global. The response shows us two global IP addresses belonging to the account. The first one is unrouted, and the second one is routed.

   <ruby>
    global_ips = @network.ips.select { |ip| ip.global? }
    # => [ <Fog::Network::Softlayer::Ip
    #  id=123456789,
    #  subnet_id=123456,
    #  address="203.0.113.5",
    #  broadcast=false,
    #  gateway=false,
    #  network=false,
    #  reserved=false,
    #  global_id=1234,
    #  destination_ip=nil,
    #  note=nil,
    #  assigned_to=nil
    # >,
\t# <Fog::Network::Softlayer::Ip
    #  id=123456790,
    #  subnet_id=123457,
    #  address="203.0.113.6",
    #  broadcast=false,
    #  gateway=false,
    #  network=false,
    #  reserved=false,
    #  global_id=1235,
    #  destination_ip= <Fog::Network::Softlayer::Ip
    #    id=123458,
    #    subnet_id=123456,
    #    address="203.0.113.7",
    #    broadcast=false,
    #    gateway=false,
    #    network=false,
    #    reserved=false,
    #    global_id=nil,
    #    destination_ip=nil,
    #    note=nil,
    #    assigned_to=nil
    #  >,
    #  note=nil,
    #  assigned_to=nil
    # >
    # ]
   </ruby>




If I want to route an unrouted global IP to a specific server I’m running in the Hong Kong data center, I could do the following:

<ruby>
global_ip = @network.ips.select { |ip| ip.global? && !ip.routed? }.first
# => <Fog::Network::Softlayer::Ip
#  id=123456789,
#  subnet_id=123456,
#  address="203.0.113.5",
#  broadcast=false,
#  gateway=false,
#  network=false,
#  reserved=false,
#  global_id=1234,
#  destination_ip=nil,
#  note=nil,
#  assigned_to=nil
# >
global_ip.routed? # => false


@compute = Fog::Compute[:softlayer]
dest_server = @compute.servers.tagged_with(['production', 'frontend', 'hkg']).first # => <Fog::Compute::Softlayer::Server>
dest_ip = @network.ips.by_address(dest_server.public_ip) # => <Fog::Network::Softlayer::Ip>


global_ip.route(dest_ip) # => true

global_ip.reload
# => <Fog::Network::Softlayer::Ip
#  id=123456789,
#  subnet_id=123456,
#  address="203.0.113.5",
#  broadcast=false,
#  gateway=false,
#  network=false,
#  reserved=false,
#  global_id=1234,
#  destination_ip= <Fog::Network::Softlayer::Ip
#    id=123458,
#    subnet_id=123456,
#    address="203.0.113.8",
#    broadcast=false,
#    gateway=false,
#    network=false,
#    reserved=false,
#    global_id=nil,
#    destination_ip=nil,
#    note=nil,
#    assigned_to=nil
#  >,
#  note=nil,
#  assigned_to=nil
# >

global_ip.routed?
# => true
</ruby>

Later, if I need to route that same address to a server in London, I can do the following:

<ruby>
global_ip = @network.ips.by_address('203.0.113.5')
global_ip.destination.address # => 203.0.113.8

london_server = @compute.servers.tagged_with(['production', 'frontend', 'lon']).first # => <Fog::Compute::Softlayer::Server>
dest_ip = @network.ips.by_address(london_server.public_ip) # => <Fog::Network::Softlayer::Ip>

global_ip.route(dest_ip) # => true
global_ip.reload # => <Fog::Network::Softlayer::Ip>
global_ip.destination.address # => 203.0.113.9
</ruby>

At some point I don't want that IP address routing anywhere so I do the following:

<ruby>
global_ip = @network.ips.by_address('203.0.113.5')
global_ip.routed? # => true

global_ip.unroute # => true
global_ip.reload # => <Fog::Network::Softlayer::Ip>

global_ip.routed? # => false
</ruby>

If I need an additional new global IP address, I can create it by doing the following:  
<em>Note that these methods are blocking and can take several seconds to respond</em>.

<ruby>
@network.create_new_global_ipv4 # => <Fog::Network::Softlayer::Ip>

# For IPv6 I simply do this:
@network.create_new_global_ipv6 # => <Fog::Network::Softlayer::Ip>
</ruby>
   \t

##### Try Before You Buy

One of the excellent features included in [fog-softlayer](http://github.com/softlayer/fog-softlayer) (and for all of the supported providers), is fantastic mocking.

Even if you don't have a SoftLayer account, you can download [fog-softlayer](https://github.com/softlayer/fog-softlayer) and start testing this code.

Just call `Fog.mock!` immediately after requiring the gem, so you can run all of the above code examples and see how easy they are to work with.

We're working hard to get full coverage of Mock classes and methods. You may run across a MockNotImplemented exception here or there. If you do, the best course is probably to fork the repo, implement the mock, and open a pull request. 

\\- Matt

--

If you have questions about or problems with [fog-softlayer](http://rubygems.org/gems/fog-softlayer) open an [issue](https://github.com/fog/fog-softlayer/issues) or [email me](mailto:matt.eldridge@us.ibm.com?subject=fog-softlayer).\t

