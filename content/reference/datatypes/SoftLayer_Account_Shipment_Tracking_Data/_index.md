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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createUserId" name=createUserId>createUserId</a>
            </span>
            <div class='views-field-body'>The create user id of the tracking data. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The unique id of the tracking data. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyUserId" name=modifyUserId>modifyUserId</a>
            </span>
            <div class='views-field-body'>The user id of the tracking data. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#packageId" name=packageId>packageId</a>
            </span>
            <div class='views-field-body'>The package id of the tracking data. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#sequence" name=sequence>sequence</a>
            </span>
            <div class='views-field-body'>The sequence of the tracking data. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#shipmentId" name=shipmentId>shipmentId</a>
            </span>
            <div class='views-field-body'>The shipment id of the tracking data. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#trackingData" name=trackingData>trackingData</a>
            </span>
            <div class='views-field-body'>The tracking data (tracking number/reference number). </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createEmployee" name=createEmployee>createEmployee</a>
            </span>
            <div class='views-field-body'>The employee who created the tracking datum. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createUser" name=createUser>createUser</a>
            </span>
            <div class='views-field-body'>The customer user who created the tracking datum. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyEmployee" name=modifyEmployee>modifyEmployee</a>
            </span>
            <div class='views-field-body'>The employee who last modified the tracking datum. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyUser" name=modifyUser>modifyUser</a>
            </span>
            <div class='views-field-body'>The customer user who last modified the tracking datum. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#shipment" name=shipment>shipment</a>
            </span>
            <div class='views-field-body'>The shipment of the tracking datum. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account_Shipment'>SoftLayer_Account_Shipment </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


