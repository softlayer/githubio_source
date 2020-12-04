---
title: "SoftLayer_User_Permission_Action"
description: "The SoftLayer_User_Permission_Action class is one of several classes that make up the customer permission system.  The s... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Action"
---
# SoftLayer_User_Permission_Action
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Permission_Action' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Permission_Action' >Datatype</a></li>
    </ul>
</div>

## Description
The SoftLayer_User_Permission_Action class is one of several classes that make up the customer permission system.  The system is a role-based system that includes defined actions which can be grouped together using a SoftLayer_User_Permission_Group.  These groups of actions are then used to define roles, and the roles are assigned to users. 

When a [SoftLayer_User_Customer]({{<ref "reference/datatypes/SoftLayer_User_Customer">}}) is created, a SoftLayer_User_Permission_Group and SoftLayer_User_Permission_Role is created specifically for the user with a group type of SYSTEM.  When the UI is used to alter the permissions of a customer user, the actions are added or removed from this group.  The api can not be used to alter the permissions in this group.  If an account wants to create their own unique permission groups and roles, the UI can not be used to manage them. 

User Customers can be assigned to multiple roles but it is recommended to either use the UI for managing account users permissions or only use the api.  Mixing the two will lead to confusing results as the UI will not show any permissions assigned to a user via a customer created role/group combination. 

Proceed with caution. 

The SoftLayer_User_Permission_Action class defines the permissions that are required in order for a SoftLayer_User_Customer to perform certain actions within IMS. 

See [SoftLayer_User_Permission_Group]({{<ref "reference/datatypes/SoftLayer_User_Permission_Group">}}) and [SoftLayer_Permission_Role]({{<ref "reference/datatypes/SoftLayer_Permission_Role">}}) for more details. 



        
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

#### [getAllObjects](/reference/services/SoftLayer_User_Permission_Action/getAllObjects)
Retrieve all customer permission actions in IMS.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_User_Permission_Action/getObject)
Retrieve a SoftLayer_User_Permission_Action record.
</div>
</div>

</div>

