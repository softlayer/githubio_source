---
title: "It pays to ask"
description: "<p>(This post refers to SoftLayer API version 1. Check out <a href=http://sldn.softlayer.com/03/2008/and-now-for-someth"
date: "2007-07-03"
author: "dharris"
tags:
    - "blog"
---

<p>(This post refers to SoftLayer API version 1. Check out <a href="http://sldn.softlayer.com/03/2008/and-now-for-something-completely-different/">API version 3</a> for our latest updates.)</p>
<p>Ask...</p>
<p><a href="http://forums.softlayer.com/showthread.php?t=1736"><img border="0" width="302" src="http://sldn.softlayer.com/wp-content/sldn/23/01-api_request-small.png" height="186" /></a></p>
<p>And you shall receive…</p>
<p>The newest addition to the API methods has been released and is now available for use. We have improved upon the Portal's monitoring features by adding just a little more data.(This post refers to SoftLayer API version 1. Check out <a href="http://sldn.softlayer.com/03/2008/and-now-for-something-completely-different/">API version 3</a> for our latest updates.)</p>
<p>Ask...</p>
<p><a href="http://forums.softlayer.com/showthread.php?t=1736"><img border="0" width="302" src="/sites/default/files/images/01-api_request-small.png" height="186" /></a></p>
<p>And you shall receive…</p>
<p>The newest addition to the API methods has been released and is now available for use. We have improved upon the Portal's monitoring features by adding just a little more data. In addition to receiving the number of servers that are up, recovering, and down, the new function also returns an array with specific details about the servers that are down. This includes: SERVER_NAME, ID, PUBLIC_IP, PRIVATE_IP, and TIME_FIRST_DOWN, which as requested is "the time that the monitoring system first detected that it was down".</p>
<p><strong>getServerStatus()</strong><br />
Retreive a server status of UP DOWN or RECOVERING for a given account id.</p>
<p>The new method is available through our SOAP and XML-RPC interfaces. Okay, so we didn't quite give you exactly what you asked for, we gave you more!</p>

