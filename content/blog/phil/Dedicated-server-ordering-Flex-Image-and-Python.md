---
title: "Dedicated server ordering with Flex Image and Python"
description: "<p>Automating server provisioning is not only fun, it can also save you the time and pain recovering from the carpal tun"
date: "2012-12-10"
author: "phil"
tags:
    - "blog"
---

<p>Automating server provisioning is not only fun, it can also save you the time and pain recovering from the carpal tunnel all of the clicking and typing ordering 100's of servers from the managment portal can cause. To save you from that fate I have put together this guide in hopes to help you explore the world of order automation with the SoftLayer API :)</p>
<p>We will assume that at some earlier point in time we have created a Flex Image. Each image is a point in time snapshot of your primary drive, complete with OS and software configurations which means less work once the server is online.</p>
<p>To create an dedicated server order using Flex Image we must define the following:<br />
*ID of the Flex Image template<br />
*Package ID<br />
*Location<br />
*Item prices(a list of items the new server will have: RAM, CPUs, storage, etc...)<br />
*List of "hardware"<br />
*Quantity of servers to order<br />
Let us start our journey into the depths of server ordering by grathering the template id of our Flex Image. However, as with most people we could not be bothered to remember the actual integer which defines our template; we simply remember the name we gave it.<br />
So off we are to search for the Flex Image's ID, armed with our trusty template name...</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;"><span style="color: #ff7700;font-weight:bold;">import</span> SoftLayer.<span style="color: black;">API</span>
<span style="color: #ff7700;font-weight:bold;">from</span> <span style="color: #dc143c;">pprint</span> <span style="color: #ff7700;font-weight:bold;">import</span> <span style="color: #dc143c;">pprint</span> <span style="color: #ff7700;font-weight:bold;">as</span> pp
apiUsername <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">''</span>
apiKey <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">''</span>
&nbsp;
&nbsp;
<span style="color: #ff7700;font-weight:bold;">def</span> getImageTemplateId<span style="color: black;">&#40;</span>templateName<span style="color: black;">&#41;</span>:
   client <span style="color: #66cc66;">=</span> SoftLayer.<span style="color: black;">API</span>.<span style="color: black;">Client</span><span style="color: black;">&#40;</span><span style="color: #483d8b;">'SoftLayer_Account'</span><span style="color: #66cc66;">,</span> <span style="color: #008000;">None</span><span style="color: #66cc66;">,</span> apiUsername<span style="color: #66cc66;">,</span> apiKey<span style="color: black;">&#41;</span>
   <span style="color: #808080; font-style: italic;"># Retrieve a list of all images</span>
   templates <span style="color: #66cc66;">=</span> client.<span style="color: black;">getBlockDeviceTemplateGroups</span><span style="color: black;">&#40;</span><span style="color: black;">&#41;</span>
   <span style="color: #808080; font-style: italic;"># Loop through each template and return the ID of our target template</span>
   <span style="color: #ff7700;font-weight:bold;">for</span> template <span style="color: #ff7700;font-weight:bold;">in</span> templates:
       <span style="color: #ff7700;font-weight:bold;">if</span> template<span style="color: black;">&#91;</span><span style="color: #483d8b;">'name'</span><span style="color: black;">&#93;</span> <span style="color: #66cc66;">==</span> templateName:
           <span style="color: #ff7700;font-weight:bold;">return</span> template<span style="color: black;">&#91;</span><span style="color: #483d8b;">'id'</span><span style="color: black;">&#93;</span>
&nbsp;
&nbsp;
pp<span style="color: black;">&#40;</span>getImageTemplateId<span style="color: black;">&#40;</span><span style="color: #483d8b;">'Image Name Here'</span><span style="color: black;">&#41;</span><span style="color: black;">&#41;</span></pre></div>
<p>We can put a checkmark next to imageTemplateId and for this example package ID and location will be a given(if you have trouble ascertaining what values to use here let me know).<br />
We will be using:</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;">   <span style="color: #483d8b;">'packageId'</span>: <span style="color: #ff4500;">23</span><span style="color: #66cc66;">,</span>  <span style="color: #808080; font-style: italic;"># Intel Xeon 3200 Series</span>
   <span style="color: #483d8b;">'location'</span>: <span style="color: #483d8b;">'SANJOSE'</span><span style="color: #66cc66;">,</span>  <span style="color: #808080; font-style: italic;"># San Jose 1</span></pre></div>
