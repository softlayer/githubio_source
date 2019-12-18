---
title: "SoftLayer_Billing_Item_Cancellation_Request"
description: "SoftLayer customers can use this API to submit a cancellation request. A single service cancellation can contain multipl... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Cancellation_Request"
---
# SoftLayer_Billing_Item_Cancellation_Request
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Billing_Item_Cancellation_Request' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request' >Datatype</a></li>
    </ul>
</div>

## Description
SoftLayer customers can use this API to submit a cancellation request. A single service cancellation can contain multiple cancellation items which contain a billing item. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [createObject](/reference/services/SoftLayer_Billing_Item_Cancellation_Request/createObject)
Creates a cancellation request.

#### [getAccount](/reference/services/SoftLayer_Billing_Item_Cancellation_Request/getAccount)
Retrieve the SoftLayer account that a service cancellation request belongs to.

#### [getAllCancellationRequests](/reference/services/SoftLayer_Billing_Item_Cancellation_Request/getAllCancellationRequests)
Returns all service cancellation requests

#### [getCancellationCutoffDate](/reference/services/SoftLayer_Billing_Item_Cancellation_Request/getCancellationCutoffDate)
Returns service cancellation cut off date.

#### [getItems](/reference/services/SoftLayer_Billing_Item_Cancellation_Request/getItems)
Retrieve a collection of service cancellation items.

#### [getObject](/reference/services/SoftLayer_Billing_Item_Cancellation_Request/getObject)
Retrieve a SoftLayer_Billing_Item_Cancellation_Request record.

#### [getStatus](/reference/services/SoftLayer_Billing_Item_Cancellation_Request/getStatus)
Retrieve the status of a service cancellation request.

#### [getTicket](/reference/services/SoftLayer_Billing_Item_Cancellation_Request/getTicket)
Retrieve the ticket that is associated with the service cancellation request.

#### [getUser](/reference/services/SoftLayer_Billing_Item_Cancellation_Request/getUser)
Retrieve the user that initiated a service cancellation request.

#### [removeCancellationItem](/reference/services/SoftLayer_Billing_Item_Cancellation_Request/removeCancellationItem)
Removes a cancellation item

#### [validateBillingItemForCancellation](/reference/services/SoftLayer_Billing_Item_Cancellation_Request/validateBillingItemForCancellation)
Examined if a billing item can be canceled or not.

#### [void](/reference/services/SoftLayer_Billing_Item_Cancellation_Request/void)
Voids a pending or approved cancellation request

</div>

