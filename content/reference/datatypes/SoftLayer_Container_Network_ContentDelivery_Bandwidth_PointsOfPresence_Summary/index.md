---
title: "SoftLayer_Container_Network_ContentDelivery_Bandwidth_PointsOfPresence_Summary"
description: "SoftLayer_Container_Network_ContentDelivery_Bandwidth_PointsOfPresence_Summary models an individual CDN point of presenc... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_ContentDelivery_Bandwidth_PointsOfPresence_Summary"
---

# SoftLayer_Container_Network_ContentDelivery_Bandwidth_PointsOfPresence_Summary
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_Bandwidth_PointsOfPresence_Summary' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_Network_ContentDelivery_Bandwidth_PointsOfPresence_Summary models an individual CDN point of presence's bandwidth usage for a CDN account within a given date range. CDN POPs are located throughout the world, so individual POP usage may be beneficial in determining who is downloading your CDN hosted content. 
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
            <span class='views-field-title'><a href="#bandwidth" name=bandwidth>bandwidth</a></span>
            <div class='views-field-body'>The amount of bandwidth used by a CDN POP. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsigned long</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#endDateTime" name=endDateTime>endDateTime</a></span>
            <div class='views-field-body'>The ending date of a CDN POP bandwidth summary. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#popName" name=popName>popName</a></span>
            <div class='views-field-body'>A CDN POP's name. This is typically the city the POP resides in. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#startDateTime" name=startDateTime>startDateTime</a></span>
            <div class='views-field-body'>The starting date of a CDN POP bandwidth summary. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#usageUnits" name=usageUnits>usageUnits</a></span>
            <div class='views-field-body'>The unit of measurement used in a CDN POP bandwidth summary. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#viewCount" name=viewCount>viewCount</a></span>
            <div class='views-field-body'>The view count </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsigned long</p></div>
        </div>
            </div>
    </div>


