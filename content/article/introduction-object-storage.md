---
title: "An Introduction to Object Storage"
description: "With the release of SoftLayer Object Storage, we wanted to integrate brand-unique, value-added features on top of the already comprehensive tools that have been set in place to provide a first-in-class product for our customers. While Object Storage has many features that come standard from the OpenStack Object Storage project (code-named Swift), the additional features we have integrated will bring your storage to the next level."
date: "2012-02-08"
tags:
    - "article"
    - "sldn"
---

<script type="text/javascript">toc_collapse=0;</script><div class="toc" id="toc12">
<div class="toc-title">Table of contents<span class="toc-toggle-message">&nbsp;</span></div>
<div class="toc-list">
<ol>
<li class="toc-level-1"><a href="#Authentication_Endpoints">Authentication Endpoints</a></li>
<li class="toc-level-1"><a href="#Key_Architecture_Points">Key Architecture Points</a>
<ol>
<li class="toc-level-2"><a href="#Account">Account</a></li>
<li class="toc-level-2"><a href="#Cluster">Cluster</a></li>
<li class="toc-level-2"><a href="#Container">Container</a></li>
<li class="toc-level-2"><a href="#Object">Object</a></li>
</ol>
</li>
<li class="toc-level-1"><a href="#Key_Object_Storage_Feature">Key Object Storage Feature</a>
<ol>
<li class="toc-level-2"><a href="#CDN_Integration">CDN Integration</a></li>
<li class="toc-level-2"><a href="#CDN_API">CDN API</a></li>
<li class="toc-level-2"><a href="#Search_Service_API">Search Service API</a></li>
<li class="toc-level-2"><a href="#Search_API">Search API</a></li>
</ol>
</li>
<li class="toc-level-1"><a href="#Language_Bindings">Language Bindings</a></li>
</ol>
</div>
</div>
<p>With the release of SoftLayer Object Storage, we wanted to integrate brand-unique, value-added features on top of the already comprehensive tools that have been set in place to provide a first-in-class product for our customers. While Object Storage has many features that come standard from the <a href="http://openstack.org/projects/storage/">OpenStack Object Storage</a> project (code-named Swift), the additional features we have integrated will bring your storage to the next level.<br />
Before introducing you to the features, we’d like to better acquaint you with the architecture you can expect to see when working with SoftLayer Object Storage.</p>
<h2 id="Authentication_Endpoints">Authentication Endpoints</h2>
<p>SoftLayer Object Storage has API endpoints on both the private network and public internet. Private network calls can only be made from servers and computing instances purchased from SoftLayer, or devices connected to the private network via VPN. Authentication requests should be sent to the endpoint associated with the location of your Object Storage account.</p>
<p>The response body of the authentication request will contain endpoint information for clusters associated with your account.</p>
<div style="background-color: #D3D3D3; padding: 2px 10px;">
<strong>Dallas:</strong><br />
    Public Network: https://dal05.objectstorage.softlayer.net/auth/v1.0<br />
    Private Network: https://dal05.objectstorage.service.networklayer.com/auth/v1.0<br />
<strong>Amsterdam:</strong><br />
    Public Network: https://ams01.objectstorage.softlayer.net/auth/v1.0<br />
    Private Network: https://ams01.objectstorage.service.networklayer.com/auth/v1.0<br />
<strong>Singapore:</strong><br />
    Public Network: https://sng01.objectstorage.softlayer.net/auth/v1.0<br />
    Private Network: https://sng01.objectstorage.service.networklayer.com/auth/v1.0
