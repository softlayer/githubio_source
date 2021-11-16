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
[billingItemId]: #billingitemid
#### [billingItemId]
The internal identifier of a billing item  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[cancellationRequestId]: #cancellationrequestid
#### [cancellationRequestId]
A cancellation request's internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A cancellation request item's internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[immediateCancellationFlag]: #immediatecancellationflag
#### [immediateCancellationFlag]
This flag indicated if a billing item should be canceled immediately or not.  Set this flag to true when creating a cancellation request.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[scheduledCancellationDate]: #scheduledcancellationdate
#### [scheduledCancellationDate]
The scheduled cancellation date  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[serviceReclaimStatusCode]: #servicereclaimstatuscode
#### [serviceReclaimStatusCode]
The reclaim status of a service.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for cancellation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**  



</div>
<div class="prop-row">

-----
[cancellationRequest]: #cancellationrequest
#### [cancellationRequest]
The service cancellation request that a cancellation item belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request'>SoftLayer_Billing_Item_Cancellation_Request </a>**  



</div>

## Count
</div>


