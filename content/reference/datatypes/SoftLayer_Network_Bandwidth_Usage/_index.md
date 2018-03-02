---
title: "SoftLayer_Network_Bandwidth_Usage"
description: "The SoftLayer_Network_Bandwidth_Usage data type contains specific information relating to bandwidth utilization at a spe... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Usage"
---

# SoftLayer_Network_Bandwidth_Usage
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Bandwidth_Usage data type contains specific information relating to bandwidth utilization at a specific point in time on a given network interface. 





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
            <span class='views-field-title'><a href="#amountIn" name=amountIn>amountIn</a></span>
            <div class='views-field-body'>Incoming bandwidth utilization. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#amountOut" name=amountOut>amountOut</a></span>
            <div class='views-field-body'>Outgoing bandwidth utilization. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#bandwidthUsageDetailTypeId" name=bandwidthUsageDetailTypeId>bandwidthUsageDetailTypeId</a></span>
            <div class='views-field-body'>ID of the bandwidth usage detail type for this record. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#trackingObject" name=trackingObject>trackingObject</a></span>
            <div class='views-field-body'>The tracking object this bandwidth usage record describes. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object'>SoftLayer_Metric_Tracking_Object </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#type" name=type>type</a></span>
            <div class='views-field-body'>In and out bandwidth utilization for a specified time stamp. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Usage_Detail_Type'>SoftLayer_Network_Bandwidth_Version1_Usage_Detail_Type </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


