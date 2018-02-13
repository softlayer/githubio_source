---
title: "PERL"
description: "Perl"
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
    - "perl"
---


<script type="text/javascript">toc_collapse=0;</script><div class="toc" id="toc9">
<div class="toc-title">Table of contents<span class="toc-toggle-message">&nbsp;</span></div>
<div class="toc-list">
<ol>
<li class="toc-level-1"><a href="#Making_API_Calls">Making API Calls</a></li>
<li class="toc-level-1"><a href="#Using_Object_Masks">Using Object Masks</a></li>
<li class="toc-level-1"><a href="#Using_Result_Limits">Using Result Limits</a></li>
<li class="toc-level-1"><a href="#Error_Handling">Error Handling</a></li>
<li class="toc-level-1"><a href="#Referenced_API_Components">Referenced API Components</a>
<ol>
<li class="toc-level-2"><a href="#Services">Services</a></li>
<li class="toc-level-2"><a href="#Data_Types">Data Types</a></li>
<li class="toc-level-2"><a href="#Methods">Methods</a></li>
</ol>
</li>
<li class="toc-level-1"><a href="#External_Links">External Links</a></li>
</ol>
</div>
</div>
<p>SoftLayer provides a Perl-based API client that takes the heavy lifting out of making manual SOAP API calls. To use this API client, the following system requirements must be met:</p>
<ul>
<li>Perl 5.6 or higher</li>
<li>SOAP::Lite</li>
<li>XML::Hash::LX</li>
</ul>
<p>Download the SoftLayer Perl API client from its project page on SoftLayer’s github profile. Once downloaded, extract the Perl API client to a directory local to your Perl project or into your Perl installation's <span class="geshifilter"><code class="text geshifilter-text">@INC</code></span> path.</p>
<p><a href="http://github.com/softlayer/softlayer-api-perl-client">Download the SoftLayer API Perl client</a></p>
<h2 id="Making_API_Calls">Making API Calls</h2>
<p>Once the API client is downloaded and installed the first thing to do is include the <span class="geshifilter"><code class="text geshifilter-text">SoftLayer::API::SOAP</code></span> module in your script. This file defines SoftLayer's client objects. You may have to add the module's parent directory to your <span class="geshifilter"><code class="text geshifilter-text">@INC</code></span> path before including the module.  Add the parent directory using the following code:</p>
<div class="geshifilter">
<pre class="perl geshifilter-perl" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;">use</span> lib <span style="color: #ff0000;">'/path/to/SoftLayer/'</span><span style="color: #339933;">;</span>
<span style="color: #000000; font-weight: bold;">use</span> SoftLayer<span style="color: #339933;">::</span><span style="color: #006600;">API</span><span style="color: #339933;">::</span><span style="color: #006600;">SOAP</span><span style="color: #339933;">;</span></pre></div>
<p>Next, create a client object for the SoftLayer API service you wish to use. <span class="geshifilter"><code class="text geshifilter-text">SoftLayer::API::SOAP->new()</code></span> will take care of this for you and takes four parameters:</p>
<ul>
<li>The name of the service you wish to call.</li>
<li>An optional id number of the specific object you wish to work with. Pass an <span class="geshifilter"><code class="text geshifilter-text">undef</code></span> value if you're either working with the <a href="/reference/services/SoftLayer_Account/">SoftLayer_Account</a> service or are not working with a specific server, support ticket, invoice, or other object. This id creates an <a href="/article/initialization parameter">initialization parameter</a> in your API call.</li>
<li>Your API username.</li>
<li>Your API key.<br />
The code snippet below provides an example of making an API call, utilizing the parameters outlined above:</li>
</ul>
<div class="geshifilter">
<pre class="perl geshifilter-perl" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;">use</span> lib <span style="color: #ff0000;">'/path/to/SoftLayer/'</span><span style="color: #339933;">;</span>
<span style="color: #000000; font-weight: bold;">use</span> SoftLayer<span style="color: #339933;">::</span><span style="color: #006600;">API</span><span style="color: #339933;">::</span><span style="color: #006600;">SOAP</span><span style="color: #339933;">;</span>
<span style="color: #000000; font-weight: bold;">use</span> strict<span style="color: #339933;">;</span>
&nbsp;
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$api_username</span> <span style="color: #339933;">=</span> <span style="color: #ff0000;">'set me'</span><span style="color: #339933;">;</span>
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$api_key</span> <span style="color: #339933;">=</span> <span style="color: #ff0000;">'set me'</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Create a client to the SoftLayer_Account API service.</span>
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$client</span> <span style="color: #339933;">=</span> SoftLayer<span style="color: #339933;">::</span><span style="color: #006600;">API</span><span style="color: #339933;">::</span><span style="color: #006600;">SOAP</span><span style="color: #339933;">-></span><span style="color: #006600;">new</span><span style="color: #009900;">&#40;</span><span style="color: #ff0000;">'SoftLayer_Account'</span><span style="color: #339933;">,</span> <a href="http://perldoc.perl.org/functions/undef.html"><span style="color: #000066;">undef</span></a><span style="color: #339933;">,</span> <span style="color: #0000ff;">$api_username</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">$api_key</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
&nbsp;
<span style="color: #666666; font-style: italic;"># Work directly with the SoftLayer_Hardware_Server record with the hardware id </span>
<span style="color: #666666; font-style: italic;"># 1234.</span>
<span style="color: #666666; font-style: italic;">#my $server_id = 1234;</span>
<span style="color: #666666; font-style: italic;">#my $client = SoftLayer::API::SOAP->new('SoftLayer_Hardware_Server', $server_id, $api_username, $api_key);</span></pre></div>
<p>Once your API client object ($client) is ready, call a SoftLayer API method as if it were local to your client object. Assign the result of your API call to a variable to get the call's result. Complex type objects are returned as hashes blessed as your call's return type. Likewise, use hashes, hashes containing hashes, or hashes containing arrays if you need to pass complex type parameters to your API calls.  For example:</p>
<div class="geshifilter">
<pre class="perl geshifilter-perl" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;">use</span> lib <span style="color: #ff0000;">'/path/to/SoftLayer/'</span><span style="color: #339933;">;</span>
<span style="color: #000000; font-weight: bold;">use</span> SoftLayer<span style="color: #339933;">::</span><span style="color: #006600;">API</span><span style="color: #339933;">::</span><span style="color: #006600;">SOAP</span><span style="color: #339933;">;</span>
<span style="color: #000000; font-weight: bold;">use</span> strict<span style="color: #339933;">;</span>
&nbsp;
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$api_username</span> <span style="color: #339933;">=</span> <span style="color: #ff0000;">'set me'</span><span style="color: #339933;">;</span>
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$api_key</span> <span style="color: #339933;">=</span> <span style="color: #ff0000;">'set me'</span><span style="color: #339933;">;</span>
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$domain_id</span> <span style="color: #339933;">=</span> <span style="color: #cc66cc;">1234</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$client</span> <span style="color: #339933;">=</span> SoftLayer<span style="color: #339933;">::</span><span style="color: #006600;">API</span><span style="color: #339933;">::</span><span style="color: #006600;">SOAP</span><span style="color: #339933;">-></span><span style="color: #006600;">new</span><span style="color: #009900;">&#40;</span><span style="color: #ff0000;">'SoftLayer_Dns_Domain'</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">$domain_id</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">$api_username</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">$api_key</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Create a new A record in a domain.</span>
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$new_record</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">$client</span><span style="color: #339933;">-></span><span style="color: #006600;">createARecord</span><span style="color: #009900;">&#40;</span><span style="color: #ff0000;">'myhost'</span><span style="color: #339933;">,</span> <span style="color: #ff0000;">'127.0.0.1'</span><span style="color: #339933;">,</span> <span style="color: #cc66cc;">86400</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<a href="http://perldoc.perl.org/functions/print.html"><span style="color: #000066;">print</span></a> <span style="color: #ff0000;">'New A record id: '</span> . <span style="color: #0000ff;">$new_record</span><span style="color: #339933;">-></span><span style="color: #009900;">&#123;</span>id<span style="color: #009900;">&#125;</span><span style="color: #339933;">;</span> 
&nbsp;
<span style="color: #666666; font-style: italic;"># Create a new domain record. </span>
<span style="color: #666666; font-style: italic;">#</span>
<span style="color: #666666; font-style: italic;"># This requires an API client with an undef id, and use a hash with an array to model </span>
<span style="color: #666666; font-style: italic;"># our new domain.</span>
<span style="color: #0000ff;">$client</span> <span style="color: #339933;">=</span> SoftLayer<span style="color: #339933;">::</span><span style="color: #006600;">API</span><span style="color: #339933;">::</span><span style="color: #006600;">SOAP</span><span style="color: #339933;">-></span><span style="color: #006600;">new</span><span style="color: #009900;">&#40;</span><span style="color: #ff0000;">'SoftLayer_Dns_Domain'</span><span style="color: #339933;">,</span> <a href="http://perldoc.perl.org/functions/undef.html"><span style="color: #000066;">undef</span></a><span style="color: #339933;">,</span> <span style="color: #0000ff;">$api_username</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">$api_key</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$domain</span> <span style="color: #339933;">=</span> <span style="color: #009900;">&#123;</span>
    <span style="color: #ff0000;">'name'</span> <span style="color: #339933;">=></span> <span style="color: #ff0000;">'example.org'</span><span style="color: #339933;">,</span>
    <span style="color: #ff0000;">'resourceRecords'</span> <span style="color: #339933;">=></span> <span style="color: #009900;">&#91;</span>
        <span style="color: #009900;">&#123;</span>
            <span style="color: #ff0000;">'host'</span> <span style="color: #339933;">=></span> <span style="color: #ff0000;">'@'</span><span style="color: #339933;">,</span>
            <span style="color: #ff0000;">'data'</span> <span style="color: #339933;">=></span> <span style="color: #ff0000;">'127.0.0.1'</span><span style="color: #339933;">,</span>
            <span style="color: #ff0000;">'type'</span> <span style="color: #339933;">=></span> <span style="color: #ff0000;">'a'</span><span style="color: #339933;">,</span>
        <span style="color: #009900;">&#125;</span>
    <span style="color: #009900;">&#93;</span>
