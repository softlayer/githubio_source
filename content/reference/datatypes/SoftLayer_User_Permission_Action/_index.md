---
title: "SoftLayer_User_Permission_Action"
description: "The SoftLayer_User_Permission_Action data type contains local attributes to identify and describe the valid actions a cu... "
layout: "datatype"
tags:
    - "datatype"
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
The SoftLayer_User_Permission_Action data type contains local attributes to identify and describe the valid actions a customer user can perform within IMS.  This includes a name, key name, and description.  This data can not be modified by users of IMS. 

It also contains relational attributes that indicate which SoftLayer_User_Permission_Group's include the action. 


### associatedMethods

*  [SoftLayer_User_Customer::getActions](/reference/services/SoftLayer_User_Customer/getActions )
*  [SoftLayer_User_Customer::getPermissions](/reference/services/SoftLayer_User_Customer/getPermissions )





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
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[key]: #key
#### [key]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[keyName]: #keyname
#### [keyName]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


