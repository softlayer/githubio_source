---
title: "The CCI VLAN Specification"
description: "<p>When ordering a CCI on our shopping cart you are currently unable to specify a VLAN. While there are exceptions in pl"
date: "2012-03-09"
author: "phil"
tags:
    - "blog"
---

<p>When ordering a CCI on our shopping cart you are currently unable to specify a VLAN. While there are exceptions in place for things like VLAN-bound firewalls and load balancers, there are a number of situations outside of those in which a shared VLAN is preferable. Good news - when placing an order via the API this is something that can be accomplished!</p>
<p>When populating the virtualGuests property of a <a href="/reference/datatypes/SoftLayer_Container_Product_Order_Virtual_Guest/">SoftLayer_Container_Product_Order_Virtual_Guest</a> you need to create an array of SoftLayer_Virtual_Guest.  Normally during this process you only need to provide a hostname and domain. However when placing an order with a specific VLAN in mind you will need to also include the VLAN id by defining primaryNetworkComponent->networkVlan->id or primaryBackendNetworkComponent->networkVlan->id .</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;">virtualGuets <span style="color: #66cc66;">=</span> <span style="color: black;">&#91;</span>
    <span style="color: black;">&#123;</span>
        <span style="color: #483d8b;">'hostname'</span> : <span style="color: #483d8b;">'testhost'</span><span style="color: #66cc66;">,</span>
        <span style="color: #483d8b;">'domain'</span> : <span style="color: #483d8b;">'example.org'</span><span style="color: #66cc66;">,</span>
\t ‘primaryNetworkComponent: <span style="color: black;">&#123;</span>
\t\t‘networkVlan’: <span style="color: black;">&#123;</span>
\t\t\t‘<span style="color: #008000;">id</span>’: <span style="color: #ff4500;">1234</span>
\t\t<span style="color: black;">&#125;</span>
\t <span style="color: black;">&#125;</span>
    <span style="color: black;">&#125;</span>
<span style="color: black;">&#93;</span></pre></div>
<p>I am going to assume that you, like myself do not carry around a little black book containing your VLAN information and suggest using an IP address which already exists on the target VLAN as a parameter to <a href="/reference/services/SoftLayer_Network_Vlan/getVlanForIpAddress">SoftLayer_Network_Vlan::getVlanForIpAddress</a>.</p>
<p>You could even use an object mask and an existing server as a shortcut:</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;"><?php</span>
<span style="color: #000088;">$client</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Hardware_Server'</span><span style="color: #339933;">,</span> <span style="color: #000088;">$serverId</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUsername</span><span style="color: #339933;">,</span>  <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$mask</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> SoftLayer_ObjectMask<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$mask</span><span style="color: #339933;">-></span><span style="color: #004000;">primaryNetworkComponent</span><span style="color: #339933;">-></span><span style="color: #004000;">primarySubnet</span><span style="color: #339933;">-></span><span style="color: #004000;">networkVlan</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">setObjectMask</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$mask</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
try <span style="color: #009900;">&#123;</span> 
    <span style="color: #000088;">$vlanId</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">getObject</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">-></span><span style="color: #004000;">primaryNetworkComponent</span><span style="color: #339933;">-></span><span style="color: #004000;">primarySubnet</span><span style="color: #339933;">-></span><span style="color: #004000;">networkVlan</span><span style="color: #339933;">-></span><span style="color: #004000;">id</span><span style="color: #339933;">;</span>
    <a href="http://www.php.net/print_r"><span style="color: #990000;">print_r</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$vlanId</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span> catch <span style="color: #009900;">&#40;</span>Exception <span style="color: #000088;">$e</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
    <a href="http://www.php.net/print"><span style="color: #990000;">print</span></a> <span style="color: #000088;">$e</span><span style="color: #339933;">-></span><span style="color: #004000;">getMessage</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span></pre></div>

