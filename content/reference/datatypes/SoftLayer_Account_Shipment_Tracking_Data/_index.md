---
title: "SoftLayer_Account_Shipment_Tracking_Data"
description: "The SoftLayer_Account_Shipment_Tracking_Data data type contains information on a single piece of tracking information pe... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Shipment_Tracking_Data"
---

# SoftLayer_Account_Shipment_Tracking_Data
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Shipment_Tracking_Data' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Shipment_Tracking_Data' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Account_Shipment_Tracking_Data data type contains information on a single piece of tracking information pertaining to a shipment. This tracking information tracking numbers by which the shipment may be tracked through the shipping courier. 





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
[createUserId]: #createuserid
#### [createUserId]
The create user id of the tracking data.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
The unique id of the tracking data.  
<span class="type-label">Type: </span>**integer**

-----
[modifyUserId]: #modifyuserid
#### [modifyUserId]
The user id of the tracking data.  
<span class="type-label">Type: </span>**integer**

-----
[packageId]: #packageid
#### [packageId]
The package id of the tracking data.  
<span class="type-label">Type: </span>**integer**

-----
[sequence]: #sequence
#### [sequence]
The sequence of the tracking data.  
<span class="type-label">Type: </span>**integer**

-----
[shipmentId]: #shipmentid
#### [shipmentId]
The shipment id of the tracking data.  
<span class="type-label">Type: </span>**integer**

-----
[trackingData]: #trackingdata
#### [trackingData]
The tracking data (tracking number/reference number).  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[createEmployee]: #createemployee
#### [createEmployee]
The employee who created the tracking datum.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**

-----
[createUser]: #createuser
#### [createUser]
The customer user who created the tracking datum.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**

-----
[modifyEmployee]: #modifyemployee
#### [modifyEmployee]
The employee who last modified the tracking datum.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**

-----
[modifyUser]: #modifyuser
#### [modifyUser]
The customer user who last modified the tracking datum.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**

-----
[shipment]: #shipment
#### [shipment]
The shipment of the tracking datum.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Shipment'>SoftLayer_Account_Shipment </a>**


## Count
</div>


