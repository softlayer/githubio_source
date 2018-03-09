---
title: "Python Client 3.0 Released"
description: "<p>We’re pleased to announce the 3.0 release of the <a href=https://github.com/softlayer/softlayer-api-python-client/>"
date: "2013-09-25"
author: "beittenc"
tags:
    - "blog"
---

<p>We’re pleased to announce the 3.0 release of the <a href="https://github.com/softlayer/softlayer-api-python-client/">Python language bindings</a> for the SLAPI. With the 3.0 release, we’ve made a number of changes and introduced a collection of features we’re really excited to share with the community.</p>
<h3>License</h3>
<p>With our 3.0 release, the license used by the Python bindings has changed from the BSD 3-Clause to the <a href="https://github.com/softlayer/softlayer-api-python-client/blob/master/LICENSE">MIT license</a>. This allows users an even greater degree of freedom to use our bindings in whatever projects they need.</p>
<h3>Standardization and Organization</h3>
<p>We’ve made great strides to standardize naming conventions and styles, particularly with the command line interface. You should see more consistency between different parts of the CLI now and things should be easier to find. Things like renaming “sl hardware” to “sl server” and flattening the CCI actions cut down on the amount of time searching through the documentation and let you keep working on the important parts of your projects.</p>
<h3>Readthedocs.org Support</h3>
<p>We’re especially happy to announce that our documentation is now available at <a href="https://softlayer-api-python-client.readthedocs.org/">https://softlayer-api-python-client.readthedocs.org/</a> for our customers. Read the Docs hosts documentation on an excellent interface, making it easy for users to find documentation for all versions of Python language bindings, not just the latest one.</p>
<h2>New Features</h2>
<h3>Network Management</h3>
<p>The 3.0 release includes a new NetworkManager class as well as an “sl network” endpoint on the command line to allow you to manage your SoftLayer network resources. The bindings have support for managing VLANs, subnets, and global IPs as well as subnet ordering. We’ve also provided the ability to manage your RWhoIs entries directly. Not sure what’s hooked up to a particular IP address? Check out the “sl subnet lookup” command at the command line. Want to get a picture of your servers as a whole? You may find “sl summary” helpful.</p>
<h3>SSH Key Management</h3>
<p>One of the newer SoftLayer product offerings is SSH key management and we’ve added it to the Python bindings as well. You can now store your public keys within the SoftLayer API and have them automatically installed on newly provisioned *nix systems using either the SshKeyManager or the “sl sshkey” command line options. When ordering a new CCI or server at command line, specifying the -k flag installs the key(s) of your choice.</p>
<h3>Ordering Templates</h3>
<p>One of the biggest new features for command line ordering is the ability to store and order CCIs and servers from templates. If you have a configuration you commonly order, you can now store it in a simple template file and use the -t flag to import the template options. For CCIs, you can also use the --like argument to order a new CCI with the exact configuration of an existing CCI or the --export flag to export a CCI’s configuration to a template file for later use.</p>
<h3>Cloud Compute Instance (CCI) Improvements</h3>
<p>Our CCI support within the Python bindings was already great, but we still found a few ways to improve it.</p>
<p>On the command line, we’ve improved the “sl cci dns sync” command to give you even more control. If you host and manage DNS with us, this command gives you a one-line operation for updating the A and PTR records for any of your CCIs.</p>
<p>SoftLayer recently introduced the concept of a private network CCI, CCI, which works exactly like a standard CCI but does not have a network port that connects the device to the public Internet.  Private Network CCIs are a great solution for applications and backend systems that don’t require public network access and are easily provisioned using our command line interface.</p>
<h3>And There’s More</h3>
<p>Even with everything we’ve listed above, there’s still more to see and try. Take a moment to install the new version so you can give 3.0 a spin. If you’ve got a question, feel free to pop into <a href="irc://freenode.net/#softlayer">#softlayer on Freenode IRC</a> and chat with us. Find a bug or want to see a new feature in the Python bindings? Open an issue on <a href="https://github.com/softlayer/softlayer-api-python-client">Github</a> and let us know. We always love hearing about the cool things you’re doing with the bindings, so send us a tweet <a href="https://twitter.com/SoftLayerDevs">@SoftLayerDevs</a> or stop by the forums at https://forums.softlayer.com/.</p>
<p>-Nathan</p>

