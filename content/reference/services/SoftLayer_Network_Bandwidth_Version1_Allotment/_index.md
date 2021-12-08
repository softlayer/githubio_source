---
title: "SoftLayer_Network_Bandwidth_Version1_Allotment"
description: "Every SoftLayer Bandwidth Pooling, Virtual Datacenter, Virtual Private Rack(VPR) is defined in the SoftLayer_Network_Ban... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
---
# SoftLayer_Network_Bandwidth_Version1_Allotment
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment' >Datatype</a></li>
    </ul>
</div>

## Description


Every SoftLayer Bandwidth Pooling, Virtual Datacenter, Virtual Private Rack(VPR) is defined in the SoftLayer_Network_Bandwidth_Version1_Allotment service as an allotment. SoftLayer allotments are a collection of servers that share all of the servers allocated bandwidth together. 

Virtual Private Rack Each server is by default a part of your Virtual Private Rack. Bandwidth overages are billed individually per server for all hardware in your Virtual Private Rack. If any one server uses more bandwidth than it is allocated, an overage charge will result. 

Bandwidth Pooling Bandwidth Pooling allow you to optimize your bandwidth usage by "pooling" all of the bandwidth together for servers in a Bandwidth Pooling. Bandwidth overages for servers in a Bandwidth Pooling are summed up as a whole and overages are calculated only if the total bandwidth of all servers exceeds the total allocated bandwidth for all servers. 

For example, if you had 5 servers, each with 2000 GB of bandwidth, and one server used 3000 GB of bandwidth while the other used only 1500 GB of bandwidth, you would not be billed for an overage because your total usage would be 9000 GB and your total allocated would be 10000 GB. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [createObject](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/createObject)
create a new allotment by passing in a allotment object.

</div>

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/editObject)
Edit a bandwidth allotment

</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getAccount)
Retrieve the account associated with this virtual rack.

</div>

<div class="method-row">

#### [getActiveDetails](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getActiveDetails)
Retrieve the bandwidth allotment detail records associated with this virtual rack.

</div>

<div class="method-row">

#### [getApplicationDeliveryControllers](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getApplicationDeliveryControllers)
Retrieve the Application Delivery Controller contained within a virtual rack.

</div>

<div class="method-row">

#### [getAverageDailyPublicBandwidthUsage](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getAverageDailyPublicBandwidthUsage)
Retrieve the average daily public bandwidth usage for the current billing cycle.

</div>

<div class="method-row deprecated">

#### [getBackendBandwidthByHour](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBackendBandwidthByHour)
[DEPRECATED] return a collection of private usage objects that contain hourly incoming and outgoing network traffic amounts for a 24 hour period. 

<span class="deprecation-label">Deprecated  </span>


</div>

<div class="method-row">

#### [getBackendBandwidthUse](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBackendBandwidthUse)
return a collection of private usage objects that contain hourly incoming and outgoing network traffic amounts for a customer date period. 

</div>

<div class="method-row">

#### [getBandwidthAllotmentType](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBandwidthAllotmentType)
Retrieve the bandwidth allotment type of this virtual rack.

</div>

<div class="method-row">

#### [getBandwidthForDateRange](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBandwidthForDateRange)
Retrieve bandwidth data from a tracking object.

</div>

<div class="method-row">

#### [getBandwidthImage](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBandwidthImage)
generate a graph image of all the bandwidth usage for an entire allotment of servers.

</div>

<div class="method-row">

#### [getBareMetalInstances](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBareMetalInstances)
Retrieve the bare metal server instances contained within a virtual rack.

</div>

<div class="method-row">

#### [getBillingCycleBandwidthUsage](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBillingCycleBandwidthUsage)
Retrieve a virtual rack's raw bandwidth usage data for an account's current billing cycle. One object is returned for each network this server is attached to.

</div>

<div class="method-row">

#### [getBillingCyclePrivateBandwidthUsage](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBillingCyclePrivateBandwidthUsage)
Retrieve a virtual rack's raw private network bandwidth usage data for an account's current billing cycle.

</div>

<div class="method-row">

#### [getBillingCyclePublicBandwidthUsage](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBillingCyclePublicBandwidthUsage)
Retrieve a virtual rack's raw public network bandwidth usage data for an account's current billing cycle.

</div>

<div class="method-row">

#### [getBillingCyclePublicUsageTotal](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBillingCyclePublicUsageTotal)
Retrieve the total public bandwidth used in this virtual rack for an account's current billing cycle.

</div>

<div class="method-row">

#### [getBillingItem](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBillingItem)
Retrieve a virtual rack's billing item.

</div>

<div class="method-row">

#### [getCurrentBandwidthSummary](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getCurrentBandwidthSummary)
Retrieve an object that provides commonly used bandwidth summary components for the current billing cycle.

</div>

<div class="method-row">

#### [getCustomBandwidthDataByDate](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getCustomBandwidthDataByDate)
Retrieve bandwidth graph by date.

