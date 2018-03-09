---
title: "PHP Default Time Zone"
description: "<p>If your company is dealing with international customers, you probably deal with lots of time conversions between diff"
date: "2011-08-04"
author: "clee"
tags:
    - "blog"
---

<p>If your company is dealing with international customers, you probably deal with lots of time conversions between different time zones. Time conversion can be tricky thanks to daylight savings time in some regions. Another factor that can cause some confusion is missing or not knowing your PHP default time zone.</p>
<p>PHP (or any other language) should have a base time zone in order to convert times. If you have not configured the default time zone for PHP, it will try to guess what the default time zone should be. It attempts to find the default time zone in the below order until it finds a valid time zone value.</p>
<ol>
<li>The time zone value set by <a href="http://php.net/date_default_timezone_set">date_default_timezone_set()</a></li>
<li>Reading the TZ environment variable</li>
<li>date.timezone value from php.ini</li>
<li>Best guess from your OS</li>
</ol>
<div style="color: #D8000C; background-color: #FFBABA; border: 1px solid; margin: 10px 10%; padding:15px 10px 15px 15px; width: 70%">The possible side effects for a missing default time zone include incorrect time conversion, adverse affects to PHP performance, and even unwanted results in regions that use dalylight-savings time.</div>
<p>Look at the code below and the results.</p>
<h2>Snippet 1</h2>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000088;">$dateObject</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> DateTime<span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'2011-07-10 01:00:00'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$utcTimeZone</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> DateTimeZone<span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'UTC'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$dateObject</span><span style="color: #339933;">-></span><span style="color: #004000;">setTimezone</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$utcTimeZone</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<a href="http://www.php.net/echo"><span style="color: #990000;">echo</span></a> <span style="color: #000088;">$dateObject</span><span style="color: #339933;">-></span><span style="color: #004000;">format</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'Y-m-d H:i:s'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<h3>Results</h3>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">// In America/Chicago time zone
2011-07-10 06:00:00
&nbsp;
// In America/Los_Angeles time zone
2011-07-10 08:00:00
&nbsp;
// In America/New_York time zone
2011-07-10 05:00:00</pre></div>
<h2>Snippet 2</h2>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #666666; font-style: italic;">/* 
Imagine your servers are spread geographically and are behind a DNS load balancer. Each server might have been configured with a system time zone appropriate for its location. If that’s the case, the last line will print different dates which you probably don’t want.
*/</span> 
<span style="color: #666666; font-style: italic;">// For the demonstration purposes, override the time zone.</span>
date_default_timezone_set<span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'America/Chicago'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$dateTemplate</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'2011-03-13 %02d:00:00'</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #b1b100;">for</span> <span style="color: #009900;">&#40;</span><span style="color: #000088;">$i</span> <span style="color: #339933;">=</span> <span style="color: #cc66cc;">1</span><span style="color: #339933;">;</span> <span style="color: #000088;">$i</span> <span style="color: #339933;"><</span> <span style="color: #cc66cc;">4</span><span style="color: #339933;">;</span> <span style="color: #000088;">$i</span><span style="color: #339933;">++</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
   <span style="color: #000088;">$dateString</span> <span style="color: #339933;">=</span> <a href="http://www.php.net/sprintf"><span style="color: #990000;">sprintf</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$dateTemplate</span><span style="color: #339933;">,</span> <span style="color: #000088;">$i</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span> <span style="color: #666666; font-style: italic;">// e.g. $dateString  = '2011-03-13 01:00:00'</span>
   <span style="color: #000088;">$dateFunctionString</span> <span style="color: #339933;">=</span> <a href="http://www.php.net/date"><span style="color: #990000;">date</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'Y-m-d H:i:s'</span><span style="color: #339933;">,</span> <a href="http://www.php.net/strtotime"><span style="color: #990000;">strtotime</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$dateString</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
   <a href="http://www.php.net/echo"><span style="color: #990000;">echo</span></a> <span style="color: #0000ff;">'Source string: '</span> <span style="color: #339933;">.</span> <span style="color: #000088;">$dateString</span> <span style="color: #339933;">.</span> <span style="color: #0000ff;">'<br /'</span><span style="color: #339933;">;</span>
   <a href="http://www.php.net/echo"><span style="color: #990000;">echo</span></a> <span style="color: #0000ff;">'date() function: '</span> <span style="color: #339933;">.</span> <span style="color: #000088;">$dateFunctionString</span> <span style="color: #339933;">.</span> <span style="color: #0000ff;">'<br /<br /'</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span></pre></div>
<h3>Result</h3>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">Source string: 2011-03-13 01:00:00
date() function: 2011-03-13 01:00:00
&nbsp;
Source string: 2011-03-13 02:00:00
date() function: 2011-03-13 03:00:00
&nbsp;
Source string: 2011-03-13 03:00:00
date() function: 2011-03-13 03:00:00</pre></div>
<p>Notice the second result. This is not necessarily wrong. In fact, PHP converts and calculates time correctly. "2010-03-13 02:00:00" was actually "2010-03-13 03:00:00" if you were in US/Central on the spring forward day. However, it will be wrong if you were to insert hourly data into a database as it will create duplicate entries for 3/14 2 a.m.</p>
<h2>Snippet 3</h2>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #666666; font-style: italic;">// For the demonstration purposes, override the time zone.</span>
date_default_timezone_set<span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'America/Chicago'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #000088;">$dateObject</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> DateTime<span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'2011-03-13 01:00:00'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #b1b100;">for</span> <span style="color: #009900;">&#40;</span><span style="color: #000088;">$i</span> <span style="color: #339933;">=</span> <span style="color: #cc66cc;">1</span><span style="color: #339933;">;</span> <span style="color: #000088;">$i</span> <span style="color: #339933;"><</span> <span style="color: #cc66cc;">4</span><span style="color: #339933;">;</span> <span style="color: #000088;">$i</span><span style="color: #339933;">++</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
   <a href="http://www.php.net/echo"><span style="color: #990000;">echo</span></a> <span style="color: #0000ff;">'DateTime object: '</span> <span style="color: #339933;">.</span> <span style="color: #000088;">$dateObject</span><span style="color: #339933;">-></span><span style="color: #004000;">format</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'Y-m-d H:i:s'</span><span style="color: #009900;">&#41;</span> <span style="color: #339933;">.</span> <span style="color: #0000ff;">'<br /'</span><span style="color: #339933;">;</span>
   <span style="color: #000088;">$dateObject</span><span style="color: #339933;">-></span><span style="color: #004000;">modify</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'+1 hour'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span></pre></div>
<h3>Result</h3>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">DateTime object: 2011-03-13 01:00:00
DateTime object: 2011-03-13 03:00:00
DateTime object: 2011-03-13 04:00:00</pre></div>
<p>Notice how the time jumps from 1 am to 3 am. You might want to use a time zone that is not affected by daylight savings time especially when you use DateTime::modify method.</p>
<p>These kinds of issues can be avoided by explicitly setting the default time zone using date_default_timezone_set() method somewhere in your configuration data. Using date_default_timezone_set() can also speed up "date" related function execution time as PHP doesn't have to search or try to guess the default time zone every time you use date*function. Finally, try to use "UTC" if possible so you can avoid issues related to the daylight savings time.</p>

