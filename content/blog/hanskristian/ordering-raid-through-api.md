---
title: "Ordering RAID Through API"
description: "<p>As a SoftLayer user, you have probably seen the beautiful RAID Configurator that greets you when you order a server o"
date: "2014-04-22"
author: "hansKristian"
tags:
    - "blog"
---

<p>As a SoftLayer user, you have probably seen the beautiful RAID Configurator that greets you when you order a server on the SoftLayer website.</p>
<p>It allows you to do anything you like, from a straight RAID configuration involving all drives in a single disk array, to a much more intricate configuration with nearly any mix of disks and RAID types.</p>
<p>However beautiful and practical the interface, sometimes you want to script this process, and the SoftLayer mantra of "Anything you can do in the Web interface, you can do on the API" also rings true in this case.</p>
<h3>Single RAID group</h3>
<p>If all your drives are the same and you simply want a single RAID group, be it RAID 0,1,5 or 10, you can achieve this by ordering the corresponding disk controller.</p>
<p>When building your order template you will see that RAID-enabled servers are listed with multiple disk controllers. Here's an example of the relevant price IDs from package 53 (Intel Xeon 3200 Series):</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">Category "Disk Controller":
     876 -- Non-RAID
     877 -- RAID 0
     878 -- RAID 1
     879 -- RAID 5
     880 -- RAID 10
     22482 -- RAID</pre></div>
<p>So ordering an Intel 3260 server with RAID 10 through the API could look like this:</p>
<div class="geshifilter">
<pre class="ruby geshifilter-ruby" style="font-family:monospace;"><span style="color:#CC0066; font-weight:bold;">require</span> <span style="color:#996600;">'rubygems'</span>
<span style="color:#CC0066; font-weight:bold;">require</span> <span style="color:#996600;">'softlayer_api'</span>
&nbsp;
<span style="color:#ff6633; font-weight:bold;">$SL_API_USERNAME</span> = <span style="color:#996600;">" PLEASE SET ME "</span>
<span style="color:#ff6633; font-weight:bold;">$SL_API_KEY</span> = <span style="color:#996600;">" PLEASE SET ME TOO "</span>
&nbsp;
client = <span style="color:#6666ff; font-weight:bold;">SoftLayer::Service</span>.<span style="color:#9900CC;">new</span><span style="color:#006600; font-weight:bold;">&#40;</span><span style="color:#996600;">"SoftLayer_Product_Order"</span><span style="color:#006600; font-weight:bold;">&#41;</span>;
&nbsp;
order = <span style="color:#006600; font-weight:bold;">&#123;</span>
 <span style="color:#ff3333; font-weight:bold;">:complexType</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#996600;">'SoftLayer_Container_Product_Order_Hardware_Server'</span>,
 <span style="color:#ff3333; font-weight:bold;">:quantity</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">1</span>,
 <span style="color:#ff3333; font-weight:bold;">:hardware</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006600; font-weight:bold;">&#91;</span><span style="color:#006600; font-weight:bold;">&#123;</span>:hostname <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#996600;">'raidtest'</span>, <span style="color:#ff3333; font-weight:bold;">:domain</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#996600;">'example.com'</span><span style="color:#006600; font-weight:bold;">&#125;</span><span style="color:#006600; font-weight:bold;">&#93;</span>,
 <span style="color:#ff3333; font-weight:bold;">:location</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">168642</span>, <span style="color:#008000; font-style:italic;"># San Jose 1</span>
 <span style="color:#ff3333; font-weight:bold;">:packageId</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">53</span>, <span style="color:#008000; font-style:italic;"># Intel Xeon 3200 Series</span>
 <span style="color:#ff3333; font-weight:bold;">:prices</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006600; font-weight:bold;">&#91;</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">2050</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Single Processor Quad Core Xeon 3460 - 2.80GHz (Lynnfield) - 1 x 8MB cache w/HT</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">17438</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># -- Ubuntu Linux 12.04.0 LTS Precise Pangolin - Minimal Install (64 bit)</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">21004</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># 4 GB DDR3 Registered 1333</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">880</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Disk controller -- RAID 10 </span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">1257</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># First hard drive -- 147GB SA-SCSI 10K RPM</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">1256</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Second hard drive -- 147GB SA-SCSI 10K RPM</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">825</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Third hard drive -- 147GB SA-SCSI 10K RPM</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">825</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Fourth hard drive -- 147GB SA-SCSI 10K RPM</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">728</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># 0 GB Bandwidth</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">898</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># 100 Mbps Private Network</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">906</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Reboot / KVM over IP  </span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">420</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Unlimited SSL VPN Users & 1 PPTP VPN User per account</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">55</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Host Ping</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">418</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Nessus Vulnerability Assessment & Reporting</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">57</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Notification -- Email and Ticket</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">58</span><span style="color:#006600; font-weight:bold;">&#125;</span> <span style="color:#008000; font-style:italic;"># Response -- Automated Notification</span>
 <span style="color:#006600; font-weight:bold;">&#93;</span>
