---
title: "World Wide Developers Conference 2012"
description: "<p>SoftLayer constantly pursues excellence in bringing the best products to our customers. We achieve this by always sta"
date: "2012-07-13"
author: "pkijowski"
tags:
    - "blog"
---

<p>SoftLayer constantly pursues excellence in bringing the best products to our customers. We achieve this by always staying up to date with the newest and most efficient technologies, having the best employees and constantly raising our qualifications. That being said, attending Apple’s 23rd World Wide Developers Conference was a must for us!</p>
<p>This year’s WWDC took place in San Francisco between June 11 and June 15 and I was the proud SoftLayer representative. The week was packed with over 100 sessions, plus numerous labs and meetings. Apple employees included UI designers, App Store reps and engineers.<br />
[inline:wwdc1.jpg]</p>
<p>Traditionally, the keynote sets things off at 10:00a.m. Monday morning; however, this year, the line for the keynote began forming around (literally) the Moscone Center almost 10 hours before! I joined, Starbucks in hand, at 5:00a.m.</p>
<p>During keynote, Apple announced its new release of Mac OS X – Mountain Lion – packed with tons of new features. To name a few... built-in support for iCloud (including documents in the Cloud), iMessage, notification center, new Safari with synced browsing history, Power Nap and AirPlay mirroring.</p>
<p>Another big item on Apple’s announcements list was iOS 6 with new Apple 3D Maps, Facebook integration, enhanced Siri release, new phone call application (which allows the user to decline phone calls with a message) do not disturb setting and guided access feature.</p>
<p>The most exciting announcement, however, was an intro of the mind-blowing “Next generation Mac Book Pro.” This machine features a 15.4” retina display with stunning architecture running a quad-core 2.7GHz processor, 16GB of RAM, GeForce GT 650M graphics, 768GB flash storage, USB2/USB3, HDMI and Thunderbolt I/O ports, Bluetooth 4.0, 802.11n Wi-Fi. And best of all, this stunning configuration is packed into a computer that’s only 0.71” thick and weights 4.46 pounds.</p>
<p>After keynote, I immediately filled my calendar with sessions and labs focused on technologies that directly benefit Softlayer iOS products customers. Here are some highlights from the most interesting:<br />
*<strong>AutoLayout sessions</strong><br />
With the new release of iOS, Apple brought a very exciting (already known to OS X Lion developers) <a href="https://developer.apple.com/library/mac/#releasenotes/UserExperience/RNAutomaticLayout/_index.html">AutoLayout</a> technology. AutoLayout allows developers to set prioritized constraints between UI components that define how they appear on the screen. The UI components constraints can be easily set from the Interface Builder as well as within code.<br />
*<strong>"Collection views" sessions</strong><br />
One feature that Apple’s mobile operating system was missing for many releases was the ability to seamlessly create grid, stack and gallery views. The iOS 6 finally filled this gap with “collection views” that introduced easy and formalized ways to create container views. Apple yet again proved that they mastered UI frameworks. The “collection view” API is robust, easy to use and is modeled after list view API.<br />
*<strong>Attributed strings sessions</strong><br />
A great addition in iOS 6, which allows for creating easy text effects, the attributed string manages character strings and their attributes (such as: font and kerning) that apply to single characters or set of characters in the string.<br />
*<strong>New Objective-C language features sessions</strong><br />
Thanks to Apple LLVM Compiler 4.0 both OS X and iOS developers now have access to the new Objective C features that increase code readability as well as developers’ productivity. The most appreciated by developers will likely be support for <a href="http://clang.llvm.org/docs/ObjectiveCLiterals.html">NSNumber Literals, Collection Literals and Object Subscripting</a>.</p>
<div class="geshifilter">
<pre class="csharp geshifilter-csharp" style="font-family:monospace;"><span style="color: #008080; font-style: italic;">// pre Apple LLVM Compiler 4.0</span>
&nbsp;
NSDictionary <span style="color: #008000;">*</span>softLayerOld <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span>NSDictionary dictionaryWithObjectsAndKeys<span style="color: #008000;">:</span>
                              <span style="color: #666666;">@"Bigger"</span>, <span style="color: #000000;">&#91;</span>NSNumber numberWithInt<span style="color: #008000;">:</span> <span style="color: #FF0000;">1</span><span style="color: #000000;">&#93;</span>,
                              <span style="color: #666666;">@"Better"</span>, <span style="color: #000000;">&#91;</span>NSNumber numberWithInt<span style="color: #008000;">:</span> <span style="color: #FF0000;">2</span><span style="color: #000000;">&#93;</span>,
                              <span style="color: #666666;">@"Badder"</span>, <span style="color: #000000;">&#91;</span>NSNumber numberWithInt<span style="color: #008000;">:</span> <span style="color: #FF0000;">3</span><span style="color: #000000;">&#93;</span>,
                               nil<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
<span style="color: #008080; font-style: italic;">// with Apple LLVM Compiler 4.0</span>
&nbsp;
NSDictionary <span style="color: #008000;">*</span>softLayerNew <span style="color: #008000;">=</span> @<span style="color: #000000;">&#123;</span> @<span style="color: #FF0000;">1</span><span style="color: #008000;">:</span> <span style="color: #666666;">@"Bigger"</span>, @<span style="color: #FF0000;">2</span><span style="color: #008000;">:</span> <span style="color: #666666;">@"Better"</span>, @<span style="color: #FF0000;">3</span><span style="color: #008000;">:</span> <span style="color: #666666;">@"Badder"</span> <span style="color: #000000;">&#125;</span><span style="color: #008000;">;</span></pre></div>
<p>Overall, I was sincerely impressed with the quality and content of the WWDC 2012 sessions. I especially appreciated the one-on-one meetings with Apple engineers where I was able to discuss issues I have encountered while working on the iOS platform. That type of interaction is rarely attainable and a great perk of being an attendee.</p>
<p>After an intense week of learning about new technologies and code engineering techniques, WWDC concluded with an all-out evening bash. There, I had the opportunity to meet other engineers and share their impressions about the conference, exchange technical know-how and contact info. I was happy to learn that multiple developers I talked to were also very satisfied SoftLayer customers.</p>
<p>[inline:wwdc2.jpg]</p>
<p>WWDC Bash at Yerba Buena Gardens.</p>
<p>I can’t wait to apply what I’ve learned and to start using the new OS features in SoftLayer’s applications.</p>
<p>See you at WWDC 2013!<br />
Pawel</p>

