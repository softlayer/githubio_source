---
title: "Go Go Gadget"
description: "<p>To gadgetize or not to gadgetize?  That is the question.  Between Apple widgets, Google gadgets, and Windows gadgets,"
date: "2011-01-03"
author: "wfrancis"
tags:
    - "blog"
---

<p>To gadgetize or not to gadgetize?  That is the question.  Between Apple widgets, Google gadgets, and Windows gadgets, these technologies have a bit of buzz associated with them.  But as with any technology, just because it’s cool doesn’t mean it makes sense in every situation.  So when I was first approached with the idea of implementing a Windows gadget to interact with the SoftLayer Application Programming Interface (SLAPI), I stepped back and asked myself what area or areas of the SLAPI make a compelling case for gadgetization.  (I know, neither gadgetize nor gadgetization is a real word but you have to admit is it sure is fun to try and say.)</p>
<p>In the end I felt of all the things I use in the SoftLayer portal, the one which is most dynamic and which I access the most frequently is tickets.  So I decided to build a gadget that would do a few things:</p>
<p>1. Show me at a glance how many tickets are open on my account.</p>
<p>2. Flash alerts when a ticket-related activity occurs.  This means:</p>
<p>&nbsp;&nbsp;   a. A new ticket is opened.</p>
<p>&nbsp;&nbsp;   b. An existing ticket is closed.</p>
<p>&nbsp;&nbsp;   c. An existing ticket gets updated by SoftLayer staff.</p>
<p>Additionally, I thought it would be really handy if I could:</p>
<p>1. Click on an alert to get additional details about the ticket.</p>
<p>2. Click on the additional details to launch the portal and edit the currently viewed ticket.</p>
<p>Here’s a quick look at my resulting gadget in the summary (normal) view. </p>
<p><img src="http://dev-sldn151.softlayer.local/sites/default/files/sl_ticket_gadget_normal.png" alt="" /></p>
<p>And here it is again in the detail (flyout) view.</p>
<p><img src="http://dev-sldn151.softlayer.local/sites/default/files/sl_ticket_gadget_flyout.png" alt="" /></p>
<p>If you’d like to see the gadget working with your own ticket queue, you can down load it from github <a href="https://github.com/softlayer/Windows-Desktop-Gadgets">HERE</a>.  Simply double clicking on the SL.GADGET file will begin the installation process.  Before the gadget can actually connect to your account, you will need to bring up the settings page by clicking on the wrench icon.  From the settings page, you can enter your own account credentials.</p>
<p>Those of you interested in expanding this gadget or creating your own will be pleased to learn gadgets are just a combination of HTML, CSS, JAVASCRIPT, and an XML file thrown in to act as a sort of makeshift manifest.  Even the .GADGET file you install is nothing more than a standard ZIP file with the extension renamed.</p>
<p>For the most part, I found plenty of tutorials on the web from Microsoft and various third-parties on creating Windows gadgets, (sometimes referred to sidebar gadgets), and as such, it seems unnecessary to go through a full blown tutorial.  The one area I did find the available documentation a little sketchy was on the subject of debugging.  A fairly important oversight assuming that the code your fingers tap out, (like mine), isn’t always perfect the first time you hit the save button.</p>
<p>While I pieced together a number of debugging scenarios from various news groups and forums, the only way that worked reasonably well for me was using Visual Studio.  Enabling debugging is a two-step process, and a little annoying since it relies on changing global settings in Internet Explorer (this is because all Windows gadgets are essentially running in a frameless version of IE).</p>
<p>First, in IE under the advanced options tab, you need to UNCHECK the buttons labeled “Disable script debugging (IE)” and “Disable script debugging (other)”.  I will warn you in advance this will cause IE to pop up all sorts of annoying scripting error messages on any number of pages you view regularly.  So save yourself a headache and be sure to put this setting back when you have completed with your gadget debugging session.</p>
<p>The second step happens in Visual Studio.  Under the tools, options, debugging, just-in-time node, you need to make sure you have CHECKED just in time debugging for “managed”, “native”, and “script”.  Now you should be ready to debug. You will want to have your gadget running on your desktop, open the main javascript file in Visual Studio, and then under the debug menu select “attach to running process”.</p>
<p>All gadgets are hosted by WindowsSidebar.Exe. You will want to find the instance of WindowsSidebar.Exe that shows your application name out to the right in parenthesis.  Once attached, you can add break points, single step, and just in general debug until your heart is content.</p>
<p>Of course whether you just want to use this gadget as is, modify it, or create your own, myself and the folks here at SoftLayer are eager to help.  Feel free to post your comments on this page or in our forums.  We especially want to hear from you if you have created your own gadget taking advantage of SoftLayer’s extensive API and are willing to share that gadget with other users in the community.  I suspect I could get some pretty cool swag from our marketing department shipped to any of our users who fall into that last category.</p>
<p>Until next time…happy gadgetizing.</p>

