---
title: "What to Expect from Bluemix VPN"
description: "<p>Both the Bluemix VPN service and the Bluemix Gateway service allow you to connect a Bluemix environment to an existin"
date: "2016-07-19"
author: "cgallo"
tags:
    - "blog"
---

<p>Both the Bluemix VPN service and the Bluemix Gateway service allow you to connect a Bluemix environment to an existing infrastructure in a very simple, secure, and straightforward manner. While the documentation on how to setup both of these services is well-organized, there isn’t very much information available on the performance of these services. So I setup a little experiment to attempt to get a rough idea of how well each service performs, and I got some very promising results in the process.</p>
<h2>Bluemix VPN</h2>
<p>First, I wanted to test out the <a href="https://console.ng.bluemix.net/docs/services/vpn/vpn_faq.html#vpn_faq">Bluemix VPN</a> service, which is used to connect your Bluemix containers (and only the containers at this time) to any other IPSEC compatible endpoint. For this experiment, I am trying two different endpoints: a dedicated server and a <a href="http://www.softlayer.com/network-appliances">Vyatta</a> gateway. On the Bluemix side, I will have two containers running <a href="https://hub.docker.com/r/networkstatic/iperf3/">iperf3</a>, which is used to push out as much traffic as possible.</p>
<p>The <a href="https://console.ng.bluemix.net/docs/services/vpn/vpn_onpremises.html#gaas">Bluemix VPN setup guides</a> are a useful and great starting point, and are required reading for this experiment.</p>
<h3>Setting up the experiment</h3>
<p>Like any good experiment, it is very important to be able to reproduce the results. Here is everything you will need to know to try this on your own. (A SoftLayer account and a Bluemix account will be required, of course.)</p>
<h3>Setting up the SoftLayer server</h3>
<p>To test the SoftLayer side of things, we will use a single bare metal server with a 1Gbps public and private network. To reduce any latency or travel time issues, the server should be located in one of the Dallas data centers (which is where the Bluemix U.S. South region is hosted as well). Any operating system should be fine, but I choose the latest Ubuntu, since that is my personal favorite to work with. Any amount of RAM/CPU/disk space will be fine as well, since we are not really testing those.</p>
<p>Once the server is provisioned, make note of the private network subnet; mine was 10.37.82.128/26 and will be referenced in this experiment.</p>
<h3>Install Iperf3</h3>
<p>Iperf3 is the best tool that I have found for easily testing network speeds. Unfortunately, Ubuntu only ships with Iperf2, which is still pretty good, but I want to use the newest version (because newer is always better), so that will require a little bit of extra work to get installed.</p>
<p><a href="http://cheatsheet.logicalwebhost.com/iperf-network-testing/">iperf3 cheatsheet</a></p>
<p><a href="https://github.com/esnet/iperf">iperf3 github</a></p>
<pre><code>cd /usr/src</code></pre>
<pre><code>apt-get install build-essential git</code></pre>
<pre><code>git clone https://github.com/esnet/iperf.git</code></pre>
<pre><code>cd iperf</code></pre>
<pre><code>./configure</code></pre>
<pre><code>make</code></pre>
<pre><code>make install</code></pre>
<pre><code>LD_LIBRARY_PATH=/usr/local/lib</code></pre>
<pre><code>export LD_LIBRARY_PATH</code></pre>
<p>After iperf3 is installed, we just need to setup a daemon to connect to. I used the following options:</p>
<pre><code>iperf3 -f m -s -D -J --logfile /var/log/iperf3.1.log -p 9001</code></pre>
<h3>Setting up the Bluemix Container</h3>
<p>Luckily, there is already an <a href="https://hub.docker.com/r/networkstatic/iperf3/">iperf3 docker container</a> available to use, so all that is required here is to publish it to our Bluemix repository and then spin one up.</p>
<p>If you haven’t already, setup the <a href="https://console.ng.bluemix.net/docs/containers/container_cli_ov.html#container_cli_ov">Bluemix Docker CLI</a>.</p>
<p>Since Bluemix uses its own repositories for Docker images, we need to build the iperf3 container first, which is easy enough. Copy the contents of the <a href="https://hub.docker.com/r/networkstatic/iperf3/~/dockerfile/">iperf3 Dockerfile</a> into a local file called “Dockerfile” then run:</p>
<pre><code>cf ic build -t iperftest3 .</code></pre>
<p>Assuming that build without errors, try running the test against the public network of your new SoftLayer server.</p>
<pre><code>cf ic run -m 64 --name iperf01 registry.ng.bluemix.net/&lt;NAMESPACE&gt;/iperftest3 -c &lt;SOFTLAYER PUBLIC IP&gt; -t 600 -i 10 -R -p 9001</code></pre>
<h3>Setting up the VPN</h3>
<p>Bluemix has some great documentation on <a href="https://console.ng.bluemix.net/docs/services/vpn/onpremises_gateway.html">Setting up VPN endpoints</a> (which you should read), but I will highlight the steps I took to get this all working.</p>
<ol start="1" type="1">
  <li>Make sure you have a Bluemix container already in use. This is required to use the Bluemix VPN service.</li>
  <li>Add the <a href="https://console.ng.bluemix.net/catalog/services/virtual-private-network-vpn">Virtual Private Network</a> service to your account.</li>
  <li>Take note of the IP address you get assigned, and leave the rest of the configurations for later.</li>
  <li>Setup StrongSwan on your SoftLayer server. Start at <a href="https://console.ng.bluemix.net/docs/services/vpn/onpremises_gateway.html#strongswan">Step 4</a>. That article says to configure the Bluemix connection first, but you need to do that LAST for it to connect properly. </li>
