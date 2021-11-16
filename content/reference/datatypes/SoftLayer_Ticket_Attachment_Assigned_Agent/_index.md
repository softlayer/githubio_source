---
title: "SoftLayer_Ticket_Attachment_Assigned_Agent"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Attachment_Assigned_Agent"
---

# SoftLayer_Ticket_Attachment_Assigned_Agent
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Ticket_Attachment_Assigned_Agent' >Datatype</a></li>
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
[assignedAgentId]: #assignedagentid
#### [assignedAgentId]
The internal identifier of an assigned Agent that is attached to a ticket.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[attachmentId]: #attachmentid
#### [attachmentId]
The internal identifier of an item that is attached to a ticket.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date that an item was attached to a ticket.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A ticket attachment's internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[ticketId]: #ticketid
#### [ticketId]
The internal identifier of the ticket that an item is attached to.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[assignedAgent]: #assignedagent
#### [assignedAgent]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>
<div class="prop-row">

-----
[resource]: #resource
#### [resource]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>
<div class="prop-row">

-----
[ticket]: #ticket
#### [ticket]
The ticket that an item is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>**  



</div>

## Count
</div>


