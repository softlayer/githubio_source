---
title: "Caching Made Easy Part 2: Pass The Stack"
description: "<p><a href=http://sldn.softlayer.com/blog/klandreth/Caching-Made-Easy-Part-I-or-How-I-learned-stop-worrying-and-love-me"
date: "2012-04-16"
author: "klandreth"
tags:
    - "blog"
---

<p><a href="http://sldn.softlayer.com/blog/klandreth/Caching-Made-Easy-Part-I-or-How-I-learned-stop-worrying-and-love-memcached">Part I</a> of our Memcached Series explored the concept of using memcached to cache entire pages. In Part II we further increase the responsiveness of your application by finding and removing unnecessary steps. By caching in memcached we are already bypassing an unholy amount of database queries and <span class="geshifilter"><code class="text geshifilter-text">foreach()</code></span> loops, not to mention all the unnecessary application logic to decide if a user can view the page or not. If we skip the application stack for anonymous page requests, we can additionally bypass the fastcgi handoff, forking of fastcgi processes, the bootstrap of your application, and the initial database connection (if not part of bootstrapping).</p>
<p>For this, we push <a href="http://nginx.org">nginx</a> to the foreground to front-end the PHP/apache2 stack!  There are memcached modules for apache2 but they work more in the fashion of a reverse proxy which differs from the warm-cache, only serving setup we covered in part one.  To provide our webservers with the comfort and support they deserve, we use <a href="http://wiki.nginx.org/HttpMemcachedModule">nginx memcached module</a> and the prefix/keyspace you designed before.</p>
<p>Below we configure a basic nginx catchall server which forwards requests back to apache for you.  This is essentially a <a href="http://tumblr.intranation.com/post/766288369/using-nginx-reverse-proxy">reverse-proxy without request caching</a>.  The plus side to this method is that there is only one configuration for all of your application stacks since you are using a safe keyname scheme and <span class="geshifilter"><code class="text geshifilter-text">$host</code></span> is passed back to the apache stack.</p>
<p>Our sample nginx configuration with inline comments:</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;">server <span style="color: black;">&#123;</span>
   listen   <span style="color: black;">&#91;</span>::<span style="color: black;">&#93;</span>:<span style="color: #ff4500;">80</span><span style="color: #66cc66;">;</span>
   access_log off<span style="color: #66cc66;">;</span>
   error_log  /dev/null crit<span style="color: #66cc66;">;</span>
   server_name yourwebasset.<span style="color: black;">com</span><span style="color: #66cc66;">;</span>
&nbsp;
   <span style="color: #808080; font-style: italic;"># only needed if serving static content</span>
   root /var/www/htdocs<span style="color: #66cc66;">;</span>
&nbsp;
   location / <span style="color: black;">&#123;</span>
      <span style="color: #808080; font-style: italic;"># Go ahead and serve static content.</span>
      <span style="color: #808080; font-style: italic;"># If you don't want to serve static content,</span>
      <span style="color: #808080; font-style: italic;"># then change location @fastpath to /</span>
      <span style="color: #808080; font-style: italic;"># and remove this location declaration.</span>
      try_files $uri <span style="color: #66cc66;">@</span>fastpath<span style="color: #66cc66;">;</span>
   <span style="color: black;">&#125;</span>
&nbsp;
   <span style="color: #808080; font-style: italic;">#Magic lies within</span>
   location <span style="color: #66cc66;">@</span>fastpath <span style="color: black;">&#123;</span>
&nbsp;
      <span style="color: #808080; font-style: italic;"># If memcached can't find an entry, it returns a 404.</span>
      <span style="color: #808080; font-style: italic;"># We intercept 404 pages and pass them along to</span>
      <span style="color: #808080; font-style: italic;"># our predefined location.  The location has access</span>
      <span style="color: #808080; font-style: italic;"># to all the same variables as before and doesn't know</span>
      <span style="color: #808080; font-style: italic;"># that a prior 404 was generated other than our debug</span>
      <span style="color: #808080; font-style: italic;"># variable.</span>
      error_page <span style="color: #ff4500;">404</span> <span style="color: #66cc66;">=</span> <span style="color: #66cc66;">@</span>appstack<span style="color: #66cc66;">;</span>
&nbsp;
      <span style="color: #808080; font-style: italic;"># I like to use these for debugging. This is the default</span>
      <span style="color: #808080; font-style: italic;"># reason for passing on to @appstack.  Variables are</span>
      <span style="color: #808080; font-style: italic;"># preserved through location passing</span>
      <span style="color: #008000;">set</span> $reason <span style="color: #483d8b;">"MISS"</span><span style="color: #66cc66;">;</span>
