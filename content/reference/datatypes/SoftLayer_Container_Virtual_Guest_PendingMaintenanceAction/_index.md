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

## Local
-----
[actionId]: #actionid
#### [actionId]
The ID of the associated action.   
<span class="type-label">Type: </span>**integer**

-----
[dueDate]: #duedate
#### [dueDate]
The datetime at which this action will be initiated regardless of customer action (if it has not already been completed).   
<span class="type-label">Type: </span>**dateTime**

-----
[status]: #status
#### [status]
User-friendly status. 

The <code>Completed</code> status means that it is done, no further action is required. The <code>Scheduled</code> status means that the action is pending and will start on the <code>dueDate</code> if no customer action is taken before such time. The <code>In Progress</code> status means the action is currently being executed.   
<span class="type-label">Type: </span>**string**

-----
[ticket]: #ticket
#### [ticket]
The ticket associated with this maintenance action.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>**

-----
[title]: #title
#### [title]
The Title for the associated action.   
<span class="type-label">Type: </span>**string**

-----
[triggerExplanation]: #triggerexplanation
#### [triggerExplanation]
The Trigger Explanation for the associated action.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>


