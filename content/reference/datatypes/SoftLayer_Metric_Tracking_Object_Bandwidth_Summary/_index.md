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
    <li id='service'> <a href='/reference/services/SoftLayer_Metric_Tracking_Object_Bandwidth_Summary' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Bandwidth_Summary' >Datatype</a></li>
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

## Local
-----
[allocationAmount]: #allocationamount
#### [allocationAmount]
This is the amount of bandwidth (measured in gigabytes) allocated for this tracking object.   
<span class="type-label">Type: </span>**float**

-----
[allocationId]: #allocationid
#### [allocationId]
  
<span class="type-label">Type: </span>**integer**

-----
[amountOut]: #amountout
#### [amountOut]
The amount of outbound bandwidth (measured in gigabytes) currently used this billing period. Same as $outboundBandwidthAmount. Aliased for backward compatability.   
<span class="type-label">Type: </span>**decimal**

-----
[averageDailyUsage]: #averagedailyusage
#### [averageDailyUsage]
The daily average amount of outbound bandwidth usage.   
<span class="type-label">Type: </span>**float**

-----
[currentlyOverAllocationFlag]: #currentlyoverallocationflag
#### [currentlyOverAllocationFlag]
A flag that tells whether or not this tracking object's bandwidth usage is already over the allocation. 1 means yes, 0 means no.   
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
The metric tracking id for this resource.   
<span class="type-label">Type: </span>**integer**

-----
[outboundBandwidthAmount]: #outboundbandwidthamount
#### [outboundBandwidthAmount]
The amount of outbound bandwidth (measured in gigabytes) currently used this billing period   
<span class="type-label">Type: </span>**decimal**

-----
[projectedBandwidthUsage]: #projectedbandwidthusage
#### [projectedBandwidthUsage]
The amount of bandwidth (measured in gigabytes) of projected usage, using a basic average calculation of daily usage.   
<span class="type-label">Type: </span>**float**

-----
[projectedOverAllocationFlag]: #projectedoverallocationflag
#### [projectedOverAllocationFlag]
A flag that tells whether or not this tracking object's bandwidth usage is projected to go over the allocation, based on daily average usage. 1 means yes, 0 means no.   
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

</div>


