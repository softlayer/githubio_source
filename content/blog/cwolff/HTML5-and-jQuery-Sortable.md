---
title: "HTML5 and jQuery Sortable"
description: "<p>If you’re a developer, you know the feeling of a constant infatuation with learning new methods, strategies and langu"
date: "2012-11-15"
author: "cwolff"
tags:
    - "blog"
---

<p>If you’re a developer, you know the feeling of a constant infatuation with learning new methods, strategies and languages. Earlier this year, I posted an introduction to HTML5 via game programming and I thought to myself, "There has to be a more practical use for this in my daily work". Thus my research began.</p>
<p>When searching for new jQuery plugins, I tend to spend hours, if not days sifting through options and comparing the pros and cons of each plugin. During one such research binge a particular plugin caught my eye.<br />
I found a nifty plugin called HTML5 Sortable, which combines with jQuery to create flexible sortable lists. The best part: it’s only 1kB gzipped and minified, which is WAY better than the average 35-40kB of other sorting plugins. Remember: each kB adds just a tiny bit of overhead to your page. So unless you need extra functionality a HUGE and incredibly versatile sorting plugin offers, it’s best to minify as much as you can.</p>
<p>As usual, let’s start with our jQuery library include (courtesy of Google Hosted APIs):</p>
<div class="geshifilter">
<pre class="html4strict geshifilter-html4strict" style="font-family:monospace;"><span style="color: #009900;"><<a href="http://december.com/html/4/element/script.html"><span style="color: #000000; font-weight: bold;">script</span></a> <span style="color: #000066;">src</span><span style="color: #66cc66;">=</span><span style="color: #ff0000;">"http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"</span>><<span style="color: #66cc66;">/</span><a href="http://december.com/html/4/element/script.html"><span style="color: #000000; font-weight: bold;">script</span></a>></span></pre></div>
<p>Now to create our HTML5 list, which will allow users to drag and drop <span class="geshifilter"><code class="html4strict geshifilter-html4strict"><span style="color: #009900;"><<a href="http://december.com/html/4/element/li.html"><span style="color: #000000; font-weight: bold;">li</span></a>></span></code></span> elements with help from our jQuery:</p>
<div class="geshifilter">
<pre class="html4strict geshifilter-html4strict" style="font-family:monospace;"><span style="color: #009900;"><section></span>
      <span style="color: #009900;"><<a href="http://december.com/html/4/element/h1.html"><span style="color: #000000; font-weight: bold;">h1</span></a>></span> This Is Our List <span style="color: #009900;"><<span style="color: #66cc66;">/</span><a href="http://december.com/html/4/element/h1.html"><span style="color: #000000; font-weight: bold;">h1</span></a>></span>
      <span style="color: #009900;"><<a href="http://december.com/html/4/element/ul.html"><span style="color: #000000; font-weight: bold;">ul</span></a> <span style="color: #000066;">class</span> <span style="color: #66cc66;">=</span> ”sortable”></span>
            <span style="color: #009900;"><<a href="http://december.com/html/4/element/li.html"><span style="color: #000000; font-weight: bold;">li</span></a> draggable<span style="color: #66cc66;">=</span>”true”></span> First Item <span style="color: #009900;"><<span style="color: #66cc66;">/</span><a href="http://december.com/html/4/element/li.html"><span style="color: #000000; font-weight: bold;">li</span></a>></span>
            <span style="color: #009900;"><<a href="http://december.com/html/4/element/li.html"><span style="color: #000000; font-weight: bold;">li</span></a> draggable<span style="color: #66cc66;">=</span>”true”></span> Second Item <span style="color: #009900;"><<span style="color: #66cc66;">/</span><a href="http://december.com/html/4/element/li.html"><span style="color: #000000; font-weight: bold;">li</span></a>></span>
            <span style="color: #009900;"><<a href="http://december.com/html/4/element/li.html"><span style="color: #000000; font-weight: bold;">li</span></a> draggable<span style="color: #66cc66;">=</span>”true”></span> Third Item <span style="color: #009900;"><<span style="color: #66cc66;">/</span><a href="http://december.com/html/4/element/li.html"><span style="color: #000000; font-weight: bold;">li</span></a>></span>
            <span style="color: #009900;"><<a href="http://december.com/html/4/element/li.html"><span style="color: #000000; font-weight: bold;">li</span></a> draggable<span style="color: #66cc66;">=</span>”true”></span> Fourth Item <span style="color: #009900;"><<span style="color: #66cc66;">/</span><a href="http://december.com/html/4/element/li.html"><span style="color: #000000; font-weight: bold;">li</span></a>></span>
            <span style="color: #009900;"><<a href="http://december.com/html/4/element/li.html"><span style="color: #000000; font-weight: bold;">li</span></a> draggable<span style="color: #66cc66;">=</span>”true”></span> Fifth Item <span style="color: #009900;"><<span style="color: #66cc66;">/</span><a href="http://december.com/html/4/element/li.html"><span style="color: #000000; font-weight: bold;">li</span></a>></span>
            <span style="color: #009900;"><<a href="http://december.com/html/4/element/li.html"><span style="color: #000000; font-weight: bold;">li</span></a> draggable<span style="color: #66cc66;">=</span>”true”></span> Sixth Item <span style="color: #009900;"><<span style="color: #66cc66;">/</span><a href="http://december.com/html/4/element/li.html"><span style="color: #000000; font-weight: bold;">li</span></a>></span>
      <span style="color: #009900;"><<span style="color: #66cc66;">/</span><a href="http://december.com/html/4/element/ul.html"><span style="color: #000000; font-weight: bold;">ul</span></a>></span>
