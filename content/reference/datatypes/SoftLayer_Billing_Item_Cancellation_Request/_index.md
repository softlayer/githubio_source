---
title: "SoftLayer_Billing_Item_Cancellation_Request"
description: "SoftLayer_Billing_Item_Cancellation_Request data type is used to cancel service billing items."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Cancellation_Request"
---

# SoftLayer_Billing_Item_Cancellation_Request
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Billing_Item_Cancellation_Request data type is used to cancel service billing items. 





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
            <span class='views-field-title'><a href="#accountId" name=accountId>accountId</a></span>
            <div class='views-field-body'>The internal identifier of the customer account that a service cancellation record belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingCancelReasonId" name=billingCancelReasonId>billingCancelReasonId</a></span>
            <div class='views-field-body'>The last modified date. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The date that a cancellation request was created. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A cancellation record's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>The last modified date. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#notes" name=notes>notes</a></span>
            <div class='views-field-body'>Brief cancellation note.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#statusId" name=statusId>statusId</a></span>
            <div class='views-field-body'>An internal identifier of the service cancellation status that this request is associated with. When a service cancellation is submitted, it will be in "Pending" status until SoftLayer Sales team reviews it. The status of a cancellation request will be updated to "Approved" or "Voided" by SoftLayer Sales. 

It will be updated to "Complete" when all services are reclaimed.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ticketId" name=ticketId>ticketId</a></span>
            <div class='views-field-body'>An internal identifier of the ticket that is associated with a service cancellation request. When a service cancellation is submitted, a support ticket will be created. This ticket contains details on your service cancellation details and SoftLayer Sales team will use it to further communicate with you.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>The SoftLayer account that a service cancellation request belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#items" name=items>items</a></span>
            <div class='views-field-body'>A collection of service cancellation items. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request_Item'>SoftLayer_Billing_Item_Cancellation_Request_Item[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#status" name=status>status</a></span>
            <div class='views-field-body'>The status of a service cancellation request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request_Status'>SoftLayer_Billing_Item_Cancellation_Request_Status </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ticket" name=ticket>ticket</a></span>
            <div class='views-field-body'>The ticket that is associated with the service cancellation request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#user" name=user>user</a></span>
            <div class='views-field-body'>The user that initiated a service cancellation request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemCount" name=itemCount>itemCount</a></span>
            <div class='views-field-body'>A count of a collection of service cancellation items. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


