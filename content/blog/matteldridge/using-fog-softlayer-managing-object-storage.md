---
title: "Using fog-softlayer for Managing Object Storage"
description: "In [part two](http://sldn.softlayer.com/blog/matteldridge/Using-fog-softlayer-Managing-Servers) of this series we explor"
date: "2014-07-18"
author: "matt.eldridge"
tags:
    - "blog"
---

In [part two](http://sldn.softlayer.com/blog/matteldridge/Using-fog-softlayer-Managing-Servers) of this series we explored using [fog-softlayer](https://github.com/softlayer/fog-softlayer) to leverage [fog](https://github.com/fog/fog), the cloud services library, for managing servers.

In this installment, we will cover several examples of using [fog-softlayer](https://github.com/softlayer/fog) to manage SoftLayer Object Storage.

#### Configure [fog-softlayer](https://github.com/softlayer/fog-softlayer) for your account.

These examples assume you have `~/.fog` which contains:

  <code>
   :softlayer_username: example-username
   :softlayer_api_key: 1a1a1a1a1a1a1a1a1a11a1a1a1a1a1a1a1a1a1 
   :softlayer_cluster: cluster # currently supported clusters are dal05, sng01, ams01
  </code>

#### Create a Connection to SoftLayer Object Storage

<ruby>
\trequire 'fog/softlayer'
\t@sl = Fog::Storage[:softlayer]
</ruby>


#### Models are Pretty

As mentioned in [part two](http://sldn.softlayer.com/blog/matteldridge/Using-fog-softlayer-Managing-Servers), fog has a fantastic object model for working with clouds to provision infrastructure. Your primary interface for working with fog should be the models. We will explore using [fog-softlayer](https://github.com/softlayer/fog-softlayer) to make requests directly in a future post.

Let's start at the beginning.

<code>1.</code> Create a directory/container.

  <ruby>
  \t@sl.directories.create(:key => 'a-container')
  </ruby>

Try creating a couple more with different names so that you have something to look at when you run the next few examples.

The next step explains how to look at the containers we have.

<code>2.</code> List directories/containers.

   <ruby>
    dirs = @sl.directories
    dirs.size # the number of directories      
   </ruby>
   
Getting a single container will include a summary of its contents.

<code>3.</code> Get a directory/container.

  <ruby>
  \tdir = @sl.directories.get('a-container')
  \tdir.key  # => 'a-container'
  </ruby>


Now, let's add some contents.

<code>4.</code> Create a new file/object.

  <ruby>
  \tdir = @sl.directories.get('a-container')
  \t# Pass a string.
  \tdir.files.create(:key => 'data.txt', :body => 'The quick brown fox jumps over the lazy dog.")
  \t# From a file.
  \tdir.files.create(:key => 'file-data.txt', :body => File.open('/path/to/file-data.txt')
  </ruby>

Now that we've done that, we can pull it back down ...


<code>5.</code> Get an existing file/object.

  <ruby>
  \tdir = @sl.directories.get('a-container')
  \tfile = dir.files.get('data.txt')
  \tfile.body # => 'The quick brown fox jumps over the lazy dog.'
  </ruby>

... or we can make a copy of it.


<code>6.</code> Copy a file/object.

  <ruby>
  \tfile  = @sl.directories.get('a-container').files.get('data.txt')
  \tcopy = file.copy('a-container', 'copy-of-data.txt')
  \tcopy.body # => 'The quick brown fox jumps over the lazy dog.'
  </ruby>

<code>7.</code> List the files in a directory/container.

  <ruby>
   @sl.directories.get('a-container').files
   # => [
   #    <Fog::Storage::Softlayer::File
   #  key="a-container/data.txt",
   #  content_length=43,
   #  content_type="text/plain",
   #  content_disposition=nil,
   #  etag="a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1",
   #  last_modified=1970-00-00 00:00:00 -0000,
   #  access_control_allow_origin=nil,
   #  origin=nil
   #  >
   # ...
  </ruby>

SoftLayer's object storage allows you to create signed URLs that expire when you want them to.

<code>8.</code> Get a signed [temporary] URL for a file/object.

   <ruby>
\t  file = @sl.directories.get('a-container').files.get('data.txt')
\t  file.url(Time.now + 300) # url expires in 5 minutes
  </ruby>
\t
Let's clean up these tests so they're not leaving behind clutter.

<code>9.</code> Delete files/objects from a directory/container.

  <ruby>
\tdir = @sl.directories('a-container')
\tdir.files.get('data.txt').destroy
\tdir.files.get('file-data.txt').destroy
\tdir.files.get('copy-of-data.txt').destroy
\t# Must destroy all files/objects before destroying container.
\tdir.destroy
  </ruby>
\t
#### Try Before You Buy

One of the excellent features included in [fog-softlayer](http://github.com/softlayer/fog-softlayer) (and for all supported providers) is fantastic mocking.

Even if you don't have a SoftLayer account, you can download [fog-softlayer](https://github.com/softlayer/fog-softlayer) and start testing this code.

Just call `Fog.mock!` immediately after requiring the gem, and you can run all of the above code examples and see how easy it is to work with.  We're working hard to get full coverage of Mock classes and methods. You may run across a MockNotImplemented exception here or there. If you do, probably the best course is to fork the repo, implement the mock, and open a pull request.

\\- Matt

--

If you have questions about or problems with [fog-softlayer](http://rubygems.org/gems/fog-softlayer) open an [issue](https://github.com/softlayer/fog-softlayer/issues) or [email me](mailto:matt.eldridge@us.ibm.com?subject=fog-softlayer).


