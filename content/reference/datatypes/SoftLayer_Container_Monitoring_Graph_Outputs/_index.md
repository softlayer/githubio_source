---
title: "SoftLayer_Container_Monitoring_Graph_Outputs"
description: "SoftLayer_Container_Monitoring_Graph_Outputs models a single outbound object for a graph of given data sets."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Monitoring_Graph_Outputs"
---

# SoftLayer_Container_Monitoring_Graph_Outputs
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Monitoring_Graph_Outputs' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_Monitoring_Graph_Outputs models a single outbound object for a graph of given data sets.


### associatedMethods

*  [SoftLayer_Metric_Tracking_Object_Monitoring_Robot::graph](/reference/services/SoftLayer_Metric_Tracking_Object_Monitoring_Robot/graph )



### seeAlso

* [SoftLayer_Container_Bandwidth_GraphInputs](/reference/datatypes/SoftLayer_Container_Bandwidth_GraphInputs )




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
[endDate]: #enddate
#### [endDate]
The maximum date included in this graph.  
<span class="type-label">Type: </span>**dateTime**

-----
[graphError]: #grapherror
#### [graphError]
Error message encountered during graphing  
<span class="type-label">Type: </span>**string**

-----
[graphImage]: #graphimage
#### [graphImage]
The raw PNG binary data to be displayed once the graph is drawn.  
<span class="type-label">Type: </span>**binary data**

-----
[startDate]: #startdate
#### [startDate]
The minimum date included in this graph.  
<span class="type-label">Type: </span>**dateTime**

</div>
<!-- LOCAL PROPERTY END -->

</div>


