---
title: "Extended Object Masks: a taste of things to come"
description: "<p>While my <a href=http://sldn.softlayer.com/blog/klandreth/Deglazing-slbackuppy-Usage-Object-Storage-Kitchen>culinar"
date: "2012-07-17"
author: "phil"
tags:
    - "blog"
---

<p>While my <a href="http://sldn.softlayer.com/blog/klandreth/Deglazing-slbackuppy-Usage-Object-Storage-Kitchen">culinary endeavors</a> have never been on par with Kevin's(he grills a mean steak), I wanted to take some time to provide this tasty morsel of the new Extended Object Masks which will soon be served in full portion for the feast.</p>
<p>As many users know, the SLAPI is able to provide you with an enormous amount of data about your environment. And as knowledge is power, having access to the SLAPI puts you at least on par with Aquaman. Sometimes however, knowledge sits heavy on the brow, especically when you require more information than current technologies can afford.</p>
<p>Take a look at this script which gathers information about the servers on your account:</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;">objectMask <span style="color: #66cc66;">=</span> <span style="color: black;">&#123;</span>
    <span style="color: #483d8b;">'hardware'</span>: <span style="color: black;">&#123;</span>
        <span style="color: #483d8b;">'frontendNetworkComponents'</span>: <span style="color: black;">&#123;</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>
        <span style="color: #483d8b;">'datacenter'</span>: <span style="color: black;">&#123;</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>
        <span style="color: #483d8b;">'billingItem'</span>: <span style="color: black;">&#123;</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>
    <span style="color: black;">&#125;</span>
<span style="color: black;">&#125;</span>
&nbsp;
&nbsp;
client.<span style="color: black;">set_object_mask</span><span style="color: black;">&#40;</span>objectMask<span style="color: black;">&#41;</span>
servers <span style="color: #66cc66;">=</span> client.<span style="color: black;">getHardware</span><span style="color: black;">&#40;</span><span style="color: black;">&#41;</span>
&nbsp;
<span style="color: #808080; font-style: italic;"># Display Format</span>
format <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">"Hostname: %s PrimaryIp: %s Location: %s Cost/Month: %s"</span>
missing <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">'n/a'</span>
&nbsp;
<span style="color: #ff7700;font-weight:bold;">for</span> server <span style="color: #ff7700;font-weight:bold;">in</span> servers:
    hostname <span style="color: #66cc66;">=</span> server.<span style="color: black;">get</span><span style="color: black;">&#40;</span><span style="color: #483d8b;">'hostname'</span><span style="color: #66cc66;">,</span> missing<span style="color: black;">&#41;</span>
    primaryIpAddress <span style="color: #66cc66;">=</span> server.<span style="color: black;">get</span><span style="color: black;">&#40;</span><span style="color: #483d8b;">'primaryIpAddress'</span><span style="color: #66cc66;">,</span> missing<span style="color: black;">&#41;</span>
    datacenter <span style="color: #66cc66;">=</span> server.<span style="color: black;">get</span><span style="color: black;">&#40;</span><span style="color: #483d8b;">'datacenter'</span><span style="color: #66cc66;">,</span> <span style="color: #008000;">dict</span><span style="color: black;">&#40;</span><span style="color: black;">&#41;</span><span style="color: black;">&#41;</span>.<span style="color: black;">get</span><span style="color: black;">&#40;</span><span style="color: #483d8b;">'name'</span><span style="color: #66cc66;">,</span> missing<span style="color: black;">&#41;</span>
    recurringFee <span style="color: #66cc66;">=</span> server.<span style="color: black;">get</span><span style="color: black;">&#40;</span><span style="color: #483d8b;">'billingItem'</span><span style="color: #66cc66;">,</span>
        <span style="color: #008000;">dict</span><span style="color: black;">&#40;</span><span style="color: black;">&#41;</span><span style="color: black;">&#41;</span>.<span style="color: black;">get</span><span style="color: black;">&#40;</span><span style="color: #483d8b;">'recurringFee'</span><span style="color: #66cc66;">,</span> missing<span style="color: black;">&#41;</span>
&nbsp;
    <span style="color: #ff7700;font-weight:bold;">print</span> format % <span style="color: black;">&#40;</span>hostname<span style="color: #66cc66;">,</span> primaryIpAddress<span style="color: #66cc66;">,</span> datacenter<span style="color: #66cc66;">,</span> recurringFee<span style="color: black;">&#41;</span></pre></div>
