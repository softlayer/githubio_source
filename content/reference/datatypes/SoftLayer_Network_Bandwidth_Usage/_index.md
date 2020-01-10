---
title: "SoftLayer_Network_Bandwidth_Usage"
description: "The SoftLayer_Network_Bandwidth_Usage data type contains specific information relating to bandwidth utilization at a spe... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Usage"
---

# SoftLayer_Network_Bandwidth_Usage
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Bandwidth_Usage data type contains specific information relating to bandwidth utilization at a specific point in time on a given network interface. 





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[amountIn]: #amountin
#### [amountIn]
Incoming bandwidth utilization.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[amountOut]: #amountout
#### [amountOut]
Outgoing bandwidth utilization.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[bandwidthUsageDetailTypeId]: #bandwidthusagedetailtypeid
#### [bandwidthUsageDetailTypeId]
ID of the bandwidth usage detail type for this record.  
<span class="type-label">Type: </span>**decimal**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[trackingObject]: #trackingobject
#### [trackingObject]
The tracking object this bandwidth usage record describes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object'>SoftLayer_Metric_Tracking_Object </a>**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
In and out bandwidth utilization for a specified time stamp.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Usage_Detail_Type'>SoftLayer_Network_Bandwidth_Version1_Usage_Detail_Type </a>**


</div>

## Count
</div>


