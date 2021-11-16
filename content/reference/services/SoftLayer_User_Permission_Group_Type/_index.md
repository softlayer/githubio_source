---
title: "SoftLayer_User_Permission_Group_Type"
description: "The SoftLayer_User_Permission_Group_Type class is one of several classes that make up the customer permission system.  T... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Group_Type"
---
# SoftLayer_User_Permission_Group_Type
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Permission_Group_Type' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Permission_Group_Type' >Datatype</a></li>
    </ul>
</div>

## Description


The SoftLayer_User_Permission_Group_Type class is one of several classes that make up the customer permission system.  This class defines the valid group types.  The SYSTEM group type is reserved for internal use. 

It is a role-based system that includes defined actions which can be "grouped" together using a SoftLayer_User_Permission_Group class. These groups of actions are then used to define roles, and the roles are assigned to users. 

When a [SoftLayer_User_Customer]({{<ref "reference/datatypes/SoftLayer_User_Customer">}}) is created, a SoftLayer_User_Permission_Group and SoftLayer_User_Permission_Role is created specifically for the user with a group type of SYSTEM.  When the UI is used to alter the permissions of a customer user, the actions are added or removed from this group.  The api can not be used to alter the permissions in this group.  If an account wants to create their own unique permission groups and roles, the UI can not be used to manage them. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [getGroups](/reference/services/SoftLayer_User_Permission_Group_Type/getGroups)
Retrieve the groups that are of this type.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_User_Permission_Group_Type/getObject)
Retrieve a SoftLayer_User_Permission_Group_Type record.

</div>
</div>

</div>

