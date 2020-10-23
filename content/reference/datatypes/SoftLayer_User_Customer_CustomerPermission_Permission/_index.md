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
    <li id='service'> <a href='/reference/services/SoftLayer_User_Customer_CustomerPermission_Permission' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission' >Datatype</a></li>
    </ul>
</div>

## Description 
Each SoftLayer portal account is assigned a series of permissions that determine what access the user has to functions within the SoftLayer customer portal. This status is reflected in the SoftLayer_User_Customer_Status data type. Permissions differ from user status in that user status applies globally to the portal while user permissions are applied to specific portal functions. 


### associatedMethods

*  [SoftLayer_User_Customer::getPermissions](/reference/services/SoftLayer_User_Customer/getPermissions )
*  [SoftLayer_User_Customer_CustomerPermission_Permission::getObject](/reference/services/SoftLayer_User_Customer_CustomerPermission_Permission/getObject )



### seeAlso

* [Permissions](/reference/datatypes/Permissions )


* [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer )




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
[key]: #key
#### [key]
A user permission's short name.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[keyName]: #keyname
#### [keyName]
A user permission's key name.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A user permission's name.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


