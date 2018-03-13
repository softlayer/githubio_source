---
title: "PHP Type Conversions for Comparison"
description: "<p>There has been some discussion recently among our dev team regarding PHP type conversion.  I’ll give some of the prob"
date: "2009-01-02"
author: "dmcaloon"
tags:
    - "blog"
---

<p>There has been some discussion recently among our dev team regarding PHP type conversion.  I’ll give some of the problems we’ve run into and then try to shed some light on the inner workings of PHP when it does comparisons.</p>
<p>The first example may seem familiar to most seasoned developers, but when chained together it brings up an interesting point about PHP: The <a href="http://www.php.net/manual/en/language.operators.comparison.php">= = operator</a> isn’t <a href="http://en.wikipedia.org/wiki/Transitive_relation">transitive</a>.  </p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><a href="http://www.php.net/echo"><span style="color: #990000;">echo</span></a> <span style="color: #009900;">&#40;</span><span style="color: #000000; font-weight: bold;">null</span>    <span style="color: #339933;">=</span> <span style="color: #339933;">=</span> <span style="color: #cc66cc;">0</span>        ? <span style="color: #0000ff;">"YES"</span> <span style="color: #339933;">:</span> <span style="color: #0000ff;">"NO"</span><span style="color: #009900;">&#41;</span> <span style="color: #339933;">.</span> <span style="color: #0000ff;">"<span style="color: #000099; font-weight: bold;">\
</span>"</span><span style="color: #339933;">;</span>  <span style="color: #666666; font-style: italic;">//YES</span>
<a href="http://www.php.net/echo"><span style="color: #990000;">echo</span></a> <span style="color: #009900;">&#40;</span><span style="color: #0000ff;">"null"</span> <span style="color: #339933;">=</span> <span style="color: #339933;">=</span> <span style="color: #cc66cc;">0</span>        ? <span style="color: #0000ff;">"YES"</span> <span style="color: #339933;">:</span> <span style="color: #0000ff;">"NO"</span><span style="color: #009900;">&#41;</span> <span style="color: #339933;">.</span> <span style="color: #0000ff;">"<span style="color: #000099; font-weight: bold;">\
</span>"</span><span style="color: #339933;">;</span>  <span style="color: #666666; font-style: italic;">//YES</span>
<a href="http://www.php.net/echo"><span style="color: #990000;">echo</span></a> <span style="color: #009900;">&#40;</span><span style="color: #0000ff;">"null"</span> <span style="color: #339933;">=</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">null</span>    ? <span style="color: #0000ff;">"YES"</span> <span style="color: #339933;">:</span> <span style="color: #0000ff;">"NO"</span><span style="color: #009900;">&#41;</span> <span style="color: #339933;">.</span> <span style="color: #0000ff;">"<span style="color: #000099; font-weight: bold;">\
</span>"</span><span style="color: #339933;">;</span>  <span style="color: #666666; font-style: italic;">//NO</span></pre></div>
<p>As you can see, null = = 0 = = "null", but null != "null"</p>
<p>You may be familiar with the following kind of error.  The erroneous code is usually similar to:</p>
<p><span class="geshifilter"><code class="php geshifilter-php"><span style="color: #b1b100;">if</span> <span style="color: #009900;">&#40;</span> <span style="color: #000088;">$a</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">"Hello"</span> <span style="color: #339933;">&&</span> <span style="color: #000088;">$b</span> <span style="color: #339933;">!=</span> <span style="color: #0000ff;">"World"</span> <span style="color: #009900;">&#41;</span></code></span></p>
<p>Seeded with $b = "World", the function assigned FALSE to $a.  This is because there was a single = instead of = = in $a = "Hello", so PHP was interpreting the whole thing as an assignment operator.  Since $b was not equal to "World" $b != "World" was returning TRUE, and TRUE was && with "Hello", so "Hello" was converted to FALSE, then FALSE && TRUE was assigned to $a.</p>
<p>PHP has a certain order of precedence for data types.  It is defined loosely in the manual’s <a href="http://www.php.net/manual/en/language.operators.comparison.php">comparison operators page</a>, but I will try to spell it out more explicitly here.  There are 8 basic types of data in PHP.  In order of operator precedence, they are:</p>
<ul>
<li>Boolean</li>
<li>Object</li>
<li>Array</li>
<li>Floating Point Number</li>
<li>Integer</li>
<li>String</li>
<li>Resource</li>
<li>NULL</li>
</ul>
<p>That is to say, if you compare any two data types on the list, the variable with the data type lower on the list will be converted to the upper variable’s data type, and then the comparison is applied.  However, when applying the first example to this hard and fast rule, we find it lacking.  In reality, there are certain comparisons that are so far off PHP converts BOTH data types to a third data type.  The first example actually works out like:</p>
<ul>
<li><b>null = = 0.</b>  both were converting to FALSE, so the comparison was succeeding</li>
<li><b>"null" = = 0.</b>  "null" was converting to 0, so the comparison was succeeding</li>
<li><b>"null" = = null.</b>  "null" was converting to TRUE, NULL was converting to false.</li>
</ul>
<p>It’s much more easily represented as a table:</p>
<div style="width: 510px; height: 510px; overflow: scroll;">
<table width="1000" border="1" cellpadding="0" style="margin: 0px; padding: 0px;">
<tr>
<td bgcolor="lightgrey" style="background:lightgrey;">&nbsp;</td>
<td align="center"><b>Boolean</b></td>
<td align="center"><b>Object</b></td>
<td align="center"><b>Array</b></td>
<td align="center"><b><nobr>Floating Point Number</nobr></b></td>
<td align="center"><b>Integer</b></td>
<td align="center"><b>String</b></td>
<td align="center"><b>Resource</b></td>
<td align="center"><b>NULL</b></td>
</tr>
<tr>
<td align="center"><b>Boolean</b></td>
<td bgcolor="lightgrey" style="background:lightgrey;">&nbsp;</td>
<td align="left">Boolean<br />Objects always resolve to true</td>
<td align="left">Boolean<br />Empty arrays are false, all others are true</td>
<td align="left">Boolean<br />0 resolves to false, all others are true</td>
<td align="left">Boolean<br />0 resolves to false, all others are true</td>
<td align="left">Boolean<br />"" resoves to false, all others are true</td>
<td align="left">Boolean<br />Resources always resolve to true</td>
<td align="left">Boolean<br />NULL is always false</td>
</tr>
<tr>
<td align="center"><b>Object</b></td>
<td align="left">Boolean<br />Objects always resolve to true</td>
<td bgcolor="lightgrey" style="background:lightgrey;">&nbsp;</td>
<td align="left"><nobr>No conversion made</nobr><br />Objects are always greater-than</td>
<td align="left"><nobr>No conversion made</nobr><br />Objects are always greater-than</td>
<td align="left"><nobr>No conversion made</nobr><br />Objects are always greater-than</td>
<td align="left"><nobr>No conversion made</nobr><br />Objects are always greater-than</td>
<td align="left"><nobr>No conversion made</nobr><br />Objects are always greater-than</td>
<td align="left">Boolean<br />Objects always resolve to true</td>
</tr>
<tr>
<td align="center"><b>Array</b></td>
<td align="left">Boolean<br />Empty arrays are false, all others are true</td>
<td align="left"><nobr>No conversion made</nobr><br />Objects are always greater-than</td>
<td bgcolor="lightgrey" style="background:lightgrey;">&nbsp;</td>
<td align="left"><nobr>No conversion made</nobr><br />Arrays are always greater-than</td>
<td align="left"><nobr>No conversion made</nobr><br />Arrays are always greater-than</td>
<td align="left"><nobr>No conversion made</nobr><br />Arrays are always greater-than</td>
<td align="left"><nobr>No conversion made</nobr><br />Arrays are always greater-than</td>
<td align="left">Boolean<br />Empty arrays are false, all others are true</td>
</tr>
<tr>
<td align="center"><b>Floating Point</b></td>
<td align="left">Boolean<br />0 resolves to false, all others are true</td>
<td align="left"><nobr>No conversion made</nobr><br />Objects are always greater-than</td>
<td align="left"><nobr>No conversion made</nobr><br />Arrays are always greater-than</td>
<td bgcolor="lightgrey" style="background:lightgrey;">&nbsp;</td>
<td align="left">Floating Point</td>
<td align="left">Floating Point</td>
<td align="left">Floating Point</td>
<td align="left">Boolean<br />0 resolves to false, all others are true</td>
</tr>
<tr>
<td align="center"><b>Integer</b></td>
<td align="left">Boolean<br />0 resolves to false, all others are true</td>
<td align="left"><nobr>No conversion made</nobr><br />Objects are always greater-than</td>
<td align="left"><nobr>No conversion made</nobr><br />Arrays are always greater-than</td>
<td align="left">Floating Point</td>
<td bgcolor="lightgrey" style="background:lightgrey;">&nbsp;</td>
<td align="left">Floating Point</td>
<td align="left">Integer</td>
<td align="left">Boolean<br />0 resolves to false, all others are true</td>
</tr>
<tr>
<td align="center"><b>String</b></td>
<td align="left">Boolean<br />0 resolves to false, all others are true</td>
<td align="left"><nobr>No conversion made</nobr><br />Objects are always greater-than</td>
<td align="left"><nobr>No conversion made</nobr><br />Arrays are always greater-than</td>
<td align="left">Floating Point</td>
<td align="left">Floating Point</td>
<td bgcolor="lightgrey" style="background:lightgrey;">&nbsp;</td>
<td align="left">Floating Point</td>
<td align="left">String<br />NULL is converted to ""</td>
</tr>
<tr>
<td align="center"><b>Resource</b></td>
<td align="left">Boolean<br />Resources always resolve to true</td>
<td align="left"><nobr>No conversion made</nobr><br />Objects are always greater-than</td>
<td align="left"><nobr>No conversion made</nobr><br />Arrays are always greater-than</td>
<td align="left">Floating Point</td>
<td align="left">Integer</td>
<td align="left">Floating Point</td>
<td bgcolor="lightgrey" style="background:lightgrey;">&nbsp;</td>
<td align="left">Boolean<br />Resources always resolve to true</td>
</tr>
<tr>
<td align="center"><b>NULL</b></td>
<td align="left">Boolean<br />NULL resolves to false</td>
<td align="left">Boolean<br />Objects always resolve to true<br />Never = = null</td>
<td align="left">Boolean<br />Empty arrays are false, all others are true</td>
<td align="left">Boolean<br />0 resolves to false, all others are true</td>
<td align="left">Boolean<br />0 resolves to false, all others are true</td>
<td align="left">String<br />NULL is converted to ""</td>
<td align="left">Boolean<br />Resources always resolve to true<br />Never = = null</td>
<td bgcolor="lightgrey" style="background:lightgrey;">&nbsp;</td>
</tr>
</table>
</div>
<p>In the table where you see the phrase "No Conversion Made" that means that those two data types will never = = each other.  However, in most of those situations data types are given specific return values for quantitative comparisons, such as greater-than and less-than.  Note the specific case of NULL, where almost every instance of comparing to NULL results in both types being converted to Boolean.  </p>
<p>Armed with this information, we are now capable of determining the outcome of almost any comparison in PHP.  We know, for instance, that array() is greater than "Hello", but "Hello" is less than 2.  We know that stdClass() is greater than array(), but both of them are equal to TRUE.  There are plenty of places where PHP contradicts normal logic, because of the sometimes convoluted process involved in comparing different data types.</p>
<p>The fact that PHP sometimes internally converts two operands to a third, unrelated data type can be quite confusing.  I hope, however, that the chart in this article will help you work out exactly what it’s doing.</p>
<p>Of course, as one of our lead developers is quick to point out, this whole discussion would be moot if everyone used = = =.</p>

