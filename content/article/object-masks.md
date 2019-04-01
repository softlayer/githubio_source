---
title: "Object-Masks"
description: "How Object Masks work. Used to specify which relational properties you would like included in your query."
date: "2012-12-03"
tags:
    - "article"
    - "sldn"
    - "objectmask"
---

<script type="text/javascript">toc_collapse=0;</script><div class="toc" id="toc14">
<div class="toc-title">Table of contents<span class="toc-toggle-message">&nbsp;</span></div>
<div class="toc-list">
<ol>
<li class="toc-level-1"><a href="#Overview">Overview</a></li>
<li class="toc-level-1"><a href="#Structure">Structure</a>
<ol>
<li class="toc-level-2"><a href="#Root_Node">Root Node</a></li>
<li class="toc-level-2"><a href="#Property">Property</a></li>
<li class="toc-level-2"><a href="#Property_Set">Property Set</a></li>
<li class="toc-level-2"><a href="#Payload_reduction">Payload reduction</a></li>
<li class="toc-level-2"><a href="#Type">Type</a></li>
</ol>
</li>
<li class="toc-level-1"><a href="#Syntax">Syntax</a></li>
<li class="toc-level-1"><a href="#API_interaction">API interaction</a>
<ol>
<li class="toc-level-2"><a href="#SOAP">SOAP</a></li>
<li class="toc-level-2"><a href="#XML-RPC">XML-RPC</a></li>
<li class="toc-level-2"><a href="#REST">REST</a></li>
</ol>
</li>
<li class="toc-level-1"><a href="#Legacy_Object_Masks_"> Legacy Object Masks </a></li>
</ol>
</div>
</div>
<h2 id="Overview">Overview</h2>
<p>In order to obtain relational data from an object in the API you must declare an object mask in your API call. With standard object masks, relational data is pulled using a SOAP header, an XML-RPC struct or a GET parameter in REST. Extended object masks make use of a <a href="http://en.wikipedia.org/wiki/Domain-specific_language" target="_blank">Domain-specific language</a> to reduce the effort required to express what data should be returned from the API. In order to support this new method of object mask, a new input method has been added to each protocol.</p>
<h2 id="Structure">Structure</h2>
<h3 id="Root_Node">Root Node</h3>
<p>Extended object masks start from a "root node" which is a <a href=#Property_Set>property set</a> or a string of "mask" which acts as an alias for the object retuned by the API call. For example, when calling <a href="/reference/services/SoftLayer_Hardware/getObject">SoftLayer_Hardware::getObject</a> the root node "mask" will represent a <a href="/reference/datatypes/SoftLayer_Hardware/">SoftLayer_Hardware Object</a>.</p>
<p>So if we were to send "<span class="geshifilter"><code class="text geshifilter-text">mask</code></span>" as our object mask for SoftLayer_Hardware::getObject, the entire SoftLayer_Hardware object would be returned as if no mask was included.</p>
<h3 id="Property">Property</h3>
<p>A property can be the name of any local or relational property of the returned object type and is appended to the mask with a peroid: "<span class="geshifilter"><code class="text geshifilter-text">.</code></span>".</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">mask.networkComponents</pre></div>
<p>The above object mask used when calling SoftLayer_Hardware::getObject will return the SoftLayer_Hardware object, in addition to an array "networkComponents" containing the SoftLayer_Network_Components associated with that hardware.</p>
<p>It is possible to chain together multiple properties in order to drill down and receive even relational properties of relational properties.  For example, if we wanted to receive a list of network components related to a specific hardware device, a list of VLANs related to those network components and even the primary subnet of each of those VLANs we could use an object mask:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">mask.networkComponents.networkVlans.primarySubnet</pre></div>
<p>Multiple properties may be defined by listing in the object mask separated by a comma.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">mask.networkComponents,mask.primaryIpAddress,mask.billingItem</pre></div>
<h3 id="Property_Set">Property Set</h3>
<p>Property sets can be used as an alternative to listing out each property from its root node. A property set is used to declare a list of properties to obtain from an object and is helpful for reducing the verbosity of an object mask.</p>
<p>A property set is a comma-separated list of properties enclosed in brackets <span class="geshifilter"><code class="text geshifilter-text">[</code></span> <span class="geshifilter"><code class="text geshifilter-text">]</code></span> which follows a property name.</p>
<p>The following masks can be considered equivalent:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">[mask.id,mask.fullyQualifiedDomainName,mask.networkComponents.networkHardware,mask.networkComponents.uplinkComponent]</pre></div>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">mask 
[
    id,fullyQualifiedDomainName,networkComponents [
        networkHardware,uplinkComponent
    ]
]</pre></div>
<h3 id="Payload_reduction">Payload reduction</h3>
<p>Any local properties defined in a mask will result in the API returning only the specified local properties of the object. This feature allows for reduction of the API return data size and can help avoid the need for pagination or additional complication.</p>
<p>For example, when invoking <a href="/reference/services/SoftLayer_Hardware/getObject">SoftLayer_Hardware::getObject</a> the following mask may be used to retrieve only the <span class="geshifilter"><code class="text geshifilter-text">id</code></span>, <span class="geshifilter"><code class="text geshifilter-text">fullyQualifiedDomainName</code></span>, and <span class="geshifilter"><code class="text geshifilter-text">primaryIpAddress</code></span> from the <a href="/reference/datatypes/SoftLayer_Hardware/">SoftLayer_Hardware</a> record. In addition, it will return only the <span class="geshifilter"><code class="text geshifilter-text">longName</code></span> from the <span class="geshifilter"><code class="text geshifilter-text">datacenter</code></span>, and the <span class="geshifilter"><code class="text geshifilter-text">id</code></span>, <span class="geshifilter"><code class="text geshifilter-text">name</code></span>, and <span class="geshifilter"><code class="text geshifilter-text">port</code></span> of each <span class="geshifilter"><code class="text geshifilter-text">networkComponent</code></span>.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">mask[id,fullyQualifiedDomainName,primaryIpAddress,datacenter.longName,networkComponents[id,name,port]]</pre></div>
<h3 id="Type">Type</h3>
<p>By default the type of returned objects will be inferred and is not required. However it is possible to declare a type for a specific property.</p>
<p>A type is defined by placing a parenthesis set after the property name with the type name enclosed. A type will need to be defined when the default property type does not have a particular property that you need.</p>
<p>For example, the <span class="geshifilter"><code class="text geshifilter-text">controlPanel</code></span> property is not defined on <a href="/reference/services/SoftLayer_Hardware/">SoftLayer_Hardware</a> and as such you will get an error if requesting it via <span class="geshifilter"><code class="text geshifilter-text">mask.controlPanel</code></span> on a call to <a href="/reference/services/SoftLayer_Account/getHardware">SoftLayer_Account::getHardware</a>. In order to request the value you must declare the <span class="geshifilter"><code class="text geshifilter-text">root property</code></span> to be of a particular type. An example is below.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">mask(SoftLayer_Hardware_Server).controlPanel</pre></div>
<p>If necessary, a property may be defined multiple times on the same level with different types.</p>
<p>The mask below is an example for invoking SoftLayer_Search::search with two expected data types to be returned:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">mask
[
    resource(SoftLayer_Hardware)
    [
        id,
        fullyQualifiedDomainName,
        datacenter.longName,
        networkComponents.primaryIpAddress
    ],
    resource(SoftLayer_Virtual_Guest)
    [
        id,
        fullyQualifiedDomainName,
        datacenter.longName,
        networkComponents.primaryIpAddress
    ]
]</pre></div>


<h2 id="API_interaction">API interaction</h2>
<h3 id="SOAP">SOAP</h3>
<p>To send the object mask to the SOAP API you will need to provide a <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_ObjectMask</code></span> header with the string object mask for the value in the <span class="geshifilter"><code class="text geshifilter-text">mask</code></span> property of the header.</p>
<h3 id="XML-RPC">XML-RPC</h3>
<p>The same SoftLayer_ObjectMask header may be provided in the XML-RPC headers section of the request.</p>
<h3 id="REST">REST</h3>
<p>The REST interface will accept the object mask via the <span class="geshifilter"><code class="text geshifilter-text">objectMask</code></span> GET parameter.</p>
<p>Our SLAPI bindings found in our github projects have been updated to support this new form of string object mask.</p>
<h2 id="Legacy_Object_Masks_"> Legacy Object Masks </h2>
<p>Please see <a href="/article/legacy-object-masks">Legacy-Object-Masks</a> for usage information on the legacy object mask syntax</p>