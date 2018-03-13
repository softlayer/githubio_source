---
title: "Using fog-softlayer for Managing Servers"
description: "In [part one](http://sldn.softlayer.com/blog/matteldridge/Fog-Gem-Support-SoftLayer) of this series we introduced a new "
date: "2014-07-01"
author: "matt.eldridge"
tags:
    - "blog"
---

In [part one](http://sldn.softlayer.com/blog/matteldridge/Fog-Gem-Support-SoftLayer) of this series we introduced a new ruby gem, [fog-softlayer](https://github.com/softlayer/fog-softlayer), which enables SoftLayer users to leverage [fog](https://github.com/fog/fog), the Ruby cloud services library.

In this installment, we will walk users through getting started with fog, covering several examples of using [fog-softlayer](https://github.com/softlayer/fog) to manage servers using both VMs and bare metal cloud instances.

#### Configure [fog-softlayer](https://github.com/softlayer/fog-softlayer) for Your Account

These examples assume you have a local file at `~/.fog` that contains:

   <yaml>  
   :softlayer_username: example-username
   :softlayer_api_key: 1a1a1a1a1a1a1a1a1a11a1a1a1a1a1a1a1a1a1 
   :softlayer_default_domain: example.com
  </yaml>
  
##### Create a Connection to SoftLayer Compute Service

Having the configuration file described above allows you to establish a connection to the SoftLayer cloud with just two lines of code.

<ruby>
\trequire 'fog/softlayer'
\t@sl = Fog::Compute[:softlayer]
</ruby>

##### Support for Multiple Accounts

Alternatively, if you require supporting multiple SoftLayer accounts, credentials and defaults can be passed as arguments when establishing a connection.

<ruby>
\tfirst_account_args = {
\t  :provider => :softlayer,
\t  :softlayer_username => 'example-username-1',
\t  :softlayer_api_key => '1a1a1a1a1a1a1a1a1a11a1a1a1a1a1a1a1a1a1',
\t  :softlayer_default_domain => 'example.com',
\t}
\t
\tsecond_account_args = {
\t  :provider => :softlayer,
\t  :softlayer_username => 'example-username-2',
\t  :softlayer_api_key => '2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b',
\t  :softlayer_default_domain => 'another-example.com',
\t}
\t
\t@sl1 = Fog::Compute.new(first_account_args)
\t@sl2 = Fog::Compute.new(second_account_args)
</ruby>
##### Use the Models

Fog has a robust, production tested, object model that is intuitive and powerful for working with clouds to provision infrastructure. Your primary interface for working with fog should be the models. If needed, you can directly make requests to SoftLayer with fog, but that code is not portable to OpenStack or other providers, and should be used only when required for performance. 

<code>1. </code> List all servers.

   <ruby>
   @sl.servers # list all servers
   @sl.servers.size # get a count of all servers 
   </ruby>

<code>2.</code> Get a server's details.

   <ruby>
   server = @sl.servers.get(<server id>)
   server.name # => 'hostname.example.com'
   server.created_at # => DateTime the server was created
   server.state # => 'Running', 'Stopped', 'Terminated', etc.
   </ruby>

<code>3.</code> Provision a new VM with flavor (simple).

   <ruby>
     opts = {
     \t:flavor_id => "m1.small",
     \t:image_id => "23f7f05f-3657-4330-8772-329ed2e816bc",
     \t:name => "test",
     \t:datacenter => {:name=>"ams01"}
     }
     new_server = @sl.servers.create(opts)
     new_server.id # => 1337
   </ruby>

<code>4.</code> Provision a new bare metal cloud instance with flavor (simple).

   <ruby>
     opts = {
     \t:flavor_id => "m1.small",
     \t:os_code => "UBUNTU_LATEST",
     \t:name => "test1",
     \t:datacenter => {:name=>"ams01"},
     \t:bare_metal => true
     }
     @sl.servers.create(opts)
     new_server.id # => 1338
   </ruby>

<code>5.</code> Provision a new VM without flavor.

   <ruby>
   \topts = {
     \t:cpu => 2,
     \t:ram => 2048,     \t
     \t:disk => [{'device' => 0, 'diskImage' => {'capacity' => 100 } }],
     \t:ephemeral_storage => true,
     \t:domain => "not-my-default.com",
     \t:name => "hostname",
     \t:os_code => "UBUNTU_LATEST",
     \t:name => "test2",
     \t:datacenter => {:name=>"ams01"},     
     }
   </ruby>

<code>6.</code> Provision a bare metal cloud instance without a flavor.

   <ruby>
   opts = {
     \t:cpu => 8,
     \t:ram => 16348,     \t
     \t:disk => {'capacity' => 100 },
     \t:ephemeral_storage => true,
     \t:domain => "not-my-default.com",
     \t:name => "hostname",
     \t:os_code => "UBUNTU_LATEST",
     \t:name => "test2",
     \t:datacenter => {:name=>"ams01"},
     \t:bare_metal => true
     }
   </ruby>

<code>7.</code> Delete a VM or bare metal cloud instance.

   <ruby>
   \t  @sl.servers.get(<server id>).destroy
   </ruby>


This wraps up our initial tour of working with the Server model using [fog-softlayer](https://github.com/softlayer/fog-softlayer). In the blog in this series we explore SoftLayer Object Storage using the Directory and File models.
   
\\- Matt

--
If you have questions about or problems with [fog-softlayer](http://rubygems.org/gems/fog-softlayer) open an [issue](https://github.com/softlayer/fog-softlayer/issues) or [email me](mailto:matt.eldridge@us.ibm.com?subject=fog-softlayer).


