---
title: "SoftLayer_Metric_Tracking_Object"
description: "Metric tracking objects provides a common interface to all metrics provided by SoftLayer. These metrics range from netwo... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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
Metric tracking objects provides a common interface to all metrics provided by SoftLayer. These metrics range from network component traffic for a server to aggregated Bandwidth Pooling traffic and more. Every object within SoftLayer's range of objects that has data that can be tracked over time has an associated tracking object. 

The SoftLayer_Metric_Tracking_Object service contains methods that allow users to retrieve data from these tracking objects in raw and graph form. 
### seeAlso
        SoftLayer_Metric_Tracking_Object_Data1                
        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Metric_Tracking_Object/getBackboneBandwidthGraph'> getBackboneBandwidthGraph</a> </span>
            <div class='views-field-body'>Retrieve a graph of a SoftLayer backbone's recent traffic activity.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Metric_Tracking_Object/getBandwidthData'> getBandwidthData</a> </span>
            <div class='views-field-body'>Retrieve raw bandwidth data from a tracking object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Metric_Tracking_Object/getBandwidthGraph'> getBandwidthGraph</a> </span>
            <div class='views-field-body'>Retrieve a bandwidth graph.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Metric_Tracking_Object/getBandwidthTotal'> getBandwidthTotal</a> </span>
            <div class='views-field-body'>Retrieve the total bandwidth used within a given time frame.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Metric_Tracking_Object/getCustomGraphData'> getCustomGraphData</a> </span>
            <div class='views-field-body'>Fetch metric data using the graph container class.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Metric_Tracking_Object/getDetailsForDateRange'> getDetailsForDateRange</a> </span>
            <div class='views-field-body'>Retrieve metric detail data over a date range.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Metric_Tracking_Object/getGraph'> getGraph</a> </span>
            <div class='views-field-body'>Retrieve a graph of a virtual hosting platform's per instance use.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Metric_Tracking_Object/getMetricDataTypes'> getMetricDataTypes</a> </span>
            <div class='views-field-body'>Returns valid metric data types for a tracking object</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Metric_Tracking_Object/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Metric_Tracking_Object record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Metric_Tracking_Object/getSummary'> getSummary</a> </span>
            <div class='views-field-body'>Retrieve metric summary.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Metric_Tracking_Object/getSummaryData'> getSummaryData</a> </span>
            <div class='views-field-body'>Returns the metric data for the date range provided</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Metric_Tracking_Object/getType'> getType</a> </span>
            <div class='views-field-body'>Retrieve the type of data that a tracking object polls.</div>
        </div>
        </div>
</div>

