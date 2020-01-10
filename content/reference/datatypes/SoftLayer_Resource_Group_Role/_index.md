---
title: "SoftLayer_Resource_Group_Role"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Resource"
classes:
    - "SoftLayer_Resource_Group_Role"
---

# SoftLayer_Resource_Group_Role
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Resource_Group_Role' >Datatype</a></li>
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
[description]: #description
#### [description]
A resource group role's description.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A resource group role's ID.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[keyName]: #keyname
#### [keyName]
A resource group role's keyname.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[memberLinks]: #memberlinks
#### [memberLinks]
A resource group's role.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Member_Role_Link'>SoftLayer_Resource_Group_Member_Role_Link[] </a>**


</div>

## Count
<div class="prop-row">

-----
[memberLinkCount]: #memberlinkcount
#### [memberLinkCount]
A count of a resource group's role.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


