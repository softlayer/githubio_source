---
title: "SoftLayer_Metric_Tracking_Object_VirtualDedicatedRack"
description: "SoftLayer_Metric_Tracking_Object_VirtualDedicatedRack models tracking objects specific to virtual dedicated racks. Bandw... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Metric"
classes:
    - "SoftLayer_Metric_Tracking_Object_VirtualDedicatedRack"
---

# SoftLayer_Metric_Tracking_Object_VirtualDedicatedRack
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_VirtualDedicatedRack' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Metric_Tracking_Object_VirtualDedicatedRack models tracking objects specific to virtual dedicated racks. Bandwidth Pooling aggregate the bandwidth used by multiple servers within the rack. 



### seeAlso

* [SoftLayer_Metric_Tracking_Object](/reference/datatypes/SoftLayer_Metric_Tracking_Object )




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
[data]: #data
#### [data]
The data recorded by a tracking object.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data'>SoftLayer_Metric_Tracking_Object_Data[] </a>**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A tracking object's internal identifier.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[label]: #label
#### [label]
Tracking object label   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[resourceTableId]: #resourcetableid
#### [resourceTableId]
The identifier of the existing resource this object is attempting to track.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[startDate]: #startdate
#### [startDate]
The date this tracker began tracking this particular resource.   
<span class="type-label">Type: </span>**dateTime**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[billingCycleBandwidthUsage]: #billingcyclebandwidthusage
#### [billingCycleBandwidthUsage]
The raw bandwidth usage data for the current billing cycle. One object is returned for each network this server is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a>**


</div>
<div class="prop-row">

-----
[billingCyclePrivateBandwidthUsage]: #billingcycleprivatebandwidthusage
#### [billingCyclePrivateBandwidthUsage]
The raw bandwidth usage data for the current billing cycle. One object is returned for each network this server is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a>**


</div>
<div class="prop-row">

-----
[billingCyclePrivateUsageIn]: #billingcycleprivateusagein
#### [billingCyclePrivateUsageIn]
The total private inbound bandwidth for this item's resource for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[billingCyclePrivateUsageOut]: #billingcycleprivateusageout
#### [billingCyclePrivateUsageOut]
The total private outbound bandwidth for this item's resource for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[billingCyclePrivateUsageTotal]: #billingcycleprivateusagetotal
#### [billingCyclePrivateUsageTotal]
The total private bandwidth for this item's resource for the current billing cycle.  
<span class="type-label">Type: </span>**unsigned integer**


</div>
<div class="prop-row">

-----
[billingCyclePublicBandwidthUsage]: #billingcyclepublicbandwidthusage
#### [billingCyclePublicBandwidthUsage]
The raw bandwidth usage data for the current billing cycle. One object is returned for each network this server is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage </a>**


</div>
<div class="prop-row">

-----
[billingCyclePublicUsageIn]: #billingcyclepublicusagein
#### [billingCyclePublicUsageIn]
The total public inbound bandwidth for this item's resource for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[billingCyclePublicUsageOut]: #billingcyclepublicusageout
#### [billingCyclePublicUsageOut]
The total public outbound bandwidth for this item's resource for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[billingCyclePublicUsageTotal]: #billingcyclepublicusagetotal
#### [billingCyclePublicUsageTotal]
The total public bandwidth for this item's resource for the current billing cycle.  
<span class="type-label">Type: </span>**unsigned integer**


</div>
<div class="prop-row">

-----
[resource]: #resource
#### [resource]
The virtual rack that this tracking object tracks.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment </a>**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The type of data that a tracking object polls.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Type'>SoftLayer_Metric_Tracking_Object_Type </a>**


</div>

## Count
<div class="prop-row">

-----
[billingCycleBandwidthUsageCount]: #billingcyclebandwidthusagecount
#### [billingCycleBandwidthUsageCount]
A count of the raw bandwidth usage data for the current billing cycle. One object is returned for each network this server is attached to.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[billingCyclePrivateBandwidthUsageCount]: #billingcycleprivatebandwidthusagecount
#### [billingCyclePrivateBandwidthUsageCount]
A count of the raw bandwidth usage data for the current billing cycle. One object is returned for each network this server is attached to.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


