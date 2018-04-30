---
title: "Directory Tree in XML"
description: "<p>As a fan of XML, <a href=http://en.wikipedia.org/wiki/Document_Object_Model>the DOM</a>, and interesting design pat"
date: "2010-10-29"
author: "dhudlow"
tags:
    - "blog"
---

<p>As a fan of XML, <a href="http://en.wikipedia.org/wiki/Document_Object_Model">the DOM</a>, and interesting design patterns, when recently asked for a way to retrieve a representation of a public directory tree on an iPhone app, I decided to code something a little more elegant than printing raw XML or, worse, some custom format. My first assumption was that I'd be building an actual DOM tree, then outputting formatted XML from there. This way, I'd be assured my output was always valid XML.</p>
<p>I then needed to decide how to recurse the directory structure. There are several ways to approach this, but since I needed an XML element for each file or directory that was read, I decided to do the reading, recursing, and node creation all in the same place: in a constructor for an element. To achieve this, I extended the PHP <a href="http://php.net/manual/en/class.domelement.php">DOMElement class</a> to a new class called <i>FileSystemNode</i>, and overrode the constructor with my new application-specific logic.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;">class</span> FileSystemElement <span style="color: #000000; font-weight: bold;">extends</span> DOMElement <span style="color: #009900;">&#123;</span>
    <span style="color: #000000; font-weight: bold;">function</span> __construct<span style="color: #009900;">&#40;</span><span style="color: #000088;">$parent</span><span style="color: #339933;">,</span> <span style="color: #000088;">$path</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
&nbsp;
        <span style="color: #666666; font-style: italic;">// Remove trailing slash, if any</span>
        <span style="color: #000088;">$path</span> <span style="color: #339933;">=</span> <a href="http://www.php.net/rtrim"><span style="color: #990000;">rtrim</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$path</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">'/'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
        <span style="color: #666666; font-style: italic;">// Call the parent constructor with the tag name (probably "file" or "dir")</span>
        parent<span style="color: #339933;">::</span>__construct<span style="color: #009900;">&#40;</span><a href="http://www.php.net/filetype"><span style="color: #990000;">filetype</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$path</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
        <span style="color: #666666; font-style: italic;">// Append this new element to its parent</span>
        <span style="color: #000088;">$parent</span><span style="color: #339933;">-></span><span style="color: #004000;">appendChild</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$this</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
        <span style="color: #666666; font-style: italic;">// Add the name of this file or directory as an attribute</span>
        <span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">setAttribute</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'name'</span><span style="color: #339933;">,</span> <a href="http://www.php.net/end"><span style="color: #990000;">end</span></a><span style="color: #009900;">&#40;</span><a href="http://www.php.net/explode"><span style="color: #990000;">explode</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'/'</span><span style="color: #339933;">,</span> <span style="color: #000088;">$path</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
        <span style="color: #666666; font-style: italic;">// If this is a readable directory...</span>
        <span style="color: #b1b100;">if</span> <span style="color: #009900;">&#40;</span><a href="http://www.php.net/is_dir"><span style="color: #990000;">is_dir</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$path</span><span style="color: #009900;">&#41;</span> <span style="color: #339933;">&&</span> <span style="color: #000088;">$handle</span> <span style="color: #339933;">=</span> <a href="http://www.php.net/opendir"><span style="color: #990000;">opendir</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$path</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
&nbsp;
            <span style="color: #666666; font-style: italic;">// read each file and directory it contains...</span>
            <span style="color: #b1b100;">while</span> <span style="color: #009900;">&#40;</span><span style="color: #000088;">$file</span> <span style="color: #339933;">=</span> <a href="http://www.php.net/readdir"><span style="color: #990000;">readdir</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$handle</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
&nbsp;
                <span style="color: #666666; font-style: italic;">// make sure it's not a self- or parent-reference ("." or "..")</span>
                <span style="color: #b1b100;">if</span> <span style="color: #009900;">&#40;</span><span style="color: #000088;">$file</span><span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">0</span><span style="color: #009900;">&#93;</span> <span style="color: #339933;">!=</span> <span style="color: #0000ff;">'.'</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
