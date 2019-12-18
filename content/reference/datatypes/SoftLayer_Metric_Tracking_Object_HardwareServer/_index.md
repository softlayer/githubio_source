---
title: "SoftLayer_Metric_Tracking_Object_HardwareServer"
description: "SoftLayer_Metric_Tracking_Object_HardwareServer models tracking objects specific to physical hardware and the data that... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Metric"
classes:
    - "SoftLayer_Metric_Tracking_Object_HardwareServer"
---

# SoftLayer_Metric_Tracking_Object_HardwareServer
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_HardwareServer' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Metric_Tracking_Object_HardwareServer models tracking objects specific to physical hardware and the data that are recorded by those servers. 



### seeAlso

* [SoftLayer_Metric_Tracking_Object](/reference/services/SoftLayer_Metric_Tracking_Object )


* [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server )




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
[data]: #data
#### [data]
The data recorded by a tracking object.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data'>SoftLayer_Metric_Tracking_Object_Data[] </a>**

-----
[id]: #id
#### [id]
A tracking object's internal identifier.   
<span class="type-label">Type: </span>**integer**

-----
[label]: #label
#### [label]
Tracking object label   
<span class="type-label">Type: </span>**string**

-----
[resourceTableId]: #resourcetableid
#### [resourceTableId]
The identifier of the existing resource this object is attempting to track.   
<span class="type-label">Type: </span>**integer**

-----
[startDate]: #startdate
#### [startDate]
The date this tracker began tracking this particular resource.   
<span class="type-label">Type: </span>**dateTime**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[billingCycleBandwidthUsage]: #billingcyclebandwidthusage
#### [billingCycleBandwidthUsage]
The raw bandwidth usage data for the current billing cycle. One object is returned for each network this server is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a>**

-----
[billingCyclePrivateBandwidthUsage]: #billingcycleprivatebandwidthusage
#### [billingCyclePrivateBandwidthUsage]
The raw bandwidth usage data for the current billing cycle. One object is returned for each network this server is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a>**

-----
[billingCyclePrivateUsageIn]: #billingcycleprivateusagein
#### [billingCyclePrivateUsageIn]
The total private inbound bandwidth for this item's resource for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**

-----
[billingCyclePrivateUsageOut]: #billingcycleprivateusageout
#### [billingCyclePrivateUsageOut]
The total private outbound bandwidth for this item's resource for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**

-----
[billingCyclePrivateUsageTotal]: #billingcycleprivateusagetotal
#### [billingCyclePrivateUsageTotal]
The total private bandwidth for this item's resource for the current billing cycle.  
<span class="type-label">Type: </span>**unsigned integer**

-----
[billingCyclePublicBandwidthUsage]: #billingcyclepublicbandwidthusage
#### [billingCyclePublicBandwidthUsage]
The raw bandwidth usage data for the current billing cycle. One object is returned for each network this server is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage </a>**

-----
[billingCyclePublicUsageIn]: #billingcyclepublicusagein
#### [billingCyclePublicUsageIn]
The total public inbound bandwidth for this item's resource for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**

-----
[billingCyclePublicUsageOut]: #billingcyclepublicusageout
#### [billingCyclePublicUsageOut]
The total public outbound bandwidth for this item's resource for the current billing cycle.  
<span class="type-label">Type: </span>**decimal**

-----
[billingCyclePublicUsageTotal]: #billingcyclepublicusagetotal
#### [billingCyclePublicUsageTotal]
The total public bandwidth for this item's resource for the current billing cycle.  
<span class="type-label">Type: </span>**unsigned integer**

-----
[resource]: #resource
#### [resource]
The server that this tracking object tracks.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Server'>SoftLayer_Hardware_Server </a>**

-----
[type]: #type
#### [type]
The type of data that a tracking object polls.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Type'>SoftLayer_Metric_Tracking_Object_Type </a>**


## Count

-----
[billingCycleBandwidthUsageCount]: #billingcyclebandwidthusagecount
#### [billingCycleBandwidthUsageCount]
A count of the raw bandwidth usage data for the current billing cycle. One object is returned for each network this server is attached to.   
<span class="type-label">Type: </span>**unsigned long**


-----
[billingCyclePrivateBandwidthUsageCount]: #billingcycleprivatebandwidthusagecount
#### [billingCyclePrivateBandwidthUsageCount]
A count of the raw bandwidth usage data for the current billing cycle. One object is returned for each network this server is attached to.   
<span class="type-label">Type: </span>**unsigned long**

</div>


