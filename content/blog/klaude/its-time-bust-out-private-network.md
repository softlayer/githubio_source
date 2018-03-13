---
title: "It's Time to Bust out of the Private Network!"
description: "<p><a href=http://forums.softlayer.com/showthread.php?t=4969>Some of you have noticed</a> that we <a href=http://sldn"
date: "2010-07-02"
author: "klaude"
tags:
    - "blog"
---

<p><a href="http://forums.softlayer.com/showthread.php?t=4969">Some of you have noticed</a> that we <a href="http://sldn.softlayer.com/06/2010/the-softlayer-mobile-client-a-new-perspective/">mentioned</a> our new <a href="http://www.softlayer.com/resources/mobile-apps/">mobile clients</a> are based on our <a href="http://sldn.softlayer.com/wiki/index.php/The_SoftLayer_API">developer API</a> but don't require a VPN connection to our <a href="http://www.softlayer.com/facilities/network-advantages/">private network</a>. Your observations are astute and indeed correct. Our iPhone and Android applications can be accessed from anywhere on the Internet, and now so can the SoftLayer API! </p>
<p>We've rolled out API endpoints on the public Internet at <b>https://api.softlayer.com</b>. Our public API uses SSL to keep your data transmission secure, but you're still free to use non-SSL HTTP on our private network. Here's a rundown of our API's endpoint locations:</p>
<p><b>SOAP:</b></p>
<ul>
<li><i>https://api.softlayer.com/soap/v3</i>: public network</li>
<li><i>https://api.service.softlayer.com/soap/v3</i>: private network</li>
</ul>
<p><b>XML-RPC:</b></p>
<ul>
<li><i>https://api.softlayer.com/xmlrpc/v3</i>: public network</li>
<li><i>https://api.service.softlayer.com/xmlrpc/v3</i>: private network</li>
</ul>
<p><b>REST:</b> (That's a new one. More on RESTful services soon!)</p>
<ul>
<li><i>https://api.softlayer.com/rest/v3</i>: public network</li>
<li><i>https://api.service.softlayer.com/rest/v3</i>: private network</li>
</ul>
<p>The private network endpoints at <i>api.service.softlayer.com</i> are still up and aren't going anywhere. In fact, we still recommend using the private network to send API calls from your servers and cloud instances in our datacenters. But those of you developing desktop and mobile clients have a whole new world of access. Our <a href="http://github.com/softlayer/">public API clients</a> will soon be updated to use our public endpoints. Try these out, log into our <a href="http://forums.softlayer.com/">forums</a>, and tell us what you think!</p>

