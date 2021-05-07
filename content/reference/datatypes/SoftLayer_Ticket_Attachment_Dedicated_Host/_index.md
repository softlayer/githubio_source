---
title: "SoftLayer_Ticket_Attachment_Dedicated_Host"
description: "SoftLayer tickets have the ability to be associated with specific dedicated hosts in a customer's inventory. Attaching a... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Attachment_Dedicated_Host"
---

# SoftLayer_Ticket_Attachment_Dedicated_Host
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Ticket_Attachment_Dedicated_Host' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer tickets have the ability to be associated with specific dedicated hosts in a customer's inventory. Attaching a dedicated host to a ticket can greatly increase response time from SoftLayer for issues that are related to one or more specific hosts on a customer's account. The SoftLayer_Ticket_Attachment_Dedicated_Host data type models the relationship between a dedicated host and a ticket. Only one attachment record can exist per dedicated host item per ticket. 


### associatedMethods

*  [SoftLayer_Ticket::getAttachedDedicatedHosts](/reference/services/SoftLayer_Ticket/getAttachedDedicatedHosts )
*  [SoftLayer_Ticket::addAttachedDedicatedHost](/reference/services/SoftLayer_Ticket/addAttachedDedicatedHost )
*  [SoftLayer_Ticket::removeAttachedDedicatedHost](/reference/services/SoftLayer_Ticket/removeAttachedDedicatedHost )



### seeAlso

* [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket )


* [SoftLayer_Ticket_Attachment_File](/reference/datatypes/SoftLayer_Ticket_Attachment_File )


* [SoftLayer_Ticket_Attachment_Virtual_Guest](/reference/datatypes/SoftLayer_Ticket_Attachment_Virtual_Guest )




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
[dedicatedHostId]: #dedicatedhostid
#### [dedicatedHostId]
The internal identifier of the Dedicated Host that is attached to a ticket.  
<span class="type-label">Type: </span>**integer**


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
[dedicatedHost]: #dedicatedhost
#### [dedicatedHost]
The dedicated dost that is attached to a ticket.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_DedicatedHost'>SoftLayer_Virtual_DedicatedHost </a>**


</div>
<div class="prop-row">

-----
[resource]: #resource
#### [resource]
The Dedicated Host that is attached to a ticket.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_DedicatedHost'>SoftLayer_Virtual_DedicatedHost </a>**


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


