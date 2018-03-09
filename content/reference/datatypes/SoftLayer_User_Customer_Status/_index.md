---
title: "SoftLayer_User_Customer_Status"
description: "Each SoftLayer portal account is assigned a status code that determines how it's treated in the customer portal. This st... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Status"
---

# SoftLayer_User_Customer_Status
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Customer_Status' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_Status' >Datatype</a></li>
    </ul>
</div>

## Description 
Each SoftLayer portal account is assigned a status code that determines how it's treated in the customer portal. This status is reflected in the SoftLayer_User_Customer_Status data type. Status differs from user permissions in that user status applies globally to the portal while user permissions are applied to specific portal functions.


### associatedMethods

*  [SoftLayer_User_Customer::getUserStatus](/reference/services/SoftLayer_User_Customer/getUserStatus )
*  [SoftLayer_User_Customer_Status::getObject](/reference/services/SoftLayer_User_Customer_Status/getObject )



### seeAlso

* [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer )




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
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>A user's status identifying number. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#keyName" name=keyName>keyName</a>
            </span>
            <div class='views-field-body'>A user's status keyname </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>A user's status. This can be either "Active" for user accounts with portal access, "Inactive" for users disabled by another portal user, "Disabled" for accounts turned off by SoftLayer, or "VPN Only" for user accounts with no access to the customer portal but VPN access to the private network. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


