---
title: "Do More with Less: A SoftLayer Knife for Chef"
description: "<p>We're excited to announce the initial release of the <a href=https://github.com/softlayer/knife-softlayer>knife-sof"
date: "2014-04-10"
author: "matt.eldridge"
tags:
    - "blog"
---

<p>We're excited to announce the initial release of the <a href="https://github.com/softlayer/knife-softlayer">knife-softlayer</a> Ruby gem.</p>
<p><a href="https://github.com/softlayer/knife-softlayer">Knife-softlayer</a> is a <a href="http://docs.opscode.com/community_plugin_knife.html">plugin</a> for the <a href="http://docs.opscode.com/knife.html">knife</a> utility used with <a href="http://docs.opscode.com/">Chef</a> that allows users to launch a <a href="http://www.softlayer.com/">SoftLayer</a> virtual server and <a href="http://docs.opscode.com/knife_bootstrap.html">bootstrap</a> it in a single command.  If you're new to Chef, here's <a href="http://sldn.softlayer.com/blog/waelriac/Introduction-Deploying-Drupal-SoftLayer-Chef-Part-1">a guide to get you started</a>.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">user@local> knife softlayer server create --hostname web --domain example.com --flavor medium</pre></div>
<p>This is a basic example using every available default, but it works.  It will launch a <a href="http://knowledgelayer.softlayer.com/topic/virtual-server-0">virtual server</a> and register it as a <a href="http://www.getchef.com/">Chef</a> node (though it won't have a run list).  The idea behind pushing your infrastructure into the cloud is that, ideally, you don't have to think about details that don't matter to you.  We've worked hard to get the number of options you're <em>required</em> to supply (decisions you need to make) as low as possible, while still giving you full control over every single detail if you need it.</p>
<p>Unlike some other clouds, we don't take away your choices; however, we don't force you to choose if you don't want to think about it.  We can't imagine why you would ever need a <a href="http://knowledgelayer.softlayer.com/topic/virtual-server-0">virtual server</a> with 16 CPU cores and only 1GB of memory. But if that's what you need, with <a href="http://www.softlayer.com/">SoftLayer</a>, you can do it.</p>
<p>This second example again launches an instance, this time specifying the number of cores, the NIC speed, the number and size of block devices, and also tells <a href="http://www.getchef.com/">Chef</a> to run a set of cookbooks on the instance.  The <a href="http://knowledgelayer.softlayer.com/topic/virtual-server-0">virtual server</a> is coming up with 1 core, 64GB of RAM, and 100GB of block device storage (disk space) on device 0.  We're also installing <a href="http://git-scm.com/">git</a> and <a href="http://redis.io/">redis</a> on it.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">user@local> knife softlayer server create -H some-host -D example.com \\
--network-interface-speed 1000 \\
--cores 1 \\
--ram 65536 \\
--block-storage 0:100 \\
--run-list 'recipe[git],recipe[redis]'</pre></div>
<p>The knife-softlayer plugin will take any options that the regular bootstrap command supports, we've also added some additional options to support launching a <a href="http://www.softlayer.com/">SoftLayer</a> virtual server.</p>
<h6>Must Haves</h6>
<ul>
<li><code>-H,--hostname</code> The hostname of the virtual server.</li>
<li><code>-D,--domain</code> The domain of the virtual server.</li>
</ul>
<h6>The Big Three</h6>
<ul>
<li><code>-C, --cores</code> will accept values from 1 - 16.</li>
<li><code>-R, --ram</code> will accept values [in MB] from the following list:
<ul>
<li><code>1024</code>,<code>2048</code>,<code>4096</code>,<code>6144</code>,<code>8192</code>,<code>12288</code>,<code>16384</code>,<code>32768</code>,<code>49152</code>,<code>65536</code></li>
</ul>
</li>
<li><code>-B, --block-storage</code> The size in GB of the block storage devices (disks) for this instance.
<ul>
<li>Specify 1 - 5 entries in a comma separated list following the format "dev:size".  Example: "0:25,2:500" would be a 25GB volume on device 0 and a 100GB volume on on device 2. [NOTE: SoftLayer virtual servers always reserve device 1 for a swap device.]  See <code>knife softlayer flavor list --all</code> for a list of available sizes.</li>
</ul>
</li>
</ul>
<p>Mix and match the above as you like!</p>
<h6>OR, Just One</h6>
<ul>
<li><code>-f, --flavor</code> Choose from a list of <code>tiny</code>, <code>small</code>, <code>medium</code>, <code>large</code>, <code>xlarge</code> and you can skip the three options above.  Alternatively, choose a flavor that gets two of these right, and override the one you want to change by specifying only that flag. </li>
</ul>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">user@local> knife softlayer server create --hostname web --domain example.com --flavor medium --cores 8</pre></div>
<p>Check out <code>knife softlayer flavor list</code> for details on what each of these flavors will give you.</p>
<h6>More Awesome Things</h6>
<ul>
<li><code>-n,--network-interface-speed</code> in MB.  See <code>knife softlayer flavor list --all</code> for available speeds.</li>
<li><code>-O,--os-code</code> Defaults to UBUNTU_LATEST.  See <code>knife softlayer flavor list --all</code> for available OS images.</li>
<li><code>--new-global-ip</code> Provision a new <a href="http://blog.softlayer.com/2012/global-ip-addresses-what-are-they-and-how-do-they-work">Global IP address</a> on your SoftLayer account and route it to the virtual server being created.</li>
<li><code>--assign-global-ip</code> Pass an existing Global IP address to this option to route it to the virtual server being created.</li>
<li><code>--single-tenant</code> Create a <a href="http://knowledgelayer.softlayer.com/topic/virtual-server-0">virtual server</a> that has a private node, which means a dedicated physical host (get rid of those noisy neighbors).</li>
<li><code>--san-storage</code> Don't bother with any local disks, use the SAN, instead of local storage, for the virtual servers instance storage.</li>
</ul>
<p>See <code>knife softlayer server create --help</code> for the full list of awesome things.</p>
<h6>A Whole Lot More</h6>
<p>Combining the power of Chef with the flexibility of the <a href="http://www.softlayer.com/">SoftLayer</a> API in a single utility brings a whole new level of fun to automating things in the <a href="http://www.softlayer.com/">SoftLayer</a> cloud.  Let us know what awesome things you're doing! We're on Twitter <a href="https://twitter.com/softlayer">@softlayer</a>.</p>
<p>-- Matt</p>
<p>If you have questions about or problems with <a href="https://github.com/softlayer/knife-softlayer">knife-softlayer</a> open an <a href="https://github.com/softlayer/knife-softlayer/issues">issue</a> or <a href="mailto:matt.eldridge@us.ibm.com?subject=knife-softlayer">email me</a></p>

