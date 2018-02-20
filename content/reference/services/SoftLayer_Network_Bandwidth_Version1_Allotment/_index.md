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
        
        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/createObject'> createObject</a> </span>
            <div class='views-field-body'>create a new allotment by passing in a allotment object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit a bandwidth allotment</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the account associated with this virtual rack.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getActiveDetails'> getActiveDetails</a> </span>
            <div class='views-field-body'>Retrieve the bandwidth allotment detail records associated with this virtual rack.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getApplicationDeliveryControllers'> getApplicationDeliveryControllers</a> </span>
            <div class='views-field-body'>Retrieve the Application Delivery Controller contained within a virtual rack.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getAverageDailyPublicBandwidthUsage'> getAverageDailyPublicBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the average daily public bandwidth usage for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBackendBandwidthByHour'> getBackendBandwidthByHour</a> </span>
            <div class='views-field-body'>return a collection of private usage objects that contain hourly incoming and outgoing network traffic amounts for a 24 hour period. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBackendBandwidthUse'> getBackendBandwidthUse</a> </span>
            <div class='views-field-body'>return a collection of private usage objects that contain hourly incoming and outgoing network traffic amounts for a customer date period. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBandwidthAllotmentType'> getBandwidthAllotmentType</a> </span>
            <div class='views-field-body'>Retrieve the bandwidth allotment type of this virtual rack.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBandwidthForDateRange'> getBandwidthForDateRange</a> </span>
            <div class='views-field-body'>Retrieve bandwidth data from a tracking object.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBandwidthImage'> getBandwidthImage</a> </span>
            <div class='views-field-body'>generate a graph image of all the bandwidth usage for an entire allotment of servers.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBareMetalInstances'> getBareMetalInstances</a> </span>
            <div class='views-field-body'>Retrieve the bare metal server instances contained within a virtual rack.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBillingCycleBandwidthUsage'> getBillingCycleBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve a virtual rack's raw bandwidth usage data for an account's current billing cycle. One object is returned for each network this server is attached to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBillingCyclePrivateBandwidthUsage'> getBillingCyclePrivateBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve a virtual rack's raw private network bandwidth usage data for an account's current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBillingCyclePublicBandwidthUsage'> getBillingCyclePublicBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve a virtual rack's raw public network bandwidth usage data for an account's current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBillingCyclePublicUsageTotal'> getBillingCyclePublicUsageTotal</a> </span>
            <div class='views-field-body'>Retrieve the total public bandwidth used in this virtual rack for an account's current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getBillingItem'> getBillingItem</a> </span>
            <div class='views-field-body'>Retrieve a virtual rack's billing item.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getCurrentBandwidthSummary'> getCurrentBandwidthSummary</a> </span>
            <div class='views-field-body'>Retrieve an object that provides commonly used bandwidth summary components for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getCustomBandwidthDataByDate'> getCustomBandwidthDataByDate</a> </span>
            <div class='views-field-body'>Retrieve bandwidth graph by date.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getDetails'> getDetails</a> </span>
            <div class='views-field-body'>Retrieve the bandwidth allotment detail records associated with this virtual rack.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getFrontendBandwidthByHour'> getFrontendBandwidthByHour</a> </span>
            <div class='views-field-body'>return a collection of public usage objects that contain hourly incoming and outgoing network traffic amounts for a 24 hour period. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getFrontendBandwidthUse'> getFrontendBandwidthUse</a> </span>
            <div class='views-field-body'>return a collection of public usage objects that contain hourly incoming and outgoing network traffic amounts for a 24 hour period. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getHardware'> getHardware</a> </span>
            <div class='views-field-body'>Retrieve the hardware contained within a virtual rack.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getInboundPublicBandwidthUsage'> getInboundPublicBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the total public inbound bandwidth used in this virtual rack for an account's current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getLocationGroup'> getLocationGroup</a> </span>
            <div class='views-field-body'>Retrieve the location group associated with this virtual rack.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getManagedBareMetalInstances'> getManagedBareMetalInstances</a> </span>
            <div class='views-field-body'>Retrieve the managed bare metal server instances contained within a virtual rack.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getManagedHardware'> getManagedHardware</a> </span>
            <div class='views-field-body'>Retrieve the managed hardware contained within a virtual rack.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getManagedVirtualGuests'> getManagedVirtualGuests</a> </span>
            <div class='views-field-body'>Retrieve the managed Virtual Server contained within a virtual rack.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getMetricTrackingObject'> getMetricTrackingObject</a> </span>
            <div class='views-field-body'>Retrieve a virtual rack's metric tracking object. This object records all periodic polled data available to this rack.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getMetricTrackingObjectId'> getMetricTrackingObjectId</a> </span>
            <div class='views-field-body'>Retrieve the metric tracking object id for this allotment.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_Bandwidth_Version1_Allotment record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getOutboundPublicBandwidthUsage'> getOutboundPublicBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the total public outbound bandwidth used in this virtual rack for an account's current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getOverBandwidthAllocationFlag'> getOverBandwidthAllocationFlag</a> </span>
            <div class='views-field-body'>Retrieve whether the bandwidth usage for this bandwidth pool for the current billing cycle exceeds the allocation.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getPrivateNetworkOnlyHardware'> getPrivateNetworkOnlyHardware</a> </span>
            <div class='views-field-body'>Retrieve the private network only hardware contained within a virtual rack.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getProjectedOverBandwidthAllocationFlag'> getProjectedOverBandwidthAllocationFlag</a> </span>
            <div class='views-field-body'>Retrieve whether the bandwidth usage for this bandwidth pool for the current billing cycle is projected to exceed the allocation.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getProjectedPublicBandwidthUsage'> getProjectedPublicBandwidthUsage</a> </span>
            <div class='views-field-body'>Retrieve the projected public outbound bandwidth for this virtual server for the current billing cycle.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getServiceProvider'> getServiceProvider</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getTotalBandwidthAllocated'> getTotalBandwidthAllocated</a> </span>
            <div class='views-field-body'>Retrieve the combined allocated bandwidth for all servers in a virtual rack.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getVdrMemberRecurringFee'> getVdrMemberRecurringFee</a> </span>
            <div class='views-field-body'>Gets the monthly recurring fee of a pooled server.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/getVirtualGuests'> getVirtualGuests</a> </span>
            <div class='views-field-body'>Retrieve the Virtual Server contained within a virtual rack.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/reassignServers'> reassignServers</a> </span>
            <div class='views-field-body'>reassign a collection of servers to a different allotment.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/requestVdrCancellation'> requestVdrCancellation</a> </span>
            <div class='views-field-body'>cancel a bandwidth pooling and assign contents, if any, to bandwidth pool.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/requestVdrContentUpdates'> requestVdrContentUpdates</a> </span>
            <div class='views-field-body'>Move servers into our out of a bandwidth pool.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/setVdrContent'> setVdrContent</a> </span>
            <div class='views-field-body'>Update bandwidth pool.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/unassignServers'> unassignServers</a> </span>
            <div class='views-field-body'>unassign a collection of servers from an allotment and insert them into the accounts VPR.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/voidPendingServerMove'> voidPendingServerMove</a> </span>
            <div class='views-field-body'>Void a pending server removal from this bandwidth pooling.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/voidPendingVdrCancellation'> voidPendingVdrCancellation</a> </span>
            <div class='views-field-body'>Void a pending cancellation on a bandwidth pool.</div>
        </div>
        </div>
</div>

