---
title: "SSL Management"
description: "Working with SSL certs"
date: "2012-03-28"
tags:
    - "article"
    - "sldn"
    - "ssl"
---



<p>3/14/2012: Added the ability to provide SSL offloading to the local Load Balancing service in Softlayer. The load balancing service allows you to manage the offload capability, as well as, access the SSL certificate manager. In order to utilize SSL offloading, a load balancer must be purchased that offers the capability.</p>
<p>The <a href="/reference/services/SoftLayer_Security_Certificate/">SoftLayer_Security_Certificate</a> service provides access to the new certificate manager. There are no restrictions on the number or origin of certificates, so please feel free to use it as a centralized storage location for all of your SSL certificates.</p>
<p>The following examples assume instantiation of the client as follows:</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;"><?php</span>
<span style="color: #000088;">$client</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Security_Certificate'</span><span style="color: #339933;">,</span> <span style="color: #000000; font-weight: bold;">null</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUsername</span><span style="color: #339933;">,</span>  <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<h3>Creating Certificates</h3>
<p>Entering a new SSL certificate into the certificate manager is accomplished by sending a <a href="/reference/datatypes/SoftLayer_Security_Certificate/">SoftLayer_Security_Certificate templateObject</a> to <a href="/reference/services/SoftLayer_Security_Certificate/createObject">SoftLayer_Security_Certificate::createObject</a>. We do not need to define common name, organization name or validity dates as the certificate manager will extrapolate them from the provided certificate. This method will ensure the  information is correct by attempting validation between the certificate, private key and intermediate certificate if provided.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;"><?php</span>
<span style="color: #000088;">$templateObject</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> stdClass<span style="color: #339933;">;</span>
&nbsp;
<span style="color: #666666; font-style: italic;">// Populate the certificate and private key.</span>
<span style="color: #666666; font-style: italic;">// Please include -----BEGIN/END ----- delimiters</span>
<span style="color: #000088;">$templateObject</span><span style="color: #339933;">-></span><span style="color: #004000;">certificate</span> <span style="color: #339933;">=</span> <span style="color: #339933;"><</span>Enter Security Certificate Here<span style="color: #339933;">>;</span>
<span style="color: #000088;">$templateObject</span><span style="color: #339933;">-></span><span style="color: #004000;">privateKey</span> <span style="color: #339933;">=</span> <span style="color: #339933;"><</span>Enter <span style="color: #000000; font-weight: bold;">Private</span> <a href="http://www.php.net/key"><span style="color: #990000;">Key</span></a> Here<span style="color: #339933;">>;</span>
&nbsp;
<span style="color: #666666; font-style: italic;">// If the certificate authority issues provided an intermediate certificate</span>
<span style="color: #666666; font-style: italic;">// you will need to include it here.</span>
<span style="color: #000088;">$templateObject</span><span style="color: #339933;">-></span><span style="color: #004000;">intermediateCertificate</span> <span style="color: #339933;">=</span> <span style="color: #339933;"><</span>Enter Intermediate Certificate Here<span style="color: #339933;">>;</span>
&nbsp;
<span style="color: #666666; font-style: italic;">// Optional</span>
<span style="color: #000088;">$templateObject</span><span style="color: #339933;">-></span><span style="color: #004000;">certificateSigningRequest</span> <span style="color: #339933;">=</span> <span style="color: #339933;"><</span>Enter CSR Here<span style="color: #339933;">>;</span>
&nbsp;
try <span style="color: #009900;">&#123;</span> 
    <span style="color: #000088;">$newCertificate</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">createObject</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$templateObject</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
    <a href="http://www.php.net/print_r"><span style="color: #990000;">print_r</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$newCertificate</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span> catch <span style="color: #009900;">&#40;</span>Exception <span style="color: #000088;">$e</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
    <a href="http://www.php.net/print"><span style="color: #990000;">print</span></a> <span style="color: #0000ff;">"Certificate creation failed: "</span> <span style="color: #339933;">.</span> <span style="color: #000088;">$e</span><span style="color: #339933;">-></span><span style="color: #004000;">getMessage</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span></pre></div>
<h3>Editing Certificates</h3>
<p>SSL certficiate manager entries can be modified with <a href="/reference/services/SoftLayer_Security_Certificate/editObject">SoftLayer_Security_Certificate::editObject</a>. Please keep in mind that certificates will only be available for modification if there are no services associated with them. As with createObject you need to pass a <a href="/reference/datatypes/SoftLayer_Security_Certificate/">SoftLayer_Security_Certificate templateObject</a> but this time with only the changed properties defined.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;"><?php</span>
<span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">setInitParameter</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$certificateId</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$certificate</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">getObject</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #b1b100;">if</span> <span style="color: #009900;">&#40;</span><span style="color: #000088;">$certificate</span><span style="color: #339933;">-></span><span style="color: #004000;">associatedServiceCount</span> <span style="color: #339933;">></span> <span style="color: #cc66cc;">0</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
    <a href="http://www.php.net/print"><span style="color: #990000;">print</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">"Please disassociate this certificate with all services before modifying"</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
    <span style="color: #b1b100;">return</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span>
