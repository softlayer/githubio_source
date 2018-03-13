---
title: "Using fog-softlayer for Managing Key Pairs"
description: "In [part four]( http://sldn.softlayer.com/blog/matteldridge/Using-fog-softlayer-Managing-DNS ) of this series, we explor"
date: "2014-07-30"
author: "matt.eldridge"
tags:
    - "blog"
---

In [part four]( http://sldn.softlayer.com/blog/matteldridge/Using-fog-softlayer-Managing-DNS ) of this series, we explored using [fog-softlayer](https://github.com/softlayer/fog-softlayer) for managing your SoftLayer tags.

In this post, we'll look at creating and assigning SSH key pairs for use with our compute instances.


##### Key Pair Examples

These examples all assume you have `~/.fog`, which contains the following:

   <code>
default:
  softlayer_username: example-username
  softlayer_api_key: 1a1a1a1a1a1a1a1a1a11a1a1a1a1a1a1a1a1a1 
  softlayer_default_domain: example.com
  </code>
  

##### Create a Connection to SoftLayer Compute Service

<ruby>
require 'fog/softlayer'
@sl = Fog::Compute[:softlayer]
</ruby><br>


##### Key Pair Basics

Create some new key pairs:
<ruby>
kp1 = @sl.key_pairs.create(:label => 'my-new-key', :key => 'ssh-rsa AAAAxbU2lx...')
# => <Fog::Compute::Softlayer::KeyPair>
kp2 = @sl.key_pairs.new
kp2.label = 'my-new-new-key'
kp2.key = 'ssh-rsa AAAAxbU2lx...'
kp2.save
# => <Fog::Compute::Softlayer::KeyPair>
</ruby>


Here's how we get key pairs that have already been created:
<ruby>
# By id:
kp = @sl.key_pairs.get(123456)
# => <Fog::Compute::Softlayer::KeyPair>

# By label:
kp = @sl.key_pairs.by_label('my-new-key')
# => <Fog::Compute::Softlayer::KeyPair>
</ruby>


Let's destroy a key pair, just for fun.

<ruby>
kp = @sl.key_pairs.by_label('my-new-key')
# => <Fog::Compute::Softlayer::KeyPair>
kp.destroy
</ruby><br>

\t
##### Key Pairs with Servers

With basic CRUD out of the way on the key pairs, let's see how we can assign them to servers.

Create a server with one or more key pairs using:

<ruby>
the_first_key = @sl.key_pairs.by_label('my-new-key')
# => <Fog::Compute::Softlayer::KeyPair>
the_second_key = @sl.key_pairs.by_label('my-other-new-key')
# => <Fog::Compute::Softlayer::KeyPair>
\t
opts = { 
\t:flavor_id => 'm1.small', 
\t:os_code => 'UBUNTU_LATEST', 
\t:datacenter => 'hkg02', 
\t:name => 'cphrmky', 
\t:key_pairs => [ the_first_key, the_second_key ]
}
@sl.servers.create(opts)
# => <Fog::Compute::Softlayer::Server>
</ruby>

If you already have the list of internal IDs that SoftLayer assigns to each of your key pairs, you can pass an array of hashes instead of loading an object for each key pair you assign to a compute instance.

<ruby>
key_pair_ids = [
\t{:id => 12345},
\t{:id => 12346},
\t{:id => 12347},
]

opts = { 
\t:flavor_id => 'm1.small', 
\t:os_code => 'UBUNTU_LATEST', 
\t:datacenter => 'hkg02', 
\t:name => 'cphrmky', 
\t:key_pairs => key_pair_ids
}
@sl.servers.create(opts)
# => <Fog::Compute::Softlayer::Server>

</ruby>

Then, look at the key pairs on a server:

<ruby>
server = @sl.servers.get(12345)
server.key_pairs
# => [ <Fog::Compute::Softlayer::Server>,
# <Fog::Compute::Softlayer::Server>]
</ruby><br>


##### Try Before You Buy

One of the excellent features included in [fog-softlayer](http://github.com/softlayer/fog-softlayer) (and for all of the supported providers), is fantastic mocking.

Even if you don't have a SoftLayer account, you can download [fog-softlayer](https://github.com/softlayer/fog-softlayer) and start testing this code.

Just call `Fog.mock!` immediately after requiring the gem, run all of the above code examples, and see how easy it is to work with. We're working hard to get full coverage of Mock classes and methods. You may run across a MockNotImplemented exception here or there. If you do, the best course is probably to fork the repo, implement the mock, and open a pull request. 

\\- Matt

--

If you have questions about or problems with [fog-softlayer](http://rubygems.org/gems/fog-softlayer) open an [issue](https://github.com/softlayer/fog-softlayer/issues) or [email me](mailto:matt.eldridge@us.ibm.com?subject=fog-softlayer).


