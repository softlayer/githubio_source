---
title: "Command Line Simplicity"
description: "<p>Sometimes when putting together a script for the API I find myself wanting to remove as much complication from the pr"
date: "2012-02-24"
author: "phil"
tags:
    - "blog"
---

<p>Sometimes when putting together a script for the API I find myself wanting to remove as much complication from the process as possible.  Maybe in need of troubleshooting simplicity to rule out the plethora of idiosyncrasies which may be causing an API call to fail, or possibly just the need to walk my way through an idea and worry about the logic later.</p>
<p>I’m sure we all have our own process to filter out all of the complications the technologies we use may cause; for me in the case of the SLAPI I fall back to a <a href="http://www.gnu.org/software/bash/">Bash shell</a>, <a href="http://curl.haxx.se/">curl</a> and our <a href="/article/REST">REST</a> endpoint.  This trio allows me to make calls to the API without having to be concerned with remembering to define my array outside of a loop.</p>
<h3>Get a list of CCIs and their primary IP addresses</h3>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">curl "https://[apiUser]:[apiKey]@api.softlayer.com/rest/v3/SoftLayer_Account/VirtualGuests.xml?objectMask=virtualGuests.id;virtualGuests.primaryIpAddress"</pre></div>
<h3>Create a CNAME record</h3>
<p>First we need to create our POST data which will contain one element named “parameters”  which contains our <a href="/article/SoftLayer_Dns_Domain_ResourceRecord templateObject (type)">SoftLayer_Dns_Domain_ResourceRecord templateObject (type)</a>.</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;"><span style="color: black;">&#123;</span>
    <span style="color: #483d8b;">"parameters"</span> : <span style="color: black;">&#91;</span>
        <span style="color: black;">&#123;</span>
            <span style="color: #483d8b;">"data"</span>: <span style="color: #483d8b;">"www.example.com."</span><span style="color: #66cc66;">,</span>
            <span style="color: #483d8b;">"domainId"</span>: <span style="color: #ff4500;">1117134</span><span style="color: #66cc66;">,</span>
            <span style="color: #483d8b;">"host"</span>: <span style="color: #483d8b;">"atest.example.com"</span><span style="color: #66cc66;">,</span>
            <span style="color: #483d8b;">"ttl"</span>: <span style="color: #ff4500;">86400</span><span style="color: #66cc66;">,</span>
            <span style="color: #483d8b;">"type"</span>: <span style="color: #483d8b;">"cname"</span>
&nbsp;
    <span style="color: black;">&#93;</span>