<span style="color:#006600; font-weight:bold;">&#125;</span>
&nbsp;
result = client.<span style="color:#9900CC;">verifyOrder</span><span style="color:#006600; font-weight:bold;">&#40;</span>order<span style="color:#006600; font-weight:bold;">&#41;</span>
<span style="color:#008000; font-style:italic;">## Uncomment when you are ready to order</span>
<span style="color:#008000; font-style:italic;"># client.placeOrder(order)</span></pre></div>
<h3>Multiple RAID groups</h3>
<p>When ordering multiple RAID groups you need to order the Disk Controller type called <code>RAID</code>, and specify your RAID groups in an attribute in the order template called <code>storageGroups</code>.<br />
storageGroups is of the type <a href="/reference/datatypes/SoftLayer_Container_Product_Order_Storage_Group/">SoftLayer_Container_Product_Order_Storage_Group</a> and the most important attributes can be explained as:</p>
<blockquote><p><strong>arrayTypeId</strong>: Integer - Required<br />
  Can be retrieved from <a href="/reference/services/SoftLayer_Configuration_Storage_Group_Array_Type/getAllObjects">SoftLayer_Configuration_Storage_Group_Array_Type::getAllObjects</a></p>
<p><strong>hardDrives</strong>: Array of integers - Required<br />
  Array of drives to take part in the given raid array. 0 = first drive, 1 = second drive, etc</p>
<p><strong>hotSpareDrives</strong>: array of integers - Optional<br />
  On raid types where hot spare is allowed, you can specify which drives to use as hot spare.<br />
  Raid types that allow hot spare can be retrieved from <em><a href="/reference/services/SoftLayer_Configuration_Storage_Group_Array_Type/getAllObjects">SoftLayer_Configuration_Storage_Group_Array_Type::getAllObjects</a></em></p>
<p><strong>partitionTemplateId</strong>: integer - Optional<br />
  To be used on the array where the operating system is to be installed.<br />
  Partition Template IDs for the relevant operating system can be retrieved from<br />
  <em><a href="/reference/services/SoftLayer_Hardware_Component_Partition_OperatingSystem/getPartitionTemplates">SoftLayer_Hardware_Component_Partition_OperatingSystem::getPartitionTemplates</a></em><br />
  use <em><a href="/reference/services/SoftLayer_Hardware_Component_Partition_OperatingSystem/getAllObjects">SoftLayer_Hardware_Component_Partition_OperatingSystem::getAllObjects</a></em> to get a list of operating system groups that has partition templates</p>
</blockquote>
<p>Let's say, for example, you want to have a server with a single SSD drive for the operating system, also hosting a large 12GB swap partition, and a separate RAID array with 3 striped 147GB SAS Drives.</p>
<p>The first thing we'll need to do is specify the controller and drives we want in our order template.</p>
<div class="geshifilter">
<pre class="ruby geshifilter-ruby" style="font-family:monospace;"><span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">22482</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Disk controller -- RAID</span>
<span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">13756</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># First hard drive -- 50GB SSD</span>
<span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">1256</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Second hard drive -- 147GB SA-SCSI 10K RPM</span>
<span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">825</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Third hard drive -- 147GB SA-SCSI 10K RPM</span>
<span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">825</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Fourth hard drive -- 147GB SA-SCSI 10K RPM</span></pre></div>
<p>To configure the RAID groups we need to populate <code>storageGroups</code><br />
The disks will be addressed in the order of their placement and template, starting at disk 0.<br />
So for the first disk that we want to be on its own we will use <code>arrayTypeId</code> 9, which is JBOD, and specify <code>partitionTemplateId</code> 226 which specifies a 12GB Swap partition</p>
<div class="geshifilter">
<pre class="ruby geshifilter-ruby" style="font-family:monospace;"><span style="color:#006600; font-weight:bold;">&#123;</span>
        <span style="color:#ff3333; font-weight:bold;">:arrayTypeId</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">9</span>, <span style="color:#008000; font-style:italic;"># JBOD -- Other types available from SoftLayer_Configuration_Storage_Group_Array_Type::getAllObjects</span>
        <span style="color:#ff3333; font-weight:bold;">:hardDrives</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006600; font-weight:bold;">&#91;</span><span style="color:#006666;">0</span><span style="color:#006600; font-weight:bold;">&#93;</span>, <span style="color:#008000; font-style:italic;"># First Hard Drive (50GB SSD)</span>
        <span style="color:#ff3333; font-weight:bold;">:partitionTemplateId</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">226</span> <span style="color:#008000; font-style:italic;"># Custom partition template - 12GB Swap</span>
