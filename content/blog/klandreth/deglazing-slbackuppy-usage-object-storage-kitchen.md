---
title: "Deglazing slbackup.py Usage In the Object Storage Kitchen"
description: "<p>Backups are dandy; especially when you delete everything by accident. But when <a href=http://sldn.softlayer.com/blo"
date: "2012-07-02"
author: "klandreth"
tags:
    - "blog"
---

<p>Backups are dandy; especially when you delete everything by accident. But when <a href="http://sldn.softlayer.com/blog/klandreth/Object-My-Backup-Storage">some joker writes a backup script</a> that you think will be helpful and doesn’t <a href="https://github.com/softlayer/softlayer-object-storage-backup/blob/master/README.md">document how to use it</a> properly, it’s probably more frustrating than figuring things out yourself.  We’ve been busy launching a <a href="http://blog.softlayer.com/2012/how-do-you-build-a-private-cloud/">private cloud offering</a> so this blog is much overdue.</p>
<p>Let’s take the very common use case of database backups.  And let’s do this up foodie style.</p>
<p><strong>1x</strong> backup user<br />
<strong>1x</strong> backup output directory<br />
<strong>1x</strong> copy of slbackup.py and it’s dependencies<br />
<strong>1x</strong> copy of a database backup script<br />
<strong>1x</strong> object storage account</p>
<p>First thing we do is take this assigned backup user and create a directory to mix everything up in; <span class="geshifilter"><code class="text geshifilter-text">mkdir ~/database-backups</code></span>.  Next we get slbackup.py setup by populating it’s config; <span class="geshifilter"><code class="text geshifilter-text">slbackup.py --example > ~/.slbackup</code></span>.  We open up ~/.slbackup with either vim, emacs, or whatever your favorite cli utensil is.  Once opened for editing, replace the words <span class="geshifilter"><code class="text geshifilter-text">MISSING</code></span> with the appropriate values (account details) and adjust any other parameters you see fit.  Add a dolup of semicolon at the beginning of a line to comment it out and slbackup.py will use the defaults.</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;"><span style="color: #66cc66;">;</span> bunch of stuff before this<span style="color: #66cc66;">,</span> skipped
<span style="color: black;">&#91;</span>slbackup<span style="color: black;">&#93;</span>
username <span style="color: #66cc66;">=</span> MISSING
datacenter <span style="color: #66cc66;">=</span> dal05
apikey <span style="color: #66cc66;">=</span> MISSING
checksum <span style="color: #66cc66;">=</span> <span style="color: #008000;">False</span>
internal <span style="color: #66cc66;">=</span> <span style="color: #008000;">False</span>
<span style="color: #66cc66;">;</span>threads <span style="color: #66cc66;">=</span> <span style="color: #ff4500;">2</span>
retention <span style="color: #66cc66;">=</span> <span style="color: #ff4500;">30</span></pre></div>
<p>Save and close the file.  Open another file called database-backup-script.sh, and put the following (please add your own personal touches here as cooking times may vary).  </p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">#!/bin/sh
database=$1
dow=$(date +%a)
mysqldump --opt $database | xz -3 - > ../../database-backups/${database}-${dow}.sql.xz</pre></div>
<p>This particular script backups up a specific database table using the day of the week (Mon, Tue, ..) as part of the filename, overwriting the file if it already exists. With the scripts configured, we need to mix everything up with cron.  Edit the user’s cron by using <span class="geshifilter"><code class="text geshifilter-text">crontab -e</code></span> (use <span class="geshifilter"><code class="text geshifilter-text">crontab -e -u backupuser</code></span> if logged in as root).   Choose an interval that’s good for your database work load, typically once a day.  </p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;"># backup an ecommerce database
15  1   *  *  *   ~/database-backup-script.sh ecommerce_site_1
# backup the database backup folder to object storage, 
# keeping old files for 8 days
20  2   *  *  *   slbackup.py -o dbbackups -s ~/database-backups -r 8</pre></div>
<p>This will place all of your database backups into the database-backups directory and then upload it to the object storage container <span class="geshifilter"><code class="text geshifilter-text">dbbackups</code></span>.  Any identically named files will be copied out of the way and will spoil after 8 days.  No worries however as the script will bin it automatically.</p>
<p>That’s it, enjoy sleeping at night as your databases are backed up and safe in your private container.  Well, at least that one ecommerce site is for now.</p>
<p>-Kevin</p>

