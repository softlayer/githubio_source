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

* [SoftLayer_Metric_Tracking_Object_Data](/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data )


        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [getBackboneBandwidthGraph](/reference/services/SoftLayer_Metric_Tracking_Object/getBackboneBandwidthGraph)
[DEPRECATED] Retrieve a graph of a SoftLayer backbone's recent traffic activity.
</div>

<div class="method-row">

#### [getBandwidthData](/reference/services/SoftLayer_Metric_Tracking_Object/getBandwidthData)
Retrieve raw bandwidth data from a tracking object.
</div>

<div class="method-row">

#### [getBandwidthGraph](/reference/services/SoftLayer_Metric_Tracking_Object/getBandwidthGraph)
Retrieve a bandwidth graph.
</div>

<div class="method-row">

#### [getBandwidthTotal](/reference/services/SoftLayer_Metric_Tracking_Object/getBandwidthTotal)
Retrieve the total bandwidth used within a given time frame.
</div>

<div class="method-row">

#### [getCustomGraphData](/reference/services/SoftLayer_Metric_Tracking_Object/getCustomGraphData)
Fetch metric data using the graph container class.
</div>

<div class="method-row">

#### [getDetailsForDateRange](/reference/services/SoftLayer_Metric_Tracking_Object/getDetailsForDateRange)
Retrieve metric detail data over a date range.
</div>

<div class="method-row">

#### [getGraph](/reference/services/SoftLayer_Metric_Tracking_Object/getGraph)
Retrieve a graph of a virtual hosting platform's per instance use.
</div>

<div class="method-row">

#### [getMetricDataTypes](/reference/services/SoftLayer_Metric_Tracking_Object/getMetricDataTypes)
Returns valid metric data types for a tracking object
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Metric_Tracking_Object/getObject)
Retrieve a SoftLayer_Metric_Tracking_Object record.
</div>

<div class="method-row">

#### [getSummary](/reference/services/SoftLayer_Metric_Tracking_Object/getSummary)
Retrieve metric summary.
</div>

<div class="method-row">

#### [getSummaryData](/reference/services/SoftLayer_Metric_Tracking_Object/getSummaryData)
Returns the metric data for the date range provided
</div>

<div class="method-row">

#### [getType](/reference/services/SoftLayer_Metric_Tracking_Object/getType)
Retrieve the type of data that a tracking object polls.
</div>
</div>

</div>