<span style="color: #009900;">&#125;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$new_domain</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">$client</span><span style="color: #339933;">-></span><span style="color: #006600;">createObject</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">$domain</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<a href="http://perldoc.perl.org/functions/print.html"><span style="color: #000066;">print</span></a> <span style="color: #ff0000;">'New domain id: '</span> . <span style="color: #0000ff;">$new_domain</span><span style="color: #339933;">-></span><span style="color: #009900;">&#123;</span>id<span style="color: #009900;">&#125;</span><span style="color: #339933;">;</span>
If you wish<span style="color: #339933;">,</span> you can declare your client object <span style="color: #b1b100;">and</span> make an API call on a single line.  The following code outlines this scenario<span style="color: #339933;">:</span>
<span style="color: #000000; font-weight: bold;">use</span> lib <span style="color: #ff0000;">'/path/to/SoftLayer/'</span><span style="color: #339933;">;</span>
<span style="color: #000000; font-weight: bold;">use</span> SoftLayer<span style="color: #339933;">::</span><span style="color: #006600;">API</span><span style="color: #339933;">::</span><span style="color: #006600;">SOAP</span><span style="color: #339933;">;</span>
<span style="color: #000000; font-weight: bold;">use</span> strict<span style="color: #339933;">;</span>
&nbsp;
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$api_username</span> <span style="color: #339933;">=</span> <span style="color: #ff0000;">'set me'</span><span style="color: #339933;">;</span>
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$api_key</span> <span style="color: #339933;">=</span> <span style="color: #ff0000;">'set me'</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$account</span> <span style="color: #339933;">=</span> SoftLayer<span style="color: #339933;">::</span><span style="color: #006600;">API</span><span style="color: #339933;">::</span><span style="color: #006600;">SOAP</span><span style="color: #339933;">-></span><span style="color: #006600;">new</span><span style="color: #009900;">&#40;</span><span style="color: #ff0000;">'SoftLayer_Account'</span><span style="color: #339933;">,</span> <a href="http://perldoc.perl.org/functions/undef.html"><span style="color: #000066;">undef</span></a><span style="color: #339933;">,</span> <span style="color: #0000ff;">$api_username</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">$api_key</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">-></span><span style="color: #006600;">getObject</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<h2 id="Using_Object_Masks">Using Object Masks</h2>
<p>Use a nested hash variable to create an <a href="/article/object mask">object mask</a> to your API call. Define the relational properties you wish to retrieve as hash keys. If you are retrieving child properties, define a nested hash for your child property.  Otherwise, define an empty hash as your key's value. Bind your object mask to your API client with <span class="geshifilter"><code class="text geshifilter-text">the setObjectMask()</code></span> method. This example retrieves an account's physical hardware records along with that hardware's operating system record, operating system passwords, network components, the datacenter the hardware is located in, and the number of processors in each hardware:</p>
<div class="geshifilter">
<pre class="perl geshifilter-perl" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;">use</span> lib <span style="color: #ff0000;">'/path/to/SoftLayer/'</span><span style="color: #339933;">;</span>
<span style="color: #000000; font-weight: bold;">use</span> SoftLayer<span style="color: #339933;">::</span><span style="color: #006600;">API</span><span style="color: #339933;">::</span><span style="color: #006600;">SOAP</span><span style="color: #339933;">;</span>
<span style="color: #000000; font-weight: bold;">use</span> strict<span style="color: #339933;">;</span>
&nbsp;
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$api_username</span> <span style="color: #339933;">=</span> <span style="color: #ff0000;">'set me'</span><span style="color: #339933;">;</span>
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$api_key</span> <span style="color: #339933;">=</span> <span style="color: #ff0000;">'set me'</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$client</span> <span style="color: #339933;">=</span> SoftLayer<span style="color: #339933;">::</span><span style="color: #006600;">API</span><span style="color: #339933;">::</span><span style="color: #006600;">SOAP</span><span style="color: #339933;">-></span><span style="color: #006600;">new</span><span style="color: #009900;">&#40;</span><span style="color: #ff0000;">'SoftLayer_Account'</span><span style="color: #339933;">,</span> <a href="http://perldoc.perl.org/functions/undef.html"><span style="color: #000066;">undef</span></a><span style="color: #339933;">,</span> <span style="color: #0000ff;">$api_username</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">$api_key</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Retrieve items related to hardware.</span>
<span style="color: #666666; font-style: italic;">#</span>
<span style="color: #666666; font-style: italic;"># Operating system, operating system passwords, all network components, the</span>
<span style="color: #666666; font-style: italic;"># datacenter the server is located in, and the number of processors in each </span>
<span style="color: #666666; font-style: italic;"># server.</span>
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$object_mask</span> <span style="color: #339933;">=</span> <span style="color: #009900;">&#123;</span>
    <span style="color: #ff0000;">'hardware'</span> <span style="color: #339933;">=></span> <span style="color: #009900;">&#123;</span>
        <span style="color: #ff0000;">'operatingSystem'</span> <span style="color: #339933;">=></span> <span style="color: #009900;">&#123;</span>
            <span style="color: #ff0000;">'passwords'</span> <span style="color: #339933;">=></span> <span style="color: #009900;">&#123;</span><span style="color: #009900;">&#125;</span><span style="color: #339933;">,</span>
        <span style="color: #009900;">&#125;</span><span style="color: #339933;">,</span>
        <span style="color: #ff0000;">'networkComponents'</span> <span style="color: #339933;">=></span> <span style="color: #009900;">&#123;</span><span style="color: #009900;">&#125;</span><span style="color: #339933;">,</span>
        <span style="color: #ff0000;">'datacenter'</span> <span style="color: #339933;">=></span> <span style="color: #009900;">&#123;</span><span style="color: #009900;">&#125;</span><span style="color: #339933;">,</span>
        <span style="color: #ff0000;">'processorCount'</span> <span style="color: #339933;">=></span> <span style="color: #009900;">&#123;</span><span style="color: #009900;">&#125;</span><span style="color: #339933;">,</span>
    <span style="color: #009900;">&#125;</span>
