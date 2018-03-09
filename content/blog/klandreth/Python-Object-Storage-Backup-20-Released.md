---
title: "Python Object Storage Backup 2.0 Released"
description: "<p>Under the cover of darkness we’ve been hard at working making more goodies for you.  We’re excited to release <a href"
date: "2013-02-06"
author: "klandreth"
tags:
    - "blog"
---

<p>Under the cover of darkness we’ve been hard at working making more goodies for you.  We’re excited to release <a href="https://github.com/softlayer/softlayer-object-storage-backup">Object Storage Backup Script 2.0</a> which is now available on <a href="http://pypi.python.org/pypi/slbackup">pypi</a>!  That’s right, not only is it up to version 2.0 full of bug fixes and enhancements, but you can now install it via pip which is <em>highly recommended</em>.</p>
<h3>To install the backup script, run the following command (as root or sudo):</h3>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">pip install slbackup</pre></div>
<h3>To upgrade, run the following command (as root or sudo):</h3>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">pip install slbackup --upgrade</pre></div>
<p>If you don’t have pip, you can find it available as these package names for your distro</p>
<ul>
<li>CentOS <a href="http://superuser.com/questions/407926/why-is-pip-not-listed-in-easy-install-on-centos-6-where-to-get-it">instructions</a>. If you are using <a href="http://fedoraproject.org/wiki/EPEL">EPEL</a>, it’s <span class="geshifilter"><code class="text geshifilter-text">yum install python-pip</code></span></li>
<li>Debian is in apt-get install python-pip</li>
<li>FreeBSD is in <a href="http://johnrlive.com/how-to-install-python-on-freebsd/">py27-pip</a></li>
</ul>
<p>What’s new in v2.0<br />
<a href="https://github.com/softlayer/softlayer-object-storage-backup/pull/10">New and improved threading</a><br />
<a href="https://github.com/softlayer/softlayer-object-storage-backup/commit/02f5914c8b4e5afb93400972a7843753fd2b70ba">Added support for additional auth urls (great for private clusters!)</a><br />
<a href="https://github.com/softlayer/softlayer-object-storage-backup/commit/699ecfe6e9bbc40df081bd0023c8a85d3a552d16">Config file testing with --test options</a><br />
<a href="https://github.com/softlayer/softlayer-object-storage-backup/issues/15">Proper exit codes</a><br />
<a href="https://github.com/softlayer/softlayer-object-storage-backup/issues/11">Better granularity of retention days</a><br />
<a href="https://github.com/softlayer/softlayer-object-storage-backup/issues/1">Added prefix support</a><br />
<a href="https://github.com/softlayer/softlayer-object-storage-backup/issues?page=1&sort=created&state=closed">and various bugs</a></p>
<p>Many of these new features and bug fixed were requested or reported by users of the script.  So please, come on by over to the <a href="https://github.com/softlayer/softlayer-object-storage-backup/issues">github page</a> and report any issues you’ve had, especially with the new version. We love to see feedback from our users so that we can make even better improvements to the Object Storage Backup script in our next release.</p>
<p>-Kevin</p>

