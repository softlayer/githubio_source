---
title: "SoftLayer_Metric_Tracking_Object"
description: "Metric tracking objects provides a common interface to all metrics provided by SoftLayer. These metrics range from netwo... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Metric"
classes:
    - "SoftLayer_Metric_Tracking_Object"
---

# SoftLayer_Metric_Tracking_Object
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Metric_Tracking_Object' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object' >Datatype</a></li>
    </ul>
</div>

## Description 
Metric tracking objects provides a common interface to all metrics provided by SoftLayer. These metrics range from network component traffic for a server to aggregated Bandwidth Pooling traffic and more. Every object within SoftLayer's range of objects that has data that can be tracked over time has an associated tracking object. Use the [SoftLayer_Metric_Tracking_Object]({{<ref "reference/datatypes/SoftLayer_Metric_Tracking_Object">}}) service to retrieve raw and graph data from a tracking object. 



### seeAlso

* [SoftLayer_Metric_Tracking_Object_Data](/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data )




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
[type]: #type
#### [type]
The type of data that a tracking object polls.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Type'>SoftLayer_Metric_Tracking_Object_Type </a>**


## Count
</div>