<span style="color: #009900;">&#125;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #0000ff;">$client</span><span style="color: #339933;">-></span><span style="color: #006600;">setObjectMask</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">$object_mask</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$hardware</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">$client</span><span style="color: #339933;">-></span><span style="color: #006600;">getHardware</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<h2 id="Using_Result_Limits">Using Result Limits</h2>
<p>When calling data, especially queries that involve pulling snippets of information from larger groups, utilizing result limits will greatly decrease your wait time for the return.<br />
Limit the number of results in your API call with your client object's <span class="geshifilter"><code class="text geshifilter-text">setResultLimit()</code></span> method. This method takes two parameters:</p>
<ul>
<li>The number of results to limit your call.</li>
<li>An optional offset to begin your result set.</li>
</ul>
<p>The code below provides an example of using result limits in y our API call.</p>
<div class="geshifilter">
<pre class="perl geshifilter-perl" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;">use</span> lib <span style="color: #ff0000;">'/path/to/SoftLayer/'</span><span style="color: #339933;">;</span>
<span style="color: #000000; font-weight: bold;">use</span> SoftLayer<span style="color: #339933;">::</span><span style="color: #006600;">API</span><span style="color: #339933;">::</span><span style="color: #006600;">SOAP</span><span style="color: #339933;">;</span>
<span style="color: #000000; font-weight: bold;">use</span> strict<span style="color: #339933;">;</span>
&nbsp;
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$api_username</span> <span style="color: #339933;">=</span> <span style="color: #ff0000;">'set me'</span><span style="color: #339933;">;</span>
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$api_key</span> <span style="color: #339933;">=</span> <span style="color: #ff0000;">'set me'</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$client</span> <span style="color: #339933;">=</span> SoftLayer<span style="color: #339933;">::</span><span style="color: #006600;">API</span><span style="color: #339933;">::</span><span style="color: #006600;">SOAP</span><span style="color: #339933;">-></span><span style="color: #006600;">new</span><span style="color: #009900;">&#40;</span><span style="color: #ff0000;">'SoftLayer_Account'</span><span style="color: #339933;">,</span> <a href="http://perldoc.perl.org/functions/undef.html"><span style="color: #000066;">undef</span></a><span style="color: #339933;">,</span> <span style="color: #0000ff;">$api_username</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">$api_key</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Retrieve our first two open support tickets.</span>
<span style="color: #0000ff;">$client</span><span style="color: #339933;">-></span><span style="color: #006600;">setResultLimit</span><span style="color: #009900;">&#40;</span><span style="color: #cc66cc;">2</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #0000ff;">$tickets</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">$client</span><span style="color: #339933;">-></span><span style="color: #006600;">getOpenTickets</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<h2 id="Error_Handling">Error Handling</h2>
<p>If a SOAP fault was thrown by your SoftLayer API call then your client object will have <span class="geshifilter"><code class="text geshifilter-text">fault</code></span> and <span class="geshifilter"><code class="text geshifilter-text">faultstring</code></span> properties populated. Check the <span class="geshifilter"><code class="text geshifilter-text">fault</code></span> property after making an API call for effective error handling. If there was an error in your call, the <span class="geshifilter"><code class="text geshifilter-text">faultstring</code></span> property contains the error returned by the SoftLayer API.  The following script contains an example of such error:</p>
<div class="geshifilter">
<pre class="perl geshifilter-perl" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;">use</span> lib <span style="color: #ff0000;">'/path/to/SoftLayer/'</span><span style="color: #339933;">;</span>
<span style="color: #000000; font-weight: bold;">use</span> SoftLayer<span style="color: #339933;">::</span><span style="color: #006600;">API</span><span style="color: #339933;">::</span><span style="color: #006600;">SOAP</span><span style="color: #339933;">;</span>
<span style="color: #000000; font-weight: bold;">use</span> strict<span style="color: #339933;">;</span>
&nbsp;
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$api_username</span> <span style="color: #339933;">=</span> <span style="color: #ff0000;">'set me'</span><span style="color: #339933;">;</span>
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$api_key</span> <span style="color: #339933;">=</span> <span style="color: #ff0000;">'an incorrect key'</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #0000ff;">$client</span> <span style="color: #339933;">=</span> SoftLayer<span style="color: #339933;">::</span><span style="color: #006600;">API</span><span style="color: #339933;">::</span><span style="color: #006600;">SOAP</span><span style="color: #339933;">-></span><span style="color: #006600;">new</span><span style="color: #009900;">&#40;</span><span style="color: #ff0000;">'SoftLayer_Account'</span><span style="color: #339933;">,</span> null<span style="color: #339933;">,</span> <span style="color: #0000ff;">$api_username</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">$api_key</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Exit the script with the message:</span>
<span style="color: #666666; font-style: italic;"># "Unable to retrieve account information: Invalid API key"</span>
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$account</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">$client</span><span style="color: #339933;">-></span><span style="color: #006600;">getObject</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #b1b100;">if</span> <span style="color: #009900;">&#40;</span><span style="color: #0000ff;">$account</span><span style="color: #339933;">-></span><span style="color: #006600;">fault</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
    <a href="http://perldoc.perl.org/functions/die.html"><span style="color: #000066;">die</span></a> <span style="color: #ff0000;">'Unable to retrieve account information: '</span> . <span style="color: #0000ff;">$account</span><span style="color: #339933;">-></span><span style="color: #006600;">faultstring</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span></pre></div>
<h2 id="Referenced_API_Components">Referenced API Components</h2>
<h3 id="Services">Services</h3>
<ul>
<li><a href="/reference/services/SoftLayer_Account/">SoftLayer_Account</a></li>
<li><a href="/reference/services/SoftLayer_Dns_Domain/">SoftLayer_Dns_Domain</a></li>
<li><a href="/reference/services/SoftLayer_Hardware_Server/">SoftLayer_Hardware_Server</a></li>
</ul>
<h3 id="Data_Types">Data Types</h3>
<ul>
<li><a href="/reference/services/SoftLayer_Hardware_Server/">SoftLayer_Hardware_Server</a></li>
</ul>
<h3 id="Methods">Methods</h3>
<ul>
<li><a href="/reference/services/SoftLayer_Account/getObject">SoftLayer_Account::getObject</a></li>
</ul>
<h2 id="External_Links">External Links</h2>
<ul>
<li><a href="http://www.perl.org/">The Perl Programming Language</a></li>
<li><a href="http://github.com/softlayer/softlayer-api-perl-client">SoftLayer API Perl client</a></li>
</ul>