---
title: "Getting started with DNS"
description: "<p>Users interact with SoftLayer's authortative DNS servers through the <a href=/reference/services/SoftLayer_Dns_Domai"
date: "2013-04-25"
author: "phil"
tags:
    - "blog"
---

<p>Users interact with SoftLayer's authortative DNS servers through the <a href="/reference/services/SoftLayer_Dns_Domain/">SoftLayer_Dns_Domain</a> service. Each <a href="/reference/datatypes/SoftLayer_Dns_Domain/">SoftLayer_Dns_Domain</a> has a collection of <a href="/reference/services/SoftLayer_Dns_Domain_ResourceRecord/">SoftLayer_DNS_Domain_ResourceRecords</a> referenced by the resourceRecords relational property. While it is possible to interact with resource records through the <a href="/reference/services/SoftLayer_Dns_Domain/">SoftLayer_Dns_Domain</a> service, it is best to use the <a href="/reference/services/SoftLayer_Dns_Domain_ResourceRecord/">SoftLayer_Dns_Domain_ResourceRecord</a> service directly after initial zone creation.</p>
<h2>Domains</h2>
<h3>Listing</h3>
<p>A list of all domains currently hosted on the SoftLayer nameservers can be retrieved with <a href="/reference/services/SoftLayer_Account/getDomains">SoftLayer_Account::getDomains</a> which  returnr an array of <a href="/reference/datatypes/SoftLayer_Dns_Domain/">SoftLayer_Dns_Domain</a> template objects. You can extend this call to also pull the records associated with these domains with an <a href="/article/object mask">object mask</a>.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000088;">$client</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Account'</span><span style="color: #339933;">,</span> <span style="color: #000000; font-weight: bold;">null</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUser</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$objectMask</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">"mask.resourceRecords"</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">setObjectMask</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$objectMask</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$domains</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">getDomains</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<a href="http://www.php.net/print_r"><span style="color: #990000;">print_r</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$domains</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<h3>Creating</h3>
<p>To create a new zone, a <a href="/reference/datatypes/SoftLayer_Dns_Domain/">SoftLayer_Dns_Domain</a> template object must be created and passed into <a href="/reference/services/SoftLayer_Dns_Domain/createObject">SoftLayer_Dns_Domain::createObject</a>.  NS records for ns1.softlayer.com and ns2.softlayer.com are automatically added during creation. Include at least one A or AAAA record with the template object for successful creation. Domain serial numbers will be added/updated by the API so there is no need to include them in the template object.</p>
<p>The following properties are necessary when creating a <a href="/reference/datatypes/SoftLayer_Dns_Domain/">SoftLayer_Dns_Domain</a> object.</p>
<ul>
<li>name - Domain name including the TDL "example.com"</li>
<li>resourceRecords - An array of at least one <a href="/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord/">SoftLayer_Dns_Domain_ResourceRecord</a></li>
</ul>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000088;">$client</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Dns_Domain'</span><span style="color: #339933;">,</span> <span style="color: #000000; font-weight: bold;">null</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUser</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$template</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> stdClass<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$template</span><span style="color: #339933;">-></span><span style="color: #004000;">name</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">"createexample.com"</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$template</span><span style="color: #339933;">-></span><span style="color: #004000;">resourceRecords</span> <span style="color: #339933;">=</span> <a href="http://www.php.net/array"><span style="color: #990000;">array</span></a><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$template</span><span style="color: #339933;">-></span><span style="color: #004000;">resourceRecords</span><span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">0</span><span style="color: #009900;">&#93;</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> stdClass<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$template</span><span style="color: #339933;">-></span><span style="color: #004000;">resourceRecords</span><span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">0</span><span style="color: #009900;">&#93;</span><span style="color: #339933;">-></span><span style="color: #004000;">data</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'127.0.0.1'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$template</span><span style="color: #339933;">-></span><span style="color: #004000;">resourceRecords</span><span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">0</span><span style="color: #009900;">&#93;</span><span style="color: #339933;">-></span><span style="color: #004000;">host</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'server1'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$template</span><span style="color: #339933;">-></span><span style="color: #004000;">resourceRecords</span><span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">0</span><span style="color: #009900;">&#93;</span><span style="color: #339933;">-></span><span style="color: #004000;">type</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'a'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$result</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">createObject</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$template</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<a href="http://www.php.net/print_r"><span style="color: #990000;">print_r</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$result</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<p><a href="/reference/services/SoftLayer_Dns_Domain/createObject">SoftLayer_Dns_Domain::createObject</a> will return a fully populated <a href="/reference/datatypes/SoftLayer_Dns_Domain/">SoftLayer_Dns_Domain</a> object.</p>
<h3>Editing</h3>
<p>Modifying existing <a href="/reference/datatypes/SoftLayer_Dns_Domain/">SoftLayer_Dns_Domain</a> entries is not possible. Changes to zone names should be refactored to creation of new zones.</p>
<h3>Deleting</h3>
<p>Removal of a zone is accomplished with <a href="/reference/services/SoftLayer_Dns_Domain/deleteObject">SoftLayer_Dns_Domain::deleteObject</a>. This method requires only an init parameter be provided.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000088;">$domainId</span> <span style="color: #339933;">=</span> <span style="color: #cc66cc;">1545925</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$client</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Dns_Domain'</span><span style="color: #339933;">,</span> <span style="color: #000088;">$domainId</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUser</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$result</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">deleteObject</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<a href="http://www.php.net/print_r"><span style="color: #990000;">print_r</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$result</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<p><a href="/reference/services/SoftLayer_Dns_Domain/deleteObject">SoftLayer_Dns_Domain::deleteObject</a> returns a bool value: true for successful, false for failed.</p>
<h2>Records</h2>
<h3>Listing</h3>
<p>In addition to the method mentioned above domain resource records can be retrieved with <a href="/reference/services/SoftLayer_Dns_Domain/getResourceRecords">SoftLayer_Dns_Domain::getResourceRecords</a> which returns an array of <a href="/reference/datatypes/SoftLayer_Dns_DomainResourceRecord/">SoftLayer_Dns_DomainResourceRecord</a> objects.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000088;">$domainId</span> <span style="color: #339933;">=</span> <span style="color: #cc66cc;">12345</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$client</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Dns_Domain'</span><span style="color: #339933;">,</span> <span style="color: #000088;">$domainId</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUser</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$result</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">getResourceRecords</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<a href="http://www.php.net/print_r"><span style="color: #990000;">print_r</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$result</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<h3>Creating</h3>
<p>Creating records directly through the <a href="/reference/services/SoftLayer_Dns_Domain_ResourceRecord/">SoftLayer_Dns_Domain_ResourceRecord</a> service is accomplished by creating a <a href="/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord/">SoftLayer_Dns_Domain_ResourceRecord</a> template object and passing it into <a href="/reference/services/SoftLayer_Dns_Domain_ResourceRecord/createObject">SoftLayer_Dns_Domain_ResourceRecord::createObject</a>. The use of '@' in the host property denotes a wildcard hostname.</p>
<p>The SoftLayer DNS system supports these record types:</p>
<ul>
<li>a</li>
<li>aaaa</li>
<li>cname</li>
<li>mx</li>
<li>ns</li>
<li>ptr</li>
<li>soa</li>
<li>spf</li>
<li>srv</li>
<li>txt</li>
</ul>
<p>At minimum the template object must contain:</p>
<ul>
<li>data - value of the record</li>
<li>host - label to be added under the zone</li>
</ul>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000088;">$client</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Dns_Domain_ResourceRecord'</span><span style="color: #339933;">,</span> <span style="color: #000000; font-weight: bold;">null</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUser</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$domainId</span> <span style="color: #339933;">=</span> <span style="color: #cc66cc;">123456</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$template</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> stdClass<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$template</span><span style="color: #339933;">-></span><span style="color: #004000;">data</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'webserver01.example.com'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$template</span><span style="color: #339933;">-></span><span style="color: #004000;">host</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'www'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$template</span><span style="color: #339933;">-></span><span style="color: #004000;">type</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'cname'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$template</span><span style="color: #339933;">-></span><span style="color: #004000;">domainId</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$domainId</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$result</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">createObject</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$template</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<a href="http://www.php.net/print_r"><span style="color: #990000;">print_r</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$result</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<h3>Editing</h3>
<p>Edit resource records by passing a template object into <a href="/reference/services/SoftLayer_Dns_Domain_ResourceRecord/editObject">SoftLayer_Dns_Domain_ResourceRecord::editObject</a>. The template object must contain:</p>
<ul>
<li>id - identifier for the <a href="/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord/">SoftLayer_Dns_Domain_ResourceRecord</a> to be edited.</li>
<li>domainId - identifier of the <a href="/reference/datatypes/SoftLayer_Dns_Domain/">SoftLayer_Dns_Domain</a> this <a href="/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord/">resource record</a> is a child to</li>
<li>properties to be changed<br />
<b>Note:</b> Domain serial numbers will be updated by the API automatically.</li>
</ul>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000088;">$domainId</span> <span style="color: #339933;">=</span> <span style="color: #cc66cc;">45567</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$resourceRecordId</span> <span style="color: #339933;">=</span> <span style="color: #cc66cc;">1234</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$client</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Dns_Domain_ResourceRecord'</span><span style="color: #339933;">,</span> <span style="color: #000088;">$resourceRecordId</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUser</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$template</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> stdClass<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$template</span><span style="color: #339933;">-></span><span style="color: #004000;">id</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$resourceRecordId</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$template</span><span style="color: #339933;">-></span><span style="color: #004000;">domainId</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$domainId</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$template</span><span style="color: #339933;">-></span><span style="color: #004000;">data</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'127.0.0.1'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$template</span><span style="color: #339933;">-></span><span style="color: #004000;">host</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'server01'</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$result</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">editObject</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$template</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<a href="http://www.php.net/print_r"><span style="color: #990000;">print_r</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$result</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<p>It is also necessary to populate the <a href="/article/init params">init params</a> with the resource records id property. A bool is returned by <a href="/reference/services/SoftLayer_Dns_Domain_ResourceRecord/editObject">SoftLayer_Dns_Domain_ResourceRecord::editObject</a></p>
<h3>Deleting</h3>
<p>Removal of a record is accomplished with <a href="/reference/services/SoftLayer_Dns_Domain_ResourceRecord/deleteObject">SoftLayer_Dns_Domain_ResourceRecord::deleteObject</a>. This method requires only an init parameter be provided.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000088;">$recordId</span> <span style="color: #339933;">=</span> <span style="color: #cc66cc;">1545925</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$client</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Dns_Domain_ResourceRecord'</span><span style="color: #339933;">,</span> <span style="color: #000088;">$recordId</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUser</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$result</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">deleteObject</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<a href="http://www.php.net/print_r"><span style="color: #990000;">print_r</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$result</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<p><a href="/reference/services/SoftLayer_Dns_Domain_ResourceRecord/deleteObject">SoftLayer_Dns_Domain_ResourceRecord::deleteObject</a> returns a bool value: true for successful, false for failed.</p>