<span style="color: black;">&#125;</span></pre></div>
<p>I have used -d to specify this request as POST and @cname.json to tell curl to look in file cname.json for the data</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">curl -d @cname.json https://[apiUser]:[apiKey]@api.softlayer.com/rest/v3/SoftLayer_Dns_Domain_ResourceRecord.json</pre></div>
<h3>Data Formats</h3>
<p>The SoftLayer API will provide responses in XML or JSON however the ease of viewing from your Bash prompt will vary.  In general XML will display in an nice easy to read format, while JSON likes to live all on one line.  A nifty trick from fellow SLDN blogger Scott T is to pipe your JSON response into python -mjson.tool or tidy-xml should you find your XML unwieldy.</p>
<p>Our next example we will be requesting JSON response data. We have used a resultLimit too keep the number of responses manageable. </p>
<h4>Raw JSON</h4>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">curl "https://[apiUser]:[apiKey]@api.softlayer.com/rest/v3/SoftLayer_Product_Package/46/getItems.json?resultLimit=1"</pre></div>
<p>Output:</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;"><span style="color: black;">&#123;</span><span style="color: #483d8b;">"capacity"</span>:<span style="color: #483d8b;">"250"</span><span style="color: #66cc66;">,</span><span style="color: #483d8b;">"description"</span>:<span style="color: #483d8b;">"250 GB (LOCAL)"</span><span style="color: #66cc66;">,</span><span style="color: #483d8b;">"id"</span>:<span style="color: #ff4500;">3916</span><span style="color: #66cc66;">,</span><span style="color: #483d8b;">"softwareDescriptionId"</span>:null<span style="color: #66cc66;">,</span><span style="color: #483d8b;">"units"</span>:<span style="color: #483d8b;">"GB"</span><span style="color: #66cc66;">,</span><span style="color: #483d8b;">"upgradeItemId"</span>:null<span style="color: #66cc66;">,</span><span style="color: #483d8b;">"prices"</span>:<span style="color: black;">&#91;</span><span style="color: black;">&#123;</span><span style="color: #483d8b;">"currentPriceFlag"</span>:null<span style="color: #66cc66;">,</span><span style="color: #483d8b;">"hourlyRecurringFee"</span>:<span style="color: #483d8b;">".02"</span><span style="color: #66cc66;">,</span><span style="color: #483d8b;">"id"</span>:<span style="color: #ff4500;">13958</span><span style="color: #66cc66;">,</span><span style="color: #483d8b;">"itemId"</span>:<span style="color: #ff4500;">3916</span><span style="color: #66cc66;">,</span><span style="color: #483d8b;">"laborFee"</span>:<span style="color: #483d8b;">"0"</span><span style="color: #66cc66;">,</span><span style="color: #483d8b;">"onSaleFlag"</span>:null<span style="color: #66cc66;">,</span><span style="color: #483d8b;">"oneTimeFee"</span>:<span style="color: #483d8b;">"0"</span><span style="color: #66cc66;">,</span><span style="color: #483d8b;">"recurringFee"</span>:<span style="color: #483d8b;">"14"</span><span style="color: #66cc66;">,</span><span style="color: #483d8b;">"setupFee"</span>:<span style="color: #483d8b;">"0"</span><span style="color: #66cc66;">,</span><span style="color: #483d8b;">"sort"</span>:<span style="color: #ff4500;">0</span><span style="color: #66cc66;">,</span><span style="color: #483d8b;">"accountRestrictions"</span>:<span style="color: black;">&#91;</span><span style="color: black;">&#123;</span><span style="color: #483d8b;">"accountId"</span>:<span style="color: #ff4500;">34455</span><span style="color: #66cc66;">,</span><span style="color: #483d8b;">"id"</span>:<span style="color: #ff4500;">3089</span><span style="color: #66cc66;">,</span><span style="color: #483d8b;">"itemPriceId"</span>:<span style="color: #ff4500;">13958</span><span style="color: black;">&#125;</span><span style="color: black;">&#93;</span><span style="color: black;">&#125;</span><span style="color: black;">&#93;</span><span style="color: black;">&#125;</span></pre></div>
<h4>Data Formatting Magic</h4>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">curl "https://[apiUser]:[apiKey]@api.softlayer.com/rest/v3/SoftLayer_Product_Package/46/getItems.json?resultLimit=1" | python -mjson.tool</pre></div>
<p>Output:</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;"><span style="color: black;">&#123;</span>
    <span style="color: #483d8b;">"capacity"</span>: <span style="color: #483d8b;">"40"</span><span style="color: #66cc66;">,</span> 
    <span style="color: #483d8b;">"description"</span>: <span style="color: #483d8b;">"40 GB NAS"</span><span style="color: #66cc66;">,</span> 
    <span style="color: #483d8b;">"id"</span>: <span style="color: #ff4500;">41</span><span style="color: #66cc66;">,</span> 
    <span style="color: #483d8b;">"prices"</span>: <span style="color: black;">&#91;</span>
        <span style="color: black;">&#123;</span>
            <span style="color: #483d8b;">"accountRestrictions"</span>: <span style="color: black;">&#91;</span><span style="color: black;">&#93;</span><span style="color: #66cc66;">,</span> 
            <span style="color: #483d8b;">"currentPriceFlag"</span>: null<span style="color: #66cc66;">,</span> 
            <span style="color: #483d8b;">"hourlyRecurringFee"</span>: <span style="color: #483d8b;">".04"</span><span style="color: #66cc66;">,</span> 
            <span style="color: #483d8b;">"id"</span>: <span style="color: #ff4500;">47</span><span style="color: #66cc66;">,</span> 
            <span style="color: #483d8b;">"itemId"</span>: <span style="color: #ff4500;">41</span><span style="color: #66cc66;">,</span> 
            <span style="color: #483d8b;">"laborFee"</span>: <span style="color: #483d8b;">"0"</span><span style="color: #66cc66;">,</span> 
            <span style="color: #483d8b;">"onSaleFlag"</span>: null<span style="color: #66cc66;">,</span> 
            <span style="color: #483d8b;">"oneTimeFee"</span>: <span style="color: #483d8b;">"0"</span><span style="color: #66cc66;">,</span> 
            <span style="color: #483d8b;">"recurringFee"</span>: <span style="color: #483d8b;">"20"</span><span style="color: #66cc66;">,</span> 
            <span style="color: #483d8b;">"setupFee"</span>: <span style="color: #483d8b;">"0"</span><span style="color: #66cc66;">,</span> 
            <span style="color: #483d8b;">"sort"</span>: <span style="color: #ff4500;">0</span>
        <span style="color: black;">&#125;</span>
    <span style="color: black;">&#93;</span><span style="color: #66cc66;">,</span> 
    <span style="color: #483d8b;">"softwareDescriptionId"</span>: null<span style="color: #66cc66;">,</span> 
    <span style="color: #483d8b;">"units"</span>: <span style="color: #483d8b;">"GIGABYTE"</span><span style="color: #66cc66;">,</span> 
    <span style="color: #483d8b;">"upgradeItemId"</span>: <span style="color: #ff4500;">42</span>
<span style="color: black;">&#125;</span></pre></div>
<p>If the commandline is not your style don't fret!  We have a <a href="https://github.com/softlayer/.NET-REST-Tool">tool</a> for creating REST calls on our <a href="http://github.com/softlayer">github</a>.</p>

