---
title: "Object Storage Uploader"
description: "<h2>Overview</h2>\n<p>We&rsquo;ve recently added the option to import customer-supplied Virtual Hard Disks (VHDs) to our"
date: "2016-11-15"
author: "ashaw"
tags:
    - "blog"
---

<h2>Overview</h2>
<p>We&rsquo;ve recently added the option to import customer-supplied Virtual Hard Disks (VHDs) to our object storage offering. This is a great option for our customers who may have special virtual machines that they have spent hours perfecting. Since learning to import these images can pose a slight challenge, especially for those unfamiliar with object storage <a href="http://docs.openstack.org/developer/swift" target="_blank">(OpenStack Swift)</a>, I wrote this blog to share scripts that will streamline the process.</p>
<h2>Object Storage</h2>
<p>SoftLayer&rsquo;s object storage is an enhanced version of <a href="http://docs.openstack.org/developer/swift" target="_blank">OpenStack Swift</a>. Although we&rsquo;ve added features to it, the API (on the whole) is still the same. Two requirements of particular importance to storing disk images are <a href="http://docs.openstack.org/developer/swift/overview_large_objects.html" target="_blank">limitations and requirements on large files</a>. Swift limits all files to be 5GB or less. To support larger files users need to create a manifest file that combines smaller files into one large file.</p>
<p>For example, to upload a 12GB VHD, the user is expected to segment the file into at least three files and then create a manifest that brings them back together.</p>
<h2>Easier Importing</h2>
<p>Since many people don&rsquo;t have the time to learn the inner workings of Swift and would just like to get VHDs running on their servers, I have created a set scripts to simplify the process. They handle the authentication, file segmentation, and dynamic manifest creation for you, so you can get up and running quickly. You can easily access them <a href="https://gist.github.com/follower46/526a7fbc81880e6f2b7e" target="_blank">here</a> .</p>
<p>You can use a Bash script or a Python 3 script. Both do the same thing, but depending on your environment you may prefer one over the other.</p>
<p>But before we jump into the scripts, you&rsquo;ll need to find your object storage username and password.</p>
<p>To get those, log in to <a href="http://control.softlayer.com" target="_blank">http://control.softlayer.com</a>, go to Storage-&gt;Object Storage, select your cluster (I would suggest Dallas 5 for your first tests), and then click &ldquo;View Credentials&rdquo; in the top left of the page. You will be presented with a modal window containing your username and API Key (or password) for object storage.</p>
<p><strong>ObjectStorageUploader.sh - Bash Edition</strong><br />
\tThe idea behind this script is to have as little user interaction as possible. By calling the script with the proper parameters, you are able to walk away and let it do its thing.</p>
<p>Simply place the bash script in your directory of VHDs. Call the script by passing in the image you want to upload, the location to upload it (container/filename), and your Swift username and password.</p>
<code>$ ./ObjectStorageUpload.sh myOS.vhd 'myContainer/myOS.vhd' 'SLOS1234-1:SL1234' 'apikey'</code>
<p>It will begin the process of walking through the segments of the file and building up your object in object storage.</p>
<p><strong>ObjectStorageUploader.py - Python 3 Edition</strong><br />
\tBefore we begin, make sure you have installed the latest version of Python 3 located here: <a href="https://www.python.org/downloads/" target="_blank">https://www.python.org/downloads/</a></p>
<p>Any Python 3 release will work, but I have been using Python 3.4.0 for my testing.</p>
<p>The idea behind this script is to actually walk you through the process of uploading a file to Swift. Use this script via supplied parameters, in &ldquo;interactive mode,&rdquo; or a combination of the two. This is particularly handy for Windows users who are newer to scripting. Simply drop the script in the folder containing your VHDs, run it, and let it guide you through uploading the image to object storage.</p>
<p>To execute the script, place it in the directory where you store your VHDs and double click it. It will then prompt you to select the file you want to upload.</p>
<p>After selecting your file, you will be asked for your Swift username and password. Authentication will be attempted and, if successful, the list of containers in your cluster will be presented.</p>
<p>Select the container you want to upload to and the script will begin uploading the VHD to object storage.</p>
<p>If you prefer the command line arguments approach, you can pass in arguments to this script too. The signature is slightly different since all the opinions are optional.</p>
<code>$ python ObjectStorageUpload.py -f myOS.vhd -t 'myContainer/myOS.vhd' -u 'SLOS1234-1:SL1234'</code>
<h2>Importing Uploaded VHD as Image Templates</h2>
<p>Now that your image is in object storage you can import your VHD into the SoftLayer template, so you can use it to provision a new virtual server!</p>
<p>Go to your <a href="https://control.softlayer.com/devices/images" target="_blank">image templates page</a> in the portal and click the &ldquo;Import Image&rdquo; tab. Select the Swift account, cluster, container, and file that you uploaded. Give your new template a name and some notes. Make sure to fill out the Operating System information properly as this is used when setting up your new server, and finally click &ldquo;Import.&rdquo;</p>
<p>Lastly, you will be emailed after the VHD has been processed by our system.</p>
<p>-Adam Shaw</p>

