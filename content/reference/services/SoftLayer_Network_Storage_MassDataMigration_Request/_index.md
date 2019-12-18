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

#### [getAccount](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getAccount)
Retrieve the account to which the request belongs.

#### [getActiveTickets](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getActiveTickets)
Retrieve the active tickets that are attached to the MDMS request.

#### [getAddress](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getAddress)
Retrieve the customer address where the device is shipped to.

#### [getAllObjects](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getAllObjects)


#### [getAllRequestStatuses](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getAllRequestStatuses)
Retrieves a list of all the possible statuses

#### [getBillingItem](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getBillingItem)
Retrieve an associated parent billing item which is active. Includes billing items which are scheduled to be cancelled in the future.

#### [getCreateEmployee](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getCreateEmployee)
Retrieve the employee user who created the request.

#### [getCreateUser](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getCreateUser)
Retrieve the customer user who created the request.

#### [getDeviceConfiguration](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getDeviceConfiguration)
Retrieve the device configurations.

#### [getDeviceModel](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getDeviceModel)
Retrieve the model of device assigned to this request.

#### [getKeyContacts](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getKeyContacts)
Retrieve the key contacts for this requests.

#### [getModifyEmployee](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getModifyEmployee)
Retrieve the employee who last modified the request.

#### [getModifyUser](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getModifyUser)
Retrieve the customer user who last modified the request.

#### [getObject](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getObject)
Retrieve a SoftLayer_Network_Storage_MassDataMigration_Request record.

#### [getPendingRequests](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getPendingRequests)
Returns placeholder MDMS requests for any MDMS order pending approval.

#### [getShipments](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getShipments)
Retrieve the shipments of the request.

#### [getStatus](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getStatus)
Retrieve the status of the request.

#### [getTicket](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getTicket)
Retrieve ticket that is attached to this mass data migration request.

#### [getTickets](/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request/getTickets)
Retrieve all tickets that are attached to the mass data migration request.

</div>

