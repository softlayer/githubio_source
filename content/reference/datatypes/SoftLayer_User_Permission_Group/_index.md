---
title: "SoftLayer_User_Permission_Group"
description: ""
layout: "datatype"
tags:
    - "datatype"
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
[accountId]: #accountid
#### [accountId]
A permission groups associated [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) id.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date the permission group record was created.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
The description of the permission group.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[expirationDate]: #expirationdate
#### [expirationDate]
The date the temporary group will be destroyed.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A permission groups internal identifying number.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date the permission group record was last modified.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The name of the permission group.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[typeId]: #typeid
#### [typeId]
The type of permission group.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[actions]: #actions
#### [actions]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Permission_Action'>SoftLayer_User_Permission_Action[] </a>**


</div>
<div class="prop-row">

-----
[roles]: #roles
#### [roles]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Permission_Role'>SoftLayer_User_Permission_Role[] </a>**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The type of the permission group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Permission_Group_Type'>SoftLayer_User_Permission_Group_Type </a>**


</div>

## Count
<div class="prop-row">

-----
[actionCount]: #actioncount
#### [actionCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[roleCount]: #rolecount
#### [roleCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


