---
title: "SoftLayer_User_Customer_CustomerPermission_Permission"
description: "Each SoftLayer portal account is assigned a series of permissions that determine what access the user has to functions w... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_CustomerPermission_Permission"
---

# SoftLayer_User_Customer_CustomerPermission_Permission
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission' >Datatype</a></li>
    </ul>
</div>

## Description 
Each SoftLayer portal account is assigned a series of permissions that determine what access the user has to functions within the SoftLayer customer portal. This status is reflected in the SoftLayer_User_Customer_Status data type. Permissions differ from user status in that user status applies globally to the portal while user permissions are applied to specific portal functions.


### associatedMethods

*  [SoftLayer_User_Customer::getPermissions](/reference/services/SoftLayer_User_Customer/getPermissions )
*  [SoftLayer_User_Customer_CustomerPermission_Permission::getObject](/reference/services/SoftLayer_User_Customer_CustomerPermission_Permission/getObject )



### seeAlso

* [Permissions](/reference/datatypes/Permissions )


* [SoftLayer_User_Customer](/reference/datatypes/SoftLayer_User_Customer )




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
            <span class='views-field-title'><a href="#key" name=key>key</a></span>
            <div class='views-field-body'>A user permission's short name. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#keyName" name=keyName>keyName</a></span>
            <div class='views-field-body'>A user permission's key name. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>A user permission's name. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
    </div>


