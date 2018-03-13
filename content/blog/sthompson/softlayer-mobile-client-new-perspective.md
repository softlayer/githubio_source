---
title: "The SoftLayer Mobile Client: A New Perspective"
description: "<p>Much of the development work that goes on here centers on the <a href=https://manage.softlayer.com/>SoftLayer Custo"
date: "2010-06-21"
author: "sthompson"
tags:
    - "blog"
---

<p>Much of the development work that goes on here centers on the <a href="https://manage.softlayer.com/">SoftLayer Customer Portal</a>. The Customer Portal is a traditional Web application that links your browser to the powerful back-end systems that our engineers have crafted over the course of many years. Most of the engineers around here are first rate hands at web application technologies like PHP, JavaScript, and HTML.</p>
<p>I don't know much HTML. I know even less PHP. I spent many years working on desktop Macintosh applications in C and C++.  With the introduction of the iPhone SDK, a new job opportunity made me an iPhone developer. The leap from the Cocoa framework, on the desktop Mac OS, to the Cocoa Touch framework of the iPhone was not difficult at all. The two frameworks share a lot in common and the parts that are different still share a lot of design patterns. All in all, making the transition to a company whose primary focus is web development was a lot more intimidating than picking up the iPhone API.</p>
<p>I joined SoftLayer specifically to work on the Mobile Client. The goal of the <a href="http://www.softlayer.com/resources/mobile-apps/">SoftLayer Mobile Client</a> is pretty straightforward, put the essential parts of the SoftLayer Customer Portal in the palm of your hand, on your favorite mobile device. We wanted to move beyond the mobile web applications the team had already created, and craft an application with a look and feel only a native applications can provide, a first rate user experience.</p>
<p>At the same time, all the attention to detail you can possibly give the front end doesn't matter unless you have some way to communicate with the server. That's where the SoftLayer v3 API comes into play.</p>
<p>The smart folks on the the web application development team work behind the scenes on the server, enjoying full access to the complex machine behind the SoftLayer Customer Portal. Their target has been a traditional web browser, running on a computer with Gigabytes of available RAM, Gigahertz of processing power, and several Megabits per second of network connectivity.</p>
<p>Comparatively, on the Mobile Applications development team, we live across the wire on tiny computers with small pipes. Mobile devices have limited memory constraints, run on a "slow" 3G networks, and have processors running at less than 1/3 of the speed of their desktop counterparts.</p>
<p>With such vast differences between the environment of a desktop computer's browser and an application running on a mobile device, SoftLayer could have crafted a custom API to give our mobile applications access tailored access to the machine behind the SoftLayer Customer Portal.</p>
<p>But we didn't want to do that.</p>
<p>With great pride of principle, our mobile applications team makes it a point to use the same API that SoftLayer presents to you, the third party developers of the SLDN network. We don't want to use back doors, and we don't want to use secret calls. Consuming our own API, "eating our own dog food" as the saying goes, gives us a unique vantage point which we hope to use to improve the API for all SLDN developers.</p>
<p>In the course of developing the Mobile Client on a variety of platforms, the mobile team has found that most aspects of the SoftLayer API work very well!  We've also found some that presented challenges to our mobile devices. Lucky for you, however, we're working very closely with the web development team to remove those challenges.</p>
<p>We plan to bring new functionality that results from our experience directly to you. In the course of the next few months, look for some changes (large and small) to the services we provide. We hope you will find them a benefit to your application development regardless of where your application runs. </p>

