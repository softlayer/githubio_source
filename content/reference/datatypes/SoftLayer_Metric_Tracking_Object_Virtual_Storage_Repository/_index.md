---
title: "SoftLayer_Metric_Tracking_Object_Virtual_Storage_Repository"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Metric"
classes:
    - "SoftLayer_Metric_Tracking_Object_Virtual_Storage_Repository"
---

# SoftLayer_Metric_Tracking_Object_Virtual_Storage_Repository
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Virtual_Storage_Repository' >Datatype</a></li>
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
[data]: #data
#### [data]
The data recorded by a tracking object.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data'>SoftLayer_Metric_Tracking_Object_Data[] </a>**

-----
[id]: #id
#### [id]
A tracking object's internal identifier.   
<span class="type-label">Type: </span>**integer**

-----
[label]: #label
#### [label]
Tracking object label   
<span class="type-label">Type: </span>**string**

-----
[resourceTableId]: #resourcetableid
#### [resourceTableId]
The identifier of the existing resource this object is attempting to track.   
<span class="type-label">Type: </span>**integer**

-----
[startDate]: #startdate
#### [startDate]
The date this tracker began tracking this particular resource.   
<span class="type-label">Type: </span>**dateTime**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[resource]: #resource
#### [resource]
The virtual storage repository that this tracking object tracks.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Storage_Repository'>SoftLayer_Virtual_Storage_Repository </a>**

-----
[type]: #type
#### [type]
The type of data that a tracking object polls.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Type'>SoftLayer_Metric_Tracking_Object_Type </a>**


## Count
</div>


