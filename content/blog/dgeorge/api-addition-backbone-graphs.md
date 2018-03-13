---
title: "API Addition - Backbone Graphs"
description: "<p>(This post refers to SoftLayer API version 1. Check out <a href=http://sldn.softlayer.com/03/2008/and-now-for-someth"
date: "2007-06-08"
author: "dgeorge"
tags:
    - "blog"
---

<p>(This post refers to SoftLayer API version 1. Check out <a href="http://sldn.softlayer.com/03/2008/and-now-for-something-completely-different/">API version 3</a> for our latest updates.)</p>
<p>Due to popular demand, we rolled out a change today which allows querying of our backbone connection graphs.  For the uninitiated, backbone graphs show the network usage between the SoftLayer datacenter and the Internet. This functionality was accomplished by adding two new methods to the SoftLayer API.</p>
<p><strong>getBackboneList</strong><br />
Retrieves an array of id and name pairs for all SoftLayer's Backbone providers</p>
<p><strong>getBackboneImage(intBackboneId)</strong><br />
Retrieves a PNG image for display or local storage</p>
<p>Both of the methods are available via the SOAP and XML-RPC interfaces.  We will be updating the documentation and examples for these methods and a few other additions (Top Secret) over the next few weeks.</p>

