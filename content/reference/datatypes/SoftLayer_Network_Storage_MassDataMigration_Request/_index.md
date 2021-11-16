---
title: "SoftLayer_Network_Storage_MassDataMigration_Request"
description: "The SoftLayer_Network_Storage_MassDataMigration_Request data type contains information on a single Mass Data Migration r... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_MassDataMigration_Request"
---

# SoftLayer_Network_Storage_MassDataMigration_Request
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_MassDataMigration_Request' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Network_Storage_MassDataMigration_Request data type contains information on a single Mass Data Migration request. Creation of these requests is limited to SoftLayer customers through the SoftLayer Customer Portal. 





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
[addressId]: #addressid
#### [addressId]
The address id of address assigned to this request.  
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
[name]: #name
#### [name]
The unique id of the request.  
<span class="type-label">Type: </span>**string**  



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
The active tickets that are attached to the MDMS request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**  



</div>
<div class="prop-row">

-----
[address]: #address
#### [address]
The customer address where the device is shipped to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Address'>SoftLayer_Account_Address </a>**  



</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
An associated parent billing item which is active. Includes billing items which are scheduled to be cancelled in the future.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**  



</div>
<div class="prop-row">

-----
[createEmployee]: #createemployee
#### [createEmployee]
The employee user who created the request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**  



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
[deviceConfiguration]: #deviceconfiguration
#### [deviceConfiguration]
The device configurations.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_MassDataMigration_Request_DeviceConfiguration'>SoftLayer_Network_Storage_MassDataMigration_Request_DeviceConfiguration </a>**  



</div>
<div class="prop-row">

-----
[deviceModel]: #devicemodel
#### [deviceModel]
The model of device assigned to this request.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[keyContacts]: #keycontacts
#### [keyContacts]
The key contacts for this requests.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_MassDataMigration_Request_KeyContact'>SoftLayer_Network_Storage_MassDataMigration_Request_KeyContact[] </a>**  



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
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_MassDataMigration_Request_Status'>SoftLayer_Network_Storage_MassDataMigration_Request_Status </a>**  



</div>
<div class="prop-row">

-----
[ticket]: #ticket
#### [ticket]
Ticket that is attached to this mass data migration request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>**  



</div>
<div class="prop-row">

-----
[tickets]: #tickets
#### [tickets]
All tickets that are attached to the mass data migration request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[activeTicketCount]: #activeticketcount
#### [activeTicketCount]
A count of the active tickets that are attached to the MDMS request.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[keyContactCount]: #keycontactcount
#### [keyContactCount]
A count of the key contacts for this requests.   
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
A count of all tickets that are attached to the mass data migration request.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


