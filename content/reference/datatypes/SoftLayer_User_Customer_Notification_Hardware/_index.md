---
title: "SoftLayer_User_Customer_Notification_Hardware"
description: "The Customer_Notification_Hardware object stores links between customers and the hardware devices they wish to monitor.... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Notification_Hardware"
---

# SoftLayer_User_Customer_Notification_Hardware
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Customer_Notification_Hardware' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_Notification_Hardware' >Datatype</a></li>
    </ul>
</div>

## Description 
The Customer_Notification_Hardware object stores links between customers and the hardware devices they wish to monitor.  This link is not enough, the user must be sure to also create SoftLayer_Network_Monitor_Version1_Query_Host instance with the response action set to "notify users" in order for the users linked to that hardware object to be notified on failure. 


### associatedMethods

*  [SoftLayer_User_Customer_Notification_Hardware::findByHardwareId](/reference/services/SoftLayer_User_Customer_Notification_Hardware/findByHardwareId )





<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
    <div id="localProperties" class="prop-content" >
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardwareId" name=hardwareId>hardwareId</a>
            </span>
            <div class='views-field-body'>The ID of the Hardware object that is to be monitored. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The unique identifier for this object </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#userId" name=userId>userId</a>
            </span>
            <div class='views-field-body'>The ID of the SoftLayer_User_Customer object that represents the user to be notified on monitoring failure. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardware" name=hardware>hardware</a>
            </span>
            <div class='views-field-body'>The hardware object that will be monitored. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#user" name=user>user</a>
            </span>
            <div class='views-field-body'>The user that will be notified when the associated hardware object fails a monitoring instance. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


