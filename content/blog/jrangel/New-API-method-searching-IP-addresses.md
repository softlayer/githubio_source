---
title: "New API method for searching IP addresses"
description: "<p>(This post refers to SoftLayer API version 1. Check out <a href=http://sldn.softlayer.com/03/2008/and-now-for-someth"
date: "2007-07-06"
author: "jrangel"
tags:
    - "blog"
---

<p>(This post refers to SoftLayer API version 1. Check out <a href="http://sldn.softlayer.com/03/2008/and-now-for-something-completely-different/">API version 3</a> for our latest updates.)</p>
<p>We've added a new feature to the<br />
Softlayer API: <b>getIPaddressDetails</b>. For a given IP address, this method will retrieve the parent subnet, VLAN identifier, IP address which it is routed to and the name of the server it's routed to. Instead of using the customer portal and typing in a slew of IP addresses one by one into the public network ip search page, simply call this IP for each IP address, saving you time and typing. It's incredibly useful for tracking down your secondary IPs. </p>
<p><b>getIPaddressDetails(strIPaddress)</b><br />
Retreive subnet and server details for given IP Address</p>
<p>This new method is available via both SOAP and XML-RPC interface.  </p>
<p>We'd love to hear your thoughts on this new feature.  Feel free to provide any comments and recommendations for improvements on this new API.</p>

