---
title: "Using CURL to access CloudLayer Storage"
description: "<p><a href=http://www.softlayer.com/cloudlayer_storage.html>CloudLayer Storage</a> is billed as providing anytime, an"
date: "2009-07-10"
author: "nday"
tags:
    - "blog"
---

<p><a href="http://www.softlayer.com/cloudlayer_storage.html">CloudLayer Storage</a> is billed as providing "anytime, anywhere access to your data".  This isn’t just referring to human interfaces, but also includes automated interfaces.</p>
<p>One easy way to automate access to CloudLayer Storage is through <a href="http://curl.haxx.se/">curl</a>.  Curl is available as a command-line tool in most every operating system and is typically used for transferring files.  In this post I’ll show some examples on how to use curl to add, get, delete, or otherwise manipulate files in CloudLayer Storage.  Note that this isn’t using the SoftLayer API, but instead interfaces directly with CloudLayer Storage.</p>
<p>Upload a file named "DSC1012.jpg" to an account owned by username "user@example.com" with a password of "PaSsWoRd":</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;"># curl –F filename=@DSC1012.jpg –u user@example.com:PaSsWoRd \\
https://storage.cloudlayer.com/v1/files/</pre></div>
<p>The command will return some XML tags.  The items of interest are "FileID" and "lockID".  These values are important for future operations on the file.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">&lt;fileID&gt;102C9C28-65C3-11DE-1234-2BE68BA216C2&lt;/fileID&gt;
&lt;lockID&gt;6CDCEEB2-6B38-11DE-A510-123F439A2728&lt;/lockID&gt;
&lt;lockDuration&gt;120&lt;/lockDuration&gt;</pre></div>
<p>The lock is to protect a file form reading or being manipulated during the upload process.  The lock will expire in "lockDuration" seconds or the user can disable the lock manually.</p>
<p>Here is how to disable the lock using the lockID  and the fileID generated from the upload operation:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;"># curl –d \\
   'action=unlock&lockid=6CDCEEB2-6B38-11DE-A510-123F439A2728' \\
   –u user@example.com:PaSsWoRd \\
   https://storage.cloudlayer.com/v1/files/102C9C28-65C3-11DE-1234-2BE68BA216C2/lock</pre></div>
<p>If you ever lose track of the FileID, you can use this command to retrieve a listing of the files and containers (directories) in an account along with the FileIDs which are listed as an "oid" XML tag.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;"># curl –u user@example.com:PaSsWoRd \\
https://storage.cloudlayer.com/v1/files/list</pre></div>
<p>To get the list of files in a container, just append the container oid to the URL.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;"># curl –u user@example.com:PaSsWoRd \\
https://storage.cloudlayer.com/v1/files/list?oid=37D0F2AC-08FC-11DE-1234-3FA3A91CD1B4</pre></div>
<p>To retrieve the file from CloudLayer Storage, use the FileID to retrieve it.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;"># curl  -u user@example.com:PaSsWoRd \\
<a href="https://storage.cloudlayer.com/v1/files/37D0F2AC-08FC-11DE-1234-3FA3A91CD1B4/" title="https://storage.cloudlayer.com/v1/files/37D0F2AC-08FC-11DE-1234-3FA3A91CD1B4/">https://storage.cloudlayer.com/v1/files/37D0F2AC-08FC-11DE-1234-3FA3A91C...</a> -o outputfilename</pre></div>
<p>Alternatively, you could use "<a href="http://www.gnu.org/software/wget/">wget</a>" to retrieve the file</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;"># wget –http-user=user@example.com -–http-password=PaSsWoRd  \\
<a href="https://storage.cloudlayer.com/v1/files/37D0F2AC-08FC-11DE-1234-3FA3A91CD1B4/" title="https://storage.cloudlayer.com/v1/files/37D0F2AC-08FC-11DE-1234-3FA3A91CD1B4/">https://storage.cloudlayer.com/v1/files/37D0F2AC-08FC-11DE-1234-3FA3A91C...</a> -O outputfilename</pre></div>
<p>To delete a file just add the POST form variable "action" with the value "delete".</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;"># curl –d 'action=delete' –u user@example.com:PaSsWoRd \\
https://storage.cloudlayer.com/v1/files/37D0F2AC-08FC-11DE-1234-3FA3A91CD1B4/</pre></div>
<p>Each of the commands listed above return data in XML format.  If you would prefer json format, add a query parameter "output=json" to the query string.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;"># curl –u user@example.com:PaSsWoRd \\
https://storage.cloudlayer.com/v1/files/list?output=json</pre></div>
<p>In order to create a public URL for a file, just send a POST variable of "action=create" to the "token" endpoint.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;"># curl -d 'action=create' -u user@example.com:PaSsWoRd \\
https://storage.cloudlayer.com/v1/files/37D0F2AC-08FC-11DE-1234-3FA3A91CD1B4/token/</pre></div>
<p>The long string "37D0F2..." is the oid (a.k.a FileID) of the file that you can get from the XML returned when the file was uploaded, or retrived using the file listing example above.</p>
<p>In the XML (or JSON) data that is returned, there will be a "token".</p>
<p><span class="geshifilter"><code class="text geshifilter-text">&lt;token&gt;B2891F7B054EF2DF764801E1CFF0079057291234&lt;/token&gt;</code></span></p>
<p>That token can be combined with the oid to create a URL that anyone can use to retrieve the file.</p>
<p>The URL looks like this:<br />
https://storage.cloudlayer.com/v1/public/{oid}/{token}</p>
<p>In our example it would be:<br />
<a href="https://storage.cloudlayer.com/v1/public/37D0F2AC-08FC-11DE-1234-3FA3A91CD1B4/B2891F7B054EF2DF764801E1CFF0079057291234" title="https://storage.cloudlayer.com/v1/public/37D0F2AC-08FC-11DE-1234-3FA3A91CD1B4/B2891F7B054EF2DF764801E1CFF0079057291234">https://storage.cloudlayer.com/v1/public/37D0F2AC-08FC-11DE-1234-3FA3A91...</a></p>
<p>If you are accessing CloudLayer Storage from inside a SoftLayer datacenter, you can access the storage over the SoftLayer private network (no bandwidth fees!).  Just use "scs.service.softlayer.com" instead of "storage.cloudlayer.com". </p>
<p>You can use the information above in conjunction with the curl libraries in <a href="http://www.php.net/curl">PHP</a>, <a href="http://curlpp.org/">C++</a>, or one of many other programming languages with <a href="http://curl.haxx.se/libcurl/bindings.html">curl bindings</a>.</p>