</div>
<h2 id="Key_Architecture_Points">Key Architecture Points</h2>
<p>Unlike the regular SoftLayer API, the Object Storage API is solely written for RESTbased programming so users will be working completely out of a browser, utilizing URLs and request headers rather than the standard methods that one might usually see. This allows us to utilize the tools and bindings that already exist to ensure you get the best version of Object Storage possible. When navigating through the Object Storage API,<br />
you’ll be working with three basic storage concepts which are easily navigable and allow you to fully customize the way you store your data.</p>
<h3 id="Account">Account</h3>
<p>The <b>account</b> for Object Storage is treated like any SoftLayer account. It is the main point of reference to which all of your data is associated. When completing request headers, your account will generally be referenced to retrieve, add or change information. From your account, clusters are created in different datacenters, which house objects as they are uploaded to the cluster.  Within each cluster, containers may be created to better organize objects, similar to filesystems used by most software today.</p>
<h3 id="Cluster">Cluster</h3>
<p>A <b>cluster</b> is a set of servers that create scalable and fault-tolerant object storage. When using SoftLayer Object Storage, your data is replicated across the cluster, ensuring that it can be retrieved in the event of node failure. Object storage clusters will be located in our Dallas, Amsterdam and Singapore datacenters.</p>
<h3 id="Container">Container</h3>
<p>The <b>container</b> is the basic storage unit for all data that you store. Containers work in Object Storage much like folders or directories work in many operating systems. The main difference between containers and folders or directories is that containers are unable to be nested. At minimum, an account must contain one container and the number of containers allowed per account is unlimited. Optionally, additional containers can be created within your account and data may be organized within those containers based on your business needs.</p>
<h3 id="Object">Object</h3>
<p>An <b>object</b> represents the data and any metadata for the files stored in the system. Through the REST interface, metadata for an object can be included by adding custom HTTP headers to the request and the data payload as the request body. Objects cannot exceed 5GB and must have names that do not exceed 1024 bytes after URL encoding. However, objects larger than 5GB can be segmented and then concatenated together so that you can upload 5 GB segments and download a single concatenated object. You can work with the segments and manifests directly with HTTP requests.</p>
<div style="background-color: #D3D3D3; padding: 2px 10px;">
<b>The core API is powered by OpenStack Object Storage.</b><br />
OpenStack Object Storage Developer Guide<br />
http://docs.openstack.org/api/openstack-object-storage/1.0/content/
</div>
<h2 id="Key_Object_Storage_Feature">Key Object Storage Feature</h2>
<p>Now that you are familiar with the basics of SoftLayer Object Storage, we’d like to briefly introduce you to two of the key features that come standard with every Object Storage account. For more information on either of these features, click the link embedded in the descriptions and you will be routed to an in-depth article on the selected feature.</p>
<h3 id="CDN_Integration">CDN Integration</h3>
<p>With CDN integration available for all Object Storage clients, you now have the option to replicate your data to all Points of Presence (PoPs) on the SoftLayer network. This means getting information stored closer to your clients worldwide and allowing your data to be retrieved from the server that will get clients' information the quickest.</p>
<div style="background-color: #D3D3D3; padding: 2px 10px;">
<h3 id="CDN_API">CDN API</h3>
<p><a href="http://sldn.softlayer.com/reference/Object-Storage-CDN">Methods</a><br />
<a href="http://sldn.softlayer.com/article/CDN-Integration-%E2%80%93-Getting-Information-you-Need-Faster">CDN Integration – Getting the Information you Need, Faster</a>
</p></div>
<h3 id="Search_Service_API">Search Service API</h3>
<p>Exclusive to SoftLayer Object Storage is the Search Service API. This API, built directly on top of the Object Storage API, allows you to customize you search not only to search by account, container or object, but also to input a variety of parameters in your request to ensure the best return possible. These parameters include, but are not limited to:</p>
<ul>
<li>Format – Specify the format in which your results are returned.  Current formatting options are json, XML and plain text.</li>
<li>Recursive – Require the system to search recursively, if desired.</li>
<li>Sort – Indicate how you would like your response sorted.  While the system defaults to sort based on the best match, users have the option to override and receive the results based on the desired property.</li>
</ul>
<div style="background-color: #D3D3D3; padding: 2px 10px;">
<h3 id="Search_API">Search API</h3>
<p><a href="http://sldn.softlayer.com/article/API-Operations-Search-Services">API Operations for Search Services</a>
</p></div>
<h2 id="Language_Bindings">Language Bindings</h2>
<p>In addition to using the REST API we provide language bindings for a number of languages.</p>
<style type="text/css">
ul.languageList {
    background: none repeat scroll 0 0 transparent;
    border-bottom: 1px dotted #CCCCCC;
    border-top: 1px dotted #CCCCCC;
    padding: 10px;
}
ul.languageList li {
    display: inline;
    list-style-type: none;
    margin-right: 23px;
}
ul.languageList li a:hover {
    opacity: 0.5;
}
ul.languageList li a {
    display: inline-block;
    height: 60px;
    overflow: hidden;
    text-indent: -9999em;
    width: 48px;
}
ul.languageList li.csharp a {
    background: url("/sites/all/themes/sldn_theme/images/docCSharp.png") no-repeat scroll 0 0 transparent;
}
ul.languageList li.perl a {
    background: url("/sites/all/themes/sldn_theme/images/docPerl.png") no-repeat scroll 0 0 transparent;
}
ul.languageList li.php a {
    background: url("/sites/all/themes/sldn_theme/images/docPHP.png") no-repeat scroll 0 0 transparent;
}
ul.languageList li.python a {
    background: url("/sites/all/themes/sldn_theme/images/docPython.png") no-repeat scroll 0 0 transparent;
}
ul.languageList li.ruby a {
    background: url("/sites/all/themes/sldn_theme/images/docRuby.png") no-repeat scroll 0 0 transparent;
}
ul.languageList li.vbnet a {
    background: url("/sites/all/themes/sldn_theme/images/docVBNet.png") no-repeat scroll 0 0 transparent;
}
ul.languageList li.java a {background: url("/sites/all/themes/sldn_theme/images/docJava.png") no-repeat scroll 0 0 transparent;}
</style>
<div style="margin: 0px auto; width: 50%">
<ul class="languageList">
<li class="php"><a href="https://github.com/softlayer/softlayer-object-storage-php"></a></li>
<li class="python"><a href="https://github.com/softlayer/softlayer-object-storage-python"></a></li>
<li class="ruby"><a href="https://github.com/softlayer/softlayer-object-storage-ruby"></a></li>
<li class="java"><a href="https://github.com/softlayer/softlayer-object-storage-java"></a></li>
</ul>
</div>