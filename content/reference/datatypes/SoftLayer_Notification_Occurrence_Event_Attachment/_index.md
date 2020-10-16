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


### associatedMethods

*  [SoftLayer_Notification_Occurrence_Event::getAttachedFile](/reference/services/SoftLayer_Notification_Occurrence_Event/getAttachedFile )



### seeAlso

* [SoftLayer_Notification_Occurrence_Event](/reference/datatypes/SoftLayer_Notification_Occurrence_Event )




<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date the file was attached to the event.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[fileName]: #filename
#### [fileName]
The name of the file attached to the event.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[fileSize]: #filesize
#### [fileSize]
The size of the file, measured in bytes.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A event attachments' unique identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[notificationOccurrenceEventId]: #notificationoccurrenceeventid
#### [notificationOccurrenceEventId]
The unique event identifier that the file is attached to.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[notificationOccurrenceEvent]: #notificationoccurrenceevent
#### [notificationOccurrenceEvent]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event'>SoftLayer_Notification_Occurrence_Event </a>**


</div>

## Count
</div>


