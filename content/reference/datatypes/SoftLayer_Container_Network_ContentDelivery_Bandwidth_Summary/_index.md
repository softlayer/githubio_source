---
title: "SoftLayer_Container_Network_ContentDelivery_Bandwidth_Summary"
description: "SoftLayer_Container_Network_ContentDelivery_Bandwidth_Summary models a CDN account's overall bandwidth usage and overage... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_ContentDelivery_Bandwidth_Summary"
---

# SoftLayer_Container_Network_ContentDelivery_Bandwidth_Summary
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_Bandwidth_Summary' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_Network_ContentDelivery_Bandwidth_Summary models a CDN account's overall bandwidth usage and overages within a given date range. 
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
            <span class='views-field-title'><a href="#cdnAccountId" name=cdnAccountId>cdnAccountId</a></span>
            <div class='views-field-body'>The CDN account id </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#endDateTime" name=endDateTime>endDateTime</a></span>
            <div class='views-field-body'>The ending date of a CDN bandwidth summary. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#fileName" name=fileName>fileName</a></span>
            <div class='views-field-body'>The name of a file that is requested by visitors </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#mediaType" name=mediaType>mediaType</a></span>
            <div class='views-field-body'>The media type </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#startDateTime" name=startDateTime>startDateTime</a></span>
            <div class='views-field-body'>The starting date of a CDN bandwidth summary. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#usage" name=usage>usage</a></span>
            <div class='views-field-body'>The amount of bandwidth used by a CDN account in between a given starting and ending date. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>float</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#usageUnits" name=usageUnits>usageUnits</a></span>
            <div class='views-field-body'>The unit of measurement used in a CDN bandwidth summary. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
    </div>


