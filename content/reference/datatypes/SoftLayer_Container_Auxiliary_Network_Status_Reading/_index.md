---
title: "SoftLayer_Container_Auxiliary_Network_Status_Reading"
description: "The SoftLayer_Container_Auxiliary_Network_Status_Reading data type contains information relating to an object being moni... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Auxiliary_Network_Status_Reading"
---

# SoftLayer_Container_Auxiliary_Network_Status_Reading
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Auxiliary_Network_Status_Reading' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Auxiliary_Network_Status_Reading data type contains information relating to an object being monitored from outside the SoftLayer network.  It is primarily used to check the status of our edge routers from multiple locations around the world. 
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
            <span class='views-field-title'><a href="#averagePing" name=averagePing>averagePing</a></span>
            <div class='views-field-body'>Average packet round-trip time. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>float</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#fails" name=fails>fails</a></span>
            <div class='views-field-body'>Number of failures since the target was last detected to be working properly. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#frequency" name=frequency>frequency</a></span>
            <div class='views-field-body'>Monitoring frequency in minutes. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#label" name=label>label</a></span>
            <div class='views-field-body'>The target babel. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#lastCheckDate" name=lastCheckDate>lastCheckDate</a></span>
            <div class='views-field-body'>Last check date and time. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#lastDownDate" name=lastDownDate>lastDownDate</a></span>
            <div class='views-field-body'>Date and time of the last problem detected. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#latency" name=latency>latency</a></span>
            <div class='views-field-body'>The total response time in seconds calculated during the last check. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>float</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#location" name=location>location</a></span>
            <div class='views-field-body'>The monitoring location name. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#maximumPing" name=maximumPing>maximumPing</a></span>
            <div class='views-field-body'>Maximum packet round-trip time. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>float</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#minimumPing" name=minimumPing>minimumPing</a></span>
            <div class='views-field-body'>Minimum packet round-trip time. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>float</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#pingLoss" name=pingLoss>pingLoss</a></span>
            <div class='views-field-body'>Packet loss percentage. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>float</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#startDate" name=startDate>startDate</a></span>
            <div class='views-field-body'>The date monitoring first began </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#statusCode" name=statusCode>statusCode</a></span>
            <div class='views-field-body'>Status Code - one of UP, Down, Test pending. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#statusMessage" name=statusMessage>statusMessage</a></span>
            <div class='views-field-body'>The status message from the last effective check. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#target" name=target>target</a></span>
            <div class='views-field-body'>The target object. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#targetType" name=targetType>targetType</a></span>
            <div class='views-field-body'>A letter indicating the target type. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
    </div>


