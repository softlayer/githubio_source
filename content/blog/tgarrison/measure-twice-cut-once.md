---
title: "Measure Twice; Cut Once"
description: "<p>Recently I launched a project that displayed items in a blog-like format with an attached thumbnail.  When I had orig"
date: "2012-04-26"
author: "tgarrison"
tags:
    - "blog"
---

<p>Recently I launched a project that displayed items in a blog-like format with an attached thumbnail.  When I had originally developed this project, I built my thumbnail generator with the intent of adding caching support to it in order to reduce the strain placed on the server during peak usage.  Unfortunately, I had forgotten to add the caching support and the product went live without.</p>
<p>When this product was launched, the initial traffic spurt was about 110 users all at the same time. Quickly, I found out that the server’s 5 minute load average had risen from values lower than 1.0 all the way up to nearly 50.0!  Panicked, I was able to locate the cause of the load, and traced it down to the thumbnail generator.  When I disabled the thumbnails, the load average quickly dropped down below 1.0 again; this promptly confirmed that the thumbnail generator was to blame.</p>
<p>The solution for this issue was actually quite simple and can be applied to nearly any programming language. However, since I was working in PHP, I will present you with a PHP example:</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;"><?php</span>
&nbsp;
      <span style="color: #000088;">$imageFile</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'foo.png'</span><span style="color: #339933;">;</span>
      <span style="color: #000088;">$thumbnailFile</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'foo-thumb.png'</span><span style="color: #339933;">;</span>
&nbsp;
      <span style="color: #b1b100;">if</span> <span style="color: #009900;">&#40;</span><span style="color: #339933;">!</span><a href="http://www.php.net/file_exists"><span style="color: #990000;">file_exists</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$thumbnailFile</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
            <span style="color: #666666; font-style: italic;">// Generate the thumbnail using GD functions</span>
            <span style="color: #666666; font-style: italic;">// The resultant image resource will be $thumbnailImage</span>
            <span style="color: #666666; font-style: italic;">// Detail omitted for clarity</span>
&nbsp;
            imagepng<span style="color: #009900;">&#40;</span><span style="color: #000088;">$thumbnailImage</span><span style="color: #339933;">,</span> <span style="color: #000088;">$thumbnailFile</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
      <span style="color: #009900;">&#125;</span>
&nbsp;
      <a href="http://www.php.net/header"><span style="color: #990000;">header</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'Content-type: image/png'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
      <a href="http://www.php.net/echo"><span style="color: #990000;">echo</span></a> <a href="http://www.php.net/file_get_contents"><span style="color: #990000;">file_get_contents</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$thumbnailFile</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
      <a href="http://www.php.net/exit"><span style="color: #990000;">exit</span></a><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<p>First off, we determine if a thumbnail image already exists for this file. If it doesn’t, we will use GD to create the thumbnail, with the new image resource being represented by the $thumbnailImage variable. Once the image is generated, it will be written to the file described in $thumbnailFile. However, if the thumbnail file exists, we can skip the thumbnail generation. Then, after all is said and done, we will send the MIME Content-type header, echo out the contents of the $thumbnailFile, then exit the script.</p>
<p>As simple as this solution is, mistakenly forgetting to cache the thumbnails once they’re generated was very detrimental to this product and it kept me busy for nearly an hour contacting to the users who were experiencing issues as a result of it.  </p>
<p>An important lesson is taught here, though:<br />
<i>Measure twice, cut once.</i></p>
<p>Or more appropriately, think things through completely before you actually execute them.  This extra measure of planning will save you tremendous amounts of headache.  No detail is too small, either!</p>

