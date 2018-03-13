---
title: "Python"
description: "Using the SoftLayer API with python"
date: "2011-06-20"
tags:
    - "tools"
    - "sldn"
    - "article"
    - "python"
---

<script type="text/javascript">toc_collapse=0;</script><div class="toc" id="toc1">
<div class="toc-title">Table of contents<span class="toc-toggle-message">&nbsp;</span></div>
<div class="toc-list">
<ol>
<li class="toc-level-1"><a href="#Python">Python</a></li>
<li class="toc-level-1"><a href="#Making_API_Calls">Making API Calls</a></li>
<li class="toc-level-1"><a href="#Using_Object_Masks">Using Object Masks</a></li>
<li class="toc-level-1"><a href="#Using_Result_Limits">Using Result Limits</a></li>
<li class="toc-level-1"><a href="#Error_Handling">Error Handling</a></li>
<li class="toc-level-1"><a href="#Managers">Managers</a></li>
<li class="toc-level-1"><a href="#More_Resources">More Resources</a></li>
</ol>
</div>
</div>
<h2 id="Python">Python</h2>
<p>SoftLayer, an IBM company, provides a <a href="http://www.python.org/">Python-based</a> API package that takes the heavy lifting out of making manual XML-RPC API calls. Our Python-based API requires  a <a href="http://www.python.org/download/">minimum of Python 2.6</a> To install the Python package into your Python installation’s site-packages directory, run the following command:</p>
<p><bash><br />
pip install softlayer<br />
</bash></p>
<p>Refer to our <a href="https://softlayer-api-python-client.readthedocs.org/en/latest/install/">Python bindings documentation</a> for more install options.</p>
<h2 id="Making_API_Calls">Making API Calls</h2>
<p>Once the API client is installed, the first thing to do is import the SoftLayer package in your script. Use the following line to do that:</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;"><span style="color: #ff7700;font-weight:bold;">import</span> SoftLayer</pre></div>
<p>Next, we need to create a client object. The code snippet below provides an example of setting up an API client:</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;"><span style="color: #ff7700;font-weight:bold;">import</span> SoftLayer
client <span style="color: #66cc66;">=</span> SoftLayer.<span style="color: black;">Client</span><span style="color: black;">&#40;</span>username<span style="color: #66cc66;">=</span><span style="color: #483d8b;">'YOUR_USERNAME'</span><span style="color: #66cc66;">,</span> api_key<span style="color: #66cc66;">=</span><span style="color: #483d8b;">'YOUR_API_KEY'</span><span style="color: black;">&#41;</span></pre></div>
<p>Once your API client object is ready, we can make calls with it. Here's how to get the account details for the current account. The call takes no parameters and doesn't require an id so it's the natural starting point.</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;">client<span style="color: black;">&#91;</span><span style="color: #483d8b;">'Account'</span><span style="color: black;">&#93;</span>.<span style="color: black;">getObject</span><span style="color: black;">&#40;</span><span style="color: black;">&#41;</span></pre></div>
<p>Here's how you'd create a new CloudLayer Computing Instance, which requires the use of the Virtual Guest record. The virtual guest record is a complex type, which is passed in as a Python dictionary.</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;">&nbsp;
client<span style="color: black;">&#91;</span><span style="color: #483d8b;">'Virtual_Guest'</span><span style="color: black;">&#93;</span>.<span style="color: black;">createObject</span><span style="color: black;">&#40;</span><span style="color: black;">&#123;</span>
    <span style="color: #483d8b;">'hostname'</span>: <span style="color: #483d8b;">'myhostname'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'domain'</span>: <span style="color: #483d8b;">'example.org'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'startCpus'</span>: <span style="color: #ff4500;">1</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'maxMemory'</span>: <span style="color: #ff4500;">1024</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'hourlyBillingFlag'</span>: <span style="color: #483d8b;">'true'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'operatingSystemReferenceCode'</span>: <span style="color: #483d8b;">'UBUNTU_LATEST'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'localDiskFlag'</span>: <span style="color: #483d8b;">'false'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'datacenter'</span>: {<span style="color: #483d8b;">'name'</span>: <span style="color: #483d8b;">'dal09'</span>}
