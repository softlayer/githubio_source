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
    <li id='service'> <a href='/reference/services/SoftLayer_Billing_Item_Cancellation_Request' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request' >Datatype</a></li>
    </ul>
</div>

## Description 


SoftLayer_Billing_Item_Cancellation_Request data type is used to cancel service billing items. 





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
[accountId]: #accountid
#### [accountId]
The internal identifier of the customer account that a service cancellation record belongs to.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[billingCancelReasonId]: #billingcancelreasonid
#### [billingCancelReasonId]
The last modified date.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date that a cancellation request was created.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A cancellation record's internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The last modified date.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
Brief cancellation note.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[statusId]: #statusid
#### [statusId]
An internal identifier of the service cancellation status that this request is associated with. When a service cancellation is submitted, it will be in "Pending" status until SoftLayer Sales team reviews it. The status of a cancellation request will be updated to "Approved" or "Voided" by SoftLayer Sales. 

It will be updated to "Complete" when all services are reclaimed.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[ticketId]: #ticketid
#### [ticketId]
An internal identifier of the ticket that is associated with a service cancellation request. When a service cancellation is submitted, a support ticket will be created. This ticket contains details on your service cancellation details and SoftLayer Sales team will use it to further communicate with you.   
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The SoftLayer account that a service cancellation request belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[items]: #items
#### [items]
A collection of service cancellation items.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request_Item'>SoftLayer_Billing_Item_Cancellation_Request_Item[] </a>**  



</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
The status of a service cancellation request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request_Status'>SoftLayer_Billing_Item_Cancellation_Request_Status </a>**  



</div>
<div class="prop-row">

-----
[ticket]: #ticket
#### [ticket]
The ticket that is associated with the service cancellation request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>**  



</div>
<div class="prop-row">

-----
[user]: #user
#### [user]
The user that initiated a service cancellation request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>

## Count
<div class="prop-row">

-----
[itemCount]: #itemcount
#### [itemCount]
A count of a collection of service cancellation items.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


