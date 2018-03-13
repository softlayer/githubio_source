---
title: "New DevOps tools for SoftLayer"
description: "<p>Today, I am happy to announce two new tools to help interact with SoftLayer environment: a <a href=https://github.co"
date: "2013-05-30"
author: "klandreth"
tags:
    - "blog"
---

<p>Today, I am happy to announce two new tools to help interact with SoftLayer environment: a <a href="https://github.com/softlayer/softlayer-api-python-client">command line tool</a> written with our python client and <a href="https://github.com/softlayer/chef-swftp">swftp-chef</a>.</p>
<p>When working with lots of servers, whether that be virtual or hardware, being able to automate tasks can be a blessing.  While on a CLI quickly sorting and grepping is common place for those in devOps roles.<br />
If you have found yourself writing something like this, these tools are probably for you...</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">cat /proc/cpuinfo  | grep "model name" | awk '{ print $NF }'</pre></div>
<p>We’ve extended the SoftLayer python bindings to also ship with a new command line tool: <span class="geshifilter"><code class="text geshifilter-text">sl</code></span>.  Simply install from pypi, configure and you are ready to go:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;"># these require python-setuptools package to be installed.
easy_install softlayer 
# alternative method, requires python-pip package 
pip install softlayer  
sl config setup  # You’ll need your API key here</pre></div>
<p>That’s it! You are all setup and ready to rock.  Try some of these commands out:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">sl --help
sl cci list
sl dns list
sl dns list | grep 20.. # notice how we adjusted the output for you?
sl dns list --format=table > dns_zones.txt  # pretty tables to a file.</pre></div>
<p>We’ve been developing this out in the open on <a href="https://github.com/softlayer/softlayer-api-python-client">github</a> and encourage your questions and suggestions be submitted there.  <a href="http://softlayer.github.io/softlayer-api-python-client/">Documentation</a> is also hosted on github to make it easier to find.  Keep in mind these aren’t full API docs like SLDN, but is a great resource for Python API references and examples.  If you are a developer using the SLAPI directly you’ll notice the python bindings are much more pythonic now.</p>
<p>To further support our devOps comrades we’ve released swftp-chef  to even further simplify deploying swftp in your fleet.  Installing is as simple as running one of these two commands:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">knife cookbook site install swftp
# if you have the knife-github gem installed
knife cookboot github install softlayer/swftp  </pre></div>
<p>Set the attributes on either the role/environment and add it to your run list.</p>
<p>We truly hope you find these useful and would love to <a href="https://github.com/softlayer/softlayer-api-python-client/issues?direction=desc&sort=updated&state=open">hear one way or the other</a>.</p>
<p>-Kevin</p>

