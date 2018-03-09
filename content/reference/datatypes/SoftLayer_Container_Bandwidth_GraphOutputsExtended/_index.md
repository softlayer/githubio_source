---
title: "SoftLayer_Container_Bandwidth_GraphOutputsExtended"
description: "SoftLayer_Container_Bandwidth_GraphOutputs models an individual bandwidth graph image and certain details about that gra... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Bandwidth_GraphOutputsExtended"
---

# SoftLayer_Container_Bandwidth_GraphOutputsExtended
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputsExtended' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_Bandwidth_GraphOutputs models an individual bandwidth graph image and certain details about that graph image.


### associatedMethods

*  [SoftLayer_Utility_Bandwidth_Graph::getBandwidthImage](/reference/services/SoftLayer_Utility_Bandwidth_Graph/getBandwidthImage )
*  [SoftLayer_Utility_Bandwidth_Graph::getBandwidthGraphParameters](/reference/services/SoftLayer_Utility_Bandwidth_Graph/getBandwidthGraphParameters )
*  [SoftLayer_Network_ContentDelivery_Account::getBandwidthImage](/reference/services/SoftLayer_Network_ContentDelivery_Account/getBandwidthImage )
*  [SoftLayer_Network_ContentDelivery_Account::getAllPopsBandwidthImage](/reference/services/SoftLayer_Network_ContentDelivery_Account/getAllPopsBandwidthImage )



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
            <span class='views-field-title'>
                <a href="#graphImage" name=graphImage>graphImage</a>
            </span>
            <div class='views-field-body'>The raw PNG binary data of a bandwidth graph image. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>binary data</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#graphTitle" name=graphTitle>graphTitle</a>
            </span>
            <div class='views-field-body'>A bandwidth graph's title. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#inBoundTotalBytes" name=inBoundTotalBytes>inBoundTotalBytes</a>
            </span>
            <div class='views-field-body'>The amount of inbound traffic reported on a bandwidth graph image. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsigned long</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#maxEndDate" name=maxEndDate>maxEndDate</a>
            </span>
            <div class='views-field-body'>The ending date of the data represented in a bandwidth graph. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#minStartDate" name=minStartDate>minStartDate</a>
            </span>
            <div class='views-field-body'>The beginning date of the data represented in a bandwidth graph. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#outBoundTotalBytes" name=outBoundTotalBytes>outBoundTotalBytes</a>
            </span>
            <div class='views-field-body'>The amount of outbound traffic reported on a bandwidth graph image. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsigned long</p>
            </div>
        </div>
            </div>
    </div>