<p>Now for the fun one: item prices. The item prices can be a bit daunting to gather at first. Each package has a configuration which defines what type of items must be included in each order. It achieves this by grouping items in categories which can be listed as optional or required. To determine a list of options from categories which must include we will use this script:</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;"><span style="color: #ff7700;font-weight:bold;">import</span> SoftLayer.<span style="color: black;">API</span>
&nbsp;
apiUsername <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">''</span>
apiKey <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">''</span>
package <span style="color: #66cc66;">=</span> <span style="color: #ff4500;">23</span>
&nbsp;
client <span style="color: #66cc66;">=</span> SoftLayer.<span style="color: black;">API</span>.<span style="color: black;">Client</span><span style="color: black;">&#40;</span><span style="color: #483d8b;">'SoftLayer_Product_Package'</span><span style="color: #66cc66;">,</span> package<span style="color: #66cc66;">,</span> apiUsername<span style="color: #66cc66;">,</span> apiKey<span style="color: black;">&#41;</span>
<span style="color: #808080; font-style: italic;"># Only retrieve the bool to determine if this category is required and the category</span>
<span style="color: #808080; font-style: italic;"># name and ID</span>
categoryObjectMask <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">"mask[isRequired, itemCategory[id, name]]"</span>
client.<span style="color: black;">set_object_mask</span><span style="color: black;">&#40;</span>categoryObjectMask<span style="color: black;">&#41;</span>
&nbsp;
<span style="color: #808080; font-style: italic;"># Retrieve a list of category confgurations associated with our chosen package</span>
configurations <span style="color: #66cc66;">=</span> client.<span style="color: black;">getConfiguration</span><span style="color: black;">&#40;</span><span style="color: black;">&#41;</span>
&nbsp;
<span style="color: #808080; font-style: italic;"># For each price we only want the id, the ID of the category(ies) it is a memeber of,</span>
<span style="color: #808080; font-style: italic;"># and the item description</span>
pricesObjectMask <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">"mask[id;item.description;categories.id]"</span>
&nbsp;
client.<span style="color: black;">set_object_mask</span><span style="color: black;">&#40;</span>pricesObjectMask<span style="color: black;">&#41;</span>
&nbsp;
<span style="color: #808080; font-style: italic;"># Get all itemPrices for this package</span>
prices <span style="color: #66cc66;">=</span> client.<span style="color: black;">getItemPrices</span><span style="color: black;">&#40;</span><span style="color: black;">&#41;</span>
&nbsp;
<span style="color: #808080; font-style: italic;"># Text format for our prettified output</span>
headerFormat <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">'%s - %s:'</span>
priceFormat <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">'    %s -- %s'</span>
&nbsp;
<span style="color: #ff7700;font-weight:bold;">for</span> configuration <span style="color: #ff7700;font-weight:bold;">in</span> configurations:
   <span style="color: #808080; font-style: italic;"># We are only concerned with reuqired categories...</span>
   <span style="color: #808080; font-style: italic;"># skip it if we do not need it!</span>
   <span style="color: #ff7700;font-weight:bold;">if</span> <span style="color: black;">&#40;</span><span style="color: #ff7700;font-weight:bold;">not</span> configuration<span style="color: black;">&#91;</span><span style="color: #483d8b;">'isRequired'</span><span style="color: black;">&#93;</span><span style="color: black;">&#41;</span>:
       <span style="color: #ff7700;font-weight:bold;">continue</span>
   <span style="color: #ff7700;font-weight:bold;">print</span> headerFormat % <span style="color: black;">&#40;</span>configuration<span style="color: black;">&#91;</span><span style="color: #483d8b;">'itemCategory'</span><span style="color: black;">&#93;</span><span style="color: black;">&#91;</span><span style="color: #483d8b;">'name'</span><span style="color: black;">&#93;</span><span style="color: #66cc66;">,</span> \\
       configuration<span style="color: black;">&#91;</span><span style="color: #483d8b;">'itemCategory'</span><span style="color: black;">&#93;</span><span style="color: black;">&#91;</span><span style="color: #483d8b;">'id'</span><span style="color: black;">&#93;</span><span style="color: black;">&#41;</span>
   <span style="color: #ff7700;font-weight:bold;">for</span> price <span style="color: #ff7700;font-weight:bold;">in</span> prices:
       <span style="color: #ff7700;font-weight:bold;">if</span> <span style="color: black;">&#40;</span><span style="color: #483d8b;">'categories'</span> <span style="color: #ff7700;font-weight:bold;">not</span> <span style="color: #ff7700;font-weight:bold;">in</span> price<span style="color: black;">&#41;</span>:
           <span style="color: #ff7700;font-weight:bold;">continue</span>
       <span style="color: #ff7700;font-weight:bold;">if</span> <span style="color: #008000;">len</span><span style="color: black;">&#40;</span><span style="color: #008000;">filter</span><span style="color: black;">&#40;</span><span style="color: #ff7700;font-weight:bold;">lambda</span> x: x.<span style="color: black;">get</span><span style="color: black;">&#40;</span><span style="color: #483d8b;">'id'</span><span style="color: black;">&#41;</span> <span style="color: #66cc66;">==</span> \\
           configuration<span style="color: black;">&#91;</span><span style="color: #483d8b;">'itemCategory'</span><span style="color: black;">&#93;</span><span style="color: black;">&#91;</span><span style="color: #483d8b;">'id'</span><span style="color: black;">&#93;</span><span style="color: #66cc66;">,</span> price<span style="color: black;">&#91;</span><span style="color: #483d8b;">'categories'</span><span style="color: black;">&#93;</span><span style="color: black;">&#41;</span><span style="color: black;">&#41;</span>:
           <span style="color: #ff7700;font-weight:bold;">print</span> priceFormat % <span style="color: black;">&#40;</span>price<span style="color: black;">&#91;</span><span style="color: #483d8b;">'id'</span><span style="color: black;">&#93;</span><span style="color: #66cc66;">,</span> price<span style="color: black;">&#91;</span><span style="color: #483d8b;">'item'</span><span style="color: black;">&#93;</span><span style="color: black;">&#91;</span><span style="color: #483d8b;">'description'</span><span style="color: black;">&#93;</span><span style="color: black;">&#41;</span></pre></div>
