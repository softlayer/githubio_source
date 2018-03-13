---
title: "Go Play in a Sandbox"
description: "<p>(This post refers to SoftLayer API version 1. Check out <a href=http://sldn.softlayer.com/03/2008/and-now-for-someth"
date: "2007-07-26"
author: "klaude"
tags:
    - "blog"
---

<p>(This post refers to SoftLayer API version 1. Check out <a href="http://sldn.softlayer.com/03/2008/and-now-for-something-completely-different/">API version 3</a> for our latest updates.)</p>
<p>I think we on the SLDN development team have it pretty lucky. You can't beat developing at a datacenter where there are umpteen, wonderful servers to test your code on. Need to reboot a box? Sure! Go for it! After all, it's just a quick phone call to the datacenter to bring it back online if your test code broke something. In the mean time there are plenty of other boxes to test on. Sure that's great for us, but it can get hairy if you only have one or two systems to test with. While our sales droids would have you fix that by ordering more servers we on the dev team just implemented a tried and true code test mechanism, the <a href="http://en.wikipedia.org/wiki/Image:Sandpit.jpg">sandbox</a>! Wait, I mean <a href="http://en.wikipedia.org/wiki/Sandbox_%28software_development%29">this sandbox</a>!</p>
<p>Our API sandbox is a way for you to safely test sensitive methods without affecting your servers. Method calls from the sandbox will return accurate return data without actually affecting your services or SoftLayer services. Most of our methods are simple get methods; those still work exactly the same. More fun methods like rebootServer() will <i>not</i> reboot your server if called from our sandbox, but will return the same response to your app as if they did.</p>
<p>To use the API sandbox change the API entry point server in your code to <b>api-sandbox.service.softlayer.com</b>. That's it! Use the same methods and parameters that you'd normally call. The sandbox works on both the XML-RPC and SOAP interfaces. When you're done testing point your API calls back to api.service.softlayer.com to return to normal functionality.</p>
<p>As always, we welcome your feedback and suggestions. Let us know what you think on our <a href="http://forums.softlayer.com/forumdisplay.php?f=27">forums</a>. See you next time!</p>

