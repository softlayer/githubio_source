---
title: "Caching Made Easy Part I or: How I learned to stop worrying and love the memcached"
description: "<p>Congratulations!  Your website just made the front page on [awesome social media site here]. And while the business f"
date: "2012-03-31"
author: "klandreth"
tags:
    - "blog"
---

<p>Congratulations!  Your website just made the front page on [awesome social media site here]. And while the business folks begin their joy-leap whose height will only be matched by the record in revenues, the server admins brace for impact as their apache/mod_php stack begins to strain under the weight of dynamically generated content. </p>
<p>The typical traffic seems abysmal in comparison to the wave of new <strong>anonymous users</strong> surging to your site. To compound the complexity site updates are instantaneous and have little or no user lag time.</p>
<p>There is more than one way to speed up your site: caching query objects, remote variables, using static memory<br />
While all of these are perfectly valid they all require complicated invalidate logic and usually some refactoring of your applications code base - both of which our current situation's time constraints do not allow for. The easiest way to speed up your site is to cache rendered pages and serve the cached page.</p>
<h2>The rules</h2>
<p>The concept of <em>anonymous users</em> defines the keystone of our caching system.  Logged in users typically will have a different set of permissions, content and experience in mind so we'll just say, for now, that all of our caching work will be related to anonymous users. But before we get into actually caching the content, we need to setup some ground rules to make caching work in our favor.  After the rules, then we'll work through the process of caching.</p>
<ol>
<li>Use a single site entry point </li>
<li>Store an authentication marker in the session cookie </li>
<li>Decide on a simple pre-shared key (4-8 characters) </li>
<li>Set the appropriate headers to prevent client caching</li>
</ol>
<h3>Using a single site entry point</h3>
<p><strong>This very important to fast caching so don't skip this section!</strong></p>
<p>If your site is available via multiple web assets such as typo domains, www or other prefixes you will need to pick one asset to funnel all your traffic into.  I'd suggest using the <a href="http://no-www.org/">base domain</a> as the primary web asset.  All other assets should gracefully redirect to the primary asset using the <a href="http://httpd.apache.org/docs/2.3/rewrite/remapping.html#canonicalhost">webserver as the redirector</a>. Doing this will make sure that cache keys are generated using uniform URLs.</p>
<h3>Store an authentication marker in the session cookie</h3>
<p>The only way to tell if a user is logged in without hitting the database is to set a marker in the cookie letting your web application know if the user is logged in or not.  Doing this will allow us or other tiers in your application attempt to serve a cached page prior to even opening up the database connection. There little security risk in doing this other than possibly exposing the UID's of your logged in users. </p>
<h3> Decide on a simple pre-shared key</h3>
<p>A pre-shared key is just a marker to prevent any collisions in your memcached instance.  For example, you might want to pick <em>anon_cache</em> as your pre-shared key or <em>pages</em> but not <em>cache</em> as it is too ominous.   In part 2 I'll cover how to take advantage of this  pre-shared key to serve your cache directly from the webserver instead of the application for a massive speed up!</p>
<h3>Headers</h3>
<ol>
<li> Set the <span class="geshifilter"><code class="text geshifilter-text">Expires</code></span> header to something far far <strong>in the past</strong>.  This can be your birthday (not suggested), the year your favorite cult classic came out (better), or your favorite historical event (best). </li>
<li>Set it to force clients to hit your website. <span class="geshifilter"><code class="text geshifilter-text">Cache-Control: must-revalidate, post-check=0, pre-check=0</code></span>
<p>In my experience webpages themselves often vary between 5kB to 80kB in contrast to images which vary between 5K and 5MB (or more). For web pages serving <a href="http://www.kegel.com/c10k.html">10,000</a> 80K pages is easier to do for a webserver than 10,000 1MB images. For this, pages themselves use <span class="geshifilter"><code class="text geshifilter-text">Expires</code></span> headers in the past, and images use <span class="geshifilter"><code class="text geshifilter-text">Expires</code></span> headers in the future to encourage client side/proxy caching of images, and not your dynamic pages.</p>
</li>
</ol>
<h2>Caching logic</h2>
<p>With some very basic rules in place, we can work on the caching logic for your web application.  This method works well even when anonymous content is allowed on the site.</p>
<h3>The Request</h3>
<ol>
<li>Is this a GET/HEAD request?
<ul>
<li>Only process GET/HEAD requests via cache, everything else would invalidate the cache</li>
</ul>
</li>
<li>Does the user have a session?
<ul>
<li>If not, create one for the user</li>
</ul>
</li>
<li>Is the user logged in?
<ul>
<li>If we just created a new session, this will always be false</li>
<li>If they are, skip over the remaining steps</li>
</ul>
</li>
<li>Check for cache
<ul>
<li>Since the user is an anonymous user, check if there is page cache using the <span class="geshifilter"><code class="text geshifilter-text">$presharedkey-$base_url/request_uri()</code></span>.  For example: <span class="geshifilter"><code class="text geshifilter-text">PAGE-http://example.com/blog/1?page=2</code></span>
  </li>
<li>You could use just request_uri() but then it would require that it be only web asset using that memcached instance.</li>
<li>If a key exists with that name, serve the page immediately</li>
<li>If <strong>no</strong> key exists with that name, continue with normal processing</li>
</ul>
</li>
</ol>
<h3>Caching a page</h3>
<ol>
<li>Generate the page as normal, but don't return it just yet
<ul>
<li>This process must happen before the page is printed. Typically a template system will be in place to handle output.</li>
</ul>
</li>
<li>Store the page in memcached
<ul>
<li>Only do this for anonymous users!</li>
<li>Key length is important! Memcached can only <a href="http://code.google.com/p/memcached/issues/detail?id=10">store 250 characters</a> as the key.</li>
<li>Size is important. By default, memcached can only store 1MB into a single slab.  Use <span class="geshifilter"><code class="text geshifilter-text">-I</code></span> to override this or you will have a lot of set_miss/get_miss in your stats.  This will result in poor performance.</li>
<li>This process invalidates the cache regardless of wether it was a GET/POST request. There will be a small window where a bunch of requests stampede memcached with set requests.  You can use locking in memcached to curb this type of behavior.</li>
</ul>
</li>
<li>Serve the page to the user</li>
</ol>
<h2>Invalidating the cache</h2>
<p>You can have cron run though and invalidate cache entries based on their age, keyname, or just nuke everything and call it a day.  The proposed method above handles cache invalidation transparently as stale content is served during the processing of a PUT/POST request, and then updates to pages are re-generated and stored in memcached.</p>

