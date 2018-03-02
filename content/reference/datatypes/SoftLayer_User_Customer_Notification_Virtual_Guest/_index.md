---
title: "SoftLayer_User_Customer_Notification_Virtual_Guest"
description: "The SoftLayer_User_Customer_Notification_Virtual_Guest object stores links between customers and the virtual guests they... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Notification_Virtual_Guest"
---

# SoftLayer_User_Customer_Notification_Virtual_Guest
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_Notification_Virtual_Guest' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_User_Customer_Notification_Virtual_Guest object stores links between customers and the virtual guests they wish to monitor.  This link is not enough, the user must be sure to also create SoftLayer_Network_Monitor_Version1_Query_Host instance with the response action set to "notify users" in order for the users linked to that hardware object to be notified on failure. 





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
            <span class='views-field-title'><a href="#guestId" name=guestId>guestId</a></span>
            <div class='views-field-body'>The ID of the virtual guest object that is to be monitored. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The unique identifier for this object </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#userId" name=userId>userId</a></span>
            <div class='views-field-body'>The ID of the SoftLayer_User_Customer object that represents the user to be notified on monitoring failure. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#guest" name=guest>guest</a></span>
            <div class='views-field-body'>The virtual guest object that will be monitored. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#user" name=user>user</a></span>
            <div class='views-field-body'>The user that will be notified when the associated virtual guest object fails a monitoring instance. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


