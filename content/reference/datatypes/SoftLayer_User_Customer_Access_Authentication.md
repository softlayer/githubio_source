---
title: "SoftLayer_User_Customer_Access_Authentication"
description: "SoftLayer_User_Customer_Access_Authentication models a single attempt to log into the SoftLayer customer portal. A SoftLayer_User_Customer_Access_Authentication record is created every time a user attempts to log into the portal. Use this service to audit your users' portal activity and diagnose potential security breaches of your SoftLayer portal accounts. 

Unsuccessful login attempts can be caused by an incorrect password, failing to answer or not answering a login security question if the user has them configured, or attempting to log in from an IP address outside of the user's IP address restriction list. 

SoftLayer employees periodically log into our customer portal as users to diagnose portal issues, verify settings and configuration, and to perform maintenance on your account or services. SoftLayer employees only log into customer accounts from the following IP ranges: 
* 2607:f0d0:1000::/48
* 2607:f0d0:2000::/48
* 2607:f0d0:3000::/48
* 66.228.118.67/32
* 66.228.118.86/32"
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Access_Authentication"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_User_Customer_Access_Authentication"
---
