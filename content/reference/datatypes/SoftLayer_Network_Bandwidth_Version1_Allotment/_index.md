---
title: "SoftLayer_Network_Bandwidth_Version1_Allotment"
description: "The SoftLayer_Network_Bandwidth_Version1_Allotment class provides methods and data structures necessary to work with an... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
---

# SoftLayer_Network_Bandwidth_Version1_Allotment
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Bandwidth_Version1_Allotment class provides methods and data structures necessary to work with an array of hardware objects associated with a single Bandwidth Pooling. 





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
            <span class='views-field-title'><a href="#accountId" name=accountId>accountId</a></span>
            <div class='views-field-body'>The user account identifier associated with this allotment. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#bandwidthAllotmentTypeId" name=bandwidthAllotmentTypeId>bandwidthAllotmentTypeId</a></span>
            <div class='views-field-body'>An identifier marking this allotment as a virtual private rack (1) or a bandwidth pooling(2). </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>Creation date for an allotment. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#endDate" name=endDate>endDate</a></span>
            <div class='views-field-body'>End date for an allotment. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A virtual rack's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#locationGroupId" name=locationGroupId>locationGroupId</a></span>
            <div class='views-field-body'>Location Group Id for an allotment </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>Text A virtual rack's name. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
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
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>The account associated with this virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#activeDetails" name=activeDetails>activeDetails</a></span>
            <div class='views-field-body'>The bandwidth allotment detail records associated with this virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment_Detail'>SoftLayer_Network_Bandwidth_Version1_Allotment_Detail[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#applicationDeliveryControllers" name=applicationDeliveryControllers>applicationDeliveryControllers</a></span>
            <div class='views-field-body'>The Application Delivery Controller contained within a virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller'>SoftLayer_Network_Application_Delivery_Controller[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#averageDailyPublicBandwidthUsage" name=averageDailyPublicBandwidthUsage>averageDailyPublicBandwidthUsage</a></span>
            <div class='views-field-body'>The average daily public bandwidth usage for the current billing cycle. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>float</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#bandwidthAllotmentType" name=bandwidthAllotmentType>bandwidthAllotmentType</a></span>
            <div class='views-field-body'>The bandwidth allotment type of this virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment_Type'>SoftLayer_Network_Bandwidth_Version1_Allotment_Type </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#bareMetalInstances" name=bareMetalInstances>bareMetalInstances</a></span>
            <div class='views-field-body'>The bare metal server instances contained within a virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingCycleBandwidthUsage" name=billingCycleBandwidthUsage>billingCycleBandwidthUsage</a></span>
            <div class='views-field-body'>A virtual rack's raw bandwidth usage data for an account's current billing cycle. One object is returned for each network this server is attached to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingCyclePrivateBandwidthUsage" name=billingCyclePrivateBandwidthUsage>billingCyclePrivateBandwidthUsage</a></span>
            <div class='views-field-body'>A virtual rack's raw private network bandwidth usage data for an account's current billing cycle. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingCyclePublicBandwidthUsage" name=billingCyclePublicBandwidthUsage>billingCyclePublicBandwidthUsage</a></span>
            <div class='views-field-body'>A virtual rack's raw public network bandwidth usage data for an account's current billing cycle. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingCyclePublicUsageTotal" name=billingCyclePublicUsageTotal>billingCyclePublicUsageTotal</a></span>
            <div class='views-field-body'>The total public bandwidth used in this virtual rack for an account's current billing cycle. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsigned integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingItem" name=billingItem>billingItem</a></span>
            <div class='views-field-body'>A virtual rack's billing item. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#currentBandwidthSummary" name=currentBandwidthSummary>currentBandwidthSummary</a></span>
            <div class='views-field-body'>An object that provides commonly used bandwidth summary components for the current billing cycle. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Bandwidth_Summary'>SoftLayer_Metric_Tracking_Object_Bandwidth_Summary </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#details" name=details>details</a></span>
            <div class='views-field-body'>The bandwidth allotment detail records associated with this virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment_Detail'>SoftLayer_Network_Bandwidth_Version1_Allotment_Detail[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardware" name=hardware>hardware</a></span>
            <div class='views-field-body'>The hardware contained within a virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#inboundPublicBandwidthUsage" name=inboundPublicBandwidthUsage>inboundPublicBandwidthUsage</a></span>
            <div class='views-field-body'>The total public inbound bandwidth used in this virtual rack for an account's current billing cycle. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#locationGroup" name=locationGroup>locationGroup</a></span>
            <div class='views-field-body'>The location group associated with this virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Location_Group'>SoftLayer_Location_Group </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#managedBareMetalInstances" name=managedBareMetalInstances>managedBareMetalInstances</a></span>
            <div class='views-field-body'>The managed bare metal server instances contained within a virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#managedHardware" name=managedHardware>managedHardware</a></span>
            <div class='views-field-body'>The managed hardware contained within a virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#managedVirtualGuests" name=managedVirtualGuests>managedVirtualGuests</a></span>
            <div class='views-field-body'>The managed Virtual Server contained within a virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#metricTrackingObject" name=metricTrackingObject>metricTrackingObject</a></span>
            <div class='views-field-body'>A virtual rack's metric tracking object. This object records all periodic polled data available to this rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_VirtualDedicatedRack'>SoftLayer_Metric_Tracking_Object_VirtualDedicatedRack </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#metricTrackingObjectId" name=metricTrackingObjectId>metricTrackingObjectId</a></span>
            <div class='views-field-body'>The metric tracking object id for this allotment. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#outboundPublicBandwidthUsage" name=outboundPublicBandwidthUsage>outboundPublicBandwidthUsage</a></span>
            <div class='views-field-body'>The total public outbound bandwidth used in this virtual rack for an account's current billing cycle. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#overBandwidthAllocationFlag" name=overBandwidthAllocationFlag>overBandwidthAllocationFlag</a></span>
            <div class='views-field-body'>Whether the bandwidth usage for this bandwidth pool for the current billing cycle exceeds the allocation. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#privateNetworkOnlyHardware" name=privateNetworkOnlyHardware>privateNetworkOnlyHardware</a></span>
            <div class='views-field-body'>The private network only hardware contained within a virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#projectedOverBandwidthAllocationFlag" name=projectedOverBandwidthAllocationFlag>projectedOverBandwidthAllocationFlag</a></span>
            <div class='views-field-body'>Whether the bandwidth usage for this bandwidth pool for the current billing cycle is projected to exceed the allocation. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#projectedPublicBandwidthUsage" name=projectedPublicBandwidthUsage>projectedPublicBandwidthUsage</a></span>
            <div class='views-field-body'>The projected public outbound bandwidth for this virtual server for the current billing cycle. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>float</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serviceProvider" name=serviceProvider>serviceProvider</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Service_Provider'>SoftLayer_Service_Provider </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#totalBandwidthAllocated" name=totalBandwidthAllocated>totalBandwidthAllocated</a></span>
            <div class='views-field-body'>The combined allocated bandwidth for all servers in a virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsigned long</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#virtualGuests" name=virtualGuests>virtualGuests</a></span>
            <div class='views-field-body'>The Virtual Server contained within a virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#activeDetailCount" name=activeDetailCount>activeDetailCount</a></span>
            <div class='views-field-body'>A count of the bandwidth allotment detail records associated with this virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#applicationDeliveryControllerCount" name=applicationDeliveryControllerCount>applicationDeliveryControllerCount</a></span>
            <div class='views-field-body'>A count of the Application Delivery Controller contained within a virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#bareMetalInstanceCount" name=bareMetalInstanceCount>bareMetalInstanceCount</a></span>
            <div class='views-field-body'>A count of the bare metal server instances contained within a virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingCycleBandwidthUsageCount" name=billingCycleBandwidthUsageCount>billingCycleBandwidthUsageCount</a></span>
            <div class='views-field-body'>A count of a virtual rack's raw bandwidth usage data for an account's current billing cycle. One object is returned for each network this server is attached to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#detailCount" name=detailCount>detailCount</a></span>
            <div class='views-field-body'>A count of the bandwidth allotment detail records associated with this virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareCount" name=hardwareCount>hardwareCount</a></span>
            <div class='views-field-body'>A count of the hardware contained within a virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#managedBareMetalInstanceCount" name=managedBareMetalInstanceCount>managedBareMetalInstanceCount</a></span>
            <div class='views-field-body'>A count of the managed bare metal server instances contained within a virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#managedHardwareCount" name=managedHardwareCount>managedHardwareCount</a></span>
            <div class='views-field-body'>A count of the managed hardware contained within a virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#managedVirtualGuestCount" name=managedVirtualGuestCount>managedVirtualGuestCount</a></span>
            <div class='views-field-body'>A count of the managed Virtual Server contained within a virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#privateNetworkOnlyHardwareCount" name=privateNetworkOnlyHardwareCount>privateNetworkOnlyHardwareCount</a></span>
            <div class='views-field-body'>A count of the private network only hardware contained within a virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#virtualGuestCount" name=virtualGuestCount>virtualGuestCount</a></span>
            <div class='views-field-body'>A count of the Virtual Server contained within a virtual rack. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


