---
title: "SoftLayer_Metric_Tracking_Object_Bandwidth_Summary"
description: "This data type provides commonly used bandwidth summary components for the current billing cycle."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Metric"
classes:
    - "SoftLayer_Metric_Tracking_Object_Bandwidth_Summary"
---

# SoftLayer_Metric_Tracking_Object_Bandwidth_Summary
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Bandwidth_Summary' >Datatype</a></li>
    </ul>
</div>

## Description 
This data type provides commonly used bandwidth summary components for the current billing cycle. 





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
            <span class='views-field-title'><a href="#allocationAmount" name=allocationAmount>allocationAmount</a></span>
            <div class='views-field-body'>This is the amount of bandwidth (measured in gigabytes) allocated for this tracking object.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>float</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#allocationId" name=allocationId>allocationId</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#amountOut" name=amountOut>amountOut</a></span>
            <div class='views-field-body'>The amount of outbound bandwidth (measured in gigabytes) currently used this billing period. Same as $outboundBandwidthAmount. Aliased for backward compatability.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#averageDailyUsage" name=averageDailyUsage>averageDailyUsage</a></span>
            <div class='views-field-body'>The daily average amount of outbound bandwidth usage.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>float</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#currentlyOverAllocationFlag" name=currentlyOverAllocationFlag>currentlyOverAllocationFlag</a></span>
            <div class='views-field-body'>A flag that tells whether or not this tracking object's bandwidth usage is already over the allocation. 1 means yes, 0 means no.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The metric tracking id for this resource.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#outboundBandwidthAmount" name=outboundBandwidthAmount>outboundBandwidthAmount</a></span>
            <div class='views-field-body'>The amount of outbound bandwidth (measured in gigabytes) currently used this billing period  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#projectedBandwidthUsage" name=projectedBandwidthUsage>projectedBandwidthUsage</a></span>
            <div class='views-field-body'>The amount of bandwidth (measured in gigabytes) of projected usage, using a basic average calculation of daily usage.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>float</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#projectedOverAllocationFlag" name=projectedOverAllocationFlag>projectedOverAllocationFlag</a></span>
            <div class='views-field-body'>A flag that tells whether or not this tracking object's bandwidth usage is projected to go over the allocation, based on daily average usage. 1 means yes, 0 means no.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
    </div>


