---
title: "SoftLayer_Ticket_Attachment_File_ServiceNow"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Attachment_File_ServiceNow"
---

# SoftLayer_Ticket_Attachment_File_ServiceNow
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Ticket_Attachment_File_ServiceNow' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Ticket_Attachment_File_ServiceNow' >Datatype</a></li>
    </ul>
</div>

## Description 








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
The date a file was originally attached to a ticket.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[fileName]: #filename
#### [fileName]
The name of a file attached to a ticket.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[fileSize]: #filesize
#### [fileSize]
The size of a file attached to a ticket, measured in bytes.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A ticket file attachment's internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date that a file attachment record was last modified.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[ticketId]: #ticketid
#### [ticketId]
The internal identifier of the ticket that a file is attached to.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[updateId]: #updateid
#### [updateId]
The internal identifier of the ticket update the attached file is associated with.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[uploaderId]: #uploaderid
#### [uploaderId]
The internal identifier of the user that uploaded a ticket file attachment. This is only used when A file attachment's ''uploaderType'' is set to "USER".   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[uploaderType]: #uploadertype
#### [uploaderType]
The type of user that attached a file to a ticket. This is either "USER" if the file was uploaded by a portal or API user or "EMPLOYEE" if the file was uploaded by a SoftLayer employee.   
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[ticket]: #ticket
#### [ticket]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>**  



</div>
<div class="prop-row">

-----
[update]: #update
#### [update]
The ticket that a file is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Update'>SoftLayer_Ticket_Update </a>**  



</div>

## Count
</div>


