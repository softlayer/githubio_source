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






<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
-----
[description]: #description
#### [description]
  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[locationGroupTypeId]: #locationgrouptypeid
#### [locationGroupTypeId]
  
<span class="type-label">Type: </span>**integer**

-----
[name]: #name
#### [name]
  
<span class="type-label">Type: </span>**string**

-----
[securityLevelId]: #securitylevelid
#### [securityLevelId]
  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[locationGroupType]: #locationgrouptype
#### [locationGroupType]
The type for this location group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Group_Type'>SoftLayer_Location_Group_Type </a>**

-----
[locations]: #locations
#### [locations]
The locations in a group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location[] </a>**


## Count

-----
[locationCount]: #locationcount
#### [locationCount]
A count of the locations in a group.   
<span class="type-label">Type: </span>**unsigned long**

</div>


