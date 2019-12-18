---
title: "SoftLayer_Ticket_Attachment_Network_Storage_Mass_Data_Migration"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Attachment_Network_Storage_Mass_Data_Migration"
---

# SoftLayer_Ticket_Attachment_Network_Storage_Mass_Data_Migration
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Ticket_Attachment_Network_Storage_Mass_Data_Migration' >Datatype</a></li>
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
[attachmentId]: #attachmentid
#### [attachmentId]
The internal identifier of an item that is attached to a ticket.  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
The date that an item was attached to a ticket.  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
A ticket attachment's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[requestId]: #requestid
#### [requestId]
  
<span class="type-label">Type: </span>**integer**

-----
[ticketId]: #ticketid
#### [ticketId]
The internal identifier of the ticket that an item is attached to.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[request]: #request
#### [request]
The Mass Data Migration request that is attached to a ticket.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_MassDataMigration_Request'>SoftLayer_Network_Storage_MassDataMigration_Request </a>**

-----
[resource]: #resource
#### [resource]
The Mass Data Migration request that is attached to a ticket.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_MassDataMigration_Request'>SoftLayer_Network_Storage_MassDataMigration_Request </a>**

-----
[ticket]: #ticket
#### [ticket]
The ticket that an item is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>**


## Count
</div>