<p>This will yeild you a text similar to the below for each server on your account:<br />
<span class="geshifilter"><code class="text geshifilter-text">Hostname: kholland-ded-centos5 PrimaryIp: 108.168.150.122 Location: dal05 Cost/Month: 0 Ticket Review: n/a</code></span><br />
Now while the output is nice and neat...the return data from the API looks a little different:</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;"><span style="color: black;">&#123;</span>   <span style="color: #483d8b;">'accountId'</span>: <span style="color: #808080; font-style: italic;">##,</span>
    <span style="color: #483d8b;">'bareMetalInstanceFlag'</span>: <span style="color: #ff4500;">0</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'billingItem'</span>: <span style="color: black;">&#123;</span>   <span style="color: #483d8b;">'allowCancellationFlag'</span>: <span style="color: #ff4500;">1</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'cancellationDate'</span>: <span style="color: #483d8b;">''</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'categoryCode'</span>: <span style="color: #483d8b;">'server'</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'createDate'</span>: <span style="color: #483d8b;">'##'</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'cycleStartDate'</span>: <span style="color: #483d8b;">'##'</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'description'</span>: <span style="color: #483d8b;">'Superawesome server with amazing performance'</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'domainName'</span>: <span style="color: #483d8b;">'softlayer.com'</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'hostName'</span>: <span style="color: #483d8b;">'server'</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'id'</span>: <span style="color: #808080; font-style: italic;">##,</span>
                       <span style="color: #483d8b;">'laborFee'</span>: <span style="color: #483d8b;">'0'</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'laborFeeTaxRate'</span>: <span style="color: #483d8b;">'0'</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'lastBillDate'</span>: <span style="color: #483d8b;">'##'</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'modifyDate'</span>: <span style="color: #483d8b;">'##'</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'nextBillDate'</span>: <span style="color: #483d8b;">'##'</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'oneTimeFee'</span>: <span style="color: #483d8b;">'0'</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'oneTimeFeeTaxRate'</span>: <span style="color: #483d8b;">'0'</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'orderItemId'</span>: <span style="color: #808080; font-style: italic;">##,</span>
                       <span style="color: #483d8b;">'parentId'</span>: <span style="color: #483d8b;">''</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'recurringFee'</span>: <span style="color: #483d8b;">'0'</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'recurringFeeTaxRate'</span>: <span style="color: #483d8b;">'0'</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'recurringMonths'</span>: <span style="color: #ff4500;">1</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'resourceTableId'</span>: <span style="color: #808080; font-style: italic;">##,</span>
                       <span style="color: #483d8b;">'serviceProviderId'</span>: <span style="color: #ff4500;">1</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'setupFee'</span>: <span style="color: #483d8b;">'0'</span><span style="color: #66cc66;">,</span>
                       <span style="color: #483d8b;">'setupFeeTaxRate'</span>: <span style="color: #483d8b;">'0'</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'datacenter'</span>: <span style="color: black;">&#123;</span>   <span style="color: #483d8b;">'id'</span>: <span style="color: #ff4500;">138124</span><span style="color: #66cc66;">,</span> <span style="color: #483d8b;">'longName'</span>: <span style="color: #483d8b;">'Dallas 5'</span><span style="color: #66cc66;">,</span> <span style="color: #483d8b;">'name'</span>: <span style="color: #483d8b;">'dal05'</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'domain'</span>: <span style="color: #483d8b;">'softlayer.com'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'frontendNetworkComponents'</span>: <span style="color: black;">&#91;</span>   <span style="color: black;">&#123;</span>   <span style="color: #483d8b;">'hardwareId'</span>: <span style="color: #808080; font-style: italic;">##,</span>
                                         <span style="color: #483d8b;">'id'</span>: <span style="color: #808080; font-style: italic;">##,</span>
                                         <span style="color: #483d8b;">'macAddress'</span>: <span style="color: #483d8b;">'##'</span><span style="color: #66cc66;">,</span>
                                         <span style="color: #483d8b;">'maxSpeed'</span>: 4x10^<span style="color: #ff4500;">20</span><span style="color: #66cc66;">,</span>
                                         <span style="color: #483d8b;">'modifyDate'</span>: <span style="color: #483d8b;">'##'</span><span style="color: #66cc66;">,</span>
                                         <span style="color: #483d8b;">'name'</span>: <span style="color: #483d8b;">'eth'</span><span style="color: #66cc66;">,</span>
                                         <span style="color: #483d8b;">'networkVlanId'</span>: <span style="color: #483d8b;">''</span><span style="color: #66cc66;">,</span>
                                         <span style="color: #483d8b;">'port'</span>: <span style="color: #ff4500;">1</span><span style="color: #66cc66;">,</span>
                                         <span style="color: #483d8b;">'primaryIpAddress'</span>: <span style="color: #483d8b;">'1'</span><span style="color: #66cc66;">,</span>
                                         <span style="color: #483d8b;">'speed'</span>: <span style="color: #ff4500;">10</span><span style="color: #66cc66;">,</span>
                                         <span style="color: #483d8b;">'status'</span>: <span style="color: #483d8b;">'ACTIVE'</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>
                                     <span style="color: black;">&#123;</span>   <span style="color: #483d8b;">'hardwareId'</span>: <span style="color: #808080; font-style: italic;">##,</span>
                                         <span style="color: #483d8b;">'id'</span>: <span style="color: #808080; font-style: italic;">##,</span>
                                         <span style="color: #483d8b;">'macAddress'</span>: <span style="color: #483d8b;">'##'</span><span style="color: #66cc66;">,</span>
                                         <span style="color: #483d8b;">'maxSpeed'</span>: <span style="color: #ff4500;">0</span><span style="color: #66cc66;">,</span>
                                         <span style="color: #483d8b;">'modifyDate'</span>: <span style="color: #483d8b;">'##'</span><span style="color: #66cc66;">,</span>
                                         <span style="color: #483d8b;">'name'</span>: <span style="color: #483d8b;">'eth'</span><span style="color: #66cc66;">,</span>
                                         <span style="color: #483d8b;">'networkVlanId'</span>: <span style="color: #483d8b;">''</span><span style="color: #66cc66;">,</span>
                                         <span style="color: #483d8b;">'port'</span>: <span style="color: #ff4500;">3</span><span style="color: #66cc66;">,</span>
                                         <span style="color: #483d8b;">'speed'</span>: <span style="color: #ff4500;">0</span><span style="color: #66cc66;">,</span>
                                         <span style="color: #483d8b;">'status'</span>: <span style="color: #483d8b;">'DISABLED'</span><span style="color: black;">&#125;</span><span style="color: black;">&#93;</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'fullyQualifiedDomainName'</span>: <span style="color: #483d8b;">'server.softlayer.com'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'globalIdentifier'</span>: <span style="color: #483d8b;">'##'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'hardwareStatusId'</span>: <span style="color: #ff4500;">5</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'hostname'</span>: <span style="color: #483d8b;">'server'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'id'</span>: <span style="color: #808080; font-style: italic;">##,</span>
    <span style="color: #483d8b;">'manufacturerSerialNumber'</span>: <span style="color: #483d8b;">'##'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'networkManagementIpAddress'</span>: <span style="color: #483d8b;">'1'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'notes'</span>: <span style="color: #483d8b;">'testing notes'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'primaryBackendIpAddress'</span>: <span style="color: #483d8b;">'##'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'primaryIpAddress'</span>: <span style="color: #483d8b;">'##'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'privateIpAddress'</span>: <span style="color: #483d8b;">'##'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'serialNumber'</span>: <span style="color: #483d8b;">'##'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'serviceProviderId'</span>: <span style="color: #ff4500;">1</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'serviceProviderResourceId'</span>: <span style="color: #808080; font-style: italic;">##}</span></pre></div>
