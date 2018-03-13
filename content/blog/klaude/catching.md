---
title: "Catching Up"
description: "<p>(This post refers to SoftLayer API version 1. Check out <a href=http://sldn.softlayer.com/03/2008/and-now-for-someth"
date: "2007-09-11"
author: "klaude"
tags:
    - "blog"
---

<p>(This post refers to SoftLayer API version 1. Check out <a href="http://sldn.softlayer.com/03/2008/and-now-for-something-completely-different/">API version 3</a> for our latest updates.)</p>
<p>Where has the time gone? We've been busy in the devCave working out some big projects and improving what we've got. In the mean time here's some new API features for ya'll to try out:</p>
<p>&nbsp;<br />
<b>Back It Up</b><br />
&nbsp;</p>
<p>You can now query the state of your NAS or lockbox accounts through the API via the <b>getNasSummaryDetails(strNasType)</b> method. Pass along the string "N" or "L" if you want to check NAS or lockbox accounts and it'll return a list of NAS accounts containing your NAS server's hostname and IP address, connect username and password, capacity, and the server id and name that the NAS account is attached to. If your NAS account isn't tied to a server then it returns "N/A" for the attached server hostname and IP address. Its another way to keep track of your services through the API. </p>
<p>&nbsp;<br />
<b>The Port Authority</b><br />
&nbsp;</p>
<p>The Port Control features of the Customer Portal are now available in the API to help you manage your ports programmatically. Now you can get the port SPEED of the given server by using the method, <b>getServerPortSpeed(strServerIdentifier)</b>. This function also returns the ID, SERVERNAME, PUBLIC IP, and PRIVATE IP.  If you would like to broaden your scope of data, use the getServerPortSpeedList() method. This function returns the same data provided by the former but for all of your servers.  </p>
<p>With access to this data, you may find that you want to make a few changes. The <b>updateServerPortSpeed(strServerIdentifier, intNewSpeed, strControlInterface)</b> function was created to do just that.  Just provide the ID of your server (IP or Hardware ID), the new port speed that you would like configured (values of 0, 10, 100, 1000), and the interface (public or private), and you are on your way. Not only will the ports for the specified server be reconfigured, but the upstream and downstream connected components will be updated as well.</p>
<p>Give it a shot and let us know your thoughts!</p>

