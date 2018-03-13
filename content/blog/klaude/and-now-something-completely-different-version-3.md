---
title: "And now for something completely different... version 3!"
description: "<p>Before I get to the good stuff I want to apologize to you guys. I haven't been active in my API evangelism as of late"
date: "2008-03-03"
author: "klaude"
tags:
    - "blog"
---

<p>Before I get to the good stuff I want to apologize to you guys. I haven't been active in my API evangelism as of late. Heck, as of the last few months. Well here's why. I am extremely ecstatic to announce the <b>release of SoftLayer's API version 3.0!</b> This has been a long time coming here at the SoftLayer devCave. This little gem has been in development for about 9 months now, and it's very fulfilling to see it finally come out. But enough about how happy we are. Here's the goods, what makes this different from API version 1:</p>
<p>- The SoftLayer API now explicitly specifies the data types it uses, making it far easier to write in major programming languages like Java and .NET.<br />
- This go around we're object-oriented. Anything that you can do in it is modeled by a service and data type. Where API version 1 had one endpoint and about 20 methods, API version 3 has about 50, one per service, and about 390 methods. That leads me to...<br />
- It does everything. Seriously, this API lets you manage every single one of your SoftLayer servers and services. In fact it lets you do everything that our portal lets you do (except purchasing servers, but we'll get to that). For you guys that have been asking, yes that includes DNS management and OS reloads. </p>
<p>We like this API so much that for the past month we've been busting our humps rewriting our customer portal as an API application. I just checked our system statistics. Load on our database is down by 25%, and load on our portal web servers is down about 10%. There's a noticeable improvement in portal responsiveness since we've started this project. A great side effect of rewriting our portal as an API application is that when we bust out new services they go into the API immediately. </p>
<p>If you've been developing against API version 1 then take a look at our <s>migration guide</s> and FAQ on our brand-spanking-new <s>SLDN documentation wiki</s>. We're really looking forward to making (and help you guys make) some cool apps with this. This is a big change for us, so please don't be shy in letting us know what you think. Our <A href="http://forums.softlayer.com/">forums</a> and email are waiting!</p>

