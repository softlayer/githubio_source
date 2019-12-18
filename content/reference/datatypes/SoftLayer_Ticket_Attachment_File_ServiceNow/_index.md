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
[createDate]: #createdate
#### [createDate]
The date a file was originally attached to a ticket.  
<span class="type-label">Type: </span>**dateTime**

-----
[fileName]: #filename
#### [fileName]
The name of a file attached to a ticket.  
<span class="type-label">Type: </span>**string**

-----
[fileSize]: #filesize
#### [fileSize]
The size of a file attached to a ticket, measured in bytes.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
A ticket file attachment's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date that a file attachment record was last modified.  
<span class="type-label">Type: </span>**dateTime**

-----
[ticketId]: #ticketid
#### [ticketId]
The internal identifier of the ticket that a file is attached to.  
<span class="type-label">Type: </span>**integer**

-----
[updateId]: #updateid
#### [updateId]
The internal identifier of the ticket update the attached file is associated with.   
<span class="type-label">Type: </span>**integer**

-----
[uploaderId]: #uploaderid
#### [uploaderId]
The internal identifier of the user that uploaded a ticket file attachment. This is only used when A file attachment's ''uploaderType'' is set to "USER".   
<span class="type-label">Type: </span>**string**

-----
[uploaderType]: #uploadertype
#### [uploaderType]
The type of user that attached a file to a ticket. This is either "USER" if the file was uploaded by a portal or API user or "EMPLOYEE" if the file was uploaded by a SoftLayer employee.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[ticket]: #ticket
#### [ticket]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>**

-----
[update]: #update
#### [update]
The ticket that a file is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket_Update'>SoftLayer_Ticket_Update </a>**


## Count
</div>


