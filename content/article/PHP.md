---
title: "PHP"
description: "SoftLayer provides a PHP-based API client that takes the heavy lifting out making manual SOAP or XML-RPC calls."
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
    - "php"
---


<p>SoftLayer provides a PHP-based API client that takes the heavy lifting out making manual SOAP or XML-RPC calls. To use the PHP-based API client, the following system requirements must be met:</p>
<ul>
<li>PHP 5.2.3 or higher</li>
<li>One of the following PHP extensions:
<ul>
<li><a href="http://php.net/manual/en/book.soap.php">SOAP</a></li>
<li><a href="http://php.net/manual/en/book.xmlrpc.php">XML-RPC</a></li>
</ul>
</li>
</ul>
<p>Download the SoftLayer PHP API client from its <a href="http://github.com/softlayer/softlayer-api-php-client">project page</a> on SoftLayer's github profile. Once downloaded, extract the PHP API Client to a directory local to your PHP project or into your PHP installation's include_path.<br />
<a href="http://github.com/softlayer/softlayer-api-php-client">Download the SoftLayer API PHP client</a></p>
<script type="text/javascript">toc_collapse=0;</script><div class="toc" id="toc2">
<div class="toc-title">Table of contents<span class="toc-toggle-message">&nbsp;</span></div>
<div class="toc-list">
<ol>
<li class="toc-level-1"><a href="#Making_SOAP_Calls">Making SOAP Calls</a></li>
<li class="toc-level-1"><a href="#Using_XML-RPC">Using XML-RPC</a></li>
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
<h2 id="Making_SOAP_Calls">Making SOAP Calls</h2>
<p>Once the API client is downloaded and installed the first thing to do is include the <span class="geshifilter"><code class="php geshifilter-php">SoapClient<span style="color: #339933;">.</span><span style="color: #000000; font-weight: bold;">class</span><span style="color: #339933;">.</span>php</code></span> file in your script. This file defines SoftLayer's client objects.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;"><?php</span>
 <span style="color: #b1b100;">require_once</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'/path/to/SoftLayer/SoapClient.class.php'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<p>Next, create a client object for the SoftLayer API <a href="http://sldn.softlayer.com/article/service">service</a> you wish to use. <span class="geshifilter"><code class="php geshifilter-php">SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span></code></span> will take care of this for you and takes four parameters:</p>
<ul>
<li>The name of the service you wish to call.</li>
<li>An optional id number of the specific object you wish to work with. Pass a <span class="geshifilter"><code class="text geshifilter-text">null</code></span> value if you're either working with the <a href="/reference/services/SoftLayer_Account/">SoftLayer_Account</a> service or are not working with a specific server, support ticket, invoice, or other object. This id creates an <a href="/article/initialization parameter">initialization parameter</a> in your API call.</li>
<li>Your API username.</li>
<li>Your API key.</li>
</ul>
<p>The code snippet below provides an example of making a SOAP call, utilizing the parameters outlined above:</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;"><?php</span>
<span style="color: #b1b100;">require_once</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'/path/to/SoftLayer/SoapClient.class.php'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$apiUsername</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'set me'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$apiKey</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'set me'</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #009933; font-style: italic;">/**
 * Create a client to the SoftLayer_Account API service.
 */</span>
<span style="color: #000088;">$client</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Account'</span><span style="color: #339933;">,</span> <span style="color: #000000; font-weight: bold;">null</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUsername</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #009933; font-style: italic;">/**
 * Work directly with the SoftLayer_Hardware_Server record with the hardware id 
 * 1234.
 */</span>
<span style="color: #000088;">$serverId</span> <span style="color: #339933;">=</span> <span style="color: #cc66cc;">1234</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$client</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Hardware_Server'</span><span style="color: #339933;">,</span> <span style="color: #000088;">$serverId</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUsername</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<p>Once your API client object is ready call a SoftLayer API method as if it were local to your client object. Assign the result of your API call to a variable to get the call's result. Complex type objects are returned as PHP stdClass objects. Likewise, use stdClass objects if you need to pass complex type parameters to your API calls.  For example:</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;"><?php</span>
<span style="color: #b1b100;">require_once</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'/path/to/SoftLayer/SoapClient.class.php'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$apiUsername</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'set me'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$apiKey</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'set me'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$domainId</span> <span style="color: #339933;">=</span> <span style="color: #cc66cc;">1234</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$client</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Dns_Domain'</span><span style="color: #339933;">,</span> <span style="color: #000088;">$domainId</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUsername</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #009933; font-style: italic;">/**
 * Create a new A record in a domain.
 */</span>
