---
title: "SoftLayer_Ticket_Attachment_Scheduled_Action"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Attachment_Scheduled_Action"
---

# SoftLayer_Ticket_Attachment_Scheduled_Action
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Ticket_Attachment_Scheduled_Action' >Datatype</a></li>
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
[runDate]: #rundate
#### [runDate]
The internal identifier of a scheduled action transaction that is attached to a ticket.  
<span class="type-label">Type: </span>**dateTime**

-----
[ticketId]: #ticketid
#### [ticketId]
The internal identifier of the ticket that an item is attached to.  
<span class="type-label">Type: </span>**integer**

-----
[transactionId]: #transactionid
#### [transactionId]
The internal identifier of a scheduled action transaction that is attached to a ticket.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[resource]: #resource
#### [resource]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>**

-----
[scheduledAction]: #scheduledaction
#### [scheduledAction]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>**

-----
[ticket]: #ticket
#### [ticket]
The ticket that an item is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>**

-----
[transaction]: #transaction
#### [transaction]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>**


## Count
</div>