<span style="color: black;">&#125;</span><span style="color: black;">&#41;</span></pre></div>
<p>Here's how you'd create a new domain zone on our DNS service.</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;">&nbsp;
new_domain <span style="color: #66cc66;">=</span> client<span style="color: black;">&#91;</span><span style="color: #483d8b;">'Dns_Domain'</span><span style="color: black;">&#93;</span>.<span style="color: black;">createObject</span><span style="color: black;">&#40;</span><span style="color: black;">&#123;</span><span style="color: black;">&#123;</span>
    <span style="color: #483d8b;">'name'</span> : <span style="color: #483d8b;">'example.org'</span><span style="color: #66cc66;">,</span>
    <span style="color: #483d8b;">'resourceRecords'</span> <span style="color: #66cc66;">=></span> <span style="color: black;">&#91;</span>
        <span style="color: black;">&#123;</span>
            <span style="color: #483d8b;">'host'</span> : <span style="color: #483d8b;">'@'</span><span style="color: #66cc66;">,</span>
            <span style="color: #483d8b;">'data'</span> : <span style="color: #483d8b;">'127.0.0.1'</span><span style="color: #66cc66;">,</span>
            <span style="color: #483d8b;">'type'</span> : <span style="color: #483d8b;">'a'</span><span style="color: #66cc66;">,</span>
        <span style="color: black;">&#125;</span>
    <span style="color: black;">&#93;</span>