<span style="color: #009900;"><<span style="color: #66cc66;">/</span>section></span></pre></div>
<p>Our nifty little list is nothing more than a plain ole unordered list, so let’s add the magic that will make it sortable!<br />
Notice we added the class “sortable” to our <span class="geshifilter"><code class="html4strict geshifilter-html4strict"><span style="color: #009900;"><<a href="http://december.com/html/4/element/ul.html"><span style="color: #000000; font-weight: bold;">ul</span></a>></span></code></span> element, this is what we use to identify it to the jQuery script: </p>
<div class="geshifilter">
<pre class="html4strict geshifilter-html4strict" style="font-family:monospace;"><span style="color: #009900;"><<a href="http://december.com/html/4/element/script.html"><span style="color: #000000; font-weight: bold;">script</span></a> <span style="color: #000066;">type</span><span style="color: #66cc66;">=</span>”<span style="color: #000066;">text</span><span style="color: #66cc66;">/</span>javascript”></span>
      $(function() {
            $(‘.sortable’).sortable();
      });
<span style="color: #009900;"><<span style="color: #66cc66;">/</span><a href="http://december.com/html/4/element/script.html"><span style="color: #000000; font-weight: bold;">script</span></a>></span></pre></div>
<p>Give it a try! It will now let you drag and drop any of the <span class="geshifilter"><code class="html4strict geshifilter-html4strict"><span style="color: #009900;"><<a href="http://december.com/html/4/element/li.html"><span style="color: #000000; font-weight: bold;">li</span></a>></span></code></span> elements in our list. But wait… there’s one problem! How do we do anything once they’ve sorted the list?<br />
Let’s add a <span class="geshifilter"><code class="html4strict geshifilter-html4strict">bind()</code></span> to our <span class="geshifilter"><code class="html4strict geshifilter-html4strict">sortable()</code></span> function. This way we can detect when a change occurs and act accordingly:</p>
<div class="geshifilter">
<pre class="html4strict geshifilter-html4strict" style="font-family:monospace;"><span style="color: #009900;"><<a href="http://december.com/html/4/element/script.html"><span style="color: #000000; font-weight: bold;">script</span></a> <span style="color: #000066;">type</span><span style="color: #66cc66;">=</span>”<span style="color: #000066;">text</span><span style="color: #66cc66;">/</span>javascript”></span>
      $(function() {
            $(‘.sortable’).sortable().bind(‘sortupdate’, function() {
                  alert(‘the list has been reordered!’);
                  // Do other stuff here to store the order, display a message, anything
            });
      });
<span style="color: #009900;"><<span style="color: #66cc66;">/</span><a href="http://december.com/html/4/element/script.html"><span style="color: #000000; font-weight: bold;">script</span></a>></span></pre></div>
<p>Now we know how to create the sortable list and how to add an action to it. Keep an eye out for future blogs! Who knows, maybe we’ll turn this into a full-scale interactive application!</p>

