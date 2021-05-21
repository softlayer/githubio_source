---
title: "SoftLayer_Ticket_Attachment"
description: "SoftLayer tickets have the ability to be associated with specific pieces of hardware in a customer's inventory. Attachin... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Attachment"
---

# SoftLayer_Ticket_Attachment
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Ticket_Attachment' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer tickets have the ability to be associated with specific pieces of hardware in a customer's inventory. Attaching hardware to a ticket can greatly increase response time from SoftLayer for issues that are related to one or more specific servers on a customer's account. The SoftLayer_Ticket_Attachment_Hardware data type models the relationship between a piece of hardware and a ticket. Only one attachment record may exist per hardware item per ticket. 



### seeAlso

* [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket )


* [SoftLayer_Ticket_Attachment_Hardware](/reference/datatypes/SoftLayer_Ticket_Attachment_Hardware )


* [SoftLayer_Ticket_Attachment_Virtual_Guest](/reference/datatypes/SoftLayer_Ticket_Attachment_Virtual_Guest )


* [SoftLayer_Ticket_Attachment_File](/reference/services/SoftLayer_Ticket_Attachment_File )




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
[ticket]: #ticket
#### [ticket]
The ticket that an item is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>**


</div>

## Count
</div>


