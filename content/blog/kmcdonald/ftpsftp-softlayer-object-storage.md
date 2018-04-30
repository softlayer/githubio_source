---
title: "FTP/SFTP for SoftLayer Object Storage"
description: "<p>Getting started with SoftLayer Object Storage can be a bit daunting. At it's core object storage is an API-driven pro"
date: "2013-02-18"
author: "kmcdonald"
tags:
    - "blog"
---

<p>Getting started with SoftLayer Object Storage can be a bit daunting. At it's core object storage is an API-driven product, which means integrating it into your solution involves writing code. To remedy that we've spent time finding some of the most popular tools that help you interact with SoftLayer Object Storage. Because SoftLayer Object Storage is powered by OpenStack Swift, it benefits from the tools that the OpenStack community produces such as <a href="https://github.com/Memset/pycloudfuse">PyCloudFuse</a>, <a href="http://code.google.com/p/s3ql/">S3QL</a>, <a href="http://www.cloudberrylab.com/openstack-tools.aspx">CloudBerry</a>, and <a href="http://cyberduck.ch/">Cyberduck</a>. But we wanted to make it even easier to use. Instead of having to use special software, we wanted to offer support for existing, standard applications that almost everyone uses today.</p>
<h4>Introducing <a href="https://github.com/softlayer/swftp">SwFTP - an FTP and SFTP interface for Openstack Object Storage</a></h4>
<p>We decided to create an FTP and SFTP server that translates the FTP/SFTP protocols into OpenStack Swift commands so you can use most SFTP or FTP clients to interact with Object Storage. While this is intended to be used with SoftLayer Object Storage, SwFTP should be compatible with most OpenStack Swift deployments.</p>
<p>SwFTP was built using <a href="http://python.org">Python</a>, <a href="http://twistedmatrix.com/">Twisted's</a> powerful evented framework and <a href="http://twistedmatrix.com/trac/wiki/TwistedConch">twisted-conch</a> which is an SSH implementation for Twisted. Testing has been done with Filezilla, Cyberduck, Transmit and Flow. This code is open source under the MIT License and is avaialble on <a href="https://github.com/softlayer/swftp">github</a>.</p>
<h4>Getting Started with the SFTP Server</h4>
<p>Getting the server up-and-going should be easy. I'm going to go through the commands to do this on Ubuntu. Some modifications may need to be made for other operating systems.</p>
<p><strong>Install pip and install swftp with pip</strong></p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">$ apt-get install pip
$ pip install swftp</pre></div>
<p><strong>Generate a public/private SSH key pair</strong></p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">$ mkdir /etc/swift
$ ssh-keygen -h -b 2048 -N "" -t rsa -f /etc/swift/id_rsa</pre></div>
<p><strong>Start the Server</strong></p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">$ twistd --nodaemon swftp-sftp -a http://dal05.objectstorage.softlayer.net/auth/v1.0</pre></div>
<p>By default, the SFTP server listens on port 5022 (configurable: see <code>twistd swftp-sftp --help</code> for more info). Now, you should be able to configure most SFTP clients to use this port and your SoftLayer Object Storage credentials.</p>
<p>To view all of the options available, you can use the <span class="geshifilter"><code class="text geshifilter-text">--help</code></span> option. Here's what that looks like:</p>
<p><strong>SFTP Command-line options</strong></p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">$ twistd swftp-sftp --help
Usage: twistd [options] swftp-sftp [options]
Options:
  -c, --config_file=  Location of the swftp config file. [default:
                      /etc/swift/swftp.conf]
  -a, --auth_url=     Auth Url to use. Defaults to the config file value if it
                      exists.[default: http://127.0.0.1:8080/auth/v1.0]
  -p, --port=         Port to bind to.
  -h, --host=         IP to bind to.
      --priv_key=     Private Key Location.
      --pub_key=      Public Key Location.
      --version       Display Twisted version and exit.
      --help          Display this help and exit.</pre></div>
<p><strong>FTP Command-line options</strong></p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">$ twistd swftp-ftp --help
Usage: twistd [options] swftp-ftp [options]
Options:
  -c, --config_file=  Location of the swftp config file. [default:
                      /etc/swift/swftp.conf]
  -a, --auth_url=     Auth Url to use. Defaults to the config file value if it
                      exists. [default: http://127.0.0.1:8080/auth/v1.0]
  -p, --port=         Port to bind to.
  -h, --host=         IP to bind to.
      --version       Display Twisted version and exit.
      --help          Display this help and exit.</pre></div>
<h3>Twistd Command-line Options</h3>
<p>In addition to the swftp-specific options, twistd adds some additional. Below are some of the most common options. To see all of them use <span class="geshifilter"><code class="text geshifilter-text">twistd --help</code></span>.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">$ twistd --help
Usage: twistd [options]
Options:
  -n, --nodaemon       don't daemonize, don't use default umask of 0077
      --syslog         Log to syslog, not to file
  -l, --logfile=       log to a specified file, - for stdout
      --pidfile=       Name of the pidfile [default: twistd.pid]
  -u, --uid=           The uid to run as.
  -g, --gid=           The gid to run as.</pre></div>
<h3>Config File</h3>
<p>Along with the command-line options, you can also configure SwFTP with a config file. The default location for the config file is <span class="geshifilter"><code class="text geshifilter-text">/etc/swift/swftp.conf</code></span>.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">[sftp]
auth_url = http://127.0.0.1:8080/auth/v1.0
host = 0.0.0.0
port = 5022
priv_key = /etc/swift/id_rsa
pub_key = /etc/swift/id_rsa.pub
num_persistent_connections = 4
connection_timeout = 240
&nbsp;
[ftp]
auth_url = http://127.0.0.1:8080/auth/v1.0
host = 0.0.0.0
port = 5021
num_persistent_connections = 4
connection_timeout = 240
welcome_message = Welcome to SwFTP - An FTP/SFTP interface for Openstack Swift</pre></div>
<h3>Caveats</h3>
<p>There are a few things you should know before using this SwFTP.</p>
<ul>
<li>You can only make directories on the top level. This is because the top level is for containers.</li>
<li>You cannot rename any non-empty directory. Most clients will explicitly delete each file/directory recursively anyway so this shouldn't be an issue.</li>
<li>Having fake directories and real objects of the same name will result in only being able view the directory. A lot of clients actually explode <a href="http://i.imgur.com/mvo0z.jpeg">supernova style</a> if a directory listing has duplicates.</li>
</ul>
<p>I encourage you to give it a try. If you run into any issues or have any questions, please open an issue on <a href="https://github.com/softlayer/swftp/issues">github</a>.</p>

