---
title: "A Conversation on API Abstraction"
description: "<p>As a developer, I have a good relationship with the PHP community.  Many of my personal friends are involved in large"
date: "2010-04-08"
author: "dmcaloon"
tags:
    - "blog"
---

<p>As a developer, I have a good relationship with the PHP community.  Many of my personal friends are involved in large PHP projects all over the world.  One friend in particular is the lead developer of <a href="http://theeasyapi.com/">The Easy API</a>.  It's an API wrapper that does the "hard parts" for you.  Some companies release "APIs" that are confusing hodgepodges of unrelated functionality.  Many times the API in question is simply a web form that developers are expected to POST to and parse poorly-formatted output.</p>
<p><a href="http://theeasyapi.com/">The Easy API</a> was designed specifically to take these poorly written APIs and wrap them up in a <em>good</em> PHP API Interface, with real functions and objects so that you can utilize a remote, web-driven API just like you would a native set of objects, or a database wrapper class.</p>
<p>I was discussing this with the lead developer of the project, and we had the following conversation:</p>
<div style="padding: 5px; background: #dddddd; border: 1px solid #999999;">
<span style="color: red; font-weight: bold;">Chad:</span> did you check out The Easy API yet?  <a href="http://theeasyapi.com">http://theeasyapi.com</a><br />
<br /><span style="color: blue; font-weight: bold;">Daniel:</span> Actually, I never had time to check it out.  While I'm doing that, check out our API: <a href="http://sldn.softlayer.com/wiki/index.php/Main_Page">http://sldn.softlayer.com/wiki/index.php/Main_Page</a><br />
<br /><span style="color: blue; font-weight: bold;">Daniel:</span> Do you think you could make an EasyAPI wrapper for that?<br />
<br /><span style="color: red; font-weight: bold;">Chad:</span> What does your company do?<br />
<br /><span style="color: blue; font-weight: bold;">Daniel:</span> unmanaged hosting<br />
<br /><span style="color: blue; font-weight: bold;">Daniel:</span> our API can do EVERYTHING, except for physically remove servers and components<br />
<br /><span style="color: red; font-weight: bold;">Chad:</span> Wow, what a huge API.  Very big indeed<br />
<br /><span style="color: blue; font-weight: bold;">Daniel:</span> you have no idea<br />
<br /><span style="color: red; font-weight: bold;">Chad:</span> yeah, just looking at the docs... i'm getting a very quick idea<br />
<br /><span style="color: blue; font-weight: bold;">Daniel:</span> you can purchase servers, purchase services, format, re-install, upgrade, downgrade, enable ports, change routes, add firewall rules, load balance, monitor, fetch billing, update tickets, even purchase whole new servers and cloud instances<br />
<br /><span style="color: blue; font-weight: bold;">Daniel:</span> all from the API<br />
<br /><span style="color: blue; font-weight: bold;">Daniel:</span> our customer portal sits on top of the api, anything you can do in the portal you can do in the api<br />
<br /><span style="color: red; font-weight: bold;">Chad:</span> yeah, it looks like it would take a lot of learning and figuring out how to do things, but it's immensely powerful<br />
<br /><span style="color: red; font-weight: bold;">Chad:</span> Your API is a perfect example of how I'm trying to figure out the best way to handle well documented large API's<br />
<br /><span style="color: blue; font-weight: bold;">Daniel:</span> We have a github project (<a href="http://github.com/softlayer">http://github.com/softlayer</a>) with an API client that translates to PHP objects already  <em>[Note: since this conversation, the <a href="http://github.com/softlayer">github page</a> has been updated with a <a href="http://sldn.softlayer.com/02/2010/something-new-for-your-api-toolbox/">PERL client</a> -ed.]</em><br />
<br /><span style="color: red; font-weight: bold;">Chad:</span> In that case, you barely even need the EasyAPI, your API already functions the way they all should.
</div>
<p>That was a great thing to hear, as a SoftLayer Developer.  The reason we wrote the API the way we did was because we were all tired of companies calling something an "API" when it was really a URL that would spit out a CSV file, or a ridiculously strict XML engine that would complain about a single space out of place.  In fact, I once worked with an API that would throw "not valid XML" errors on perfectly valid XML.  The most ironic part was that the "not valid XML" error itself was not valid XML.</p>
<p>As developers who spend much of our time integrating third party products, APIs, and services, we know how hard it is to work with a poorly documented, poorly implemented interface.  That's why part of our standard release procedure is having our <a href="http://sldn.softlayer.com/author/klaude/">API Evangelist</a> review our method names, variable names, class names, and all related documentation to make sure they're not only easy to read, but follow the pattern that the rest of the API follows.  That's why you always see "hardware" keys on our objects: we're simply not allowed to call something "servers," the code cannot be released until the API-exposed functionality is ready for public consumption.</p>
<p>We've all worked very hard on the API, because the API is what drives the portal, and the portal is what drives our customers.  We're happy to see everyone using the portal, but what really excites us is when customers use the API directly to form their own custom tools.  The portal is a wonderful, powerful tool, but we understand that not every customer is happy with using the same thing.  That's why we exposed the API to our customers: so you could ALL write your own custom API-enabled objects.  If you do, please share them, if not with the community at large, than at least with us directly.  We'd love to see how customers are using the API, and if you share with us your most difficult API tasks, we'll work to make them better.  Even though the current SoftLayer API makes API-wrapper authors say "wow," we want to make it even better.</p>

