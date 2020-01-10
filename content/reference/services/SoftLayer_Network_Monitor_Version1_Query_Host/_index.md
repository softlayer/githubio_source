---
title: "SoftLayer_Network_Monitor_Version1_Query_Host"
description: "The Query_Host service is the core of the monitoring system.  Each instance of this service represents a monitoring inst... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor_Version1_Query_Host"
---
# SoftLayer_Network_Monitor_Version1_Query_Host
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host' >Datatype</a></li>
    </ul>
</div>

## Description
The Query_Host service is the core of the monitoring system.  Each instance of this service represents a monitoring instance.  Each monitoring instance consists of a hardware ID to monitor, an IP address attached to that hardware ID, a method of monitoring, and what to do in the instance that the monitor ever fails. 

The monitoring services are scheduled jobs, and cannot be initiated by the user.  Simply creating the object is enough, the monitor will begin working in 5-10 minutes.  Deleting a monitor will immediately remove it from the monitoring queue.  Modifications will take effect in 5-10 minutes. 

If the user wishes to be notified, or have other users on the account notified when a monitoring instance fails, a response type that includes "notify users" must be included on the query host object, and a SoftLayer_User_Customer_Notification_Hardware instance must be saved linking the desired users to the hardware being monitored.  In order for users to be notified, a SoftLayer_User_Customer_Notification_Hardware object MUST exist linking them to a hardware object, and a monitoring instance on that hardware object must be set to "notify users" 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [createObject](/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/createObject)
Create a monitoring entry
</div>

<div class="method-row">

#### [createObjects](/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/createObjects)
Create multiple monitoring entries at once
</div>

<div class="method-row">

#### [deleteObject](/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/deleteObject)
Delete a Query_Host object by passing in a version of it
</div>

<div class="method-row">

#### [deleteObjects](/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/deleteObjects)
Delete a group of Query_Host objects by passing in a collection of them
</div>

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/editObject)
Edit the object by passing in a modified instance of the object
</div>

<div class="method-row">

#### [editObjects](/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/editObjects)
Edit a group of Query_Host objects by passing in a collection of them.
</div>

<div class="method-row">

#### [findByHardwareId](/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/findByHardwareId)
Return all monitoring instances associated with the passed hardware ID
</div>

<div class="method-row">

#### [getHardware](/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/getHardware)
Retrieve the hardware that is being monitored by this monitoring instance
</div>

<div class="method-row">

#### [getLastResult](/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/getLastResult)
Retrieve the most recent result for this particular monitoring instance.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/getObject)
Retrieve a SoftLayer_Network_Monitor_Version1_Query_Host record.
</div>

<div class="method-row">

#### [getQueryType](/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/getQueryType)
Retrieve the type of monitoring query that is executed when this hardware is monitored.
</div>

<div class="method-row">

#### [getResponseAction](/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/getResponseAction)
Retrieve the action taken when a monitor fails.
</div>
</div>

</div>

