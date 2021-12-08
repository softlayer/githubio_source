---
title: "SoftLayer_Product_Upgrade_Request"
description: "The SoftLayer_Product_Upgrade_Request data type contains general information relating to a hardware, virtual server, or... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Upgrade_Request"
---

# SoftLayer_Product_Upgrade_Request
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Product_Upgrade_Request' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Upgrade_Request' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Product_Upgrade_Request data type contains general information relating to a hardware, virtual server, or service upgrade. It also relates a [SoftLayer_Billing_Order]({{<ref "reference/datatypes/SoftLayer_Billing_Order">}}) to a [SoftLayer_Ticket]({{<ref "reference/datatypes/SoftLayer_Ticket">}}). 



### seeAlso

* [SoftLayer_Billing_Order](/reference/services/SoftLayer_Billing_Order )


* [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket )




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
The unique internal id of a SoftLayer account  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date an upgrade request was created.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[employeeId]: #employeeid
#### [employeeId]
The unique internal id of the last modified user  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[guestId]: #guestid
#### [guestId]
The unique internal id of the virtual server that an upgrade will be done  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[hardwareId]: #hardwareid
#### [hardwareId]
The unique internal id of the hardware that an upgrade will be done  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
An upgrade request's internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[maintenanceStartTimeUtc]: #maintenancestarttimeutc
#### [maintenanceStartTimeUtc]
The time that system admin starts working on the order item.  This is used for upgrade orders.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date an upgrade request was last modified.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[orderId]: #orderid
#### [orderId]
The unique internal id of the order that an upgrade request is related to  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[orderTotal]: #ordertotal
#### [orderTotal]
The total amount of fees  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[proratedTotal]: #proratedtotal
#### [proratedTotal]
The prorated total amount of recurring fees  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[statusId]: #statusid
#### [statusId]
The unique internal id of an upgrade status  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[ticketId]: #ticketid
#### [ticketId]
The unique internal id of the ticket related to an upgrade request  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[userId]: #userid
#### [userId]
The unique internal id of the customer who place the order  
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
The account that an order belongs to  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[completedFlag]: #completedflag
#### [completedFlag]
Indicates that the upgrade request has completed or has been cancelled.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[invoice]: #invoice
#### [invoice]
This is the invoice associated with the upgrade request. For hourly servers or services, an invoice will not be available.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a>**  



</div>
<div class="prop-row">

-----
[order]: #order
#### [order]
An order record associated to the upgrade request  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order </a>**  



</div>
<div class="prop-row">

-----
[server]: #server
#### [server]
A server object associated with the upgrade request if any.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**  



</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
The current status of the upgrade request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Upgrade_Request_Status'>SoftLayer_Product_Upgrade_Request_Status </a>**  



</div>
<div class="prop-row">

-----
[ticket]: #ticket
#### [ticket]
The ticket that is used to coordinate the upgrade process.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>**  



</div>
<div class="prop-row">

-----
[user]: #user
#### [user]
The user that placed the order.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>
<div class="prop-row">

-----
[virtualGuest]: #virtualguest
#### [virtualGuest]
A virtual server object associated with the upgrade request if any.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**  



</div>

## Count
</div>