&nbsp;
                    <span style="color: #666666; font-style: italic;">// and construct it as another element</span>
                    <span style="color: #000000; font-weight: bold;">new</span> FileSystemElement<span style="color: #009900;">&#40;</span><span style="color: #000088;">$this</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">"<span style="color: #006699; font-weight: bold;">$path</span>/<span style="color: #006699; font-weight: bold;">$file</span>"</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
                <span style="color: #009900;">&#125;</span>
            <span style="color: #009900;">&#125;</span>
            <a href="http://www.php.net/closedir"><span style="color: #990000;">closedir</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$handle</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
        <span style="color: #009900;">&#125;</span>
    <span style="color: #009900;">&#125;</span>
<span style="color: #009900;">&#125;</span></pre></div>
<p>With the reading of the file system and the construction of the DOM tree done, all that's left is to create the DOM Document to create the tree into, and format and print the output appropriately. For my example output below, I'm outputting the files and directories of a <a href="http://haveamint.com/">Mint</a> installation.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000088;">$document</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> DOMDocument<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span> 
&nbsp;
<span style="color: #000088;">$root</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> FileSystemElement<span style="color: #009900;">&#40;</span><span style="color: #000088;">$document</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">'mint'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #000088;">$document</span><span style="color: #339933;">-></span><span style="color: #004000;">formatOutput</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">true</span><span style="color: #339933;">;</span>
<a href="http://www.php.net/print"><span style="color: #990000;">print</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$document</span><span style="color: #339933;">-></span><span style="color: #004000;">saveXML</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<p> This produces the below output (which has been clipped to a reasonable length).</p>
<div class="geshifilter">
<pre class="xml geshifilter-xml" style="font-family:monospace;"><span style="color: #009900;"><span style="color: #000000; font-weight: bold;"><?xml</span> <span style="color: #000066;">version</span>=<span style="color: #ff0000;">"1.0"</span><span style="color: #000000; font-weight: bold;">?></span></span>
<span style="color: #009900;"><span style="color: #000000; font-weight: bold;"><dir</span> <span style="color: #000066;">name</span>=<span style="color: #ff0000;">"mint"</span><span style="color: #000000; font-weight: bold;">></span></span>
  <span style="color: #009900;"><span style="color: #000000; font-weight: bold;"><dir</span> <span style="color: #000066;">name</span>=<span style="color: #ff0000;">"pepper"</span><span style="color: #000000; font-weight: bold;">></span></span>
    <span style="color: #009900;"><span style="color: #000000; font-weight: bold;"><dir</span> <span style="color: #000066;">name</span>=<span style="color: #ff0000;">"shauninman"</span><span style="color: #000000; font-weight: bold;">></span></span>
      <span style="color: #009900;"><span style="color: #000000; font-weight: bold;"><dir</span> <span style="color: #000066;">name</span>=<span style="color: #ff0000;">"geomint"</span><span style="color: #000000; font-weight: bold;">></span></span>
        <span style="color: #009900;"><span style="color: #000000; font-weight: bold;"><file</span> <span style="color: #000066;">name</span>=<span style="color: #ff0000;">"readme.txt"</span><span style="color: #000000; font-weight: bold;">/></span></span>
        <span style="color: #009900;"><span style="color: #000000; font-weight: bold;"><file</span> <span style="color: #000066;">name</span>=<span style="color: #ff0000;">"blank.gif"</span><span style="color: #000000; font-weight: bold;">/></span></span>
        <span style="color: #009900;"><span style="color: #000000; font-weight: bold;"><file</span> <span style="color: #000066;">name</span>=<span style="color: #ff0000;">"class.php"</span><span style="color: #000000; font-weight: bold;">/></span></span> 
        ...</pre></div>
<p>And we're done! Are there any problems with this approach, or things you would do differently? Let me know in the comments!</p>

