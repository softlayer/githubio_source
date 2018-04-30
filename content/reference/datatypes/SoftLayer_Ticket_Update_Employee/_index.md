---
title: "SoftLayer_Ticket_Update_Employee"
description: "The SoftLayer_Ticket_Update_Employee data type models an update to a ticket made by a SoftLayer employee."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Update_Employee"
---

# SoftLayer_Ticket_Update_Employee
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Ticket_Update_Employee' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Ticket_Update_Employee' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Ticket_Update_Employee data type models an update to a ticket made by a SoftLayer employee. 



### seeAlso

* [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket )


* [SoftLayer_Ticket_Update](/reference/datatypes/SoftLayer_Ticket_Update )


* [SoftLayer_Ticket_Update_Customer](/reference/datatypes/SoftLayer_Ticket_Update_Customer )




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
            <span class='views-field-title'>
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>The data a ticket update was created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#editorId" name=editorId>editorId</a>
            </span>
            <div class='views-field-body'>The internal identifier of the SoftLayer portal or API user who created a ticket update. This is only used if a ticket update's ''editorType'' property is "USER".  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#editorType" name=editorType>editorType</a>
            </span>
            <div class='views-field-body'>The type user who created a ticket update. This is either "USER" for an update created by a SoftLayer portal or API user, "EMPLOYEE" for an update created by a SoftLayer employee, or "AUTO" if a ticket update was generated automatically by SoftLayer's backend systems.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#entry" name=entry>entry</a>
            </span>
            <div class='views-field-body'>The contents of a ticket update. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>A ticket update's internal identifier. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#responseRating" name=responseRating>responseRating</a>
            </span>
            <div class='views-field-body'>A ticket update's response rating. Ticket updates posted by SoftLayer employees have the option of earning a rating from SoftLayer's customers. Ratings are based on a 1 - 5 scale, with one being a poor rating while 5 is a very high rating. This is only used if a ticket update's ''editorType'' property is "EMPLOYEE".  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ticketId" name=ticketId>ticketId</a>
            </span>
            <div class='views-field-body'>The internal identifier of the ticket that a ticket update belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#changeOwnerActivity" name=changeOwnerActivity>changeOwnerActivity</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#editor" name=editor>editor</a>
            </span>
            <div class='views-field-body'>A representation of the SoftLayer employee who created a ticket update. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#fileAttachment" name=fileAttachment>fileAttachment</a>
            </span>
            <div class='views-field-body'>The files attached to a ticket update. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Ticket_Attachment_File'>SoftLayer_Ticket_Attachment_File[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ticket" name=ticket>ticket</a>
            </span>
            <div class='views-field-body'>The ticket that a ticket update belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#type" name=type>type</a>
            </span>
            <div class='views-field-body'>The Type of update to this ticket </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Ticket_Update_Type'>SoftLayer_Ticket_Update_Type </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#fileAttachmentCount" name=fileAttachmentCount>fileAttachmentCount</a>
            </span>
            <div class='views-field-body'>A count of the files attached to a ticket update. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


