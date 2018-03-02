---
title: "SoftLayer_Container_Bandwidth_Projection"
description: "SoftLayer_Container_Bandwidth_Projection models projected bandwidth use over a time range."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Bandwidth_Projection"
---

# SoftLayer_Container_Bandwidth_Projection
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Bandwidth_Projection' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_Bandwidth_Projection models projected bandwidth use over a time range.


### associatedMethods

*  [SoftLayer_Bandwidth_Manager::getBandwidthList](/reference/services/SoftLayer_Bandwidth_Manager/getBandwidthList )





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
            <span class='views-field-title'><a href="#allowedUsage" name=allowedUsage>allowedUsage</a></span>
            <div class='views-field-body'>Bandwidth limit for this hardware. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#estimatedUsage" name=estimatedUsage>estimatedUsage</a></span>
            <div class='views-field-body'>Estimated bandwidth usage so far this billing cycle. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareId" name=hardwareId>hardwareId</a></span>
            <div class='views-field-body'>Hardware ID of server to monitor. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#projectedUsage" name=projectedUsage>projectedUsage</a></span>
            <div class='views-field-body'>Projected usage for this hardware based on previous usage this billing cycle. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serverName" name=serverName>serverName</a></span>
            <div class='views-field-body'>the text name of the server being monitored. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#startDate" name=startDate>startDate</a></span>
            <div class='views-field-body'>The minimum date included in this list. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
            </div>
    </div>


