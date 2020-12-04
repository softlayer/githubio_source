---
title: "SoftLayer_User_Permission_Group_Type"
description: "The SoftLayer_User_Permission_Group_Type class is one of several classes that make up the customer permission system.  T... "
layout: "datatype"
tags:
    - "datatype"
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
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[keyName]: #keyname
#### [keyName]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[groups]: #groups
#### [groups]
The groups that are of this type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Permission_Group'>SoftLayer_User_Permission_Group[] </a>**


</div>

## Count
<div class="prop-row">

-----
[groupCount]: #groupcount
#### [groupCount]
A count of the groups that are of this type.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