&nbsp;
<span style="color: #000088;">$templateObject</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> stdClass<span style="color: #339933;">;</span>
<span style="color: #000088;">$templateObject</span><span style="color: #339933;">></span>notes <span style="color: #339933;">=</span> ‘Let this be noted<span style="color: #339933;">!</span>’<span style="color: #339933;">;</span>
&nbsp;
try <span style="color: #009900;">&#123;</span> 
    <span style="color: #000088;">$result</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$client</span><span style="color: #339933;">-></span><span style="color: #004000;">editObject</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$templateObject</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
    <a href="http://www.php.net/print_r"><span style="color: #990000;">print_r</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$result</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span> catch <span style="color: #009900;">&#40;</span>Exception <span style="color: #000088;">$e</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
    <a href="http://www.php.net/print"><span style="color: #990000;">print</span></a> <span style="color: #0000ff;">"Certificate modification failed: "</span> <span style="color: #339933;">.</span> <span style="color: #000088;">$e</span><span style="color: #339933;">-></span><span style="color: #004000;">getMessage</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span></pre></div>
<h3>Load Balancer Integration</h3>
<p>If you have singed up for the SSL offloading service it is not inconceivable that associating your newly created SSL certificate with your load balancer may be advantageous. After purchasing a load balancer with SSL offload capability and adding your certificate <a href="/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/editObject">SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress::editObject</a> will be used to update your load balancer with the new certificate ID. This is accomplished by populating the securityCertificateId property in your <a href="/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/">templateObject</a>.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;"><?php</span>
<span style="color: #000088;">$virtualIpAddressClient</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress'</span><span style="color: #339933;">,</span> <span style="color: #000088;">$virtualIpAddressId</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUsername</span><span style="color: #339933;">,</span>  <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$templateObject</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> stdClass<span style="color: #339933;">;</span>
<span style="color: #000088;">$templateObject</span><span style="color: #339933;">-></span><span style="color: #004000;">securityCertificateId</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$certificateId</span><span style="color: #339933;">;</span>
try <span style="color: #009900;">&#123;</span> 
    <span style="color: #000088;">$result</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$virtualIpAddressClient</span><span style="color: #339933;">-></span><span style="color: #004000;">editObject</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$templateObject</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
    <a href="http://www.php.net/print_r"><span style="color: #990000;">print_r</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$result</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span> catch <span style="color: #009900;">&#40;</span>Exception <span style="color: #000088;">$e</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
    <a href="http://www.php.net/print"><span style="color: #990000;">print</span></a> <span style="color: #0000ff;">"Certificate association failed: "</span> <span style="color: #339933;">.</span> <span style="color: #000088;">$e</span><span style="color: #339933;">-></span><span style="color: #004000;">getMessage</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span></pre></div>
<p><a href="/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/startSsl">SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress::startSsl</a> and <a href="/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/stopSsl">SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress::stopSsl</a> are used to toggle the SSL offloading service and the bool property sslActiveFlag will show the current state of the offloading service. The toggleSsl function below will use the current state of sslActiveFlag to determine the approprate API call. If necessary you can also use the sslEnabledFlag to determine if a specific VIP has SSL offloading available for use.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;"><?php</span>
<span style="color: #000000; font-weight: bold;">function</span> toggleSsl<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
    <span style="color: #000088;">$virtualIpAddressClient</span> <span style="color: #339933;">=</span> SoftLayer_SoapClient<span style="color: #339933;">::</span><span style="color: #004000;">getClient</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress'</span><span style="color: #339933;">,</span> <span style="color: #000088;">$virtualIpAddressId</span><span style="color: #339933;">,</span> <span style="color: #000088;">$apiUsername</span><span style="color: #339933;">,</span>  <span style="color: #000088;">$apiKey</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
    <span style="color: #000088;">$action</span> <span style="color: #339933;">=</span> <span style="color: #009900;">&#40;</span><span style="color: #000088;">$virtualIpAddressClient</span><span style="color: #339933;">::</span><span style="color: #004000;">getObject</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">-></span><span style="color: #004000;">sslActiveFlag</span><span style="color: #009900;">&#41;</span> ? <span style="color: #0000ff;">'stopSsl'</span> <span style="color: #339933;">:</span> <span style="color: #0000ff;">'startSsl'</span><span style="color: #339933;">;</span>
&nbsp;
    try <span style="color: #009900;">&#123;</span> 
        <span style="color: #000088;">$result</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$virtualIpAddressClient</span><span style="color: #339933;">-></span><span style="color: #000088;">$action</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
        <a href="http://www.php.net/print_r"><span style="color: #990000;">print_r</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$result</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
    <span style="color: #009900;">&#125;</span> catch <span style="color: #009900;">&#40;</span>Exception <span style="color: #000088;">$e</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
        <a href="http://www.php.net/print"><span style="color: #990000;">print</span></a> <span style="color: #0000ff;">"<span style="color: #006699; font-weight: bold;">$action</span> failed: "</span> <span style="color: #339933;">.</span> <span style="color: #000088;">$e</span><span style="color: #339933;">-></span><span style="color: #004000;">getMessage</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
    <span style="color: #009900;">&#125;</span>
<span style="color: #009900;">&#125;</span></pre></div>