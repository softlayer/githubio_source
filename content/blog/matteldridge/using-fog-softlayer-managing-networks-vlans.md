---
title: "Using fog-softlayer for Managing Networks (VLANs)"
description: "In [part five]( http://sldn.softlayer.com/blog/matteldridge/Using-fog-softlayer-Managing-Key-Pairs) of this series, we e"
date: "2014-07-31"
author: "matt.eldridge"
tags:
    - "blog"
---

In [part five]( http://sldn.softlayer.com/blog/matteldridge/Using-fog-softlayer-Managing-Key-Pairs) of this series, we explored using [fog-softlayer](https://github.com/softlayer/fog-softlayer) for managing your SoftLayer key pairs.

In this blog, we'll look at creating and assigning VLANs for use with our virtual servers.


######Network Examples

Note that SoftLayer uses the term `VLAN`. The Fog project tries to keep things provider-independent, so we'll be referring to them as `networks`.


These examples all assume you have `~/.fog`, which contain the following:


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

##### Use the Models
List existing networks using:

   <ruby>
    nets = @sl.networks
    # => [ <Fog::Network::Softlayer::Network
    #  \tid=123456,
    #\tname="some-optional-name",
    #\tmodify_date="2014-06-25T17:10:57-05:00",
    #\tnote=nil,
    #\ttags=["sparkle", "motion", "public"],
    #\ttype="STANDARD",
    #\tdatacenter=\t<Fog::Network::Softlayer::Datacenter
    #\t\tid=12345,
    #\t\tlong_name="Washington, DC 1",
    #\t\tname="wdc01"
    #\t\t>,
    #\tnetwork_space="PUBLIC"
    #\trouter={"hostname"=>"fcr02.wdc01", "id"=>40378, "datacenter"=>{"id"=>37473, "longName"=>"Washington, DC 1", "name"=>"wdc01"}}
    #\t>,
    #\t<Fog::Network::Softlayer::Network
    #\tid=123457,
    #\tname="some-other-optional-name",
    #\tmodify_date="2014-06-25T17:11:57-05:00",
    #\tnote=nil,
    #\ttags=["sparkle", "motion", "private"],
    #\ttype="STANDARD",
    #\tdatacenter=\t<Fog::Network::Softlayer::Datacenter
    #\t\tid=12345,
    #\t\tlong_name="Washington, DC 1",
    #\t\tname="wdc01"
    #\t\t>,
    #\tnetwork_space="PRIVATE"
    #\trouter={"hostname"=>"bcr02.wdc01", "id"=>40379, "datacenter"=>{"id"=>37473, "longName"=>"Washington, DC 1", "name"=>"wdc01"}}
    #\t>,    \t  \t
\t# ]
   </ruby>
   \t
Next, get a network by name. SoftLayer offers the option to assign a name to each VLAN on your account. Here's how to look up a VLAN by name:  

<ruby>
\t@sl.networks.by_name('some-name')
\t# => <Fog::Network::Softlayer::Network
    #\tid=123456,
    #\tname="some-name",
    #\tmodify_date="2014-06-25T17:10:57-05:00",
    #\tnote=nil,
    #\ttags=["sparkle", "motion", "public"],
    #\ttype="STANDARD",
    #\tdatacenter=\t<Fog::Network::Softlayer::Datacenter
    #\t\tid=12345,
    #\t\tlong_name="Washington, DC 1",
    #\t\tname="wdc01"
    #\t\t>,
    #\tnetwork_space="PUBLIC"
    #\trouter={"hostname"=>"fcr02.wdc01", "id"=>40378, "datacenter"=>{"id"=>37473, "longName"=>"Washington, DC 1", "name"=>"wdc01"}}
    #\t>
</ruby>

To get a network by ID, use:

<ruby>
\tnet = @sl.networks.get(123456)
\t# => <Fog::Network::Softlayer::Network
    #\tid=123456,
    #\tname="some-name",
    #\tmodify_date="2014-06-25T17:10:57-05:00",
    #\tnote=nil,
    #\ttags=["sparkle", "motion", "public"],
    #\ttype="STANDARD",
    #\tdatacenter=\t<Fog::Network::Softlayer::Datacenter
    #\t\tid=12345,
    #\t\tlong_name="Washington, DC 1",
    #\t\tname="wdc01"
    #\t\t>,
    #\tnetwork_space="PUBLIC"
    #\trouter={"hostname"=>"fcr02.wdc01", "id"=>40378, "datacenter"=>{"id"=>37473, "longName"=>"Washington, DC 1", "name"=>"wdc01"}}
    #\t>
</ruby>

\t
Here’s how to get all networks with a particular tag. (I recommend using tags to bring order to cloud assets that will scale to `N` instances.)

<ruby>
prod_backend_nets = @sl.networks.tagged_with(['production', 'private'])
# => [<Fog::Network::Softlayer::Network>,
#\t<Fog::Network::Softlayer::Network>,
#\t<Fog::Network::Softlayer::Network>,
#\t]    \t
</ruby>
\t
To get a network's tags:

<ruby>
net = @sl.networks.get(123456)
net.tags
# => ['sparkle', 'motion', 'production', 'public']
</ruby>
\t
To get a network's router:

<ruby>
net = @sl.networks.by_name('some-name')
net.router
# => {"hostname"=>"bcr02a.ams01",
# "id"=>190854,
# "datacenter"=>{"id"=>265592, "longName"=>"Amsterdam 1", "name"=>"ams01"}}
</ruby>

To get a network's subnets:

<ruby>
net = @sl.networks.get(123456)
net.subnets
# => [  <Fog::Network::Softlayer::Subnet
# id=123456,
# name=nil,
# network_id="37.58.125.72",
# vlan_id=123456,
# cidr=29,
# ip_version=4,
# type="ADDITIONAL_PRIMARY",
# gateway_ip="37.58.125.73",
# broadcast="37.58.125.79",
# gateway=nil,
# datacenter="ams01"
# >,
# <Fog::Network::Softlayer::Subnet
# id=123457,
# name=nil,
# network_id="81.95.147.148",
# vlan_id=123456,
# cidr=30,
# ip_version=4,
# type="PRIMARY",
# gateway_ip="81.95.147.149",
# broadcast="81.95.147.151",
# gateway=nil,
# datacenter="ams01"
# >]
</ruby>
\t
To get a subnet's IP addresses:

<ruby>
net = @sl.networks.get(123456)
# Here I'm selecting the primary subnet...
subnet = net.subnets.select { |vlan| vlan.type == "PRIMARY" }.first
# => <Fog::Network::Softlayer::Subnet
# id=123457,
# ...
# >
addys = subnet.addresses
# => [  <Fog::Network::Softlayer::Ip
# id=19222174,
# subnet_id=630962,
# address="37.58.125.72",
# broadcast=false,
# gateway=false,
# network=true,
# reserved=false,
# note=nil,
# assigned_to=nil
# >,
# <Fog::Network::Softlayer::Ip
#  id=19222174,
#  subnet_id=630962,
#  address="37.58.125.73",
#  broadcast=false,
#  gateway=true,
#  network=false,
#  reserved=false,
#  note=nil,
#  assigned_to=nil
#  >,
# <Fog::Network::Softlayer::Ip
#  id=19222174,
#  subnet_id=630962,
#  address="37.58.125.74",
#  broadcast=false,
#  gateway=false,
#  network=false,
#  reserved=false,
#  note=nil,
#  assigned_to={"fullyQualifiedDomainName"=>"hostname.example.com", "id"=>281730}
#  >,
# <Fog::Network::Softlayer::Ip
#  id=19222174,
#  subnet_id=630962,
#  address="37.58.125.75",
#  broadcast=false,
#  gateway=false,
#  network=false,
#  reserved=false,
#  note=nil,
#  assigned_to={"fullyQualifiedDomainName"=>"hostname-2.example.com", "id"=>281730}
#  >,
# ...,
#  ]
</ruby>
\t
######How to Create a new Network

<ruby>\t\t
# We're creating a network in wdc01, and the same steps will work for any datacenter.
# @sl.datacenters will give you a list of available datacenters.

wdc01 = @sl.datacenters.by_name('wdc01')
wdc01.routers
# => [{"hostname"=>"bcr01.wdc01", "id"=>16358},
# {"hostname"=>"bcr02.wdc01", "id"=>40379},
# {"hostname"=>"bcr03a.wdc01", "id"=>85816},
# {"hostname"=>"bcr04a.wdc01", "id"=>180611},
# {"hostname"=>"bcr05a.wdc01", "id"=>235754},
# {"hostname"=>"fcr01.wdc01", "id"=>16357},
# {"hostname"=>"fcr02.wdc01", "id"=>40378},
# {"hostname"=>"fcr03a.wdc01", "id"=>85814},
# {"hostname"=>"fcr04a.wdc01", "id"=>180610},
# {"hostname"=>"fcr05a.wdc01", "id"=>235748}]

# We want to create a public network, so be sure to use one of the fcr* routers.
# If we were creating a private network, we'd want to use a bcr* router.

opts = {
    :name => 'my-new-network',
    :datacenter => wdc01,
    :router => wdc01.routers[4],
    :network_space => 'PUBLIC',
}

@sl.networks.create(opts)\t\t
</ruby><br>

##### Try Before You Buy

One of the excellent features included in [fog-softlayer](http://github.com/softlayer/fog-softlayer) (and for all of the supported providers), is fantastic mocking.

Even if you don't have a SoftLayer account, you can download [fog-softlayer](https://github.com/softlayer/fog-softlayer) and start testing this code.

Just call `Fog.mock!` immediately after requiring the gem, so you can run all of the above code examples and see how easy it is to work with.

We're working hard to get full coverage of Mock classes and methods.  You may run across a MockNotImplemented exception here or there. If you do, probably the best course is to fork the repo, implement the mock, and open a pull request. 

\\- Matt

--

If you have questions about or problems with [fog-softlayer](http://rubygems.org/gems/fog-softlayer) open an [issue](https://github.com/fog/fog-softlayer/issues) or [email me](mailto:matt.eldridge@us.ibm.com?subject=fog-softlayer).

