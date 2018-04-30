---
title: "REST"
description: "Getting started with REST API calls"
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
---


<p>SoftLayer provides a RESTful API in addition to RPC-style API services. Use the REST API in cases where your programming language may not have good SOAP or XML-RPC support but can perform simple HTTP protocol actions and can interpret XML or JSON data.</p>
<script type="text/javascript">toc_collapse=0;</script><div class="toc" id="toc8">
<div class="toc-title">Table of contents<span class="toc-toggle-message">&nbsp;</span></div>
<div class="toc-list">
<ol>
<li class="toc-level-1"><a href="#REST_URLs">REST URLs</a></li>
<li class="toc-level-1"><a href="#HTTP_Request_Types">HTTP Request Types</a>
<ol>
<li class="toc-level-2"><a href="#DELETE">DELETE</a></li>
<li class="toc-level-2"><a href="#GET">GET</a></li>
<li class="toc-level-2"><a href="#POST">POST</a></li>
<li class="toc-level-2"><a href="#PUT">PUT</a></li>
</ol>
</li>
<li class="toc-level-1"><a href="#Passing_Method_Parameters">Passing Method Parameters</a></li>
<li class="toc-level-1"><a href="#Alternate_Ways_to_Set_Parameter_and_Return_Formats">Alternate Ways to Set Parameter and Return Formats</a></li>
<li class="toc-level-1"><a href="#Using_Object_Masks">Using Object Masks</a></li>
<li class="toc-level-1"><a href="#Using_Result_Limits">Using Result Limits</a></li>
<li class="toc-level-1"><a href="#Error_Handling">Error Handling</a>
<ol>
<li class="toc-level-2"><a href="#Authentication_Errors">Authentication Errors</a></li>
</ol>
</li>
<li class="toc-level-1"><a href="#Caveats">Caveats</a>
<ol>
<li class="toc-level-2"><a href="#Specifying_Complex_Types">Specifying Complex Types</a></li>
</ol>
</li>
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
<p></p>
<h2 id="REST_URLs">REST URLs</h2>
<p>REST API URLs are structured to easily traverse SoftLayer's object hierarchy. A basic REST request is structured as follows:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://[username]:[apiKey]@api.[service.]softlayer.com/rest/v3/[serviceName]/[initializationParameter].[returnDatatype]</pre></div>
<ul>
<li>All REST requests, even private network requests, must be passed through HTTP SSL.</li>
<li>Use your API username and key to authenticate your request through HTTP authentication.</li>
<li>The base hostname and folder name for a REST request is either <tt>api.softlayer.com/rest/v3/</tt> or <tt>api.service.softlayer.com/rest/v3/</tt>. Use <tt>api.service.softlayer.com/rest/v3/</tt> to access the REST API over SoftLayer's private network. It's a more secure way to communicate with SoftLayer, but the system making API calls must be on SoftLayer's private network (either purchased from SoftLayer of logged into SoftLayer's private network VPN).</li>
<li>Follow up the base URL with the name of the API service you wish to call, for instance "SoftLayer_Account" or "SoftLayer_Hardware_Server".</li>
<li>If your API request requires an initialization parameter then add a slash followed by your init parameter id to your URL.</li>
<li>The SoftLayer REST API can return either XML or JSON formatted output. Add ".xml" or ".json" to the end of your request to specify which format you'd like to receive data in.</li>
</ul>
<p>A request like this calls the <tt>getObject()</tt> method of the API service you're trying to call. <a href="/reference/services/SoftLayer_Account/getObject">SoftLayer_Account::getObject</a> doesn't require an initialization parameter, so its REST URL looks like this:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Account.json</pre></div>
<p>However, to call the <a href="/reference/services/SoftLayer_Hardware_Server/getObject">getObject()</a> method for a specific <a href="/reference/services/SoftLayer_Hardware_Server/">SoftLayer_Hardware_Server</a> record use the following URL, assuming "1234" is the id of the server you wish to retrieve:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Hardware_Server/1234.json</pre></div>
<p>
Call API methods other than <tt>getObject()</tt> by placing the method's name after your initialization parameter. If your method begins with "get", then remove the word "get" from the method name and convert it's first letter to uppercase. This method can also be used to quickly access an object's relational properties. For instance, the <a href="/reference/services/SoftLayer_Account/getHardware">getHardware()</a> method and <tt>hardware</tt> relational property in the SoftLayer_Account API service can be reached at:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Account/Hardware.json</pre></div>
<p>Similarly, a server's network components can be reached at the following URL:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Hardware_Server/1234/NetworkComponents.json</pre></div>
<p>
Chain a combination of initialization parameter ids and relational properties to drill down into specific object components. Every id added will drill into that specific relational property. For instance, if you wish to get server 1234's network component with id 5678 use the URL:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Hardware_Server/1234/NetworkComponents/5678.json</pre></div>
<p>And to get that network component's uplink connection:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Hardware_Server/1234/NetworkComponents/5678/uplinkNetworkComponents.json</pre></div>
<h2 id="HTTP_Request_Types">HTTP Request Types</h2>
<h3 id="DELETE">DELETE</h3>
<p>Use an HTTP DELETE request to delete an object instead of a service's <tt>deleteObject()</tt> method. For instance, pass an HTTP DELETE request to the following URL in order to remove domain record 1234 from SoftLayer's DNS servers.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Dns_Domain/1234.json</pre></div>
<h3 id="GET">GET</h3>
<p>Use HTTP GET requests for simple object retrieval and method calls. For instance, retrieve domain record id 1234 with an HTTP GET request to the URL:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Dns_Domain/1234.json</pre></div>
<h3 id="POST">POST</h3>
<p>Use an HTTP POST request to create an object instead of a service's <tt>createObject()</tt> or <tt>createObjects()</tt> methods. POST a single JSON or XML structure containing a single element called "parameters" containing your object's skeleton structure and any orther parameters required by your API service's <tt>createObject()</tt> method. For instance, pass an HTTP POST request with the following data to the following URL in order to create a domain record in SoftLayer's DNS servers.</p>
<div class="geshifilter">
<pre class="xml geshifilter-xml" style="font-family:monospace;">{
    "parameters" : [
        {
            "name" : "example.org",
            "resourceRecords" : [
                {
                    "type" : "a",
                    "host" : "@",
                    "data" : "127.0.0.1"
                }
            ]
        }
    ]
}</pre></div>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Dns_Domain.json</pre></div>
<h3 id="PUT">PUT</h3>
<p>Use an HTTP PUT request to edit an object instead of a service's <tt>editObject()</tt> or <tt>editObjects()</tt> methods. PUT a single JSON or XML structure containing a single element called "parameters" containing your object's skeleton structure and any orther parameters required by your API service's <tt>editObject()</tt> method. For instance, pass an HTTP PUT request with the following data to the following URL in order to edit domain resource record 5678 within domain record 1234 on SoftLayer's DNS servers, changing its <tt>data</tt> to "10.0.0.1".</p>
<div class="geshifilter">
<pre class="xml geshifilter-xml" style="font-family:monospace;">{
    "parameters" : [
        {
            "data" : "10.0.0.1",
        }
    ]
}</pre></div>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Dns_Domain/1234/ResourceRecords/5678.json</pre></div>
<h2 id="Passing_Method_Parameters">Passing Method Parameters</h2>
<p>Parameters are passed in our REST API by appending each to the path of the <a href="http://en.wikipedia.org/wiki/Uniform_Resource_Locator#Syntax">URL</a>.<br />
These should be passed in the same order they are listed in the documentation for each method, from top to bottom.</p>
<p>For example <a href="/reference/services/SoftLayer_Monitoring_Agent/setActiveAlarmSubscriber">SoftLayer_Monitoring_Agent::setActiveAlarmSubscriber</a> requires the userRecordId parameter:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Monitoring_Agent/1234/setActiveAlarmSubscriber/5678.json</pre></div>
<p>Some methods will request a single parameter which is an array such as <a href="/reference/services/SoftLayer_Dns_Domain_ResourceRecord/createObjects">SoftLayer_Dns_Domain_ResourceRecord::createObjects</a>:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;"> {
  "parameters":
    [
      [
        {"host":"hosta","data":"127.0.0.1","ttl":"900","type":"a","domainId":"1234"}
        ,
        {"host":"hostb","data":"127.0.0.1","ttl":"900","type":"a","domainId":"1234"}
      ]
    ]
}</pre></div>
<h2 id="Alternate_Ways_to_Set_Parameter_and_Return_Formats">Alternate Ways to Set Parameter and Return Formats</h2>
<p>In addition to adding ".json" and ".xml" to your REST URL you can also set API call return formats by passing a MIME-type (<tt>application/json</tt> for JSON and <tt>text/xml</tt>for XML)  in HTTP <tt>Accept</tt> or <tt>Content-Type</tt> headers in your request.</p>
<h2 id="Using_Object_Masks">Using Object Masks</h2>
<p>Create an <a href="/article/object mask">object mask</a> in your API call URL by adding an <tt>objectMask</tt> variable to your query string. Object masks are a semicolon delineated list of relational properties, with chained relational properties separated by periods. In order to save space in the query string, REST object masks are relative to the data type at the end of your URL instead of the API service you're querying. Likewise, REST object masks don't contain a <tt>mask</tt> property.</p>
<p>The following URL creates an object mask that retrieves an account's hardware records along with the datacenters that hardware is located in. Note that the object mask only contains the relational property we want to retrieve related to hardware, not our account.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Account/Hardware.json?objectMask=datacenter</pre></div>
<p>
This URL gets an account's hardware records along with that hardware's associated datacenter, operating system, and network component records. Note that these relational items are separate by semicolons.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Account/Hardware.json?objectMask=datacenter;operatingSystem;networkComponents</pre></div>
<p>
This URL gets an account's hardware records along with that hardware's associated datacenter, operating system, operating system password, and network component records. Chained relational properties are separated by periods.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Account/Hardware.json?objectMask=datacenter;operatingSystem.passwords;networkComponents</pre></div>
<p>
The REST API can handle object masks in a slightly different way than SoftLayer's SOAP And XML-RPC APIs. REST object masks can be made to filter local data type properties retrieved form the SoftLayer API. If you define a local property in your mask, then the SoftLayer API treats your mask as a filter, and will only retrieve the local properties specified in your mask. For example, this URL retrieves only the id and hostnameproperties in an account's hardware records:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Account/Hardware.json?objectMask=hardware.id;hardware.hostname</pre></div>
<h2 id="Using_Result_Limits">Using Result Limits</h2>
<p>Limit the number of results in an API call by adding a <tt>resultLimit</tt> variable to your query string.  Set your <tt>resultLimit</tt> variable to a comma delineated set of two numbers:</p>
<ul>
<li>The offset to begin your result set at.</li>
<li>The number of results to limit your call to.</li>
</ul>
<p>This URL retrieves the first two tickets open on an account, calling the <a href="/reference/services/SoftLayer_Account/getOpenTickets">SoftLayer_Account::getOpenTickets</a> method:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Account/OpenTickets.json?resultLimit=0,2</pre></div>
<h2 id="Error_Handling">Error Handling</h2>
<p>The SoftLayer REST API returns XML or JSON output with a single <tt>error</tt> node containing any error messages returned by your API call. For instance, the URL to the nonexistent service:<br />
 <span class="geshifilter"><code class="text geshifilter-text">https://username:apiKey@api.softlayer.com/rest/v3/Nonexistent.xml</code></span><br />
