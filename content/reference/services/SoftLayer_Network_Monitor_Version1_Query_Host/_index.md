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



        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/createObject'> createObject</a> </span>
            <div class='views-field-body'>Create a monitoring entry</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/createObjects'> createObjects</a> </span>
            <div class='views-field-body'>Create multiple monitoring entries at once</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Delete a Query_Host object by passing in a version of it</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/deleteObjects'> deleteObjects</a> </span>
            <div class='views-field-body'>Delete a group of Query_Host objects by passing in a collection of them</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit the object by passing in a modified instance of the object</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/editObjects'> editObjects</a> </span>
            <div class='views-field-body'>Edit a group of Query_Host objects by passing in a collection of them.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/findByHardwareId'> findByHardwareId</a> </span>
            <div class='views-field-body'>Return all monitoring instances associated with the passed hardware ID</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/getHardware'> getHardware</a> </span>
            <div class='views-field-body'>Retrieve the hardware that is being monitored by this monitoring instance</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/getLastResult'> getLastResult</a> </span>
            <div class='views-field-body'>Retrieve the most recent result for this particular monitoring instance.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_Monitor_Version1_Query_Host record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/getQueryType'> getQueryType</a> </span>
            <div class='views-field-body'>Retrieve the type of monitoring query that is executed when this hardware is monitored.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/getResponseAction'> getResponseAction</a> </span>
            <div class='views-field-body'>Retrieve the action taken when a monitor fails.</div>
        </div>
        </div>
</div>

