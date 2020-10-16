---
title: "SoftLayer_Metric_Tracking_Object_Abstract"
description: "SoftLayer_Metric_Tracking_Object_Abstract models a generic tracking object type. Typically a tracking object with a spec... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Metric"
classes:
    - "SoftLayer_Metric_Tracking_Object_Abstract"
---

# SoftLayer_Metric_Tracking_Object_Abstract
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Abstract' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Metric_Tracking_Object_Abstract models a generic tracking object type. Typically a tracking object with a specific purpose has it's own data type defined within the SoftLayer API. 



### seeAlso

* [SoftLayer_Metric_Tracking_Object](/reference/datatypes/SoftLayer_Metric_Tracking_Object )




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
[data]: #data
#### [data]
The data recorded by a tracking object.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data'>SoftLayer_Metric_Tracking_Object_Data[] </a>**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A tracking object's internal identifier.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[label]: #label
#### [label]
Tracking object label   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[resourceTableId]: #resourcetableid
#### [resourceTableId]
The identifier of the existing resource this object is attempting to track.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[startDate]: #startdate
#### [startDate]
The date this tracker began tracking this particular resource.   
<span class="type-label">Type: </span>**dateTime**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[type]: #type
#### [type]
The type of data that a tracking object polls.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Type'>SoftLayer_Metric_Tracking_Object_Type </a>**


</div>

## Count
</div>


