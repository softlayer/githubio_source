---
title: "SoftLayer_User_Permission_Group_Type"
description: "These are the attributes which describe a SoftLayer_User_Permission_Group_Type. All SoftLayer_User_Permission_Group obje... "
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


These are the attributes which describe a SoftLayer_User_Permission_Group_Type. All SoftLayer_User_Permission_Group objects must be linked to one of these types. 

For further information see: [SoftLayer_User_Permission_Group]({{<ref "reference/datatypes/SoftLayer_User_Permission_Group">}}). 





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
Unique Record ID.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[keyName]: #keyname
#### [keyName]
The keyname for the group type.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A descriptive name for the group type.  
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