</div>

<div class="method-row">

#### [getDetails](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getDetails)
Retrieve the bandwidth allotment detail records associated with this virtual rack.

</div>

<div class="method-row deprecated">

#### [getFrontendBandwidthByHour](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getFrontendBandwidthByHour)
[DEPRECATED] return a collection of public usage objects that contain hourly incoming and outgoing network traffic amounts for a 24 hour period. 

<span class="deprecation-label">Deprecated  </span>


</div>

<div class="method-row">

#### [getFrontendBandwidthUse](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getFrontendBandwidthUse)
return a collection of public usage objects that contain hourly incoming and outgoing network traffic amounts for a 24 hour period. 

</div>

<div class="method-row">

#### [getHardware](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getHardware)
Retrieve the hardware contained within a virtual rack.

</div>

<div class="method-row">

#### [getInboundPublicBandwidthUsage](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getInboundPublicBandwidthUsage)
Retrieve the total public inbound bandwidth used in this virtual rack for an account's current billing cycle.

</div>

<div class="method-row">

#### [getLocationGroup](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getLocationGroup)
Retrieve the location group associated with this virtual rack.

</div>

<div class="method-row">

#### [getManagedBareMetalInstances](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getManagedBareMetalInstances)
Retrieve the managed bare metal server instances contained within a virtual rack.

</div>

<div class="method-row">

#### [getManagedHardware](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getManagedHardware)
Retrieve the managed hardware contained within a virtual rack.

</div>

<div class="method-row">

#### [getManagedVirtualGuests](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getManagedVirtualGuests)
Retrieve the managed Virtual Server contained within a virtual rack.

</div>

<div class="method-row">

#### [getMetricTrackingObject](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getMetricTrackingObject)
Retrieve a virtual rack's metric tracking object. This object records all periodic polled data available to this rack.

</div>

<div class="method-row">

#### [getMetricTrackingObjectId](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getMetricTrackingObjectId)
Retrieve the metric tracking object id for this allotment.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getObject)
Retrieve a SoftLayer_Network_Bandwidth_Version1_Allotment record.

</div>

<div class="method-row">

#### [getOutboundPublicBandwidthUsage](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getOutboundPublicBandwidthUsage)
Retrieve the total public outbound bandwidth used in this virtual rack for an account's current billing cycle.

</div>

<div class="method-row">

#### [getOverBandwidthAllocationFlag](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getOverBandwidthAllocationFlag)
Retrieve whether the bandwidth usage for this bandwidth pool for the current billing cycle exceeds the allocation.

</div>

<div class="method-row">

#### [getPrivateNetworkOnlyHardware](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getPrivateNetworkOnlyHardware)
Retrieve the private network only hardware contained within a virtual rack.

</div>

<div class="method-row">

#### [getProjectedOverBandwidthAllocationFlag](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getProjectedOverBandwidthAllocationFlag)
Retrieve whether the bandwidth usage for this bandwidth pool for the current billing cycle is projected to exceed the allocation.

</div>

<div class="method-row">

#### [getProjectedPublicBandwidthUsage](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getProjectedPublicBandwidthUsage)
Retrieve the projected public outbound bandwidth for this virtual server for the current billing cycle.

</div>

<div class="method-row">

#### [getServiceProvider](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getServiceProvider)


</div>

<div class="method-row">

#### [getTotalBandwidthAllocated](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getTotalBandwidthAllocated)
Retrieve the combined allocated bandwidth for all servers in a virtual rack.

</div>

<div class="method-row">

#### [getVdrMemberRecurringFee](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getVdrMemberRecurringFee)
Gets the monthly recurring fee of a pooled server.

</div>

<div class="method-row">

#### [getVirtualGuests](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getVirtualGuests)
Retrieve the Virtual Server contained within a virtual rack.

</div>

<div class="method-row">

#### [reassignServers](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/reassignServers)
reassign a collection of servers to a different allotment.

</div>

<div class="method-row">

#### [requestVdrCancellation](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/requestVdrCancellation)
cancel a bandwidth pooling and assign contents, if any, to bandwidth pool.

</div>

<div class="method-row">

#### [requestVdrContentUpdates](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/requestVdrContentUpdates)
Move servers into our out of a bandwidth pool.

</div>

<div class="method-row">

#### [setVdrContent](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/setVdrContent)
Update bandwidth pool.

</div>

<div class="method-row">

#### [unassignServers](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/unassignServers)
unassign a collection of servers from an allotment and insert them into the accounts VPR.

</div>

<div class="method-row">

#### [voidPendingServerMove](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/voidPendingServerMove)
Void a pending server removal from this bandwidth pooling.

</div>

<div class="method-row">

#### [voidPendingVdrCancellation](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/voidPendingVdrCancellation)
Void a pending cancellation on a bandwidth pool.

</div>
</div>

</div>