</ol>
<p>The RIGHT side is Bluemix information. The LEFT side is SoftLayer information.</p>
<p>Just copy all the config files from that tutorial, and you should only need to edit the LEFT/RIGHT networks. Make sure your “rightid” field is set to the IP of your Bluemix VPN tunnel and not “%any” from <a href="http://stackoverflow.com/questions/36871101/bluemix-vpn-strongswan-specification-example-gateway-ip-address-usage">stackoverflow</a>. You will likely want to set your own secret key as well.</p>
<p>To setup a VPN connection with a Vyatta Endpoint instead, follow this guide on getting <a href="https://sldn.softlayer.com/blog/rtiffany/bluemix-vpn-softlayer-vyatta-cloud-communication">Bluemix + Vyatta Connected</a>:</p>
<ol start="1" type="1">
  <li>Finish setting up the <a href="https://console.ng.bluemix.net/docs/services/vpn/index.html#site">Bluemix VPN connection</a>; generally use the default values unless you know what you are doing.</li>
  <li>Once finished, refresh the page, and check that the status is “UP”. If not, check your StrongSwan status to see what errors you might have. If the error is about getting clear text responses, try removing and recreating the VPN connection. Delete the connection and recreate it; you don’t need to delete the entire VPN service.</li>
</ol>
<h3>Run a test</h3>
<p>Now that everything is setup, we need to get some meaningful data. This is done by spinning up a Docker instance and pointing it at the private IP of our SoftLayer server.</p>
<pre><code>cf ic run -m 64 --name iperf01 registry.ng.bluemix.net/cgallo/iperftest3 -c 10.37.82.159 -t 600 -i 10 -p 9001</code></pre>
<p>Wait for that to finish (should be exactly 600 seconds), and then you can test the reverse speed (-R flag does this). A single iperf3 instance can only run one test at a time, so if you wanted to run two Docker instances and test both upstream and downstream speeds at the same time, you would need two iperf3 instances running on two different ports—which I will leave as an exercise for the reader.</p>
<pre><code>cf ic run -m 64 --name iperf02 registry.ng.bluemix.net/cgallo/iperftest3 -c 10.37.82.159 -t 600 -i 10 -R -p 9001</code></pre>
<p>Hopefully your results match mine, which are explained below.</p>
<h3>Results</h3>
<p><img src="http://sldn.softlayer.com/sites/default/files/assets/blog_post/BMToSL-final.png" alt="Bluemix to SoftLayer" height="351" width="700"/></p>
<p>To give the VPN speeds some perspective, I also wanted to test SoftLayer-to-SoftLayer and Bluemix-to-Bluemix.</p>
<h3>SoftLayer-to-SoftLayer</h3>
<p>Predictably, the connection between two bare metal servers in the same data center across the back-end network is really, really fast.</p>
<h3>Container-to-Container</h3>
<p>The connection between two containers was a lot lower than I expected, but they were still able to communicate at over 100Mbit/s, which is fairly respectable.</p>
<h3>Container-to-SoftLayer</h3>
<p>Now the part we really care about: transit over the VPN link.</p>
<p>I did two different tests: one through an instance of StrongSwan that I personally setup and one through a Vyatta Gateway. The speeds to Bluemix were about the same for both tests, but interestingly, the speeds to SoftLayer through the Vyatta were much higher. I suspect the difference in speeds here is likely due to a change in traffic congestion on the Bluemix side of things, but I’m sure having a dedicated gateway appliance played a small part as well.</p>
<h3>VPN Conclusion</h3>
<p>Overall, the VPN connection should be viable for any workloads that do not exceed 100Mbit/s. It is very easy to setup, and once running, requires almost no maintenance.</p>
<p>Latency over this connection was also excellent.</p>
<pre><code>--- 10.176.18.4 ping statistics ---</code></pre>
<pre><code>600 packets transmitted, 600 received, 0% packet loss, time 599734ms</code></pre>
<pre><code>rtt min/avg/max/mdev = 2.020/2.344/19.238/0.728 ms</code></pre>
<h2>Bluemix Gateway</h2>
<p>The Bluemix Gateway service allows Bluemix applications to connect into private networks by exposing a URL and port combination on the Bluemix side for your application to connect to, and a process running inside your private network to actually move the traffic. <a href="https://developer.ibm.com/bluemix/2015/03/27/bluemix-secure-gateway-yes-can-get/">(Here’s some required reading</a>.)</p>
<h3>Setting up the experiment</h3>
<p>For this section, I have created a small Bluemix application that contains the binary and library we need to launch iperf3, and a simple Python web server to launch the command.</p>
<h3>The Application</h3>
<p>My <a href="https://hub.jazz.net/project/allmightyspiff/iperf3Test/overview">iperf3 project</a> is available on hub.jazz.net and is very rough and simple, but it gets the job done. Download the code and upload it to your Bluemix account.</p>
<pre><code>git clone https://hub.jazz.net/git/allmightyspiff/iperf3Test </code></pre>
<pre><code>cd iperf3Test</code></pre>
<pre><code>cf push</code></pre>
<p>Once the code is uploaded and the application is running, we need to get the secure gateway connected.</p>
<h3>The Gateway</h3>
<p>First, add the <a href="https://console.ng.bluemix.net/catalog/services/secure-gateway">Secure Gateway</a> service to your account and bind it to your new application. Then follow the <a href="https://console.ng.bluemix.net/docs/services/SecureGateway/secure_gateway.html">Secure Gateway Documentation</a> to get everything setup.</p>
<p>The securegateway_clientd application will run on the server that is running iperf3. Once it is installed and running, it will register itself (thanks to the provided authentication tokens) with the secure gateway. When you send data to the secure gateway URL, the secure gateway will send that data to the client running on the SoftLayer server, which is then sent to the address listed as the destination + port.</p>
<p>Traffic originating from the application will go to an “On Premises” destination, while traffic originating from a SoftLayer server going to your application will be a “Cloud Destination.”</p>
<h3>Running the test</h3>
<p>The URL needed to launch the test is formatted as follows:</p>
<pre><code>A normal test</code></pre>
<pre><code>http://&lt;APPLCIATION URL&gt;/iperf/&lt;DESTINATION&gt;/&lt;PORT&gt;</code></pre>
<pre><code>For a reverse test</code></pre>
<pre><code>http://&lt;APPLCIATION URL&gt;/iperf/&lt;DESTINATION&gt;/&lt;PORT&gt;/R</code></pre>
<p>That will launch iperf3 in the background. You will need to check on it manually since I didn’t create anything fancy to acknowledge the test finishing. The files can be retrieved with the cf cli tool:</p>
<pre><code>cf files iperf3Test app</code></pre>
<pre><code>cf files iperf3Test app/iperf3.secureR-1465496323.43.log</code></pre>
<h3>The Results</h3>
<p><img src="http://sldn.softlayer.com/sites/default/files/assets/blog_post/secureGateway-1.png" alt="Secure gateway" height="461" width="700"/></p>
<p>I ran two sets of tests: one over the public internet and one over the secure gateway.</p>
<h3>Public Internet</h3>
<p>SoftLayer-to-Bluemix had a decent average speed, averaging 89 Mbits/s. Bluemix-to-Softlayer, however, had significantly higher results, with a pretty impressive average speed of 514 Mbits/s. While the traffic spikes and dips a lot, even the minimum speed of 105 Mbits/s is really good.</p>
<h3>Secure Gateway</h3>
<p>The speeds of Bluemix-to-SoftLayer were rather poor, at an average of 20 Mbits/s, which is not really ideal for sending any decent amounts of data into a private network. However, SoftLayer-to-Bluemix was really great, at an average speed of 100 Mbits/s. Any data that lived in your private network that needed to be sent to Bluemix for processing would get there just fine.</p>
<h2>Conclusion</h2>
<p>Overall, both the VPN and secure gateways provide great ways of connecting your cloud and private infrastructures together so that data can be shared quickly and securely between them.</p>


