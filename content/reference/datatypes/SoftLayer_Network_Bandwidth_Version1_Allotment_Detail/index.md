---
title: "SoftLayer_Network_Bandwidth_Version1_Allotment_Detail"
description: "The SoftLayer_Network_Bandwidth_Version1_Allotment_Detail data type contains specific information relating to a single b... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment_Detail"
---

# SoftLayer_Network_Bandwidth_Version1_Allotment_Detail
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment_Detail' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Bandwidth_Version1_Allotment_Detail data type contains specific information relating to a single bandwidth allotment record. 
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
            <span class='views-field-title'><a href="#allocationId" name=allocationId>allocationId</a></span>
            <div class='views-field-body'>Allocated bandwidth. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#bandwidthAllotmentId" name=bandwidthAllotmentId>bandwidthAllotmentId</a></span>
            <div class='views-field-body'>Bandwidth Pool associated with this detail. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#effectiveDate" name=effectiveDate>effectiveDate</a></span>
            <div class='views-field-body'>Beginning this date the bandwidth allotment is active.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#endEffectiveDate" name=endEffectiveDate>endEffectiveDate</a></span>
            <div class='views-field-body'>From this date the bandwidth allotment is no longer active.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>Internal ID associated with this allotment detail. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serviceProviderId" name=serviceProviderId>serviceProviderId</a></span>
            <div class='views-field-body'>Service Provider Id for an allotment </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#allocation" name=allocation>allocation</a></span>
            <div class='views-field-body'>Allocated bandwidth. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allocation'>SoftLayer_Network_Bandwidth_Version1_Allocation </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#bandwidthAllotment" name=bandwidthAllotment>bandwidthAllotment</a></span>
            <div class='views-field-body'>The parent Bandwidth Pool. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#bandwidthUsage" name=bandwidthUsage>bandwidthUsage</a></span>
            <div class='views-field-body'>Bandwidth used. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Usage'>SoftLayer_Network_Bandwidth_Version1_Usage[] </a></p></div>
        </div>
            </div>
</div>


