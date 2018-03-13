---
title: "How to Use The SoftLayer API to Authorize Guest VMs to iSCSI Storage"
description: "SoftLayer iSCSI storage is a great platform for running a clustered OS and file system. Featuring Multipath I/O (MPIO), "
date: "2015-07-16"
author: "sjanowiak"
tags:
    - "blog"
---

SoftLayer iSCSI storage is a great platform for running a clustered OS and file system. Featuring Multipath I/O (MPIO), industry leading durability, and our global footprint, the [Endurance and Performance](https://www.softlayer.com/block-storage) iSCSI block storage products are a great fit for a variety of workloads worldwide. 

One important feature of our Endurance and Performance block storage options is the ability to give access and authorization to any host(s) you choose via the SoftLayer customer portal or API. Once you’ve authorized a host to access a storage device, you’ve created a unique authentication string to build into your iSCSI initiator. 

If you are building a clustered server environment on guest machines inside a hypervisor, you’ll need unique authentication parameters. You can generate unique authentication information for your cluster nodes by authorizing hosts on your SoftLayer account. However, if you want to authorize specific guest VMs within your hypervisor, you have the option to generate unique authentication parameters via the SoftLayer API.  

Let’s walk through the steps to use the SoftLayer API and the SoftLayer Python CLI to identify the parameters you need in order to authorize additional IP addresses to Endurance and Performance Storage at SoftLayer.  

##<strong>Gather Your Tools</strong>
The first step is to identify all the parameters you will need to authorize secondary IP addresses to storage. We need to identify the storage itself, and find the identifier for the actual IP address you want to authorize.  

I recommend downloading the SoftLayer CLI for Python for this first piece. The documentation can be found [here](https://softlayer-api-python-client.readthedocs.org/en/latest/). However if you have a SoftLayer server running Linux on your account, you can easily install with pip the following command:  

<code>pip install softlayer </code>

Once SoftLayer is installed via pip, follow the quick two-step configuration outlined here. 

Begin the setup process using:

<code>slcli setup </code>

Input your user credentials and API key. You can use the public or private network endpoint. Once complete, you’re ready to advance to ... 

##<strong>Gather Your Resources</strong>
There are three parameters you need: 
<ol><li>Storage ID 
<li>Subnet ID 
<li>IP Address ID 
</ol>

For the first two, use the slcli to grab the data. Let’s start with the storage ID. This command is:
 
<code>slcli iscsi list</code>

This will produce an easy to read table of all your storage volumes. Find the volume you want to authorize your IP address and record your storage ID. 

Next, find the IP address ID. To get this, you’ll first need to identify the subnet ID by listing all your subnets via the SoftLayer CLI by running this command:

<code>slcli subnet list</code>

This will produce an easy-to-read table of all your subnets. Find the subnet that contains the IP addresses you want to authorize and record the subnet ID. 

Finally, you can use curl to identify the IP Address ID from within the subnet we just identified:  
<code>
curl -# -X GET https://[USERNAME]:[APIKEY]@api.softlayer.com/rest/v3/SoftLayer_Network_Subnet/[SUBNET ID]/getIpAddresses.xml?objectMask='id;ipAddress' 
</code>

This will return an XML file listing all of the IP addresses and their IP Address IDs. Record the IP Address ID that you want to authorize. 

##<strong>Putting it all Together</strong> 
Now that you have all of your parameters in place, you can run additional curl commands to authorize IP Address IDs to your storage: 

<code>
curl -v -i -X POST -d '{"parameters": [{"id": [IP ADDRESS ID]}]}' -u "[USERNAME]:[APIKEY]" https://api.softlayer.com/rest/v3/SoftLayer_Network_Storage/[STORAGE ID]/allowAccessFromIpAddress.json 
</code>

This command should produce an output of “OK.” Now log in to your portal, and verify that the storage device now has an entry for the IP address. 

You’ll see that the IP addresses you deployed on guest VMs within your hypervisor now have unique authorization credentials to connect to the iSCSI storage. Now you can use those credentials within your guest machines to attach to the iSCSI volumes.

Feel free to reach out to us on via [social@softlayer.com](mailto:social@softlayer.com), [Facebook](http://www.facebook.com/SoftLayer) or [Twitter](https://twitter.com/SoftLayer) if you have any suggestions or questions. 

-Seth


