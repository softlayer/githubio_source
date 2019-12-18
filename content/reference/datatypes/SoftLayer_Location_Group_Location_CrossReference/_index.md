---
title: "SoftLayer_Location_Group_Location_CrossReference"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Group_Location_CrossReference"
---

# SoftLayer_Location_Group_Location_CrossReference
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Location_Group_Location_CrossReference' >Datatype</a></li>
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
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[locationGroupId]: #locationgroupid
#### [locationGroupId]
  
<span class="type-label">Type: </span>**integer**

-----
[locationId]: #locationid
#### [locationId]
  
<span class="type-label">Type: </span>**integer**

-----
[priority]: #priority
#### [priority]
If set, this is the priority of this cross reference record in the group.   
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[location]: #location
#### [location]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[locationGroup]: #locationgroup
#### [locationGroup]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Group'>SoftLayer_Location_Group </a>**


## Count
</div>


