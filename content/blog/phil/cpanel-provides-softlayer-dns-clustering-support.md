---
title: "cPanel Provides SoftLayer DNS Clustering Support"
description: "<p>Since the release of <a href=http://www.cpanel.net/2011/08/cpanel-expands-its-dns-cluster-functionality-with-softlay"
date: "2011-09-26"
author: "phil"
tags:
    - "blog"
---

<p>Since the release of <a href="http://www.cpanel.net/2011/08/cpanel-expands-its-dns-cluster-functionality-with-softlayer-and-vpsnet.html">cPanel & WHM 11.30</a>, users of the control panel have had the ability to incorporate the native DNS Cluster Management with DNS services offered by SoftLayer and UK2Group (under the brand VPS.NET). While the benefits utilizing a geographically diverse and scalable DNS architecture merit a <a href="http://blog.softlayer.com/2010/dns-from-all-angles/">post</a> dedicated to them, it is the implementation of this feature which has caught my attention.<br />
Simply providing a SLAPI user with DNS management permissions and its associated SLAPI key allows cPanel to seamlessly integrate interaction with the SoftLayer DNS infrastructure. Once the straightforward setup is complete, any zones currently on SoftLayer's DNS servers will be available for administration.</p>
<p>All of this was accomplished with the same tools and APIs exposed to our entire customer base; no special endpoints or services were needed to utilize the API in this manner. Below is one piece of the DNS management puzzle: an example of how to create an A record on an existing zone using the <a href="https://github.com/softlayer/softlayer-api-php-client">SoftLayer PHP SOAP client</a>.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;"><?php</span>
<span style="color: #666666; font-style: italic;">// Set our API User/Key information and the ID of our domain</span>
<span style="color: #000088;">$apiUsername</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'SET ME'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$apiKey</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'SET ME'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$domainId</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'SET ME'</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #666666; font-style: italic;">// Create a SLAPI client for the SoftLayer_Dns_Domain_ResourceRecord service</span>
<span style="color: #000088;">$client</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Dns_Domain_ResourceRecord'</span><span style="color: #339933;">,</span> <span style="color: #000088;">$domainId</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUsername</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #666666; font-style: italic;">// SoftLayer_Dns_Domain_ResourceRecord::createObject expects an object with specific properties defined</span>
<span style="color: #000088;">$newRecord</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> stdObject<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$newRecord</span><span style="color: #339933;">-></span><span style="color: #004000;">data</span> <span style="color: #339933;">=></span> <span style="color: #0000ff;">'127.0.0.1'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$newRecord</span><span style="color: #339933;">-></span><span style="color: #004000;">host</span> <span style="color: #339933;">=></span> <span style="color: #0000ff;">'hostname'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$newRecord</span><span style="color: #339933;">-></span><span style="color: #004000;">domainId</span> <span style="color: #339933;">=></span> <span style="color: #000088;">$domainId</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$newRecord</span><span style="color: #339933;">-></span><span style="color: #004000;">ttl</span> <span style="color: #339933;">=></span> <span style="color: #cc66cc;">990</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$newRecord</span><span style="color: #339933;">-></span><span style="color: #004000;">type</span> <span style="color: #339933;">=></span> <span style="color: #0000ff;">'a'</span><span style="color: #339933;">;</span>
&nbsp;
try <span style="color: #009900;">&#123;</span>
                <span style="color: #000088;">$result</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">createObject</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$newRecord</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
                <a href="http://www.php.net/print_r"><span style="color: #990000;">print_r</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$result</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span> catch <span style="color: #009900;">&#40;</span>Exception <span style="color: #000088;">$e</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
                <a href="http://www.php.net/die"><span style="color: #990000;">die</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">"Record creation failed: <span style="color: #006699; font-weight: bold;">$e->getMessage</span>()"</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span></pre></div>

