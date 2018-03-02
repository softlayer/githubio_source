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

* [SoftLayer_Ticket](/reference/datatypes/SoftLayer_Ticket )


* [SoftLayer_Ticket_Attachment_File](/reference/datatypes/SoftLayer_Ticket_Attachment_File )


* [SoftLayer_Ticket_Attachment_Virtual_Guest](/reference/datatypes/SoftLayer_Ticket_Attachment_Virtual_Guest )




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
            <span class='views-field-title'><a href="#attachmentId" name=attachmentId>attachmentId</a></span>
            <div class='views-field-body'>The internal identifier of an item that is attached to a ticket. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The date that an item was attached to a ticket. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#dedicatedHostId" name=dedicatedHostId>dedicatedHostId</a></span>
            <div class='views-field-body'>The internal identifier of the Dedicated Host that is attached to a ticket. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A ticket attachment's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ticketId" name=ticketId>ticketId</a></span>
            <div class='views-field-body'>The internal identifier of the ticket that an item is attached to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#dedicatedHost" name=dedicatedHost>dedicatedHost</a></span>
            <div class='views-field-body'>The dedicated dost that is attached to a ticket. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_DedicatedHost'>SoftLayer_Virtual_DedicatedHost </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#resource" name=resource>resource</a></span>
            <div class='views-field-body'>The Dedicated Host that is attached to a ticket. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_DedicatedHost'>SoftLayer_Virtual_DedicatedHost </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ticket" name=ticket>ticket</a></span>
            <div class='views-field-body'>The ticket that an item is attached to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


