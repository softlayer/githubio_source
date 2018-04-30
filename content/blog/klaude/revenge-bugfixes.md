---
title: "Revenge of the bugfixes"
description: "<p>(This post refers to SoftLayer API version 1. Check out <a href=http://sldn.softlayer.com/03/2008/and-now-for-someth"
date: "2007-08-15"
author: "klaude"
tags:
    - "blog"
---

<p>(This post refers to SoftLayer API version 1. Check out <a href="http://sldn.softlayer.com/03/2008/and-now-for-something-completely-different/">API version 3</a> for our latest updates.)</p>
<p>We've updated the API again! This latest refresh sports:</p>
<ul>
<li><b>fixed:</b> <b>getBandwidthList()</b>'s output now mirrors the estimated and projected bandwidth amounts measured by our management portal.</li>
<li><b>fixed:</b> Hostnames and domain names in server names are now separated by a period in <b>getBandwidthList()</b>'s output.</li>
<li><b>fixed:</b> The Savvis #2 and Global Grossing links are now properly reported in <b>getBackboneList()</b>.</li>
<li><b>added:</b> The <b>getServerBandwidthDetails()</b> method has been added to the SoftLayer API. getServerBandwidthDetails() mirrors getBandwidthList()'s output for a single server. It returns an array and requires two paraeters:
<p><b>strServerIdentifier</b>: A server ID, public IP addres, or private IP address.<br />
<b>strBandwidthType</b>: The string "public" or "private" depending on which port you want to retrieve bandwidth data from. This value defaults to "public".
</li>
</ul>
<p>We really should give a shout out to those that have been keeping us on our toes by reporting issues to us on our forums and in support tickets. Please keep them coming. Your contributions are turning the API into a great product. See ya'll next time!</p>

