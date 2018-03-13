---
title: "Fog Gem Support for SoftLayer"
description: "Things just got easier for developers working with the SoftLayer API.  Support for SoftLayer is introduced with the rele"
date: "2014-06-19"
author: "matt.eldridge"
tags:
    - "blog"
---

Things just got easier for developers working with the SoftLayer API.  Support for SoftLayer is introduced with the release of [fog-softlayer](http://rubygems.org/gems/fog-softlayer), which is a provider gem for [fog](http://fog.io/), the Ruby cloud services library.

Fog is an open source cloud services library implemented in Ruby.  

##### **Call it what you will, fog calls it what it is.**

`CCI`, `VM`, `Cloud Server`, `Elastic Cloud Compute Instance`, `EC2`, `Compute Instance`. All of these terms mean the exact same thing! They're all different ways of saying **an instance of an operating system is running on virtualized hardware in a cloud**. The name you use depends on which cloud provider you're working with. 

When you're using fog gem's production proven object models, there is *one* set of resource names shared among every provider. It doesn't matter what the provider calls the resource. And it doesn’t matter if the API that has access to it is REST, SOAP, or uses XML or JSON, as a developer you have one interface to learn and use.

Within fog are different providers, each one represents a cloud provider with publicly accessible APIs. Through the release of [fog-softlayer](http://rubygems.org/gems/fog-softlayer), SoftLayer is now available as a provider.

Each provider offers at least the three following services.

* Compute – A service that supports actions to create/update/destroy one or more instances of a cloud server.    
* DNS – A service that allows you to create/update/destroy records in the [Domain Name System](http://en.wikipedia.org/wiki/Domain_Name_System).
* Storage – A service that allows you to create/update/destroy directories and files in an [object-storage](http://en.wikipedia.org/wiki/Object_storage) service.

In turn, each service exposes a set of models associated with that service. Based on the capabilities of different providers, there is some variation in models associated with a given service.

  * Compute Models: Server, Image and Flavor
  * DNS Models: Zone and Record
  * Storage Models: Directory and File


##### **Fog in Action**
Let's take a look at two examples. The first launches a server on OpenStack and the second on native SoftLayer.

<ruby>
require 'fog/softlayer'

# initialize an OpenStack provider object.
@openstack = Fog::Compute[:openstack] # assumes credentials are in ~/.fog config file

# get smallest flavor ID and default image ID for OpenStack
flavor = @openstack.flavors.first.id # => "1"
image = @openstack.images.first.id # => "0e09fbd6-43c5-448a-83e9-0d3d05f9747e"

# launch a small server on OpenStack
openstack_server = @openstack.servers.create(:flavor_ref => flavor, :image_ref => image, :name => 'test-server')



# initialize a SoftLayer provider object.
@softlayer = Fog::Compute[:softlayer] # assumes credentials are in ~/.fog config file

# get smallest flavor ID and default image ID for SoftLayer 
flavor = @softlayer.flavors.first.id # => "m1.tiny"
image = @softlayer.images.first.id #=> "3b235124-a190-40b5-9720-c020e61b99e1"

# launch a small server on OpenStack
softlayer_server = @softlayer.servers.create(:flavor_id => flavor, :image_id => image, :name => 'test-server')

</ruby>

That's about as painless as we can ask for. Most of the code is actually the same. 

Let's get even those lingering differences out of the way. 

<ruby>
require 'fog/softlayer'

class SmallServer
  attr_accessor :name
  attr_reader :flavor, :image
  def initialize(provider)
    @provider = provider
    @connection = Fog::Compute[provider]
    self.launch
  end

  def launch
    begin
      @connection.servers.create(options)
    end
  end

  def flavor
    @connection.flavors.first.id
  end

  def image
    @connection.images.first.id
  end

  def name
    @name ||= 'test'
  end

  def options
    _flavor = openstack? ? :flavor_ref : :flavor_id
    _image = openstack? ? :image_ref : :image_id
    { _flavor => flavor, _image => image, :name => name}
  end

  def openstack?
    @provider.match(/openstack/)
  end
end

</ruby>
With that class available, let's implement our example task of launching one server on each cloud.

<ruby>
require 'fog/softlayer'
include SmallServer

# launch a small server on OpenStack
openstack_server = SmallServer.new(:openstack)

# launch a small server on SoftLayer
sl_server = SmallServer.new(:softlayer)
</ruby>

If we don't count `require` and `include`, we're down to *two* lines of code.


You can install fog-softlayer from [rubygems.org](http://rubygems.org/) via `gem install fog-softlayer`, or you can grab [the source](https://github.com/softlayer/fog-softlayer) from [github.com](https://github.com/).

Alternatively, for something a little more lightweight, you can use the SoftLayer module as a stand-alone gem. Install that with `gem install fog-softlayer` or use [the source](https://github.com/softlayer/fog-softlayer). 


\\- Matt

--
If you have questions about or problems with [fog-softlayer](http://rubygems.org/gems/fog-softlayer) open an [issue](https://github.com/softlayer/fog-softlayer/issues) or [email me](mailto:matt.eldridge@us.ibm.com?subject=fog-softlayer).