<p>Now we can just choose an option from each of the categories listed to populate our itemPrices property.</p>
<p>This is the entire order script with the priceId options I chose:</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;"><span style="color: #ff7700;font-weight:bold;">import</span> SoftLayer.<span style="color: black;">API</span>
<span style="color: #ff7700;font-weight:bold;">from</span> <span style="color: #dc143c;">pprint</span> <span style="color: #ff7700;font-weight:bold;">import</span> <span style="color: #dc143c;">pprint</span> <span style="color: #ff7700;font-weight:bold;">as</span> pp
&nbsp;
apiUsername <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">'abcd'</span>
apiKey <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">'abcd1234'</span>
templateId <span style="color: #66cc66;">=</span> <span style="color: #ff4500;">1234</span>
&nbsp;
client <span style="color: #66cc66;">=</span> SoftLayer.<span style="color: black;">API</span>.<span style="color: black;">Client</span><span style="color: black;">&#40;</span><span style="color: #483d8b;">'SoftLayer_Product_Order'</span><span style="color: #66cc66;">,</span> <span style="color: #008000;">None</span><span style="color: #66cc66;">,</span> apiUsername<span style="color: #66cc66;">,</span> apiKey<span style="color: black;">&#41;</span>
&nbsp;
order <span style="color: #66cc66;">=</span> <span style="color: black;">&#123;</span>
&nbsp;
    <span style="color: #808080; font-style: italic;"># The API appreciates knowing what type of object we are sending...</span>
    <span style="color: #483d8b;">'complexType'</span>: <span style="color: #483d8b;">'SoftLayer_Container_Product_Order_Hardware_Server'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'quantity'</span>: <span style="color: #ff4500;">2</span><span style="color: #66cc66;">,</span>
    <span style="color: #808080; font-style: italic;"># An array of SoftLayer_Virtual_Guest objects with at minimum the</span>
    <span style="color: #808080; font-style: italic;"># ‘hostname’ and ‘domain’ properties defined. Provide SoftLayer_Hardware</span>
    <span style="color: #808080; font-style: italic;"># objects equal to the quanity defined above</span>
    <span style="color: #483d8b;">'hardware'</span>: <span style="color: black;">&#91;</span>
        <span style="color: black;">&#123;</span><span style="color: #483d8b;">'hostname'</span>: <span style="color: #483d8b;">'host1'</span><span style="color: #66cc66;">,</span> <span style="color: #483d8b;">'domain'</span>: <span style="color: #483d8b;">'example.com'</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>
        <span style="color: black;">&#123;</span><span style="color: #483d8b;">'hostname'</span>: <span style="color: #483d8b;">'host2'</span><span style="color: #66cc66;">,</span> <span style="color: #483d8b;">'domain'</span>: <span style="color: #483d8b;">'example.com'</span><span style="color: black;">&#125;</span>
    <span style="color: black;">&#93;</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'location'</span>: <span style="color: #483d8b;">'SANJOSE'</span><span style="color: #66cc66;">,</span>  <span style="color: #808080; font-style: italic;"># San Jose 1</span>
    <span style="color: #483d8b;">'packageId'</span>: <span style="color: #ff4500;">23</span><span style="color: #66cc66;">,</span>  <span style="color: #808080; font-style: italic;"># Intel Xeon 3200 Series</span>
    <span style="color: #483d8b;">'imageTemplateId'</span>: templateId<span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'prices'</span>: <span style="color: black;">&#91;</span>
        <span style="color: black;">&#123;</span><span style="color: #483d8b;">'id'</span>:  <span style="color: #ff4500;">1613</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>  <span style="color: #808080; font-style: italic;"># Server - Single Processor Quad Core Xeon 3230 - 2.60GHz  (Kentsfield) - 2 x 4MB cache</span>
        <span style="color: black;">&#123;</span><span style="color: #483d8b;">'id'</span>: <span style="color: #ff4500;">21001</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>  <span style="color: #808080; font-style: italic;"># Ram - 4 GB DDR2 667</span>
        <span style="color: black;">&#123;</span><span style="color: #483d8b;">'id'</span>:   <span style="color: #ff4500;">876</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>  <span style="color: #808080; font-style: italic;"># Disk Controller - Non-RAID</span>
        <span style="color: black;">&#123;</span><span style="color: #483d8b;">'id'</span>:  <span style="color: #ff4500;">1272</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>  <span style="color: #808080; font-style: italic;"># First Hard Drive - 73GB SA-SCSI 10K RPM</span>
        <span style="color: black;">&#123;</span><span style="color: #483d8b;">'id'</span>:   <span style="color: #ff4500;">131</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>  <span style="color: #808080; font-style: italic;"># Public Bandwidth - 10000 GB Bandwidth</span>
        <span style="color: black;">&#123;</span><span style="color: #483d8b;">'id'</span>:   <span style="color: #ff4500;">272</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>  <span style="color: #808080; font-style: italic;"># Uplink Port Speeds - 10 Mbps Public & Private Networks</span>
        <span style="color: black;">&#123;</span><span style="color: #483d8b;">'id'</span>:   <span style="color: #ff4500;">906</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>  <span style="color: #808080; font-style: italic;"># Remote Management - Reboot / KVM over IP</span>
        <span style="color: black;">&#123;</span><span style="color: #483d8b;">'id'</span>:    <span style="color: #ff4500;">21</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>  <span style="color: #808080; font-style: italic;"># Primary IP Addresses - 1 IP Address</span>
        <span style="color: black;">&#123;</span><span style="color: #483d8b;">'id'</span>:    <span style="color: #ff4500;">51</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>  <span style="color: #808080; font-style: italic;"># Lockbox - 1 GB Lockbox</span>
        <span style="color: black;">&#123;</span><span style="color: #483d8b;">'id'</span>:    <span style="color: #ff4500;">55</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>  <span style="color: #808080; font-style: italic;"># Monitoring - Host Ping</span>
        <span style="color: black;">&#123;</span><span style="color: #483d8b;">'id'</span>:    <span style="color: #ff4500;">57</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>  <span style="color: #808080; font-style: italic;"># Notification - Email and Ticket</span>
        <span style="color: black;">&#123;</span><span style="color: #483d8b;">'id'</span>:    <span style="color: #ff4500;">60</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>  <span style="color: #808080; font-style: italic;"># Response - 24x7x365 NOC Monitoring, Notification, and Response</span>
        <span style="color: black;">&#123;</span><span style="color: #483d8b;">'id'</span>:   <span style="color: #ff4500;">420</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>  <span style="color: #808080; font-style: italic;"># VPN Management - Private Network - Unlimited SSL VPN Users & 1 PPTP VPN User per account</span>
        <span style="color: black;">&#123;</span><span style="color: #483d8b;">'id'</span>:   <span style="color: #ff4500;">418</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>  <span style="color: #808080; font-style: italic;"># Vulnerability Assessments & Management - Nessus Vulnerability Assessment & Reporting</span>
    <span style="color: black;">&#93;</span>
<span style="color: black;">&#125;</span>
&nbsp;
result <span style="color: #66cc66;">=</span> client.<span style="color: black;">verifyOrder</span><span style="color: black;">&#40;</span>order<span style="color: black;">&#41;</span>
pp<span style="color: black;">&#40;</span>result<span style="color: black;">&#41;</span></pre></div>
<p>There is no particular need to have all of these scripts in this discrete format. In fact, they are most useful when combined together into a super-automation-script...but that task I leave to you. Hopefully this will help light your path on the way to no-hands server ordering!</p>
<p>-Phil<br />
<a href="https://gist.github.com/4067388">Get image template by name</a><br />
<a href="https://gist.github.com/4067364">Get required item prices for package listed by category</a><br />
<a href="https://gist.github.com/4226296">Place a Server with a Flex Image specified</a></p>

