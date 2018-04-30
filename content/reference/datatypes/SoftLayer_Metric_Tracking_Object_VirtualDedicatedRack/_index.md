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

* [SoftLayer_Metric_Tracking_Object](/reference/services/SoftLayer_Metric_Tracking_Object )




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
                <a href="#data" name=data>data</a>
            </span>
            <div class='views-field-body'>The data recorded by a tracking object.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data'>SoftLayer_Metric_Tracking_Object_Data[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>A tracking object's internal identifier.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#label" name=label>label</a>
            </span>
            <div class='views-field-body'>Tracking object label  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#resourceTableId" name=resourceTableId>resourceTableId</a>
            </span>
            <div class='views-field-body'>The identifier of the existing resource this object is attempting to track.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#startDate" name=startDate>startDate</a>
            </span>
            <div class='views-field-body'>The date this tracker began tracking this particular resource.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCycleBandwidthUsage" name=billingCycleBandwidthUsage>billingCycleBandwidthUsage</a>
            </span>
            <div class='views-field-body'>The raw bandwidth usage data for the current billing cycle. One object is returned for each network this server is attached to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePrivateBandwidthUsage" name=billingCyclePrivateBandwidthUsage>billingCyclePrivateBandwidthUsage</a>
            </span>
            <div class='views-field-body'>The raw bandwidth usage data for the current billing cycle. One object is returned for each network this server is attached to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePrivateUsageIn" name=billingCyclePrivateUsageIn>billingCyclePrivateUsageIn</a>
            </span>
            <div class='views-field-body'>The total private inbound bandwidth for this item's resource for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePrivateUsageOut" name=billingCyclePrivateUsageOut>billingCyclePrivateUsageOut</a>
            </span>
            <div class='views-field-body'>The total private outbound bandwidth for this item's resource for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePrivateUsageTotal" name=billingCyclePrivateUsageTotal>billingCyclePrivateUsageTotal</a>
            </span>
            <div class='views-field-body'>The total private bandwidth for this item's resource for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsigned integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePublicBandwidthUsage" name=billingCyclePublicBandwidthUsage>billingCyclePublicBandwidthUsage</a>
            </span>
            <div class='views-field-body'>The raw bandwidth usage data for the current billing cycle. One object is returned for each network this server is attached to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePublicUsageIn" name=billingCyclePublicUsageIn>billingCyclePublicUsageIn</a>
            </span>
            <div class='views-field-body'>The total public inbound bandwidth for this item's resource for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePublicUsageOut" name=billingCyclePublicUsageOut>billingCyclePublicUsageOut</a>
            </span>
            <div class='views-field-body'>The total public outbound bandwidth for this item's resource for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePublicUsageTotal" name=billingCyclePublicUsageTotal>billingCyclePublicUsageTotal</a>
            </span>
            <div class='views-field-body'>The total public bandwidth for this item's resource for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsigned integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#resource" name=resource>resource</a>
            </span>
            <div class='views-field-body'>The virtual rack that this tracking object tracks. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment'>SoftLayer_Network_Bandwidth_Version1_Allotment </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#type" name=type>type</a>
            </span>
            <div class='views-field-body'>The type of data that a tracking object polls. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Type'>SoftLayer_Metric_Tracking_Object_Type </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCycleBandwidthUsageCount" name=billingCycleBandwidthUsageCount>billingCycleBandwidthUsageCount</a>
            </span>
            <div class='views-field-body'>A count of the raw bandwidth usage data for the current billing cycle. One object is returned for each network this server is attached to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePrivateBandwidthUsageCount" name=billingCyclePrivateBandwidthUsageCount>billingCyclePrivateBandwidthUsageCount</a>
            </span>
            <div class='views-field-body'>A count of the raw bandwidth usage data for the current billing cycle. One object is returned for each network this server is attached to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


