---
title: "Introduction: Deploying Drupal on SoftLayer with Chef - Part 2"
description: "<p>In our <a href=http://sldn.softlayer.com/blog/waelriac/Introduction-Deploying-Drupal-SoftLayer-Chef-Part-1>first in"
date: "2014-05-02"
author: "waelriac"
tags:
    - "blog"
---

<p>In our <a href="http://sldn.softlayer.com/blog/waelriac/Introduction-Deploying-Drupal-SoftLayer-Chef-Part-1">first installment</a>, I gave an overview of the Chef automation, framework, and terminology and introduced Drupal. Now, let’s install and configure our Chef server, workstation, and client node. First, we need to configure our development machine with the SoftLayer CLI in order to create three virtual servers in SoftLayer. You can also create the virtual servers using the SoftLayer customer portal, if you prefer.</p>
<p>We will use three servers: chef-server-demo, chef-ws-demo, and chef-drupal-demo, each running Ubuntu 12.04 LTS under the domain softlayer.com.  Note that you can run the Chef workstation on your development machine as well, but I prefer to keep those separate.</p>
<h2>Set up the Development Machine</h2>
<p>I’m using an Ubuntu 12.04 LTS as my development machine. Let’s install the SoftLayer Python client.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">apt-get -y install python-pip
pip install softlayer</pre></div>
<p>Now configure the client using <span class="geshifilter"><code class="text geshifilter-text">sl config setup</code></span>.</p>
<p><img src= https://farm3.staticflickr.com/2911/14091292564_7ea8307a1a_c.jpg width=700 /><br />
For more information on setting up the SoftLayer Python client, see <a href="http://sldn.softlayer.com/blog/phil/Getting-Started-Python-CLI">Getting Started with the Python CLI</a>.</p>
<h2>Set up the Chef Server</h2>
<p>Next, we will create the virtual server for our Chef server. We will use a 100GB local disk and the latest Ubuntu version.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">sl cci create --hostname=chef-server-demo --domain=softlayer.com --cpu=1 --memory=1024 --hourly --os=UBUNTU_12_64 --disk=100 </pre></div>
<p>Once the provisioning is complete, run <span class="geshifilter"><code class="text geshifilter-text">sl cci detail <id> --passwords</code></span> where <span class="geshifilter"><code class="text geshifilter-text">id</code></span> is the ID of the CCI returned from the step above.</p>
<p>Log in to the Chef server. Ensure that the hostname of your server is a FQDN. Here are <a href="http://docs.opscode.com/install_server.html">detailed instructions</a> for this, or you can run <span class="geshifilter"><code class="text geshifilter-text">hostname</code></span>. This should return the FQDN chef-server-demo.softlayer.com. If it does not, run the following command:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">sudo hostname chef-server-demo.softlayer.com
echo chef-server-demo.softlayer.com | sudo tee /etc/hostname</pre></div>
<p>Follow the <a href="http://www.getchef.com/chef/install/?__hstc=153815783.4e101c2a2421b8354db282a5192d48e6.1389397540433.1389397540433.1392671182981.2&__hssc=153815783.1.1392671182981&__hsfp=2895222059">Chef install page</a>:</p>
<ul>
<li>Select the Chef server tab.</li>
<li>Select the Operating System (Ubuntu in our example).</li>
<li>Select the Operating System version and the platform (12.04 and x86_64).</li>
<li>Select the Chef server version to download (11.0.10).</li>
<li>The package will display as an option; right click and copy the URL link.</li>
</ul>
<p>Download the package on your Chef server (using wget, for example). Install the package, using the correct method, on your system. In our example using Ubuntu, the command is <span class="geshifilter"><code class="text geshifilter-text">dpkg –i xxx.deb</code></span>.</p>
<p>Once installed, configure the Chef server by running <span class="geshifilter"><code class="text geshifilter-text">sudo chef-server-ctl reconfigure</code></span>.<br />
Optionally, you can ensure that the Chef server is configured correctly by running <span class="geshifilter"><code class="text geshifilter-text">sudo chef-server-ctl test</code></span>.</p>
<p>As an additional validation step, you can log in to the <a href="https://chef-server-demo.softlayer.com">Chef server UI</a>. The default username and password are located on the right side of the portal.</p>
<p><img src= https://farm8.staticflickr.com/7307/14087625711_33b420c199_o.png width=700 /><br />
<strong>Chef server portal - Default password on right side</strong></p>
<h2>Set up the Chef Workstation</h2>
<p>Now, let’s create the virtual server for our Chef workstation. We will use the same CLI command as we did for the Chef server:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">sl cci create --hostname=chef-ws-demo --domain=softlayer.com --cpu=1 --memory=1024 --hourly --os=UBUNTU_12_64 --disk=100</pre></div>
<p>You can find detailed instructions on setting up the workstation <a href="http://docs.opscode.com/install_workstation.html">here</a>.</p>
<p>Log in to the Chef workstation. Ensure that the hostname of the workstation is FQDN, following the same steps as under the Chef server section.</p>
<p>Ensure that the Chef server hostname is resolvable from the workstation server. If it is not, add the host and IP address of the Chef server in the <span class="geshifilter"><code class="text geshifilter-text">/etc/hosts</code></span> file.</p>
<p>Next, install the basic packages that will be needed:<br />
<span class="geshifilter"><code class="text geshifilter-text">apt-get –y install curl git vim</code></span></p>
<p>Install the Chef-client:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">curl -L https://www.opscode.com/chef/install.sh | sudo bash</pre></div>
<p>Once the installation is complete, make sure the Chef-client installed successfully by running:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">chef-client –v</pre></div>
<p>You should see the version returned.</p>
<p>Clone the Chef-repo under your home directory using:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">git clone git://github.com/opscode/chef-repo.git</pre></div>
<p>Create the .chef directory in order to store the knife.rb file and the required keys using:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">mkdir –p ~/chef-repo/.chef</pre></div>
<p>Copy the <span class="geshifilter"><code class="text geshifilter-text">admin.pem</code></span> and <span class="geshifilter"><code class="text geshifilter-text">chef-validator.pem</code></span> files from the Chef server <span class="geshifilter"><code class="text geshifilter-text">/etc/chef-server/</code></span> directory to the <span class="geshifilter"><code class="text geshifilter-text">~/chef-repo/.chef/</code></span> folder using:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">scp root@chef-server-demo:/etc/chef-server/admin.pem ~/chef-repo/.chef/
scp root@chef-server-demo:/etc/chef-server/chef-validator.pem ~/chef-repo/.chef/</pre></div>
<p>Run the chef-validator utility:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">knife configure –initial</pre></div>
<p>This will prompt you to answer several questions, shown here with our example answers:</p>
<ol>
<li>Where should I put the config file?  <span class="geshifilter"><code class="text geshifilter-text">~/chef-repo/.chef/knife.rb</code></span></li>
<li>Please enter the Chef server URL:  <span class="geshifilter"><code class="text geshifilter-text">https://chef-server-demo.softlayer.com:443</code></span>;</li>
<li>Please enter a name for the new user:  <span class="geshifilter"><code class="text geshifilter-text">wsadmin</code></span></li>
<li>Please enter the existing admin name:  <span class="geshifilter"><code class="text geshifilter-text">admin</code></span></li>
<li>Please enter the location of the existing admin's private key: <span class="geshifilter"><code class="text geshifilter-text">~/chef-repo/.chef/admin.pem</code></span></li>
<li>Please enter the validation clientname:  <span class="geshifilter"><code class="text geshifilter-text">chef-validator</code></span></li>
<li>Please enter the location of the validation key:  <span class="geshifilter"><code class="text geshifilter-text">~/chef-repo/.chef/chef-validator.pem</code></span></li>
<li>Please enter the path to a Chef repository:  <span class="geshifilter"><code class="text geshifilter-text">~/chef-repo</code></span></li>
<li>Then enter a user name for the new user:  <span class="geshifilter"><code class="text geshifilter-text">wsadmin</code></span></li>
</ol>
<p>Verify that the configuration is correct.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">cd ~/chef-repo
knife client list  </pre></div>
<p>You should get some input back like this:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">chef-validator 
chef-webui</pre></div>
<p>Now, we will install the sendmail cookbook. This cookbook will be needed to properly install Drupal.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">knife cookbook site install sendmail</pre></div>
<p>Next, install the Drupal cookbook.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">knife cookbook site install drupal</pre></div>
<p>If you’re unlucky like me, you may experience some problems. While writing this blog I hit two issues when deploying the Drupal cookbook on a node, and had to make the following fixes:</p>
<ul>
<li>Edit the file <span class="geshifilter"><code class="text geshifilter-text">vim ~/chef-repo/cookbooks/drupal/templates/default/grants.sql.erb</code></span> and change the % symbol to <span class="geshifilter"><code class="text geshifilter-text">localhost</code></span> such as:<br />
<span class="geshifilter"><code class="text geshifilter-text">GRANT ALL ON <%= @database %>.* TO '<%= @user %>'@'localhost' IDENTIFIED BY '<%= @password %>';</code></span></li>
<li>Edit the file <span class="geshifilter"><code class="text geshifilter-text">vim ~/chef-repo/cookbooks/drupal/recipes/default.rb</code></span> and change <span class="geshifilter"><code class="text geshifilter-text">server&#95;aliases node['fqdn']</code></span> to <span class="geshifilter"><code class="text geshifilter-text">server_aliases [node['fqdn']]</code></span></li>
</ul>
<p>Upload the Drupal cookbook to the Chef server:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">knife cookbook upload --all</pre></div>
<p><img src= https://farm8.staticflickr.com/7357/13904241760_375885475a_c.jpg  width=700 /><br />
At this point, I have all that I need to start installing Drupal on my nodes.</p>
<h2>Bootstrapping the Client</h2>
<p>Bootstrapping the client is the process of installing the Chef-client on the node and starting it. This process will pull the configuration associated with that node from the Chef server.</p>
<p>First, let’s create a virtual server for our client. I will be using the minimum configuration as before.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">sl cci create --hostname=chef-drupal-demo --domain=softlayer.com --cpu=1 --memory=1024 --hourly --os=UBUNTU_12_64 --disk=100</pre></div>
<p>Fix the hostname, and include the Chef server hostname in <span class="geshifilter"><code class="text geshifilter-text">/etc/hosts</code></span> on the chef-drupal-demo machine.</p>
<ul>
<li>Log in to the chef-drupal-demo machine and follow the same steps for setting the FQDN on the system.</li>
<li>Add an entry in <span class="geshifilter"><code class="text geshifilter-text">/etc/hosts</code></span> for the Chef server.</li>
</ul>
<p>Note: The steps to fix the hostnames are not required if you use a valid DNS service on SoftLayer.</p>
<p>On the workstation node enter <span class="geshifilter"><code class="text geshifilter-text">cd ~/chef-repo</code></span>.</p>
<p>Next, we will bootstrap the new node using <span class="geshifilter"><code class="text geshifilter-text">knife</code></span>. This includes telling it which recipe to assign to the node, the attributes needed for changing the default passwords, and passing the user and password of the operating system. The command will look like:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">knife bootstrap --run-list "recipe[sendmail],recipe[drupal]" --json-attributes '{"drupal": {"version": "7.26", "db": {"password": "mydbpassword"},"site": {"admin": "zAdmin", "pass": "mypassword", "name": "DemoChefSite"}}}' --ssh-user root --ssh-password mypassword 9.23.82.188</pre></div>
<p>So, what does this command do?</p>
<p>First, we tell knife to bootstrap the node with IP 9.23.82.188 and to access that node using the credentials specified by ssh-user/ssh-password. As part of the initial configuration, we also tell Chef to install the sendmail and Drupal recipes, and to override some of the default parameters for Drupal (for example, which version to use and which users/passwords to set).</p>
<p>Once this script is complete your node should be configured with Drupal. You may log in to the UI with the Drupal admin and password you specified on the command line, using the default http port http://9.23.82.188.</p>
<p>In the next installment, I will describe how to automate the deployment process. This will give you an end-to-end script for provisioning and configuring an instance.</p>
<p>-Wissam</p>

