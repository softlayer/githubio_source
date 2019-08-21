---
title: "SoftLayer_Container_Virtual_Guest_PendingMaintenanceAction"
description: "The SoftLayer_Container_Virtual_Guest_PendingMaintenanceAction data type contains information relating to a SoftLayer_Vi... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Virtual_Guest_PendingMaintenanceAction"
---

# SoftLayer_Container_Virtual_Guest_PendingMaintenanceAction
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Virtual_Guest_PendingMaintenanceAction' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Virtual_Guest_PendingMaintenanceAction data type contains information relating to a SoftLayer_Virtual_Guest's pending maintenance actions. 





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
                <a href="#actionId" name=actionId>actionId</a>
            </span>
            <div class='views-field-body'>The ID of the associated action.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#dueDate" name=dueDate>dueDate</a>
            </span>
            <div class='views-field-body'>The datetime at which this action will be initiated regardless of customer action (if it has not already been completed).  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#status" name=status>status</a>
            </span>
            <div class='views-field-body'>User-friendly status. 

The <code>Completed</code> status means that it is done, no further action is required. The <code>Scheduled</code> status means that the action is pending and will start on the <code>dueDate</code> if no customer action is taken before such time. The <code>In Progress</code> status means the action is currently being executed.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ticket" name=ticket>ticket</a>
            </span>
            <div class='views-field-body'>The ticket associated with this maintenance action.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a></p>
            </div>
        </div>
            </div>
    </div>