<span style="color: black;">&#125;</span><span style="color: black;">&#41;</span></pre></div>
<p>Now that we have a zone created for our domain, the following example shows how you add an A record in that zone after the fact. Note how parameters are passed in as positional arguments and the required domain id is passed using the id keyword argument. This example uses the domain id that was created in the last call.</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;">new_record <span style="color: #66cc66;">=</span> client<span style="color: black;">&#91;</span><span style="color: #483d8b;">'Dns_Domain'</span><span style="color: black;">&#93;</span>.<span style="color: black;">createARecord</span><span style="color: black;">&#40;</span><span style="color: #483d8b;">'myhost'</span><span style="color: #66cc66;">,</span> <span style="color: #483d8b;">'127.0.0.1'</span><span style="color: #66cc66;">,</span> <span style="color: #ff4500;">86400</span><span style="color: #66cc66;">,</span> <span style="color: #008000;">id</span><span style="color: #66cc66;">=</span>new_domain<span style="color: black;">&#91;</span><span style="color: #483d8b;">'id'</span><span style="color: black;">&#93;</span><span style="color: black;">&#41;</span>
&nbsp;
<span style="color: #ff7700;font-weight:bold;">print</span><span style="color: black;">&#40;</span><span style="color: #483d8b;">"New A record id: %"</span><span style="color: #66cc66;">,</span> new_record<span style="color: black;">&#91;</span><span style="color: #483d8b;">'id'</span><span style="color: black;">&#93;</span><span style="color: black;">&#41;</span></pre></div>
<h2 id="Using_Object_Masks">Using Object Masks</h2>
<p>Object masks allow you to control what attributes are returned in each call. It can be used to dig much deeper into an object to get specific</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;"><span style="color: #808080; font-style: italic;"># Because of the object mask that we're using we will retrieve the following</span>
<span style="color: #808080; font-style: italic;"># for each server:</span>
<span style="color: #808080; font-style: italic;"># * operating system passwords</span>
<span style="color: #808080; font-style: italic;"># * all network components</span>
<span style="color: #808080; font-style: italic;"># * the datacenter the server is located in</span>
<span style="color: #808080; font-style: italic;"># * the number of processors</span>
object_mask <span style="color: #66cc66;">=</span> <span style="color: #483d8b;">'operatingSystem.passwords, networkComponents, datacenter, processorCount'</span>
hardware <span style="color: #66cc66;">=</span> client<span style="color: black;">&#91;</span><span style="color: #483d8b;">'Account'</span><span style="color: black;">&#93;</span>.<span style="color: black;">getHardware</span><span style="color: black;">&#40;</span>mask<span style="color: #66cc66;">=</span>object_mask<span style="color: black;">&#41;</span></pre></div>
<h2 id="Using_Result_Limits">Using Result Limits</h2>
<p>The SoftLayer API allows limits to the number of returned results and offsets to better control the amount of data returned on certain calls. Below is an example showing pagination.</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;">client<span style="color: black;">&#91;</span><span style="color: #483d8b;">'Account'</span><span style="color: black;">&#93;</span>.<span style="color: black;">getVirtualGuests</span><span style="color: black;">&#40;</span>limit<span style="color: #66cc66;">=</span><span style="color: #ff4500;">10</span><span style="color: #66cc66;">,</span> offset<span style="color: #66cc66;">=</span><span style="color: #ff4500;">0</span><span style="color: black;">&#41;</span>  <span style="color: #808080; font-style: italic;"># Page 1</span>
client<span style="color: black;">&#91;</span><span style="color: #483d8b;">'Account'</span><span style="color: black;">&#93;</span>.<span style="color: black;">getVirtualGuests</span><span style="color: black;">&#40;</span>limit<span style="color: #66cc66;">=</span><span style="color: #ff4500;">10</span><span style="color: #66cc66;">,</span> offset<span style="color: #66cc66;">=</span><span style="color: #ff4500;">10</span><span style="color: black;">&#41;</span>  <span style="color: #808080; font-style: italic;"># Page 2</span></pre></div>
<h2 id="Error_Handling">Error Handling</h2>
<p>Errors that happen when making SoftLayer API calls appear as exceptions. The following script provides an example of how an API error can be handled. In this case we simply print out the details of the error and exit:</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;">client <span style="color: #66cc66;">=</span> SoftLayer.<span style="color: black;">Client</span><span style="color: black;">&#40;</span>username<span style="color: #66cc66;">=</span><span style="color: #483d8b;">'invalid'</span><span style="color: #66cc66;">,</span> api_key<span style="color: #66cc66;">=</span><span style="color: #483d8b;">'invalid'</span><span style="color: black;">&#41;</span>
&nbsp;
<span style="color: #ff7700;font-weight:bold;">try</span>:
    account <span style="color: #66cc66;">=</span> client<span style="color: black;">&#91;</span><span style="color: #483d8b;">'Account'</span><span style="color: black;">&#93;</span>.<span style="color: black;">getObject</span><span style="color: black;">&#40;</span><span style="color: black;">&#41;</span>
<span style="color: #ff7700;font-weight:bold;">except</span> SoftLayer.<span style="color: black;">SoftLayerAPIError</span> <span style="color: #ff7700;font-weight:bold;">as</span> e:
    <span style="color: #ff7700;font-weight:bold;">print</span><span style="color: black;">&#40;</span><span style="color: #483d8b;">"Unable to retrieve account information faultCode=%s, faultString=%s"</span>
          % <span style="color: black;">&#40;</span>e.<span style="color: black;">faultCode</span><span style="color: #66cc66;">,</span> e.<span style="color: black;">faultString</span><span style="color: black;">&#41;</span><span style="color: black;">&#41;</span>
    exit<span style="color: black;">&#40;</span><span style="color: #ff4500;">1</span><span style="color: black;">&#41;</span>
