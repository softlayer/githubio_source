---
title: "SoftLayer_Resource_Group_Member"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Resource"
classes:
    - "SoftLayer_Resource_Group_Member"
---

# SoftLayer_Resource_Group_Member
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Resource_Group_Member' >Datatype</a></li>
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
[createDate]: #createdate
#### [createDate]
A resource group member's creation date.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A resource group member's ID.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
A resource group member's status.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[attributes]: #attributes
#### [attributes]
A resource group member's associated attributes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Member_Attribute'>SoftLayer_Resource_Group_Member_Attribute[] </a>**


</div>
<div class="prop-row">

-----
[descendantMembers]: #descendantmembers
#### [descendantMembers]
A resource group member's associated member descendants.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Member'>SoftLayer_Resource_Group_Member[] </a>**


</div>
<div class="prop-row">

-----
[group]: #group
#### [group]
A resource group member's resource group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group'>SoftLayer_Resource_Group </a>**


</div>
<div class="prop-row">

-----
[roles]: #roles
#### [roles]
A resource group member's associated roles.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Role'>SoftLayer_Resource_Group_Role[] </a>**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
A resource group member's type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Member_Type'>SoftLayer_Resource_Group_Member_Type </a>**


</div>

## Count
<div class="prop-row">

-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of a resource group member's associated attributes.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[descendantMemberCount]: #descendantmembercount
#### [descendantMemberCount]
A count of a resource group member's associated member descendants.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[roleCount]: #rolecount
#### [roleCount]
A count of a resource group member's associated roles.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


