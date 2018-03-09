---
title: "Pure CSS Modal Overlays"
description: "<p>If you’ve read my previous blogs, you know that I tend to focus on very user-friendly tips and tricks, small tidbits "
date: "2012-11-05"
author: "cwolff"
tags:
    - "blog"
---

<p>If you’ve read my previous blogs, you know that I tend to focus on very user-friendly tips and tricks, small tidbits that make the browsing experience more appealing to the end users. Nowadays, if you don’t spruce up your content and make it look like a million bucks, you’ll lose your users’ interest. They say you have less than eight seconds to make an impression!</p>
<p>One method to increase usability I employ on nearly every site I build has been integrating modal overlays to display various content. An overlay can contain nothing more than a paragraph of instructions or even complicated forms.<br />
Though I am an advocate of jQuery and PHP, I find that sometimes these can be overkill for tasks such as this; you can accomplish the same effect using nothing more than CSS and a little bit of standard Javascript (without need for library inclusion).</p>
<p>You can see some examples of the “lightbox effect” here: <a href="http://lokeshdhakar.com/projects/lightbox2/" title="http://lokeshdhakar.com/projects/lightbox2/">http://lokeshdhakar.com/projects/lightbox2/</a> . This is exactly what we’re going to recreate. Only, no inclusions, no special coding, just regular ol’ styling.</p>
<p>Let’s get started!</p>
<p>First, let’s create our <span class="geshifilter"><code class="text geshifilter-text">DIV</code></span> element that acts as the overlay. This div won’t be visible until it’s called upon:</p>
<div class="geshifilter">
<pre class="html4strict geshifilter-html4strict" style="font-family:monospace;"><span style="color: #009900;"><<a href="http://december.com/html/4/element/div.html"><span style="color: #000000; font-weight: bold;">div</span></a> <span style="color: #000066;">id</span><span style="color: #66cc66;">=</span>”overlay”></span>
    This is where you will put your inline HTML for the content inside of the overlay
<span style="color: #009900;"><<span style="color: #66cc66;">/</span><a href="http://december.com/html/4/element/div.html"><span style="color: #000000; font-weight: bold;">div</span></a>></span></pre></div>
<p>Next, let’s create our capsule (that encapsulates the whole page) to act as our “fading effect.”</p>
<div class="geshifilter">
<pre class="html4strict geshifilter-html4strict" style="font-family:monospace;"><span style="color: #009900;"><<a href="http://december.com/html/4/element/div.html"><span style="color: #000000; font-weight: bold;">div</span></a> <span style="color: #000066;">id</span><span style="color: #66cc66;">=</span>”fade”><<span style="color: #66cc66;">/</span><a href="http://december.com/html/4/element/div.html"><span style="color: #000000; font-weight: bold;">div</span></a>></span></pre></div>
<p>There’s no content inside because it will only provide the background fading effect to our overlay.</p>
<p>Fantastic! Next, let’s add our styling:</p>
<div class="geshifilter">
<pre class="html4strict geshifilter-html4strict" style="font-family:monospace;"><span style="color: #009900;"><<a href="http://december.com/html/4/element/style.html"><span style="color: #000000; font-weight: bold;">style</span></a> <span style="color: #000066;">type</span><span style="color: #66cc66;">=</span>”<span style="color: #000066;">text</span><span style="color: #66cc66;">/</span>css”></span>
#overlay {
    display: none; /* ensures it’s invisible until it’s called */
    position: absolute; /* makes the div go into a position that’s absolute to the browser viewing area */
    left: 25%; /* positions the div half way horizontally */
    top: 25%; /* positions the div half way vertically */
    padding: 25px; 
    border: 2px solid black;
    background-color: #ffffff;
    width: 50%;
    height: 50%;
    z-index: 100; /* makes the div the top layer, so it’ll lay on top of the other content */
}
#fade {
    display: none;  /* ensures it’s invisible until it’s called */
    position: absolute;  /* makes the div go into a position that’s absolute to the browser viewing area */
    left: 0%; /* makes the div span all the way across the viewing area */
    top: 0%; /* makes the div span all the way across the viewing area */
    background-color: black;
    -moz-opacity: 0.7; /* makes the div transparent, so you have a cool overlay effect */
    opacity: .70;
    filter: alpha(opacity=70);
    width: 100%;
    height: 100%;
    z-index: 90; /* makes the div the second most top layer, so it’ll lay on top of everything else EXCEPT for divs with a higher z-index (meaning the #overlay ruleset) */
}
<span style="color: #009900;"><<span style="color: #66cc66;">/</span><a href="http://december.com/html/4/element/style.html"><span style="color: #000000; font-weight: bold;">style</span></a>></span></pre></div>
<p>Now... to create the trigger for the effect: the ability to open and close our “popup.”<br />
Create an anchor tag:</p>
<div class="geshifilter">
<pre class="html4strict geshifilter-html4strict" style="font-family:monospace;"><span style="color: #009900;"><<a href="http://december.com/html/4/element/a.html"><span style="color: #000000; font-weight: bold;">a</span></a> </span>
<span style="color: #009900;">    <span style="color: #000066;">onclick</span><span style="color: #66cc66;">=</span><span style="color: #ff0000;">"document.getElementById('overlay').style.display='block';document.getElementById('fade').style.display='block'"</span></span>
<span style="color: #009900;">    <span style="color: #000066;">href</span><span style="color: #66cc66;">=</span><span style="color: #ff0000;">"javascript:void(0)"</span>Click here to open the overlay</span>
<span style="color: #009900;"><<span style="color: #66cc66;">/</span><a href="http://december.com/html/4/element/a.html"><span style="color: #000000; font-weight: bold;">a</span></a>></span></pre></div>
<p>Looks like a lot going on in the link, but let’s chop it down. </p>
<div class="geshifilter">
<pre class="html4strict geshifilter-html4strict" style="font-family:monospace;">document.getElementById(‘overlay’).style.display=’block’;</pre></div>
<p>What you’re doing here is adding the style of “display=”block” to the DIV that has an ID of ‘overlay.’ By adding this style, we’re triggering the overlay and it’s fading background to show. In the second part of that anchor tag, you’re just repeating the same thing to the ‘fade’ DIV.</p>
<p>Finally, we need a link to close the overlay! Inside of your ‘overlay’ DIV, let’s add another anchor tag:</p>
<div class="geshifilter">
<pre class="html4strict geshifilter-html4strict" style="font-family:monospace;"><span style="color: #009900;"><<a href="http://december.com/html/4/element/a.html"><span style="color: #000000; font-weight: bold;">a</span></a> </span>
<span style="color: #009900;">    <span style="color: #000066;">onclick</span><span style="color: #66cc66;">=</span><span style="color: #ff0000;">"document.getElementById('overlay').style.display='none';document.getElementById('fade').style.display='none'"</span></span>
<span style="color: #009900;">    <span style="color: #000066;">href</span><span style="color: #66cc66;">=</span><span style="color: #ff0000;">"javascript:void(0)"</span>Click here to open the overlay</span>
<span style="color: #009900;"><<span style="color: #66cc66;">/</span><a href="http://december.com/html/4/element/a.html"><span style="color: #000000; font-weight: bold;">a</span></a>></span></pre></div>
<p>This time, all we’re doing is simply changing the “display: block” to “display: none” to make the overlay and it’s background fade disappear!<br />
The final result:<br />
[inline:cwolfoverlay.jpg]</p>

