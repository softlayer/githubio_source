---
title: "SoftLayer_Network_Bandwidth_Version1_Usage"
description: "The SoftLayer_Network_Bandwidth_Version1_Usage data type contains general information relating to a single bandwidth usa... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Usage"
---

# SoftLayer_Network_Bandwidth_Version1_Usage
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Usage' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Bandwidth_Version1_Usage data type contains general information relating to a single bandwidth usage record. 





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
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#bandwidthAllotmentDetail" name=bandwidthAllotmentDetail>bandwidthAllotmentDetail</a></span>
            <div class='views-field-body'>Bandwidth allotment detail for this hardware. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment_Detail'>SoftLayer_Network_Bandwidth_Version1_Allotment_Detail </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#bandwidthUsageDetail" name=bandwidthUsageDetail>bandwidthUsageDetail</a></span>
            <div class='views-field-body'>Bandwidth usage details for this hardware. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Usage_Detail'>SoftLayer_Network_Bandwidth_Version1_Usage_Detail[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#bandwidthUsageDetailCount" name=bandwidthUsageDetailCount>bandwidthUsageDetailCount</a></span>
            <div class='views-field-body'>A count of bandwidth usage details for this hardware. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


