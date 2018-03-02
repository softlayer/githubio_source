---
title: "SoftLayer_Billing_Item_Cancellation_Request_Item"
description: "SoftLayer_Billing_Item_Cancellation_Request_Item data type contains a billing item for cancellation. This data type is u... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Cancellation_Request_Item"
---

# SoftLayer_Billing_Item_Cancellation_Request_Item
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request_Item' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Billing_Item_Cancellation_Request_Item data type contains a billing item for cancellation. This data type is used to harness billing items to the associated service. 





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
            <span class='views-field-title'><a href="#billingItemId" name=billingItemId>billingItemId</a></span>
            <div class='views-field-body'>The internal identifier of a billing item </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cancellationRequestId" name=cancellationRequestId>cancellationRequestId</a></span>
            <div class='views-field-body'>A cancellation request's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A cancellation request item's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#immediateCancellationFlag" name=immediateCancellationFlag>immediateCancellationFlag</a></span>
            <div class='views-field-body'>This flag indicated if a billing item should be canceled immediately or not.  Set this flag to true when creating a cancellation request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#scheduledCancellationDate" name=scheduledCancellationDate>scheduledCancellationDate</a></span>
            <div class='views-field-body'>The scheduled cancellation date </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serviceReclaimStatusCode" name=serviceReclaimStatusCode>serviceReclaimStatusCode</a></span>
            <div class='views-field-body'>The reclaim status of a service. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingItem" name=billingItem>billingItem</a></span>
            <div class='views-field-body'>The billing item for cancellation. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cancellationRequest" name=cancellationRequest>cancellationRequest</a></span>
            <div class='views-field-body'>The service cancellation request that a cancellation item belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request'>SoftLayer_Billing_Item_Cancellation_Request </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


