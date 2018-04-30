---
title: "SoftLayer_Container_Network_Bandwidth_Version1_Usage"
description: "SoftLayer_Container_Network_Bandwidth_Version1_Usage models an hourly bandwidth record."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_Bandwidth_Version1_Usage"
---

# SoftLayer_Container_Network_Bandwidth_Version1_Usage
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_Bandwidth_Version1_Usage' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_Network_Bandwidth_Version1_Usage models an hourly bandwidth record.


### associatedMethods

*  [SoftLayer_Hardware::getBandwidthByHour](/reference/services/SoftLayer_Hardware/getBandwidthByHour )



### seeAlso

* [SoftLayer_Container_Network_Bandwidth_Version1_Allotment](/reference/datatypes/SoftLayer_Container_Network_Bandwidth_Version1_Allotment )




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
            <span class='views-field-title'>
                <a href="#incomingAmount" name=incomingAmount>incomingAmount</a>
            </span>
            <div class='views-field-body'>The amount of incoming bandwidth that a server has used within the hour of the recordedDate. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#outgoingAmount" name=outgoingAmount>outgoingAmount</a>
            </span>
            <div class='views-field-body'>The amount of outgoing bandwidth that a server has used within the hour of the recordedDate. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#recordedDate" name=recordedDate>recordedDate</a>
            </span>
            <div class='views-field-body'>The date and time that the bandwidth was used by a piece of hardware </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
            </div>
    </div>


