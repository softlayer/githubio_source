---
title: "SoftLayer_Network_Monitor_Version1_Query_Host"
description: "The Query_Host service is the core of the monitoring system.  Each instance of this service represents a monitoring instance.  Each monitoring instance consists of a hardware ID to monitor, an IP address attached to that hardware ID, a method of monitoring, and what to do in the instance that the monitor ever fails. 

The monitoring services are scheduled jobs, and cannot be initiated by the user.  Simply creating the object is enough, the monitor will begin working in 5-10 minutes.  Deleting a monitor will immediately remove it from the monitoring queue.  Modifications will take effect in 5-10 minutes. 

If the user wishes to be notified, or have other users on the account notified when a monitoring instance fails, a response type that includes 'notify users' must be included on the query host object, and a SoftLayer_User_Customer_Notification_Hardware instance must be saved linking the desired users to the hardware being monitored.  In order for users to be notified, a SoftLayer_User_Customer_Notification_Hardware object MUST exist linking them to a hardware object, and a monitoring instance on that hardware object must be set to 'notify users' "
date: "2018-02-12"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor_Version1_Query_Host"
type: "reference"
layout: "service"
mainService : "SoftLayer_Network_Monitor_Version1_Query_Host"
---