&nbsp;
      <span style="color: #808080; font-style: italic;"># This is only passed on to the client if we actually get a hit,</span>
      <span style="color: #808080; font-style: italic;"># otherwise the add_header is thrown away when we</span>
      <span style="color: #808080; font-style: italic;"># pass processing onto @appstack</span>
      <span style="color: #808080; font-style: italic;"># Remember the far future cache control headers from Part I?</span>
      add_header X-Cache-debug <span style="color: #483d8b;">"HIT"</span><span style="color: #66cc66;">;</span>
      add_header Expires <span style="color: #483d8b;">"Tue, 1 Jun 1979 12:01:00 GMT"</span><span style="color: #66cc66;">;</span>
      add_header Cache-Control <span style="color: #483d8b;">"must-revalidate, post-check=0, pre-check=0"</span><span style="color: #66cc66;">;</span>
&nbsp;
      <span style="color: #808080; font-style: italic;"># Check to see if someone passed in ?nocache=1</span>
      <span style="color: #808080; font-style: italic;"># This is not required</span>
      <span style="color: #808080; font-style: italic;"># but good for testing your app</span>
      <span style="color: #ff7700;font-weight:bold;">if</span> <span style="color: black;">&#40;</span> $args <span style="color: #66cc66;">~</span>* <span style="color: #483d8b;">"nocache=1"</span> <span style="color: black;">&#41;</span> <span style="color: black;">&#123;</span>
          <span style="color: #008000;">set</span> $reason <span style="color: #483d8b;">"nocache override"</span><span style="color: #66cc66;">;</span>
          <span style="color: #ff7700;font-weight:bold;">return</span> <span style="color: #ff4500;">404</span><span style="color: #66cc66;">;</span>
      <span style="color: black;">&#125;</span>
&nbsp;
      <span style="color: #808080; font-style: italic;"># Only GET/HEAD requests are safe</span>
      <span style="color: #ff7700;font-weight:bold;">if</span> <span style="color: black;">&#40;</span> $request_method <span style="color: #66cc66;">!~</span> ^<span style="color: black;">&#40;</span>GET|HEAD<span style="color: black;">&#41;</span>$<span style="color: black;">&#41;</span> <span style="color: black;">&#123;</span>
          <span style="color: #008000;">set</span> $reason <span style="color: #483d8b;">"method not safe"</span><span style="color: #66cc66;">;</span>
          <span style="color: #ff7700;font-weight:bold;">return</span> <span style="color: #ff4500;">404</span><span style="color: #66cc66;">;</span>
      <span style="color: black;">&#125;</span>
&nbsp;
      <span style="color: #808080; font-style: italic;"># From Part I we set a unique authentication</span>
      <span style="color: #808080; font-style: italic;"># token in the cookies. Here we check and see if</span>
      <span style="color: #808080; font-style: italic;"># this token is set and, if so, skip memcache for</span>
      <span style="color: #808080; font-style: italic;"># authenticated users.</span>
      <span style="color: #ff7700;font-weight:bold;">if</span> <span style="color: black;">&#40;</span> $http_cookie <span style="color: #66cc66;">~</span>* <span style="color: #483d8b;">"AUTH_UID"</span> <span style="color: black;">&#41;</span> <span style="color: black;">&#123;</span>
          <span style="color: #008000;">set</span> $reason <span style="color: #483d8b;">"authenticated"</span><span style="color: #66cc66;">;</span>
          <span style="color: #ff7700;font-weight:bold;">return</span> <span style="color: #ff4500;">404</span><span style="color: #66cc66;">;</span>
      <span style="color: black;">&#125;</span>
&nbsp;
      <span style="color: #808080; font-style: italic;"># If you want to cache URL arguments, use $request_uri below</span>
      <span style="color: #808080; font-style: italic;"># otherwise, use $uri. Using $request_uri will result in more</span>
      <span style="color: #808080; font-style: italic;"># cache misses, but caches potentially more complex pages. </span>
      <span style="color: #808080; font-style: italic;"># Arguments are preserved in the key</span>
      <span style="color: #808080; font-style: italic;"># Uncomment this conditional when using $uri</span>
      <span style="color: #808080; font-style: italic;">#if ( $args ) { </span>
      <span style="color: #808080; font-style: italic;">#   set $reason "arguments";</span>
      <span style="color: #808080; font-style: italic;">#    return 404;</span>
      <span style="color: #808080; font-style: italic;">#}</span>
      <span style="color: #008000;">set</span> $memcached_key prefix-$scheme://$host$uri<span style="color: #66cc66;">;</span>
      memcached_pass 127.0.0.1:<span style="color: #ff4500;">11211</span><span style="color: #66cc66;">;</span>
