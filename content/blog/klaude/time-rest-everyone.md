---
title: "Time for a REST, Everyone"
description: "<p>In our <a href=http://sldn.softlayer.com/07/2010/its-time-to-bust-out-of-the-private-network/>last post</a> we ment"
date: "2010-07-23"
author: "klaude"
tags:
    - "blog"
---

<p>In our <a href="http://sldn.softlayer.com/07/2010/its-time-to-bust-out-of-the-private-network/">last post</a> we mentioned that our API now supports a <a href="http://en.wikipedia.org/wiki/Representational_State_Transfer">REST</a> interface. It's really true, and it's really here! Quoth our new, fancy, <a href="http://sldn.softlayer.com/wiki/index.php/REST">manual page</a>:</p>
<blockquote><p>
REST API URLs are structured to easily traverse SoftLayer's object hierarchy. A basic REST request is structured as follows:</p>
<p><tt>https://<username>:<apiKey>@api.[service.]softlayer.com/rest/v3/<br />
<serviceName>[/initializationParameter].<returnDatatype></tt></p>
<ul>
<li>All REST requests, even private network requests, must be passed through HTTP SSL.</li>
<li>Use your API username and key to authenticate your request through HTTP authentication.</li>
<li>The base hostname and folder name for a REST request is either api.softlayer.com/rest/v3/ or api.service.softlayer.com/rest/v3/. Use api.service.softlayer.com/rest/v3/ to access the REST API over SoftLayer's private network. It's a more secure way to communicate with SoftLayer, but the system making API calls must be on SoftLayer's private network (either purchased from SoftLayer of logged into SoftLayer's private network VPN).</li>
<li>Follow up the base URL with the name of the API service you wish to call, for instance "SoftLayer_Account" or "SoftLayer_Hardware_Server".</li>
<li>If your API request requires an initialization parameter then add a slash followed by your init parameter id to your URL.</li>
<li>The SoftLayer REST API can return either XML or JSON formatted output. Add ".xml" or ".json" to the end of your request to specify which format you'd like to receive data in.</li>
</ul>
</blockquote>
<p>&nbsp;</p>
<p>Now that the boring stuff is out of the way here are a few sample calls:</p>
<p>The most basic call in the SoftLayer API is the <a href="http://sldn.softlayer.com/wiki/index.php/SoftLayer_Account::getObject">getObject()</a> method in the <a href="http://sldn.softlayer.com/wiki/index.php/SoftLayer_Account">SoftLayer_Account</a> API service. It also has the simplest URL in our REST API:</p>
<pre style="background: #DDD; border: 1px solid #999; display: block; padding: 5px;">https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Account.json</pre><p>&nbsp;</p>
<p>If you need to retrieve a particular object then append its id number to the end of the URL. This URL retrieves information about the <a href="http://sldn.softlayer.com/wiki/index.php/SoftLayer_Hardware_Server">SoftLayer_Hardware_Server</a> record 1234:</p>
<pre style="background: #DDD; border: 1px solid #999; display: block; padding: 5px;">https://username:apiKey@api.softlayer.com/rest/v3/
SoftLayer_Hardware_Server/1234.json</pre><p>&nbsp;</p>
<p>One of the coolest things in our API is how all of our objects relate to each other. Append a relational property to the end of your URL to retrieve that object's related objects. This URL retrieves server 1234's <a href="http://sldn.softlayer.com/wiki/index.php/SoftLayer_Network_Component">network component</a> records:</p>
<pre style="background: #DDD; border: 1px solid #999; display: block; padding: 5px;">https://username:apiKey@api.softlayer.com/rest/v3/
SoftLayer_Hardware_Server/1234/NetworkComponents.json</pre><p>&nbsp;</p>
<p>Chain these relational properties as far as you need to go. You can also specify single relational properties by adding its id to the end of the URL. This URL retrieves network component record 5678 from server record 1234:</p>
<pre style="background: #DDD; border: 1px solid #999; display: block; padding: 5px;">https://username:apiKey@api.softlayer.com/rest/v3/
SoftLayer_Hardware_Server/1234/NetworkComponents/5678.json</pre><p>&nbsp;</p>
<p>Since hardware records relate back to the SoftLayer_Account service, your URL can also relate back to it. Your SoftLayer_Account record has properties for nearly every service available to you, and is handy for providing a truly RESTful interface. </p>
<pre style="background: #DDD; border: 1px solid #999; display: block; padding: 5px;">https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Account/
Hardware/1234/NetworkComponents/5678.json</pre><p>&nbsp;</p>
<p>I'm absolutely loving how well this works. Being able to test API functionality right in my web browser has made troubleshooting a lot easier on me. Our REST interface also supports object creation, edit, and deletion and SoftLayer API specific options like <a href="http://sldn.softlayer.com/wiki/index.php/Object_Mask">object masks</a> and <a href="http://sldn.softlayer.com/wiki/index.php/ResultLimit">result limits</a>. Check out our <a href="http://sldn.softlayer.com/wiki/index.php/REST">manual page</a> for the scoop. Please give it a whirl and tell us what you think. We've got more good stuff coming your way soon!</p>