<span style="color: #808080; font-style: italic;"># This should output:</span>
<span style="color: #808080; font-style: italic;"># Unable to retrieve account information faultCode=SoftLayer_Exception, faultString=Invalid API token.</span></pre></div>
<h2 id="Managers">Managers</h2>
<p>Everything above this section has addressed how to use the base API client to interact with the XML-RPC API that's documented here on SLDN. The Python bindings also have managers that abstract away some functionality from direct API calls. For reference of all available managers, refer to our <a href="https://softlayer-api-python-client.readthedocs.org/en/latest/api/client/#managers">API Python Client documentation</a>.</p>
<p>Creating a new CloudLayer Computing Instance, as we did above, would look something like this using our Python API Client managers (unsure if Python API Client managers is right, but feel free to replace that with what is, if you need to):</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;"><span style="color: #ff7700;font-weight:bold;">import</span> SoftLayer
client <span style="color: #66cc66;">=</span> SoftLayer.<span style="color: black;">Client</span><span style="color: black;">&#40;</span>username<span style="color: #66cc66;">=</span><span style="color: #483d8b;">'YOUR_USERNAME'</span><span style="color: #66cc66;">,</span> api_key<span style="color: #66cc66;">=</span><span style="color: #483d8b;">'YOUR_API_KEY'</span><span style="color: black;">&#41;</span>
cci_manager <span style="color: #66cc66;">=</span> SoftLayer.<span style="color: black;">CCIManager</span><span style="color: black;">&#40;</span>client<span style="color: black;">&#41;</span>
cci_manager.<span style="color: black;">create_instance</span><span style="color: black;">&#40;</span>
    hostname<span style="color: #66cc66;">=</span><span style="color: #483d8b;">'myhostname'</span><span style="color: #66cc66;">,</span>
    domain<span style="color: #66cc66;">=</span><span style="color: #483d8b;">'example.org'</span><span style="color: #66cc66;">,</span>
    cpus<span style="color: #66cc66;">=</span><span style="color: #ff4500;">1</span><span style="color: #66cc66;">,</span>
    memory<span style="color: #66cc66;">=</span><span style="color: #ff4500;">1024</span><span style="color: #66cc66;">,</span>
    hourly<span style="color: #66cc66;">=</span><span style="color: #008000;">True</span><span style="color: #66cc66;">,</span>
    os_code<span style="color: #66cc66;">=</span><span style="color: #483d8b;">'UBUNTU_LATEST'</span><span style="color: #66cc66;">,</span>
    local_disk<span style="color: #66cc66;">=</span><span style="color: #008000;">False</span><span style="color: black;">&#41;</span></pre></div>
<p>Below is an example of listing hardware servers with more than 8 gigabytes of memory in the dal05 datacenter.</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;">hardware_manager <span style="color: #66cc66;">=</span> SoftLayer.<span style="color: black;">HardwareManager</span><span style="color: black;">&#40;</span>client<span style="color: black;">&#41;</span>
hardware <span style="color: #66cc66;">=</span> hardware_manager.<span style="color: black;">list_hardware</span><span style="color: black;">&#40;</span>datacenter<span style="color: #66cc66;">=</span><span style="color: #483d8b;">'dal05'</span><span style="color: #66cc66;">,</span> memory<span style="color: #66cc66;">=</span><span style="color: #483d8b;">'> 8'</span><span style="color: black;">&#41;</span></pre></div>
<p>The managers are a good way of being introduced to a smaller subset of the API and provide a reference for doing common tasks.</p>
<h2 id="More_Resources">More Resources</h2>
<p>The Python bindings are publicly developed <a href="https://github.com/softlayer/softlayer-api-python-client">on GitHub</a>. New features are developed and bugs are reported through <a href="https://github.com/softlayer/softlayer-api-python-client/issues">GitHub's Integrated Issue Tracking</a>. The full documentation for SoftLayer API Python client is available <a href="https://softlayer-api-python-client.readthedocs.org">here</a>. The bindings also have a command-line interface that hasn't been mentioned here. You can find more information on that in its <a href="https://softlayer-api-python-client.readthedocs.org">full documentation site</a>.</p>