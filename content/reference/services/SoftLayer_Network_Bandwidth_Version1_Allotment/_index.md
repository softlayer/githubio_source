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
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [createObject](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/createObject)
create a new allotment by passing in a allotment object.

#### [editObject](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/editObject)
Edit a bandwidth allotment

#### [getAccount](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getAccount)
Retrieve the account associated with this virtual rack.

#### [getActiveDetails](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getActiveDetails)
Retrieve the bandwidth allotment detail records associated with this virtual rack.

#### [getApplicationDeliveryControllers](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getApplicationDeliveryControllers)
Retrieve the Application Delivery Controller contained within a virtual rack.

#### [getAverageDailyPublicBandwidthUsage](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getAverageDailyPublicBandwidthUsage)
Retrieve the average daily public bandwidth usage for the current billing cycle.

#### [getBackendBandwidthByHour](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBackendBandwidthByHour)
return a collection of private usage objects that contain hourly incoming and outgoing network traffic amounts for a 24 hour period. 

#### [getBackendBandwidthUse](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBackendBandwidthUse)
return a collection of private usage objects that contain hourly incoming and outgoing network traffic amounts for a customer date period. 

#### [getBandwidthAllotmentType](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBandwidthAllotmentType)
Retrieve the bandwidth allotment type of this virtual rack.

#### [getBandwidthForDateRange](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBandwidthForDateRange)
Retrieve bandwidth data from a tracking object.

#### [getBandwidthImage](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBandwidthImage)
generate a graph image of all the bandwidth usage for an entire allotment of servers.

#### [getBareMetalInstances](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBareMetalInstances)
Retrieve the bare metal server instances contained within a virtual rack.

#### [getBillingCycleBandwidthUsage](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBillingCycleBandwidthUsage)
Retrieve a virtual rack's raw bandwidth usage data for an account's current billing cycle. One object is returned for each network this server is attached to.

#### [getBillingCyclePrivateBandwidthUsage](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBillingCyclePrivateBandwidthUsage)
Retrieve a virtual rack's raw private network bandwidth usage data for an account's current billing cycle.

#### [getBillingCyclePublicBandwidthUsage](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBillingCyclePublicBandwidthUsage)
Retrieve a virtual rack's raw public network bandwidth usage data for an account's current billing cycle.

#### [getBillingCyclePublicUsageTotal](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBillingCyclePublicUsageTotal)
Retrieve the total public bandwidth used in this virtual rack for an account's current billing cycle.

#### [getBillingItem](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBillingItem)
Retrieve a virtual rack's billing item.

#### [getCurrentBandwidthSummary](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getCurrentBandwidthSummary)
Retrieve an object that provides commonly used bandwidth summary components for the current billing cycle.

#### [getCustomBandwidthDataByDate](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getCustomBandwidthDataByDate)
Retrieve bandwidth graph by date.

#### [getDetails](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getDetails)
Retrieve the bandwidth allotment detail records associated with this virtual rack.

#### [getFrontendBandwidthByHour](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getFrontendBandwidthByHour)
return a collection of public usage objects that contain hourly incoming and outgoing network traffic amounts for a 24 hour period. 

#### [getFrontendBandwidthUse](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getFrontendBandwidthUse)
return a collection of public usage objects that contain hourly incoming and outgoing network traffic amounts for a 24 hour period. 

#### [getHardware](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getHardware)
Retrieve the hardware contained within a virtual rack.

#### [getInboundPublicBandwidthUsage](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getInboundPublicBandwidthUsage)
Retrieve the total public inbound bandwidth used in this virtual rack for an account's current billing cycle.

#### [getLocationGroup](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getLocationGroup)
Retrieve the location group associated with this virtual rack.

#### [getManagedBareMetalInstances](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getManagedBareMetalInstances)
Retrieve the managed bare metal server instances contained within a virtual rack.

#### [getManagedHardware](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getManagedHardware)
Retrieve the managed hardware contained within a virtual rack.

#### [getManagedVirtualGuests](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getManagedVirtualGuests)
Retrieve the managed Virtual Server contained within a virtual rack.

#### [getMetricTrackingObject](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getMetricTrackingObject)
Retrieve a virtual rack's metric tracking object. This object records all periodic polled data available to this rack.

#### [getMetricTrackingObjectId](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getMetricTrackingObjectId)
Retrieve the metric tracking object id for this allotment.

#### [getObject](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getObject)
Retrieve a SoftLayer_Network_Bandwidth_Version1_Allotment record.

#### [getOutboundPublicBandwidthUsage](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getOutboundPublicBandwidthUsage)
Retrieve the total public outbound bandwidth used in this virtual rack for an account's current billing cycle.

#### [getOverBandwidthAllocationFlag](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getOverBandwidthAllocationFlag)
Retrieve whether the bandwidth usage for this bandwidth pool for the current billing cycle exceeds the allocation.

#### [getPrivateNetworkOnlyHardware](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getPrivateNetworkOnlyHardware)
Retrieve the private network only hardware contained within a virtual rack.

#### [getProjectedOverBandwidthAllocationFlag](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getProjectedOverBandwidthAllocationFlag)
Retrieve whether the bandwidth usage for this bandwidth pool for the current billing cycle is projected to exceed the allocation.

#### [getProjectedPublicBandwidthUsage](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getProjectedPublicBandwidthUsage)
Retrieve the projected public outbound bandwidth for this virtual server for the current billing cycle.

#### [getServiceProvider](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getServiceProvider)


#### [getTotalBandwidthAllocated](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getTotalBandwidthAllocated)
Retrieve the combined allocated bandwidth for all servers in a virtual rack.

#### [getVdrMemberRecurringFee](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getVdrMemberRecurringFee)
Gets the monthly recurring fee of a pooled server.

#### [getVirtualGuests](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getVirtualGuests)
Retrieve the Virtual Server contained within a virtual rack.

#### [reassignServers](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/reassignServers)
reassign a collection of servers to a different allotment.

#### [requestVdrCancellation](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/requestVdrCancellation)
cancel a bandwidth pooling and assign contents, if any, to bandwidth pool.

#### [requestVdrContentUpdates](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/requestVdrContentUpdates)
Move servers into our out of a bandwidth pool.

#### [setVdrContent](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/setVdrContent)
Update bandwidth pool.

#### [unassignServers](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/unassignServers)
unassign a collection of servers from an allotment and insert them into the accounts VPR.

#### [voidPendingServerMove](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/voidPendingServerMove)
Void a pending server removal from this bandwidth pooling.

#### [voidPendingVdrCancellation](/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/voidPendingVdrCancellation)
Void a pending cancellation on a bandwidth pool.

</div>

