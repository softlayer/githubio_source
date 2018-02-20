---
title: "SoftLayer_Notification_Occurrence_Event_Attachment"
description: "SoftLayer events can have have files attached to them by a SoftLayer employee. Attaching a file to a event is a way to p... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_Occurrence_Event_Attachment"
---

# SoftLayer_Notification_Occurrence_Event_Attachment
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event_Attachment' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer events can have have files attached to them by a SoftLayer employee. Attaching a file to a event is a way to provide supplementary information such as a RFO (reason for outage) document or root cause analysis. The SoftLayer_Notification_Occurrence_Event_Attachment data type models a single file attached to a event. 
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
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The date the file was attached to the event. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#fileName" name=fileName>fileName</a></span>
            <div class='views-field-body'>The name of the file attached to the event. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#fileSize" name=fileSize>fileSize</a></span>
            <div class='views-field-body'>The size of the file, measured in bytes. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A event attachments' unique identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#notificationOccurrenceEventId" name=notificationOccurrenceEventId>notificationOccurrenceEventId</a></span>
            <div class='views-field-body'>The unique event identifier that the file is attached to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#notificationOccurrenceEvent" name=notificationOccurrenceEvent>notificationOccurrenceEvent</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event'>SoftLayer_Notification_Occurrence_Event </a></p></div>
        </div>
            </div>
</div>


