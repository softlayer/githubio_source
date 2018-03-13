---
title: "Nessus Security Scans Using the SoftLayer API"
description: "<p>SoftLayer offers free vulnerability scans with all servers. When utilized through the customer portal, it will run a "
date: "2014-04-15"
author: "jmarhee"
tags:
    - "blog"
---

<p>SoftLayer offers free vulnerability scans with all servers. When utilized through the customer portal, it will run a scan on the primary IP for the given server. Because vulnerabilities and misconfiguration are a fact of life in server administration, SoftLayer recommends running scan regularly to keep you you up-to-date on security risks that may impact your server.</p>
<p>Automating regular vulnerability scans can become effortless when using the SoftLayer API.</p>
<p>Using the SoftLayer API, the <a href="/reference/services/SoftLayer_Network_Security_Scanner_Request/">SoftLayer_Network_Security_Scanner_Request</a> service can scan any IP address belonging to your account (primary IPs, portable IPs, Static secondary IPs). Below is an example of a CLI script, where the IP you’d like as the target is passed as a command-line argument:</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #b1b100;">require_once</span> <a href="http://www.php.net/dirname"><span style="color: #990000;">dirname</span></a><span style="color: #009900;">&#40;</span><span style="color: #000000; font-weight: bold;">__FILE__</span><span style="color: #009900;">&#41;</span> <span style="color: #339933;">.</span> <span style="color: #0000ff;">'/softlayer-api-php-client/SoftLayer/SoapClient.class.php'</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$user</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">""</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$key</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">""</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$ip</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$argv</span><span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">1</span><span style="color: #009900;">&#93;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$accountClient</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Account'</span><span style="color: #339933;">,</span> <span style="color: #000000; font-weight: bold;">Null</span><span style="color: #339933;">,</span> <span style="color: #000088;">$user</span><span style="color: #339933;">,</span> <span style="color: #000088;">$key</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$account</span> <span style="color: #339933;">=</span> accountClient<span style="color: #339933;">.</span>getObject<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$scanClient</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Network_Security_Scanner_Request'</span><span style="color: #339933;">,</span> <span style="color: #000000; font-weight: bold;">Null</span><span style="color: #339933;">,</span> <span style="color: #000088;">$user</span><span style="color: #339933;">,</span> <span style="color: #000088;">$key</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #666666; font-style: italic;">//The class requires, at least, the following two parameters</span>
<span style="color: #000088;">$scanTemplate</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> stdClass<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$scanTemplate</span><span style="color: #339933;">-></span><span style="color: #004000;">accountId</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$account</span><span style="color: #339933;">-></span><span style="color: #004000;">id</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$scanTemplate</span><span style="color: #339933;">-></span><span style="color: #004000;">ipAddress</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$ip</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$scanner</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$scanClient</span><span style="color: #339933;">-></span><span style="color: #004000;">createObject</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$scanTemplate</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<p>Above, you are creating a <a href="/reference/datatypes/SoftLayer_Network_Security_Scanner_Request/">SoftLayer_Network_Security_Scanner_Request</a> template object, and defining the target IP and your SoftLayer account ID.</p>
<p>Now that you’ve started the scan, the status of a any given scan can be checked with its ID and <a href="/reference/services/SoftLayer_Network_Security_Scanner_Request/getStatus">SoftLayer_Network_Security_Scanner_Request::getStatus</a>:</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000088;">$scanner</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$scanClient</span><span style="color: #339933;">-></span><span style="color: #004000;">getStatus</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$scanID</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span> </pre></div>
<p>The benefit of this approach to vulnerability scanning is that you can scan your secondary addresses or virtual machines (for those of us hosting a private cloud on SoftLayer) for a more complete security plan.</p>
<p>Your scans will be available to you through the customer portal once they are complete. They’ll define any perceived vulnerabilities or possible exploitation points for your server so you and your administration team can keep everything running smoothly and securely.</p>
<p>-Joseph</p>

