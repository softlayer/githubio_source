---
title: "Our Python client is out!"
description: "Lately I've seen a lot of people around me writing and hacking in <a href=http://www.python.org/>Python</a>. Way back "
date: "2010-04-21"
author: "klaude"
tags:
    - "blog"
---

Lately I've seen a lot of people around me writing and hacking in <a href="http://www.python.org/">Python</a>. Way back when API v1 was out we <a href="http://sldn.softlayer.com/06/2007/api-hacking-fun-with-python/">noted</a> that Python has built-in XML-RPC support. Built-in XML-RPC support is great. It makes calling our API, especially our latest API, a snap. Some of y'all on our <a href="http://forums.softlayer.com/">forums</a> have been doing very cool things with our API in Python. 

Python hackers and users, we've just made your lives easier. I'm pleased to present our latest language tool for your API toolbox, a <b><a href="http://github.com/softlayer/softlayer-api-python-client/">Python library for the SoftLayer API</a></b>. This library functions very similarly to our <a href="http://github.com/softlayer/softlayer-api-php-client">PHP</a> and <a href="http://github.com/softlayer/softlayer-api-perl-client">Perl</a> clients. Before you had to juggle API call headers to pass along things like initialization parameters and object masks to your API calls. Now you all you have to do is declare an API client object and run methods on it. It's much easier and saves a lot of coding on your part.

I've been talking to a lot of people who are building dynamic Cloud Computing Instances using our API. I wrote a simple example for one of our forum users a while back to accomplish this task in Python using it's built-in XML-RPC support:

<script src="https://gist.github.com/328806.js?file=orderCciFromTemplate.py"></script>

Here's that same functionality using our new Python library:

<script src="https://gist.github.com/374419.js"> </script>

This saved 20 lines of code and is much easier to read. Our client is supported in both Python 2 and Python 3 and has a handy installation script. Please download it, go nuts, and speak up on our forums, IRC channel, or a support ticket if you have any questions. As always, we're happy to hear your feedback. Thanks, everyone!
<br />

<b><a href="http://github.com/softlayer/softlayer-api-python-client/">http://github.com/softlayer/softlayer-api-python-client/</a></b>

