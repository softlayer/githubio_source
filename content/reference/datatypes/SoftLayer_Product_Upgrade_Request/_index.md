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

## Local
-----
[accountId]: #accountid
#### [accountId]
The unique internal id of a SoftLayer account  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
The date an upgrade request was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[employeeId]: #employeeid
#### [employeeId]
The unique internal id of the last modified user  
<span class="type-label">Type: </span>**integer**

-----
[guestId]: #guestid
#### [guestId]
The unique internal id of the virtual server that an upgrade will be done  
<span class="type-label">Type: </span>**integer**

-----
[hardwareId]: #hardwareid
#### [hardwareId]
The unique internal id of the hardware that an upgrade will be done  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
An upgrade request's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[maintenanceStartTimeUtc]: #maintenancestarttimeutc
#### [maintenanceStartTimeUtc]
The time that system admin starts working on the order item.  This is used for upgrade orders.  
<span class="type-label">Type: </span>**dateTime**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date an upgrade request was last modified.  
<span class="type-label">Type: </span>**dateTime**

-----
[orderId]: #orderid
#### [orderId]
The unique internal id of the order that an upgrade request is related to  
<span class="type-label">Type: </span>**integer**

-----
[orderTotal]: #ordertotal
#### [orderTotal]
The total amount of fees  
<span class="type-label">Type: </span>**decimal**

-----
[proratedTotal]: #proratedtotal
#### [proratedTotal]
The prorated total amount of recurring fees  
<span class="type-label">Type: </span>**decimal**

-----
[statusId]: #statusid
#### [statusId]
The unique internal id of an upgrade status  
<span class="type-label">Type: </span>**integer**

-----
[ticketId]: #ticketid
#### [ticketId]
The unique internal id of the ticket related to an upgrade request  
<span class="type-label">Type: </span>**integer**

-----
[userId]: #userid
#### [userId]
The unique internal id of the customer who place the order  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account that an order belongs to  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[completedFlag]: #completedflag
#### [completedFlag]
Indicates that the upgrade request has completed or has been cancelled.  
<span class="type-label">Type: </span>**boolean**

-----
[invoice]: #invoice
#### [invoice]
This is the invoice associated with the upgrade request. For hourly servers or services, an invoice will not be available.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a>**

-----
[order]: #order
#### [order]
An order record associated to the upgrade request  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order </a>**

-----
[server]: #server
#### [server]
A server object associated with the upgrade request if any.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**

-----
[status]: #status
#### [status]
The current status of the upgrade request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Upgrade_Request_Status'>SoftLayer_Product_Upgrade_Request_Status </a>**

-----
[ticket]: #ticket
#### [ticket]
The ticket that is used to coordinate the upgrade process.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>**

-----
[user]: #user
#### [user]
The user that placed the order.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**

-----
[virtualGuest]: #virtualguest
#### [virtualGuest]
A virtual server object associated with the upgrade request if any.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**


## Count
</div>


