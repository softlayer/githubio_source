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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#endDate" name=endDate>endDate</a></span>
            <div class='views-field-body'>The maximum date included in this graph. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#graphError" name=graphError>graphError</a></span>
            <div class='views-field-body'>Error message encountered during graphing </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#graphImage" name=graphImage>graphImage</a></span>
            <div class='views-field-body'>The raw PNG binary data to be displayed once the graph is drawn. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>binary data</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#startDate" name=startDate>startDate</a></span>
            <div class='views-field-body'>The minimum date included in this graph. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
            </div>
    </div>


