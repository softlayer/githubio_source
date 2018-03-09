---
title: "Something new for your API Toolbox"
description: "<p>An interesting facet of the development and systems administration business is the number of 80% projects that build "
date: "2010-02-25"
author: "klaude"
tags:
    - "blog"
---

<p>An interesting facet of the development and systems administration business is the number of 80% projects that build up over time. An 80% project is that awesome library, script, rewrite, new system, or what have you that's cooling on your back burner. It's almost done but it's missing the finishing touches. Maybe it needs a few code tweaks. Maybe it needs a little more documentation. Maybe you're still finalizing settings and playing with patches. Don't lie; we know you've got these projects hanging around. I've got a list of 80% projects as long as my arm.</p>
<p>It's time to check something off my 80% projects list. I've finally finished documenting and am happy to release the SoftLayer API Perl client library! This module will make Perl API hackers' lives a whole lot easier. Previously you had to build SOAP API calls manually using the <a href="http://www.soaplite.com/">SOAP::Lite</a> module and parse the response into something easier to handle.  Now you can accomplish the same thing with a series of easy to use helper methods. Functionality is very similar to our <a href="http://github.com/softlayer/softlayer-api-php-client">PHP client</a> but with a Perl twist. For instance, you can do clever one liners!</p>
<div class="geshifilter">
<pre class="perl geshifilter-perl" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;">use</span> SoftLayer<span style="color: #339933;">::</span><span style="color: #006600;">API</span><span style="color: #339933;">::</span><span style="color: #006600;">SOAP</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Grab my account information.</span>
<span style="color: #b1b100;">my</span> <span style="color: #0000ff;">$account</span> <span style="color: #339933;">=</span> SoftLayer<span style="color: #339933;">::</span><span style="color: #006600;">API</span><span style="color: #339933;">::</span><span style="color: #006600;">SOAP</span><span style="color: #339933;">-></span><span style="color: #006600;">new</span><span style="color: #009900;">&#40;</span>
    <span style="color: #ff0000;">'SoftLayer_Account'</span><span style="color: #339933;">,</span> 
    <a href="http://perldoc.perl.org/functions/undef.html"><span style="color: #000066;">undef</span></a><span style="color: #339933;">,</span> 
    <span style="color: #ff0000;">'my API username'</span><span style="color: #339933;">,</span> 
    <span style="color: #ff0000;">'my API key'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">-></span><span style="color: #006600;">getObject</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<p>Check out our <a href="http://github.com/softlayer/softlayer-api-perl-client/blob/master/README.pod">README</a> for many and more comprehensive examples. Download the library from our <a href="http://github.com/softlayer">github page</a> at:</p>
<p><a href="http://github.com/softlayer/softlayer-api-perl-client">http://github.com/softlayer/softlayer-api-perl-client</a></p>
<p>As with all of our projects we're very open to feedback, so please comment or post on our <a href="http://forums.softlayer.com/">forums</a> and let us know what you think. I can't wait knock a few more 80% projects off the ol' list. You're going to love them. :) See y'all next time!</p>

