---
title: "Helper Functions: Small Changes, Big Win"
description: "<p>If your job is anything like mine, there is just never enough time to finish everything.  When working on projects, I"
date: "2011-08-31"
author: "tgarrison"
tags:
    - "blog"
---

<p>If your job is anything like mine, there is just never enough time to finish everything.  When working on projects, I try to find ways which can speed up my development process.  There are many tools and ideas which can help greatly in this area, however, sometimes very small behavioral changes can result in a cumulative win.  When working on web-based projects in PHP, I often find that I need to see what’s contained in an array or an object so I can get my code just right.  PHP offers a nice way to do this with the print_r() function, but there’s a problem in using it for web apps: It’s monospaced.</p>
<p>Now, this may seem like a miniscule problem, as you can easily wrap the print_r() in <span class="geshifilter"><code class="text geshifilter-text"><pre></pre></code></span>, but that takes away keystrokes that would be better suited for other tasks. To get around this repetitive bloat, I normally declare a function in the global scope of my project. This function simply accepts the object you wish to print out,  and wraps it in the HTML <span class="geshifilter"><code class="text geshifilter-text"><pre></pre></code></span> tags to display the monospaced text as intended, The code snippet below outlines this task a little more clearly:</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;">    <span style="color: #000000; font-weight: bold;">function</span> ap<span style="color: #009900;">&#40;</span><span style="color: #000088;">$var</span><span style="color: #009900;">&#41;</span> 
    <span style="color: #009900;">&#123;</span> 
        <a href="http://www.php.net/echo"><span style="color: #990000;">echo</span></a> <span style="color: #0000ff;">'<pre>'</span><span style="color: #339933;">;</span> 
        <a href="http://www.php.net/print_r"><span style="color: #990000;">print_r</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$var</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span> 
        <a href="http://www.php.net/echo"><span style="color: #990000;">echo</span></a> <span style="color: #0000ff;">'</pre>'</span><span style="color: #339933;">;</span> 
    <span style="color: #009900;">&#125;</span></pre></div>
<p>Using print_r() alone:<br />
<span class="geshifilter"><code class="php geshifilter-php"><a href="http://www.php.net/array"><span style="color: #990000;">Array</span></a> <span style="color: #009900;">&#40;</span> <span style="color: #009900;">&#91;</span>name<span style="color: #009900;">&#93;</span> <span style="color: #339933;">=></span> Tim Garrison <span style="color: #009900;">&#91;</span>favoriteFoods<span style="color: #009900;">&#93;</span> <span style="color: #339933;">=></span> <a href="http://www.php.net/array"><span style="color: #990000;">Array</span></a> <span style="color: #009900;">&#40;</span> <span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">0</span><span style="color: #009900;">&#93;</span> <span style="color: #339933;">=></span> Blueberry Pie <span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">1</span><span style="color: #009900;">&#93;</span> <span style="color: #339933;">=></span> Pizza <span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">2</span><span style="color: #009900;">&#93;</span> <span style="color: #339933;">=></span> Tortelini <span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#41;</span></code></span></p>
<p>Using this ap() function:</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><a href="http://www.php.net/array"><span style="color: #990000;">Array</span></a>
<span style="color: #009900;">&#40;</span>
    <span style="color: #009900;">&#91;</span>name<span style="color: #009900;">&#93;</span> <span style="color: #339933;">=></span> Tim Garrison
    <span style="color: #009900;">&#91;</span>favoriteFoods<span style="color: #009900;">&#93;</span> <span style="color: #339933;">=></span> <a href="http://www.php.net/array"><span style="color: #990000;">Array</span></a>
        <span style="color: #009900;">&#40;</span>
            <span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">0</span><span style="color: #009900;">&#93;</span> <span style="color: #339933;">=></span> Blueberry Pie
            <span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">1</span><span style="color: #009900;">&#93;</span> <span style="color: #339933;">=></span> Pizza
            <span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">2</span><span style="color: #009900;">&#93;</span> <span style="color: #339933;">=></span> Tortelini
        <span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #009900;">&#41;</span></pre></div>
<p>By using this function, you simply issue a ap($foo); in your code, rather than having to spell out each bit of the HTML tag. This is just one example of how making a small change in how you code results in directing your efforts on actually writing code rather than formatting your debugging statements! </p>

