---
title: "SoftLayer_Ticket_Attachment_File"
description: "SoftLayer tickets can have have files attached to them. Attaching a file to a ticket is a good way to report issues, pro... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Attachment_File"
---

# SoftLayer_Ticket_Attachment_File
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Ticket_Attachment_File' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Ticket_Attachment_File' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer tickets can have have files attached to them. Attaching a file to a ticket is a good way to report issues, provide documentation, and give examples of an issue. Both SoftLayer customers and employees have the ability to attach files to a ticket. The SoftLayer_Ticket_Attachment_File data type models a single file attached to a ticket. 


### associatedMethods

*  [SoftLayer_Ticket::getAttachedFiles](/reference/services/SoftLayer_Ticket/getAttachedFiles )
*  [SoftLayer_Ticket::getAttachedFile](/reference/services/SoftLayer_Ticket/getAttachedFile )



### seeAlso

* [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket )


* [SoftLayer_Ticket_Attachment_Hardware](/reference/datatypes/SoftLayer_Ticket_Attachment_Hardware )




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
            <div class='views-field-body'>The date a file was originally attached to a ticket. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#fileName" name=fileName>fileName</a>
            </span>
            <div class='views-field-body'>The name of a file attached to a ticket. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#fileSize" name=fileSize>fileSize</a>
            </span>
            <div class='views-field-body'>The size of a file attached to a ticket, measured in bytes. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>A ticket file attachment's internal identifier. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>The date that a file attachment record was last modified. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ticketId" name=ticketId>ticketId</a>
            </span>
            <div class='views-field-body'>The internal identifier of the ticket that a file is attached to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#updateId" name=updateId>updateId</a>
            </span>
            <div class='views-field-body'>The internal identifier of the ticket update the attached file is associated with.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#uploaderId" name=uploaderId>uploaderId</a>
            </span>
            <div class='views-field-body'>The internal identifier of the user that uploaded a ticket file attachment. This is only used when A file attachment's ''uploaderType'' is set to "USER".  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#uploaderType" name=uploaderType>uploaderType</a>
            </span>
            <div class='views-field-body'>The type of user that attached a file to a ticket. This is either "USER" if the file was uploaded by a portal or API user or "EMPLOYEE" if the file was uploaded by a SoftLayer employee.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ticket" name=ticket>ticket</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#update" name=update>update</a>
            </span>
            <div class='views-field-body'>The ticket that a file is attached to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Ticket_Update'>SoftLayer_Ticket_Update </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


