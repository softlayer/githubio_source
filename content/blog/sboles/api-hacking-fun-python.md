---
title: "API Hacking Fun With Python"
description: "<p>(This post refers to SoftLayer API version 1. Check out <a href=http://sldn.softlayer.com/03/2008/and-now-for-someth"
date: "2007-06-21"
author: "sboles"
tags:
    - "blog"
---

<p>(This post refers to SoftLayer API version 1. Check out <a href="http://sldn.softlayer.com/03/2008/and-now-for-something-completely-different/">API version 3</a> for our latest updates.)</p>
<p>Hello!  I'm Shawn, one of new "Code Writing Professionals" at SoftLayer. When a call went out for examples using SoftLayer's new API, I immediately signed up to write the <a href="http://en.wikipedia.org/wiki/Intercal">INTERCAL</a>, <a href="http://en.wikipedia.org/wiki/Prolog">Prolog</a>, and <a href="http://en.wikipedia.org/wiki/Apollo_Guidance_Computer">Apollo Guidance Computer</a> modules. I was told to make those <strong>low</strong> priority projects, and to perhaps focus on hacking with <a href="http://www.python.org/">Python</a> instead. If you just want to see the finished code without all the Python evangelization, skip to the end of the post. For those of you who haven't hacked with Python yet, follow along for the ride!</p>
<p>In case you don't know, Python is an incredibly simple and clean looking programming language. Many people have picked it up in just a few minutes! If you already program in another programming language (like C, Java, PHP, SH, or Perl (shiver)), Python may look a bit strange. But it's not too strange at all. In fact, the only "strange" bits in Python are it's reliance on whitespace (you have to line up your code) and the lack of braces.</p>
<p>Any good FORTRAN coder will tell you that whitespace is good.</p>
<p>If you run a flavor of UNIX, Linux, or BSD, you most likely have Python already installed. If you are running Windows or if your distribution doesn't come with a recent Python package installed you will need to install Python. You Linux guys can install it with your favorite package manager (it's usually named<strong> python</strong>). Windows users (or UNIX haxxors who prefer tarballs), pick up the latest version of Python from <a href="http://www.activestate.com/Products/activepython/">ActiveState</a>. (You will also want to check out ActiveState's free(!) Komodo Edit)</p>
<p>Install Python and we are ready to go!</p>
<p>Open up a UNIX Terminal or the Windows command line (Start->Run... type CMD {enter}), then type "python". This boots up the Interactive Python Interpreter. One of the cool things about Python is that you can whip up a Python Interpreter and just start typing in program fragments. It's like the "immediate" mode in QBASIC for DOS, but neater. You should see something like this:<br />
&nbsp;<br />
<a href="http://sldn.softlayer.com/sites/default/files/01-python-cmd.png" target="_blank"><img src="http://sldn.softlayer.com/sites/default/files/01-python-cmd.png" border="0" width="152" height="100" /></a><br />
&nbsp;<br />
The first step is to <em>import</em> the XML-RPC library for Python. In keeping with Python's "Batteries Included" approach, the most useful libraries come standard with any complete download of the Python interpreter, and this includes the standard XML-RPC library. To do this, type:<br />
&nbsp;</p>
<pre lang="python">import xmlrpclib</pre><p>&nbsp;<br />
Now Python has all the functionality needed to make and receive XML-RPC calls loaded into the interpreter.  Let's set up some variables to make hacking with the library much easier. In the interpreter, type:<br />
&nbsp;</p>
<pre lang="python">url = "http://api.service.softlayer.com/xmlrpc/v1/SL-Service.html"
key = "YOUR SOFTLAYER API KEY"
usr = "YOUR SOFTLAYER API USERNAME"</pre><p>&nbsp;<br />
Now we need to set up a Server Proxy. This is an object that we can make method calls against that does all the dirty work of compiling the XML and parsing the data... all the boring stuff. Using the proxy we get to make XML-RPC calls as if all the work was being done on the local machine. This is easy to do. Type this into the interpreter:<br />
&nbsp;</p>
<pre lang="python">server = xmlrpclib.ServerProxy(url)</pre><p>&nbsp;<br />
Now you have your proxy. If you print out the server variable (<em>print server</em>) you will see that server is an instance of the ServerProxy class made to communicate with the SoftLayer XML-RPC server.  Now, let's actually do something!<br />
&nbsp;</p>
<pre lang="python">serverList = server.getServerList(key, usr)</pre><p>&nbsp;<br />
This invokes the XML-RPC <em>getServerList</em> method, which retrieves your list of servers and stashes it into <strong>serverList</strong>. Let's see what you got:<br />
&nbsp;</p>
<pre lang="python">print serverList</pre><p>&nbsp;<br />
The data is returned as a LIST of DICTIONARIES, with one DICTIONARY per server. Let's loop through this list and display the servername of all your servers:<br />
&nbsp;</p>
<pre lang="python">for thisServer in serverList:
  print thisServer["SERVERNAME"]</pre><p>&nbsp;<br />
The two space indentation at the beginning of the second line are required or else the code won't work. Hit enter twice, and Python will print out the Servername (hostname + domain name) for all servers in your account. You can pull more data out of the dictionary easily:<br />
&nbsp;</p>
<pre lang="python">for thisServer in serverList:
  print thisServer["SERVERNAME"], thisServer["PUBLIC_IP_ADDRESS"]</pre><p>&nbsp;<br />
You can make all the method calls listed in the SoftLayer API Documentation by calling them as methods of the server class:<br />
&nbsp;</p>
<pre lang="python">server.getBandwidthList(key, usr, "192.168.1.1")
server.getServerNetworkDetails(key, usr, "192.168.1.1")
server.rebootServer(key, usr, "192.168.1.1", "Soft Reboot")</pre><p>&nbsp;<br />
Python is easy to pick up and play with, and with it's XML-RPC library, it's probably the fastest way for people to hack with the SoftLayer API.  The complete code listing to display all your servernames is below:<br />
&nbsp;</p>
<pre lang="python"># Quickie Python XML-RPC Demo for the SoftLayer API
# Written by Shawn Boles, SoftLayer Development

# API Connection Details
url = "http://api.service.softlayer.com/xmlrpc/v1/SL-Service.html"
key = "PUT YOUR SOFTLAYER API KEY HERE..."
usr = "PUT YOUR API USERNAME HERE..."

# This is the XML-RPC Library for Python.  It comes standard!
import xmlrpclib

# Set up the proxy object for the SoftLayer server.  You can make
# calls against this object as if the processing is local.
server = xmlrpclib.ServerProxy(url)

# Make a method call on getServerList from the API.
# Don't forget to pass the key and usr variables as the first
# two parameters, in that order!
serverList = server.getServerList(key, usr)

# Loop through all servers, displaying their servernames.
for myserver in serverList:
    print myserver["SERVERNAME"]</pre><p>&nbsp;<br />
Only 8 lines of code, ignoring comments and empty lines. Hacking indeed! When a new API method comes out you can pop open a command line and slap together a test case in a minute or two to try it out!</p>
<p>Extra Credit:  Let's do something a little more useful with our new |33+ Python API Hacking Skilz:<br />
&nbsp;</p>
<pre lang="python"># Display all my servers and IP addresses, using the SoftLayer API
# Written by Shawn Boles, SoftLayer Development

# API Connection Details
url = "http://api.service.softlayer.com/xmlrpc/v1/SL-Service.html"
key = "PUT YOUR SOFTLAYER API KEY HERE..."
usr = "PUT YOUR API USERNAME HERE..."

# This is the XML-RPC Library for Python.  It comes standard!
import xmlrpclib

# Set up the proxy object for the SoftLayer server.  You can make
# calls against this object as if the processing is local.
server = xmlrpclib.ServerProxy(url)

# Make a method call on getServerList from the API.
# Don't forget to pass the key and usr variables as the first
# two parameters, in that order!
serverList = server.getServerList(key, usr)

# Loop through all servers, displaying their servernames.
for myserver in serverList:
    # Get the list of Server Details from the API for each server:
    serverDetail = server.getServerDetails(key, usr, myserver["ID"])

    # "Unfold" the Server Details data structure and give us access
    # to only the IP information...
    prettyServerDetail = serverDetail[2][0]

    try:
        print myserver["SERVERNAME"], \\
            "\
\\tPublic IP:", prettyServerDetail["PRIMARY_PUBLIC_IP"], \\
            "(", prettyServerDetail["PUBLIC_PORT_SPEED"], "),", \\
            "\
\\tPrivate IP:", prettyServerDetail["PRIMARY_PRIVATE_IP"], \\
            "(", prettyServerDetail["PRIVATE_PORT_SPEED"], "),", \\
            "\
\\tManage IP:", prettyServerDetail["MGMT_IP"], "\
"
    except KeyError:
        print "NONE\
"
        pass</pre><p>&nbsp;<br />
Here's a <a href="http://sldn.softlayer.com/wp-content/sldn/20/api_example-python.zip">direct link</a> to the sample file for your editing pleasure.</p>
<p>In no time at all you will be hacking apps for your API no sweat!  And you aren't locked down to command line tools, either.  Python comes with just about every GUI kit, can be used to make your own Python-powered control panel...</p>
<p>Have fun hacking!</p>

