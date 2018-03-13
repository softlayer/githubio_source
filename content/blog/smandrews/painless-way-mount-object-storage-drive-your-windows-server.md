---
title: "The painless way to mount Object Storage as a drive in your Windows server"
description: "In light of the upcoming legacy storage device End of Life preparation, this how-to for mounting object storage as a dri"
date: "2016-01-13"
author: "smandrews"
tags:
    - "blog"
---

In light of the upcoming legacy storage device End of Life preparation, this how-to for mounting object storage as a drive in your Windows server can help ease the pain.

This guide uses a tool called [ExpanDrive](http://www.expandrive.com/), which connects myriad storage services and maps them as network attached drives. I chose this product after testing a number of them, and found this to be the one with the smallest footprint of the bunch, the most reliable, and the easiest to use. You’ll want to install the software [http://www.expandrive.com/download-expandrive/](http://www.expandrive.com/download-expandrive/), which gives you a seven-day free trial to test it out. Once installed, simply open ExpanDrive and we can walk through the setup for connecting to your SoftLayer object storage account.  

<p style="text-align:center;"><a href="http://cdn.softlayer.com/ExpanDriveEmptyBox.jpg"><img src="http://cdn.softlayer.com/ExpanDriveEmptyBox.jpg" height=450 width=250></a></p> 

Your screen should look similar to one above, minus the OpenStack drive that I already have mounted. This is the main hub of the program. This is how you add, remove, mount, and unmount your object storage as a drive. From here, you click the + sign in the lower left-hand corner. A list of cloud-based storage pops up, along with sFTP and FTP choices. The only one we care about is “OpenStack Swift Storage,” as shown in the next image. 

<p style="text-align:center;"><a href="http://cdn.softlayer.com/ExpanDriveBoxFull.jpg"><img src="http://cdn.softlayer.com/ExpanDriveBoxFull.jpg"/ width=250 height=450></a></p>
 
Click on the OpenStack Swift Storage option and you get a new screen asking for the authentication server, the username, and your API key. You can find that information by logging into the SoftLayer customer portal and clicking on Storage ?  ObjectStorage ? Your username (SLOS99999-1 for example) ? then the cluster of your choice that you have decided to use. Once you’re on the object storage screen, you should see a link that says “View Credentials.” Click that for a new pop-up with your login information.

<p style="text-align:center;"><a href="http://cdn.softlayer.com/accountcredentials.jpg"><img src="http://cdn.softlayer.com/accountcredentials.jpg"/ width=600></a></p>

Since this will be used to connect with the server, let’s use the private endpoint (it won’t count against your bandwidth and it’s almost always a faster connection). Take note of the username’s format as you will need that entire part (“SLOS99999-1:sluser”) to login.

Now that we have that information up, we can go back to the ExpanDrive screen, as seen below, and fill out the required information as follows and click “Connect.”

<p style="text-align:center;"><a href="http://cdn.softlayer.com/Openstackwindow.jpg"><img src="http://cdn.softlayer.com/Openstackwindow.jpg"/ width=250 height=450></a></p>

Once you save and connect, the program will authenticate and launch a new Windows Explorer screen of the new mapped network drive.

Here are a few caveats about how the mounted drive works vs. the portal:

<ul><li>Containers are located on the top-level directory. They are containers in the portal, but they show up as folders in the mount.
<li>If you need to create an empty folder, do it from the portal—the drive doesn’t save the names of folder and will rename it “New Folder.”
<li>The mount syncs in real-time with the object storage servers, so whatever changes you make are reflected almost immediately.
<li>Anything you delete on this mount is also deleted from your object storage account.
<li>The top-level directory is strictly containers.</li>
</ul>

-Shawn Andrews