<p>I think we can all agree that this is one mighty fine looking piece of JSON however, the 5 data-points required for our use came with a lot of baggage. Not much of an inconvenience for a few servers, but when making this call on 10's or 100' of objects you run into the risk of the API returning an error due to the size of the return data being too large to handle.</p>
<p>You could fix this using <a href="/article/Result Limits">Result Limits</a> to paginate the servers. This works, but there is additional logic which needs to be developed and arguably a performance impact which must be mitigated.</p>
<p>Today's solution will use our new Extended Object Mask's ability to reduce the payload size by specifying an inclusive list of the properties you need...in similar fashion to our <a href="http://sldn.softlayer.com/article/rest#Using_Object_Masks_">REST API's Object Masks</a>.</p>
<p>Note - You will need to update your API client to the latest version found on our <a href="http://github.com/softlayer">GitHub</a> to use this new feature.</p>
<p>All we need to do is change the Object Mask</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;">mask <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">"""
mask[
    hostname,
    datacenter.name,
    primaryIpAddress,
    billingItem.recurringFee
]
"""</span></pre></div>
<p>The new object mask should be a string and contain a comma separated list enclosed by <span class="geshifilter"><code class="text geshifilter-text">mask[]</code></span>. You are able to specify properties inside of complex data types with a period, [complexType].[property].</p>
<p>The output of the script will remain the same but lets check out the return data from the api:</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;"><span style="color: black;">&#123;</span>   <span style="color: #483d8b;">'billingItem'</span>: <span style="color: black;">&#123;</span>   <span style="color: #483d8b;">'recurringFee'</span>: <span style="color: #483d8b;">'##'</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'datacenter'</span>: <span style="color: black;">&#123;</span>   <span style="color: #483d8b;">'name'</span>: <span style="color: #483d8b;">'dal05'</span><span style="color: black;">&#125;</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'hostname'</span>: <span style="color: #483d8b;">'server'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'primaryIpAddress'</span>: <span style="color: #483d8b;">'##'</span><span style="color: black;">&#125;</span></pre></div>
<p>The Extended Object Masks can be used with our REST, XML-RPC and SOAP endpoints and are currently available for use in a beta state. Please send us your feedback!</p>
<p>Keep an eye out in the coming weeks for more documentation on their use...</p>
<p>-Phil</p>

