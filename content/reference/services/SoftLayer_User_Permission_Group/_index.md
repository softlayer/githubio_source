---
title: "SoftLayer_User_Permission_Group"
description: "The SoftLayer_User_Permission_Group class is one of several classes that make up the customer permission system.  It is... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Group"
---
# SoftLayer_User_Permission_Group
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Permission_Group' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Permission_Group' >Datatype</a></li>
    </ul>
</div>

## Description


The SoftLayer_User_Permission_Group class is one of several classes that make up the customer permission system.  It is a role-based system that includes defined actions which can be "grouped" together using a SoftLayer_User_Permission_Group class. These groups of actions are then used to define roles, and the roles are assigned to users.  The SoftLayer_User_Permission_Group is also used to track the resources or account devices to which a user has been granted access. The types of resources that users can be granted access is defined in [SoftLayer_User_Permission_Resource_Type]({{<ref "reference/datatypes/SoftLayer_User_Permission_Resource_Type">}}). 

When a [SoftLayer_User_Customer]({{<ref "reference/datatypes/SoftLayer_User_Customer">}}) is created, a SoftLayer_User_Permission_Group and SoftLayer_User_Permission_Role is created specifically for the user with a group type of SYSTEM.  When the UI is used to alter the permissions of a customer user, the actions are added or removed from this group.  The api can not be used to alter the permissions in this group.  If an account wants to create their own unique permission groups and roles, the UI can not be used to manage them. 

This is also true for device access.  Either, the UI can be used to track the devices to which users are granted access which will use the SYSTEM group, or the api can be used, making the UI information inaccurate. 

User Customers can be assigned to multiple roles but it is recommended to either use the UI for managing account users permissions or only use the api.  Mixing the two will lead to confusing results as the UI will not show any permissions assigned to a user via a customer created role/group combination. 

Proceed with caution. 

One or more [SoftLayer_User_Permission_Action]({{<ref "reference/datatypes/SoftLayer_User_Permission_Action">}}) are assigned to one or more SoftLayer_User_Permission_Group Objects. One ore more SoftLayer_User_Permission_Group objects can be linked to a [SoftLayer_User_Permission_Role]({{<ref "reference/datatypes/SoftLayer_User_Permission_Role">}}). A single SoftLayer_User_Permission_Group object can be linked to multiple SoftLayer_User_Permission_Role objects. The [SoftLayer_User_Permission_Role]({{<ref "reference/datatypes/SoftLayer_User_Permission_Role">}}) is assigned to one or more [SoftLayer_User_Customer]({{<ref "reference/datatypes/SoftLayer_User_Customer">}}). 

The [SoftLayer_User_Permission_Action]({{<ref "reference/datatypes/SoftLayer_User_Permission_Action">}}) class defines the permissions that are required in order for a [SoftLayer_User_Customer]({{<ref "reference/datatypes/SoftLayer_User_Customer">}}) to perform certain actions within IMS. 

Resources belonging to the user's account can also be linked to permission groups. See [SoftLayer_User_Permission_Resource_Type]({{<ref "reference/datatypes/SoftLayer_User_Permission_Resource_Type">}}). 



        
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

#### [addAction](/reference/services/SoftLayer_User_Permission_Group/addAction)
Add a permission action to the group.

</div>

<div class="method-row">

#### [addBulkActions](/reference/services/SoftLayer_User_Permission_Group/addBulkActions)
Adds a list of permission actions to the group.

</div>

<div class="method-row">

#### [addBulkResourceObjects](/reference/services/SoftLayer_User_Permission_Group/addBulkResourceObjects)
Links multiple account device objects of the same resource type to the group.

</div>

<div class="method-row">

#### [addResourceObject](/reference/services/SoftLayer_User_Permission_Group/addResourceObject)
Links a hardware, virtual guest, or dedicated host object on the

</div>

<div class="method-row">

#### [createObject](/reference/services/SoftLayer_User_Permission_Group/createObject)
Create a new customer permission group

</div>

<div class="method-row">

#### [deleteObject](/reference/services/SoftLayer_User_Permission_Group/deleteObject)
Delete a new customer permission group

</div>

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_User_Permission_Group/editObject)
Edit an existing customer permission group

</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_User_Permission_Group/getAccount)


</div>

<div class="method-row">

#### [getActions](/reference/services/SoftLayer_User_Permission_Group/getActions)


</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_User_Permission_Group/getObject)
Retrieve a SoftLayer_User_Permission_Group record.

</div>

<div class="method-row">

#### [getRoles](/reference/services/SoftLayer_User_Permission_Group/getRoles)


</div>

<div class="method-row">

#### [getType](/reference/services/SoftLayer_User_Permission_Group/getType)
Retrieve the type of the permission group.

</div>

<div class="method-row">

#### [linkRole](/reference/services/SoftLayer_User_Permission_Group/linkRole)
Links a permission role to the group.

</div>

<div class="method-row">

#### [removeAction](/reference/services/SoftLayer_User_Permission_Group/removeAction)
Remove a permission action from the group.

</div>

<div class="method-row">

#### [removeBulkActions](/reference/services/SoftLayer_User_Permission_Group/removeBulkActions)
Remove a list of permission actions from the group.

</div>

<div class="method-row">

#### [removeBulkResourceObjects](/reference/services/SoftLayer_User_Permission_Group/removeBulkResourceObjects)
Unlinks multiple account device objects of the same resource type from the group.

</div>

<div class="method-row">

#### [removeResourceObject](/reference/services/SoftLayer_User_Permission_Group/removeResourceObject)
Unlinks a hardware, virtual guest, or dedicated host object on the

</div>

<div class="method-row">

#### [unlinkRole](/reference/services/SoftLayer_User_Permission_Group/unlinkRole)
Unlinks a permission role from the group.

</div>
</div>

</div>