<span style="color: #000088;">$newRecord</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">createARecord</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'myhost'</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">'127.0.0.1'</span><span style="color: #339933;">,</span> <span style="color: #cc66cc;">86400</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<a href="http://www.php.net/echo"><span style="color: #990000;">echo</span></a> <span style="color: #0000ff;">'New A record id: '</span> <span style="color: #339933;">.</span> <span style="color: #000088;">$newRecord</span><span style="color: #339933;">-></span><span style="color: #004000;">id</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #009933; font-style: italic;">/**
 * Create a new domain record. 
 * 
 * This requires an API client with a null id, and use a stdClass object to model 
 *our new domain.
 */</span>
<span style="color: #000088;">$client</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Dns_Domain'</span><span style="color: #339933;">,</span> <span style="color: #000000; font-weight: bold;">null</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUsername</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$domain</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> stdClass<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$domain</span><span style="color: #339933;">-></span><span style="color: #004000;">name</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'example.org'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$domain</span><span style="color: #339933;">-></span><span style="color: #004000;">resourceRecords</span> <span style="color: #339933;">=</span> <a href="http://www.php.net/array"><span style="color: #990000;">array</span></a><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$domain</span><span style="color: #339933;">-></span><span style="color: #004000;">resourceRecords</span><span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">0</span><span style="color: #009900;">&#93;</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> stdClass<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$domain</span><span style="color: #339933;">-></span><span style="color: #004000;">resourceRecords</span><span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">0</span><span style="color: #009900;">&#93;</span><span style="color: #339933;">-></span><span style="color: #004000;">host</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'@'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$domain</span><span style="color: #339933;">-></span><span style="color: #004000;">resourceRecords</span><span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">0</span><span style="color: #009900;">&#93;</span><span style="color: #339933;">-></span><span style="color: #004000;">data</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'127.0.0.1'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$domain</span><span style="color: #339933;">-></span><span style="color: #004000;">resourceRecords</span><span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">0</span><span style="color: #009900;">&#93;</span><span style="color: #339933;">-></span><span style="color: #004000;">type</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'a'</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$newDomain</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">createObject</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$domain</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<a href="http://www.php.net/echo"><span style="color: #990000;">echo</span></a> <span style="color: #0000ff;">'New domain id: '</span> <span style="color: #339933;">.</span> <span style="color: #000088;">$newDomain</span><span style="color: #339933;">-></span><span style="color: #004000;">id</span><span style="color: #339933;">;</span></pre></div>
<h2 id="Using_XML-RPC">Using XML-RPC</h2>
<p>The SoftLayer API PHP client supports both the SOAP and XML-RPC protocols interchangeably. If you wish to use XML-RPC instead of SOAP, two changes are required:</p>
<ul>
<li>Include <span class="geshifilter"><code class="text geshifilter-text">XmlrpcClient.class.php</code></span> instead of <span class="geshifilter"><code class="text geshifilter-text">SoapClient.class.php</code></span></li>
<li>Create an API client with <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_XmlrpcClient::getClient()</code></span> instead of <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_SoapClient::getClient()</code></span><br />
For instance:</li>
</ul>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;"><?php</span>
<span style="color: #b1b100;">require_once</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'/path/to/SoftLayer/XmlrpcClient.class.php'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$apiUsername</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'set me'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$apiKey</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'set me'</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$client</span> <span style="color: #339933;">=</span> SoftLayer_XmlrpcClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Account'</span> <span style="color: #000000; font-weight: bold;">null</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUsername</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<h2 id="Using_Object_Masks">Using Object Masks</h2>
<p>Create an <a href="/article/object mask">object mask</a> in your API call by first declaring a new <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_ObjectMask</code></span> object. Define the relational properties you wish to retrieve as local properties in your new mask object. Finally, bind it to your API client by using the <span class="geshifilter"><code class="text geshifilter-text">setObjectMask()</code></span> method. This example retrieves the following information:</p>
<ul>
<li>The account's physical hardware </li>
<li>The hardware's operating system record </li>
<li>Operating system password</li>
<li>Network components</li>
<li>The datacenter in which the hardware is located </li>
<li>The number of processors in each hardware</li>
</ul>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;"><?php</span>
<span style="color: #b1b100;">require_once</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'/path/to/SoftLayer/SoapClient.class.php'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$apiUsername</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'set me'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$apiKey</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'set me'</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$client</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Account'</span><span style="color: #339933;">,</span> <span style="color: #000000; font-weight: bold;">null</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUsername</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #009933; font-style: italic;">/**
 * Retrieve items related to hardware.
 *
 * Operating system, operating system passwords, all network components, the
 * datacenter the server is located in, and the number of processors in each 
 * server.
 */</span>
