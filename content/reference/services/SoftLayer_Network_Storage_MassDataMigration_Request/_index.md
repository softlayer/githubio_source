---
title: "SoftLayer_Network_Storage_MassDataMigration_Request"
description: "Mass Data Migration Request Service allows users to request Massive storage device to copy onsite data. Once user has co... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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
Mass Data Migration Request Service allows users to request Massive storage device to copy onsite data. Once user has copied their data onto device, they ship it back to SoftLayer where device is connected to network and data is transferred to Object Storage bucket. Currently, the initial usage period is two weeks . Additional time for maintaining the media for continued may be purchased. Please contact sales for additional information regarding this. Once the usage period has elapsed. SoftLayer will disconnect the device. 



        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit a Mass Data Migration request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the account to which the request belongs.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getActiveTickets'> getActiveTickets</a> </span>
            <div class='views-field-body'>Retrieve the active tickets that are attached to the MDMS request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getAddress'> getAddress</a> </span>
            <div class='views-field-body'>Retrieve the customer address where the device is shipped to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getAllObjects'> getAllObjects</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getAllRequestStatuses'> getAllRequestStatuses</a> </span>
            <div class='views-field-body'>Retrieves a list of all the possible statuses</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getBillingItem'> getBillingItem</a> </span>
            <div class='views-field-body'>Retrieve an associated parent billing item which is active. Includes billing items which are scheduled to be cancelled in the future.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getCreateEmployee'> getCreateEmployee</a> </span>
            <div class='views-field-body'>Retrieve the employee user who created the request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getCreateUser'> getCreateUser</a> </span>
            <div class='views-field-body'>Retrieve the customer user who created the request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getDeviceConfiguration'> getDeviceConfiguration</a> </span>
            <div class='views-field-body'>Retrieve the device configurations.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getKeyContacts'> getKeyContacts</a> </span>
            <div class='views-field-body'>Retrieve the key contacts for this requests.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getModifyEmployee'> getModifyEmployee</a> </span>
            <div class='views-field-body'>Retrieve the employee who last modified the request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getModifyUser'> getModifyUser</a> </span>
            <div class='views-field-body'>Retrieve the customer user who last modified the request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_Storage_MassDataMigration_Request record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getPendingRequests'> getPendingRequests</a> </span>
            <div class='views-field-body'>Returns placeholder MDMS requests for any MDMS order pending approval.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getShipments'> getShipments</a> </span>
            <div class='views-field-body'>Retrieve the shipments of the request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getStatus'> getStatus</a> </span>
            <div class='views-field-body'>Retrieve the status of the request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getTicket'> getTicket</a> </span>
            <div class='views-field-body'>Retrieve ticket that is attached to this mass data migration request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getTickets'> getTickets</a> </span>
            <div class='views-field-body'>Retrieve all tickets that are attached to the mass data migration request.</div>
        </div>
        </div>
</div>