<span style="color:#006600; font-weight:bold;">&#125;</span>,</pre></div>
<p>For the second group we specify <code>arrayTypeId</code> 1, which is RAID 0 - Striped</p>
<div class="geshifilter">
<pre class="ruby geshifilter-ruby" style="font-family:monospace;"><span style="color:#006600; font-weight:bold;">&#123;</span>
        <span style="color:#ff3333; font-weight:bold;">:arrayTypeId</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">1</span>, <span style="color:#008000; font-style:italic;"># RAID 0 -- Other types available from SoftLayer_Configuration_Storage_Group_Array_Type::getAllObjects</span>
        <span style="color:#ff3333; font-weight:bold;">:hardDrives</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006600; font-weight:bold;">&#91;</span><span style="color:#006666;">1</span>,<span style="color:#006666;">2</span>,<span style="color:#006666;">3</span><span style="color:#006600; font-weight:bold;">&#93;</span> <span style="color:#008000; font-style:italic;"># Second, third and fourth hard drives (147GB SAS)</span>
<span style="color:#006600; font-weight:bold;">&#125;</span></pre></div>
<p>All together, the order will look like this:</p>
<div class="geshifilter">
<pre class="ruby geshifilter-ruby" style="font-family:monospace;"><span style="color:#CC0066; font-weight:bold;">require</span> <span style="color:#996600;">'rubygems'</span>
<span style="color:#CC0066; font-weight:bold;">require</span> <span style="color:#996600;">'softlayer_api'</span>
&nbsp;
<span style="color:#ff6633; font-weight:bold;">$SL_API_USERNAME</span> = <span style="color:#996600;">" PLEASE SET ME "</span>
<span style="color:#ff6633; font-weight:bold;">$SL_API_KEY</span> = <span style="color:#996600;">" PLEASE SET ME TOO "</span>
&nbsp;
client = <span style="color:#6666ff; font-weight:bold;">SoftLayer::Service</span>.<span style="color:#9900CC;">new</span><span style="color:#006600; font-weight:bold;">&#40;</span><span style="color:#996600;">"SoftLayer_Product_Order"</span><span style="color:#006600; font-weight:bold;">&#41;</span>;
&nbsp;
order = <span style="color:#006600; font-weight:bold;">&#123;</span>
 <span style="color:#ff3333; font-weight:bold;">:complexType</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#996600;">'SoftLayer_Container_Product_Order_Hardware_Server'</span>,
 <span style="color:#ff3333; font-weight:bold;">:quantity</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">1</span>,
 <span style="color:#ff3333; font-weight:bold;">:hardware</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006600; font-weight:bold;">&#91;</span><span style="color:#006600; font-weight:bold;">&#123;</span>:hostname <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#996600;">'raidtest'</span>, <span style="color:#ff3333; font-weight:bold;">:domain</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#996600;">'example.com'</span><span style="color:#006600; font-weight:bold;">&#125;</span><span style="color:#006600; font-weight:bold;">&#93;</span>,
 <span style="color:#ff3333; font-weight:bold;">:location</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">168642</span>, <span style="color:#008000; font-style:italic;"># San Jose 1</span>
 <span style="color:#ff3333; font-weight:bold;">:packageId</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">53</span>, <span style="color:#008000; font-style:italic;"># Intel Xeon 3200 Series</span>
 <span style="color:#ff3333; font-weight:bold;">:prices</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006600; font-weight:bold;">&#91;</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">2050</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Single Processor Quad Core Xeon 3460 - 2.80GHz (Lynnfield) - 1 x 8MB cache w/HT</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">17438</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># -- Ubuntu Linux 12.04.0 LTS Precise Pangolin - Minimal Install (64 bit)</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">21004</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># 4 GB DDR3 Registered 1333</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">22482</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Disk controller -- RAID</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">13756</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># First hard drive -- 50GB SSD</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">1256</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Second hard drive -- 147GB SA-SCSI 10K RPM</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">825</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Third hard drive -- 147GB SA-SCSI 10K RPM</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">825</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Fourth hard drive -- 147GB SA-SCSI 10K RPM</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">728</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># 0 GB Bandwidth</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">898</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># 100 Mbps Private Network</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">906</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Reboot / KVM over IP  </span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">420</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Unlimited SSL VPN Users & 1 PPTP VPN User per account</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">55</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Host Ping</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">418</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Nessus Vulnerability Assessment & Reporting</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">57</span><span style="color:#006600; font-weight:bold;">&#125;</span>, <span style="color:#008000; font-style:italic;"># Notification -- Email and Ticket</span>
  <span style="color:#006600; font-weight:bold;">&#123;</span>:id <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">58</span><span style="color:#006600; font-weight:bold;">&#125;</span> <span style="color:#008000; font-style:italic;"># Response -- Automated Notification</span>
 <span style="color:#006600; font-weight:bold;">&#93;</span>,
