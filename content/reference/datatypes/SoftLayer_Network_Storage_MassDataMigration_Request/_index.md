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
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_MassDataMigration_Request' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Storage_MassDataMigration_Request data type contains information on a single Mass Data Migration request. Creation of these requests is limited to SoftLayer customers through the SoftLayer Customer Portal. 





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
            <div class='views-field-body'>The account id of the request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#addressId" name=addressId>addressId</a></span>
            <div class='views-field-body'>The address id of address assigned to this request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createUserId" name=createUserId>createUserId</a></span>
            <div class='views-field-body'>The create user id of the request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#endDate" name=endDate>endDate</a></span>
            <div class='views-field-body'>The end date of the request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The unique id of the request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyUserId" name=modifyUserId>modifyUserId</a></span>
            <div class='views-field-body'>The modify user id of the request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>The unique id of the request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#startDate" name=startDate>startDate</a></span>
            <div class='views-field-body'>The start date of the request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#statusId" name=statusId>statusId</a></span>
            <div class='views-field-body'>The status id of the request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>The account to which the request belongs. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#activeTickets" name=activeTickets>activeTickets</a></span>
            <div class='views-field-body'>The active tickets that are attached to the MDMS request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#address" name=address>address</a></span>
            <div class='views-field-body'>The customer address where the device is shipped to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account_Address'>SoftLayer_Account_Address </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingItem" name=billingItem>billingItem</a></span>
            <div class='views-field-body'>An associated parent billing item which is active. Includes billing items which are scheduled to be cancelled in the future. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createEmployee" name=createEmployee>createEmployee</a></span>
            <div class='views-field-body'>The employee user who created the request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createUser" name=createUser>createUser</a></span>
            <div class='views-field-body'>The customer user who created the request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#deviceConfiguration" name=deviceConfiguration>deviceConfiguration</a></span>
            <div class='views-field-body'>The device configurations. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Storage_MassDataMigration_Request_DeviceConfiguration'>SoftLayer_Network_Storage_MassDataMigration_Request_DeviceConfiguration </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#keyContacts" name=keyContacts>keyContacts</a></span>
            <div class='views-field-body'>The key contacts for this requests. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Storage_MassDataMigration_Request_KeyContact'>SoftLayer_Network_Storage_MassDataMigration_Request_KeyContact[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyEmployee" name=modifyEmployee>modifyEmployee</a></span>
            <div class='views-field-body'>The employee who last modified the request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyUser" name=modifyUser>modifyUser</a></span>
            <div class='views-field-body'>The customer user who last modified the request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#shipments" name=shipments>shipments</a></span>
            <div class='views-field-body'>The shipments of the request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account_Shipment'>SoftLayer_Account_Shipment[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#status" name=status>status</a></span>
            <div class='views-field-body'>The status of the request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Storage_MassDataMigration_Request_Status'>SoftLayer_Network_Storage_MassDataMigration_Request_Status </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#tickets" name=tickets>tickets</a></span>
            <div class='views-field-body'>All tickets that are attached to the mass data migration request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#activeTicketCount" name=activeTicketCount>activeTicketCount</a></span>
            <div class='views-field-body'>A count of the active tickets that are attached to the MDMS request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#keyContactCount" name=keyContactCount>keyContactCount</a></span>
            <div class='views-field-body'>A count of the key contacts for this requests. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#shipmentCount" name=shipmentCount>shipmentCount</a></span>
            <div class='views-field-body'>A count of the shipments of the request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ticketCount" name=ticketCount>ticketCount</a></span>
            <div class='views-field-body'>A count of all tickets that are attached to the mass data migration request. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


