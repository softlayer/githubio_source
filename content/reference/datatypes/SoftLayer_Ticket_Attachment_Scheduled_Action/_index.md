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
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A ticket attachment's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#runDate" name=runDate>runDate</a></span>
            <div class='views-field-body'>The internal identifier of a scheduled action transaction that is attached to a ticket. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ticketId" name=ticketId>ticketId</a></span>
            <div class='views-field-body'>The internal identifier of the ticket that an item is attached to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#transactionId" name=transactionId>transactionId</a></span>
            <div class='views-field-body'>The internal identifier of a scheduled action transaction that is attached to a ticket. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#resource" name=resource>resource</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#scheduledAction" name=scheduledAction>scheduledAction</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ticket" name=ticket>ticket</a></span>
            <div class='views-field-body'>The ticket that an item is attached to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#transaction" name=transaction>transaction</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


