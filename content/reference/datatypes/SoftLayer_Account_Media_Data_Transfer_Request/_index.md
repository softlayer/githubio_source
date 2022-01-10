---
title: "SoftLayer_Account_Media_Data_Transfer_Request"
description: "The SoftLayer_Account_Media_Data_Transfer_Request data type contains information on a single Data Transfer Service reque... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Media_Data_Transfer_Request"
---

# SoftLayer_Account_Media_Data_Transfer_Request
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Media_Data_Transfer_Request' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Media_Data_Transfer_Request' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Account_Media_Data_Transfer_Request data type contains information on a single Data Transfer Service request. Creation of these requests is limited to SoftLayer customers through the SoftLayer Customer Portal. 





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
The account id of the request.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[createUserId]: #createuserid
#### [createUserId]
The create user id of the request.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[endDate]: #enddate
#### [endDate]
The end date of the request.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique id of the request.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyUserId]: #modifyuserid
#### [modifyUserId]
The modify user id of the request.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[startDate]: #startdate
#### [startDate]
The start date of the request.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[statusId]: #statusid
#### [statusId]
The status id of the request.  
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
The account to which the request belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[activeTickets]: #activetickets
#### [activeTickets]
The active tickets that are attached to the data transfer request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**  



</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for the original request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**  



</div>
<div class="prop-row">

-----
[createUser]: #createuser
#### [createUser]
The customer user who created the request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>
<div class="prop-row">

-----
[media]: #media
#### [media]
The media of the request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Media'>SoftLayer_Account_Media </a>**  



</div>
<div class="prop-row">

-----
[modifyEmployee]: #modifyemployee
#### [modifyEmployee]
The employee who last modified the request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**  



</div>
<div class="prop-row">

-----
[modifyUser]: #modifyuser
#### [modifyUser]
The customer user who last modified the request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>
<div class="prop-row">

-----
[shipments]: #shipments
#### [shipments]
The shipments of the request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Shipment'>SoftLayer_Account_Shipment[] </a>**  



</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
The status of the request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Media_Data_Transfer_Request_Status'>SoftLayer_Account_Media_Data_Transfer_Request_Status </a>**  



</div>
<div class="prop-row">

-----
[tickets]: #tickets
#### [tickets]
All tickets that are attached to the data transfer request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[activeTicketCount]: #activeticketcount
#### [activeTicketCount]
A count of the active tickets that are attached to the data transfer request.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[shipmentCount]: #shipmentcount
#### [shipmentCount]
A count of the shipments of the request.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[ticketCount]: #ticketcount
#### [ticketCount]
A count of all tickets that are attached to the data transfer request.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


