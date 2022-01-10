---
title: "SoftLayer_Location_Group"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Group"
---

# SoftLayer_Location_Group
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Location_Group' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Location_Group' >Datatype</a></li>
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
[locationGroupTypeId]: #locationgrouptypeid
#### [locationGroupTypeId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[securityLevelId]: #securitylevelid
#### [securityLevelId]
  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[locationGroupType]: #locationgrouptype
#### [locationGroupType]
The type for this location group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Group_Type'>SoftLayer_Location_Group_Type </a>**  



</div>
<div class="prop-row">

-----
[locations]: #locations
#### [locations]
The locations in a group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[locationCount]: #locationcount
#### [locationCount]
A count of the locations in a group.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


