---
title: "Using fog-softlayer for Managing DNS"
description: "This is Part 4 of a series, so to get the most out of it you may want to [start at the beginning](http://sldn.softlayer."
date: "2014-07-25"
author: "matt.eldridge"
tags:
    - "blog"
---

This is Part 4 of a series, so to get the most out of it you may want to [start at the beginning](http://sldn.softlayer.com/blog/matteldridge/Fog-Gem-Support-SoftLayer). This post explores using [fog-softlayer](https://github.com/softlayer/fog-softlayer) to manage your SoftLayer DNS.  

First however, to give credit where it's due, a thank you goes out to [@fernandes](https://github.com/fernandes). He sent in the initial pull request that adds this DNS support.


##### Configure 

These examples all assume you have `~/.fog`, which contains the following.

   <code>
   :softlayer_username: example-username
   :softlayer_api_key: 1a1a1a1a1a1a1a1a1a11a1a1a1a1a1a1a1a1a1
  </code>

Connect to SoftLayer DNS Service.

<ruby>
\trequire 'fog/softlayer'
    @sl = Fog::DNS[:softlayer]
</ruby>

##### Create 

As mentioned in previous installments of this series, the fog object model is highly refined and makes working with clouds to provision an infrastructure simple and intuitive.

The first thing we need to do is create a domain.

  <ruby>
  \t@domain = @sl.domains.create('example.com')
  </ruby>

With a domain registered on our SoftLayer account, we can now create one or more records.


   <ruby>
    opts = {
    \t'value' => '127.0.0.1',
    \t'host' => '@',
    \t'type' => 'a',
    }
    @domain.create_record(opts)
   </ruby>
   
##### Read

We can list all domains on the account.

  <ruby>
\t@domains = @sl.domains.all
  \t@domain = @domains.first
  </ruby>

If we know the ID of a domain, we can get the domain by ID.

  <ruby>
\t@domains = @sl.domains.get(123456)
  </ruby>

Of course, the reason for DNS is that names are easier for people to remember than numbers.


  <ruby>
\t@domain = @sl.domains.get_by_name('example.com')
  </ruby>

##### Update

Our last record for this domain needs to point to a new IP.

  <ruby>
  \trecord = @domain.records.last
  \trecord.value = '33.33.33.33' # set the new value only on the local object
  \trecord.save # POST the changes back to the SoftLayer API.
  </ruby>

##### Destroy

Destroy a domain.

  <ruby>
    @domain = @sl.domains.get(123456)
    @domain.destroy
  </ruby>

Destroy a record.

  <ruby>
\trecord = @domain.records.last
\trecord.destroy
  </ruby>
\t
##### Mock

I've mentioned it before, but it bears repeating: Fog has excellent mocking not just for testing, but also for working through a proof on concept.

Even if you don't have a SoftLayer account, you can download [fog-softlayer](https://github.com/softlayer/fog-softlayer) and start testing this code.

Simply by calling `Fog.mock!` immediately after requiring the gem you can run all of the above code examples and see how easy it is to work with. We're working hard to get full mock coverage of all classes and methods. You may run across a MockNotImplemented exception here or there. If you do, the best course is probably to fork the repo, implement the mock, and open a pull request. 

\\- Matt

--

If you have questions about or problems with [fog-softlayer](http://rubygems.org/gems/fog-softlayer), open an [issue](https://github.com/softlayer/fog-softlayer/issues) or [email me](mailto:matt.eldridge@us.ibm.com?subject=fog-softlayer).


