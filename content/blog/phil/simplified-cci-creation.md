---
title: "Simplified CCI Creation"
description: "<p>The SoftLayer API is a thorough beast...many ins and outs, options and choices. It is aimed to impart the greatest le"
date: "2012-12-18"
author: "phil"
tags:
    - "blog"
---

<p>The SoftLayer API is a thorough beast...many ins and outs, options and choices. It is aimed to impart the greatest level of control to our customers and partners as possible. Our ordering system is a prime example. With it you are able to not only choose the standard assortment of specifications for a cloud server, but also if you want your storage stored locally vs on a SAN or even how you want us to contact you if there is an issue with a particular CCI...</p>
<p>However with great choice comes great complexity.</p>
<p>I am an avid supporter of the lazy developer as the lazy tend to find the simple and efficient solution. It is also true that our ordering API in the past has not necessarily catered towards the simple and efficient. Now however, we hope to inspire glee into the hearts of SLAPI developers lazy or not with the release of <a href="/reference/services/SoftLayer_Virtual_Guest/createObject">SoftLayer_Virtual_Guest::createObject</a>. This new method will provide a simplified way to create a Cloud Computing Instance order.</p>
<p>What first jumped out at me with this new sytem is the amount of information required to place the order has been significantly reduced by the implementation of default values. When placing an order through <a href="/reference/services/SoftLayer_Virtual_Guest/createObject">SoftLayer_Virtual_Guest::createObject</a> only 7 data points are required compared to the 19 of the old system.</p>
<p>The number of needed properties is not the only improvement, actually I would venture to say its not even the coolest...This new ordering process also comes with a new way to gather the possible values for your order. A quick call to <a href="/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions">SoftLayer_Virtual_Guest::getCreateObjectOptions</a> will return all of the possible values to choose from in a organized list just begging to be put into your shopping cart.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">'blockDevices': [{'itemPrice': {'hourlyRecurringFee': '0',
                                 'item': {'description': '25 GB (SAN)'},
                                 'recurringFee': '0'},
                   'template': {'blockDevices': [{'device': '0',
                                                  'diskImage': {'capacity': 25}}],
...
 'datacenters': [{'template': {'datacenter': {'name': 'ams01'}}},
                 {'template': {'datacenter': {'name': 'dal01'}}},
&nbsp;
...
 'memory': [{'itemPrice': {'hourlyRecurringFee': '.03',
                           'item': {'description': '1 GB'},
                           'recurringFee': '21'},
...</pre></div>
<p>Once you have decided which options to go with you need to put the values into a <a href="/reference/datatypes/SoftLayer_Virtual_Guest/">SoftLayer_Virtual_Guest</a> template object and pass to SoftLayer_Virtual_Guest::createObject</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;"><span style="color: #ff7700;font-weight:bold;">import</span> SoftLayer.<span style="color: black;">API</span>
<span style="color: #ff7700;font-weight:bold;">from</span> <span style="color: #dc143c;">pprint</span> <span style="color: #ff7700;font-weight:bold;">import</span> <span style="color: #dc143c;">pprint</span> <span style="color: #ff7700;font-weight:bold;">as</span> pp
&nbsp;
api_username <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">'arst'</span>
api_key <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">'1234arst'</span>
&nbsp;
client <span style="color: #66cc66;">=</span> SoftLayer.<span style="color: black;">Client</span><span style="color: black;">&#40;</span>
    username<span style="color: #66cc66;">=</span>api_username<span style="color: #66cc66;">,</span>
    api_key<span style="color: #66cc66;">=</span>api_key
<span style="color: black;">&#41;</span>
&nbsp;
newCCI <span style="color: #66cc66;">=</span> <span style="color: black;">&#123;</span>
    <span style="color: #483d8b;">'hostname'</span>: <span style="color: #483d8b;">'test1'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'domain'</span>: <span style="color: #483d8b;">'example.com'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'startCpus'</span>: <span style="color: #ff4500;">1</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'maxMemory'</span>: <span style="color: #ff4500;">1024</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'hourlyBillingFlag'</span>: <span style="color: #483d8b;">'true'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'operatingSystemReferenceCode'</span>: <span style="color: #483d8b;">'UBUNTU_LATEST'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'localDiskFlag'</span>: <span style="color: #483d8b;">'false'</span>
<span style="color: black;">&#125;</span>
&nbsp;
result <span style="color: #66cc66;">=</span> client<span style="color: black;">&#91;</span><span style="color: #483d8b;">'Virtual_Guest'</span><span style="color: black;">&#93;</span>.<span style="color: black;">createObject</span><span style="color: black;">&#40;</span>newCCI<span style="color: black;">&#41;</span>
pp<span style="color: black;">&#40;</span>result<span style="color: black;">&#41;</span></pre></div>
<p>To check if the new CCI has completed the provisioning process we can look for the <span class="geshifilter"><code class="text geshifilter-text">provisionDate</code></span>:</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;">client <span style="color: #66cc66;">=</span> SoftLayer.<span style="color: black;">Client</span><span style="color: black;">&#40;</span>
    username<span style="color: #66cc66;">=</span> <span style="color: #483d8b;">"arst"</span>
    api_key <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">"1234arst"</span>
<span style="color: black;">&#41;</span> 
&nbsp;
object_mask <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">'mask.provisionDate'</span>
&nbsp;
cci <span style="color: #66cc66;">=</span> client<span style="color: black;">&#91;</span><span style="color: #483d8b;">'Virtual_Guest'</span><span style="color: black;">&#93;</span>.<span style="color: black;">getObject</span><span style="color: black;">&#40;</span>mask<span style="color: #66cc66;">=</span>object_mask<span style="color: black;">&#41;</span>
&nbsp;
<span style="color: #ff7700;font-weight:bold;">if</span> <span style="color: black;">&#40;</span> <span style="color: #483d8b;">'provisionDate'</span> <span style="color: #ff7700;font-weight:bold;">in</span> cci <span style="color: #ff7700;font-weight:bold;">and</span> cci<span style="color: black;">&#91;</span><span style="color: #483d8b;">'provisionDate'</span><span style="color: black;">&#93;</span> <span style="color: #66cc66;">!=</span> <span style="color: black;">&#41;</span>:
    <span style="color: #ff7700;font-weight:bold;">print</span> <span style="color: #483d8b;">'CCI %s is online'</span> % cci<span style="color: black;">&#91;</span><span style="color: #483d8b;">'hostname'</span><span style="color: black;">&#93;</span>
<span style="color: #ff7700;font-weight:bold;">else</span>:
    <span style="color: #ff7700;font-weight:bold;">print</span> <span style="color: #483d8b;">'CCI %s is provisioning'</span> % cci<span style="color: black;">&#91;</span><span style="color: #483d8b;">'hostname'</span><span style="color: black;">&#93;</span></pre></div>
<p>While this new process should be straight forward, please do not hesitate to reach out if you have any questions, concerns or suggestions for future improvements.</p>
<p>-Phil</p>
<p>Example snippets for <a href="/reference/services/SoftLayer_Virtual_Guest/createObject">SoftLayer_Virtual_Guest::createObject</a>:<br />
<a href="https://gist.github.com/4271418" title="https://gist.github.com/4271418">https://gist.github.com/4271418</a> - Python<br />
<a href="https://gist.github.com/4271461" title="https://gist.github.com/4271461">https://gist.github.com/4271461</a> - PHP<br />
<a href="https://gist.github.com/4318794" title="https://gist.github.com/4318794">https://gist.github.com/4318794</a> - Ruby</p>