&nbsp;
      <span style="color: #808080; font-style: italic;"># Since we can't store any complex data, we blindly return the value.</span>
      <span style="color: #808080; font-style: italic;"># Make sure you don't gzip any data that you store in memcached.</span>
      <span style="color: #808080; font-style: italic;"># Memcached also already fastlz's anything you store in there.</span>
      default_type text/html<span style="color: #66cc66;">;</span>
      charset utf-<span style="color: #ff4500;">8</span><span style="color: #66cc66;">;</span>
   <span style="color: black;">&#125;</span>
&nbsp;
&nbsp;
   location <span style="color: #66cc66;">~</span> \\.<span style="color: black;">php</span>$ <span style="color: black;">&#123;</span>
      <span style="color: #808080; font-style: italic;"># protect your php files (or any files)</span>
      error_page <span style="color: #ff4500;">592</span> <span style="color: #66cc66;">=</span> <span style="color: #66cc66;">@</span>appstack<span style="color: #66cc66;">;</span>
      <span style="color: #ff7700;font-weight:bold;">return</span> <span style="color: #ff4500;">592</span><span style="color: #66cc66;">;</span>
   <span style="color: black;">&#125;</span>
&nbsp;
   <span style="color: #808080; font-style: italic;"># if you are using fastcgi, you can use that </span>
   <span style="color: #808080; font-style: italic;"># here instead of the proxy_pass items</span>
   location <span style="color: #66cc66;">@</span>appstack <span style="color: black;">&#123;</span>
&nbsp;
      proxy_pass  http://127.0.0.1:<span style="color: #ff4500;">8080</span><span style="color: #66cc66;">;</span>
      proxy_redirect off<span style="color: #66cc66;">;</span>
      proxy_set_header   Host             $host<span style="color: #66cc66;">;</span>
      proxy_set_header   X-Real-IP        $remote_addr<span style="color: #66cc66;">;</span>
      proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for<span style="color: #66cc66;">;</span>
      proxy_max_temp_file_size <span style="color: #ff4500;">0</span><span style="color: #66cc66;">;</span>
&nbsp;
      client_max_body_size       10m<span style="color: #66cc66;">;</span>
      client_body_buffer_size    128k<span style="color: #66cc66;">;</span>
      proxy_connect_timeout      <span style="color: #ff4500;">90</span><span style="color: #66cc66;">;</span>
      proxy_send_timeout         <span style="color: #ff4500;">90</span><span style="color: #66cc66;">;</span>
      proxy_read_timeout         <span style="color: #ff4500;">90</span><span style="color: #66cc66;">;</span>
&nbsp;
      proxy_buffer_size          4k<span style="color: #66cc66;">;</span>
      proxy_buffers              <span style="color: #ff4500;">4</span> 32k<span style="color: #66cc66;">;</span>
      proxy_busy_buffers_size    64k<span style="color: #66cc66;">;</span>
      proxy_temp_file_write_size 64k<span style="color: #66cc66;">;</span>
&nbsp;
      add_header X-Cache-debug $reason<span style="color: #66cc66;">;</span>
   <span style="color: black;">&#125;</span>
<span style="color: black;">&#125;</span></pre></div>
<p>If you aren't already using nginx+fastcgi, you'll need to configure your application to correctly use the <span class="geshifilter"><code class="text geshifilter-text">X-Forwared-For</code></span> header and <span class="geshifilter"><code class="text geshifilter-text">X-Real-IP</code></span> headers instead of the standard IP detection. This is because proxying requests are passing from the client back to apache which causes connections to originate from <span class="geshifilter"><code class="text geshifilter-text">127.0.0.1</code></span>.  While undesirable, this can easily be corrected by considering the right headers.</p>
<p> To recap, in this series (<a href="http://sldn.softlayer.com/blog/klandreth/Caching-Made-Easy-Part-I-or-How-I-learned-stop-worrying-and-love-memcached">Part I</a> and Part II) we have gone over how to cache anonymous pages with memcache and nginx. This paradigm is best implemented when the majority of site traffic is comprised of anonymous users with ads or other personalized content served via AJAX.  Sites with a majority of traffic being authenticated users can still employ many of these concepts but require more detailed logic on when to serve a cached page, or which page elements to AJAX and so on. </p>
<p>Keep a look out for more entries like this from myself and other SoftLayer developers in the coming months.  Want to see something specific?  Leave a comment below as to what you’d like to see from a SoftLayer developer’s perspective and we’ll do our best to deliver!</p>