&nbsp;
 <span style="color:#ff3333; font-weight:bold;">:storageGroups</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006600; font-weight:bold;">&#91;</span>
     <span style="color:#006600; font-weight:bold;">&#123;</span> <span style="color:#008000; font-style:italic;"># RAID Array 1</span>
        <span style="color:#ff3333; font-weight:bold;">:arrayTypeId</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">9</span>, <span style="color:#008000; font-style:italic;"># JBOD</span>
        <span style="color:#ff3333; font-weight:bold;">:hardDrives</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006600; font-weight:bold;">&#91;</span><span style="color:#006666;">0</span><span style="color:#006600; font-weight:bold;">&#93;</span>, <span style="color:#008000; font-style:italic;"># First Hard Drive (50GB SSD)</span>
        <span style="color:#ff3333; font-weight:bold;">:partitionTemplateId</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">226</span> <span style="color:#008000; font-style:italic;"># Custom partition template - 12GB Swap</span>
     <span style="color:#006600; font-weight:bold;">&#125;</span>,
     <span style="color:#006600; font-weight:bold;">&#123;</span> <span style="color:#008000; font-style:italic;"># RAID Array 2</span>
        <span style="color:#ff3333; font-weight:bold;">:arrayTypeId</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006666;">1</span>, <span style="color:#008000; font-style:italic;"># RAID 0</span>
        <span style="color:#ff3333; font-weight:bold;">:hardDrives</span> <span style="color:#006600; font-weight:bold;">=></span> <span style="color:#006600; font-weight:bold;">&#91;</span><span style="color:#006666;">1</span>,<span style="color:#006666;">2</span>,<span style="color:#006666;">3</span><span style="color:#006600; font-weight:bold;">&#93;</span> <span style="color:#008000; font-style:italic;"># Second, third and fourth hard drives (147GB SAS)</span>
     <span style="color:#006600; font-weight:bold;">&#125;</span>
  <span style="color:#006600; font-weight:bold;">&#93;</span>
<span style="color:#006600; font-weight:bold;">&#125;</span>
&nbsp;
&nbsp;
result = client.<span style="color:#9900CC;">verifyOrder</span><span style="color:#006600; font-weight:bold;">&#40;</span>order<span style="color:#006600; font-weight:bold;">&#41;</span>
<span style="color:#008000; font-style:italic;">## Uncomment when you're ready to order</span>
<span style="color:#008000; font-style:italic;"># client.placeOrder(order)</span></pre></div>
<h3>Links and other useful information</h3>
<ul>
<li><a href="https://gist.github.com/hassenius/10728414">order_multiple_raid_groups.rb</a></li>
<li><a href="https://gist.github.com/hassenius/10728568">order_single_raid_group.rb</a></li>
<li><a href="https://gist.github.com/hassenius/10421344">get_package_options.rb (command line tool)</a></li>
</ul>
<p>//hansKristian</p>