returns the error:</p>
<div class="geshifilter">
<pre class="xml geshifilter-xml" style="font-family:monospace;"><span style="color: #009900;"><span style="color: #000000; font-weight: bold;"><root><span style="color: #000000; font-weight: bold;">></span></span></span>
   <span style="color: #009900;"><span style="color: #000000; font-weight: bold;"><error><span style="color: #000000; font-weight: bold;"></span></span></span>Service does not exist<span style="color: #009900;"><span style="color: #000000; font-weight: bold;"></error><span style="color: #000000; font-weight: bold;">></span></span></span>
<span style="color: #009900;"><span style="color: #000000; font-weight: bold;"></root><span style="color: #000000; font-weight: bold;">></span></span></span></pre></div>
<p>While it's JSON equivalent:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://username:apiKey@api.softlayer.com/rest/v3/Nonexistent.json</pre></div>
<p>returns the error:</p>
<div class="geshifilter">
<pre class="xml geshifilter-xml" style="font-family:monospace;">{
    "error": "Service does not exist"
}</pre></div>
<h3 id="Authentication_Errors">Authentication Errors</h3>
<p>The SoftLayer REST API returns an HTTP 401 Unauthorized error if an invalid username / API key combination is used when requesting a REST URL.</p>
<h2 id="Caveats">Caveats</h2>
<h3 id="Specifying_Complex_Types">Specifying Complex Types</h3>
<p>As with XML-RPC, the REST API cannot determine extended complex types in certain parameters. In these cases you should define a <tt>complexType</tt> property in your complex parameters set to the type of object you're sending to your method.</p>
<h2 id="Referenced_API_Components">Referenced API Components</h2>
<h3 id="Services">Services</h3>
<ul>
<li><a href="/reference/services/SoftLayer_Account/">SoftLayer_Account</a></li>
<li><a href="/reference/services/SoftLayer_Dns_Domain/">SoftLayer_Dns_Domain</a></li>
<li><a href="/reference/services/SoftLayer_Hardware_Server/">SoftLayer_Hardware_Server</a></li>
</ul>
<h3 id="Data_Types">Data Types</h3>
<ul>
<li><a href="/reference/datatypes/SoftLayer_Hardware_Server/">SoftLayer_Hardware_Server</a></li>
</ul>
<h3 id="Methods">Methods</h3>
<ul>
<li><a href="/reference/services/SoftLayer_Account/getHardware">SoftLayer_Account::getHardware</a></li>
</ul>
<h2 id="External_Links">External Links</h2>
<ul>
<li><a href="http://en.wikipedia.org/wiki/Representational_State_Transfer">Representational State Transfer</a> at <a href="http://en.wikipedia.org/">Wikipedia</a></li>
</ul>