<span style="color: #000088;">$objectMask</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> SoftLayer_ObjectMask<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$objectMask</span><span style="color: #339933;">-></span><span style="color: #004000;">hardware</span><span style="color: #339933;">-></span><span style="color: #004000;">operatingSystem</span><span style="color: #339933;">-></span><span style="color: #004000;">passwords</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$objectMask</span><span style="color: #339933;">-></span><span style="color: #004000;">hardware</span><span style="color: #339933;">-></span><span style="color: #004000;">networkComponents</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$objectMask</span><span style="color: #339933;">-></span><span style="color: #004000;">hardware</span><span style="color: #339933;">-></span><span style="color: #004000;">datacenter</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$objectMask</span><span style="color: #339933;">-></span><span style="color: #004000;">hardware</span><span style="color: #339933;">-></span><span style="color: #004000;">processorCount</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">setObjectMask</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$objectMask</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$hardware</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">getHardware</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<h2 id="Using_Result_Limits">Using Result Limits</h2>
<p>When calling data, especially queries that involve pulling snippets of information from larger groups, utilizing result limits will greatly decrease your wait time for the return.<br />
Limit the number of results in your API call with your client object's <span class="geshifilter"><code class="text geshifilter-text">setResultLimit()</code></span> method. This method takes two parameters:</p>
<ul>
<li>The number of results to limit your call.</li>
<li>An optional offset to begin your result set.<br />
The example below incorporates the required information to set a result limit:</li>
</ul>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;"><?php</span>
<span style="color: #b1b100;">require_once</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'/path/to/SoftLayer/SoapClient.class.php'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$apiUsername</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'set me'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$apiKey</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'set me'</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$client</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Account'</span><span style="color: #339933;">,</span> <span style="color: #000000; font-weight: bold;">null</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUsername</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #009933; font-style: italic;">/**
 * Retrieve our first two open support tickets.
 */</span>
<span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">setResultLimit</span><span style="color: #009900;">&#40;</span><span style="color: #cc66cc;">2</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$tickets</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">getOpenTickets</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<h2 id="Error_Handling">Error Handling</h2>
<p>SoftLayer API call errors are thrown by the PHP client as <a href="/article/exceptions">exceptions</a>. Place calls to the SoftLayer API inside try/catch blocks to ensure proper handling. Use the PHP exception classes' <span class="geshifilter"><code class="text geshifilter-text">getMessage()</code></span> method to access errors returned by the SoftLayer API.  The following script contains an example of such error:</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;"><?php</span>
<span style="color: #b1b100;">require_once</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'/path/to/SoftLayer/SoapClient.class.php'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$apiUsername</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'set me!'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$apiKey</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'an incorrect API key'</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$client</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> SoftLayer_SoapClient<span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Account'</span><span style="color: #339933;">,</span> <span style="color: #000000; font-weight: bold;">null</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUsername</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #009933; font-style: italic;">/**
 * Exit the script with the message:
 * "Unable to retrieve account information: Invalid API key"
 */</span>
try <span style="color: #009900;">&#123;</span>
    <span style="color: #000088;">$account</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">getObject</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span> catch <span style="color: #009900;">&#40;</span>Exception <span style="color: #000088;">$e</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
    <a href="http://www.php.net/die"><span style="color: #990000;">die</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'Unable to retrieve account information: '</span> <span style="color: #339933;">.</span> <span style="color: #000088;">$e</span><span style="color: #339933;">-></span><span style="color: #004000;">getMessage</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
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
<li><a href="/reference/services/SoftLayer_Account/getHardware">SoftLayer_Account::getHardware</a></li>
<li><a href="/reference/services/SoftLayer_Account/getOpenTickets">SoftLayer_Account::getOpenTickets</a></li>
<li><a href="/reference/services/SoftLayer_Dns_Domain/createARecord">SoftLayer_Dns_Domain::createARecord</a></li>
</ul>
<h2 id="External_Links">External Links</h2>
<ul>
<li><a href="http://www.php.net/">PHP: Hypertext Processor</a></li>
<li><a href="http://github.com/softlayer/softlayer-api-php-client">The SoftLayer API PHP Client</a> at <a href="http://github.com">github</a></li>
</ul>