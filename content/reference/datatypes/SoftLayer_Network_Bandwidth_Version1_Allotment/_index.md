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
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Network_Bandwidth_Version1_Allotment class provides methods and data structures necessary to work with an array of hardware objects associated with a single Bandwidth Pooling. 





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
[accountId]: #accountid
#### [accountId]
The user account identifier associated with this allotment.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[bandwidthAllotmentTypeId]: #bandwidthallotmenttypeid
#### [bandwidthAllotmentTypeId]
An identifier marking this allotment as a virtual private rack (1) or a bandwidth pooling(2).  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
Creation date for an allotment.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[endDate]: #enddate
#### [endDate]
End date for an allotment.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A virtual rack's internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[locationGroupId]: #locationgroupid
#### [locationGroupId]
Location Group Id for an allotment  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
Text A virtual rack's name.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[serviceProviderId]: #serviceproviderid
#### [serviceProviderId]
Service Provider Id for an allotment  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account associated with this virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[activeDetails]: #activedetails
#### [activeDetails]
The bandwidth allotment detail records associated with this virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment_Detail'>SoftLayer_Network_Bandwidth_Version1_Allotment_Detail[] </a>**  



</div>
<div class="prop-row">

-----
[applicationDeliveryControllers]: #applicationdeliverycontrollers
#### [applicationDeliveryControllers]
The Application Delivery Controller contained within a virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller'>SoftLayer_Network_Application_Delivery_Controller[] </a>**  



</div>
<div class="prop-row">

-----
[averageDailyPublicBandwidthUsage]: #averagedailypublicbandwidthusage
#### [averageDailyPublicBandwidthUsage]
The average daily public bandwidth usage for the current billing cycle.  
<span class="type-label">Type: </span>**float**  



</div>
<div class="prop-row">

-----
[bandwidthAllotmentType]: #bandwidthallotmenttype
#### [bandwidthAllotmentType]
The bandwidth allotment type of this virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment_Type'>SoftLayer_Network_Bandwidth_Version1_Allotment_Type </a>**  



</div>
<div class="prop-row">

-----
[bareMetalInstances]: #baremetalinstances
#### [bareMetalInstances]
The bare metal server instances contained within a virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**  



</div>
<div class="prop-row">

-----
[billingCycleBandwidthUsage]: #billingcyclebandwidthusage
#### [billingCycleBandwidthUsage]
A virtual rack's raw bandwidth usage data for an account's current billing cycle. One object is returned for each network this server is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a>**  



</div>
<div class="prop-row">

-----
[billingCyclePrivateBandwidthUsage]: #billingcycleprivatebandwidthusage
#### [billingCyclePrivateBandwidthUsage]
A virtual rack's raw private network bandwidth usage data for an account's current billing cycle.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage </a>**  



</div>
<div class="prop-row">

-----
[billingCyclePublicBandwidthUsage]: #billingcyclepublicbandwidthusage
#### [billingCyclePublicBandwidthUsage]
A virtual rack's raw public network bandwidth usage data for an account's current billing cycle.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage </a>**  



</div>
<div class="prop-row">

-----
[billingCyclePublicUsageTotal]: #billingcyclepublicusagetotal
#### [billingCyclePublicUsageTotal]
The total public bandwidth used in this virtual rack for an account's current billing cycle.  
<span class="type-label">Type: </span>**unsigned integer**  



</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
A virtual rack's billing item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**  



</div>
<div class="prop-row">

-----
[currentBandwidthSummary]: #currentbandwidthsummary
#### [currentBandwidthSummary]
An object that provides commonly used bandwidth summary components for the current billing cycle.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Bandwidth_Summary'>SoftLayer_Metric_Tracking_Object_Bandwidth_Summary </a>**  



</div>
<div class="prop-row">

-----
[details]: #details
#### [details]
The bandwidth allotment detail records associated with this virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment_Detail'>SoftLayer_Network_Bandwidth_Version1_Allotment_Detail[] </a>**  



</div>
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
The hardware contained within a virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**  



</div>
<div class="prop-row">

-----
[inboundPublicBandwidthUsage]: #inboundpublicbandwidthusage
#### [inboundPublicBandwidthUsage]
The total public inbound bandwidth used in this virtual rack for an account's current billing cycle.  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[locationGroup]: #locationgroup
#### [locationGroup]
The location group associated with this virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Group'>SoftLayer_Location_Group </a>**  



</div>
<div class="prop-row">

-----
[managedBareMetalInstances]: #managedbaremetalinstances
#### [managedBareMetalInstances]
The managed bare metal server instances contained within a virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**  



</div>
<div class="prop-row">

-----
[managedHardware]: #managedhardware
#### [managedHardware]
The managed hardware contained within a virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**  



</div>
<div class="prop-row">

-----
[managedVirtualGuests]: #managedvirtualguests
#### [managedVirtualGuests]
The managed Virtual Server contained within a virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**  



</div>
<div class="prop-row">

-----
[metricTrackingObject]: #metrictrackingobject
#### [metricTrackingObject]
A virtual rack's metric tracking object. This object records all periodic polled data available to this rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_VirtualDedicatedRack'>SoftLayer_Metric_Tracking_Object_VirtualDedicatedRack </a>**  



</div>
<div class="prop-row">

-----
[metricTrackingObjectId]: #metrictrackingobjectid
#### [metricTrackingObjectId]
The metric tracking object id for this allotment.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[outboundPublicBandwidthUsage]: #outboundpublicbandwidthusage
#### [outboundPublicBandwidthUsage]
The total public outbound bandwidth used in this virtual rack for an account's current billing cycle.  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[overBandwidthAllocationFlag]: #overbandwidthallocationflag
#### [overBandwidthAllocationFlag]
Whether the bandwidth usage for this bandwidth pool for the current billing cycle exceeds the allocation.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[privateNetworkOnlyHardware]: #privatenetworkonlyhardware
#### [privateNetworkOnlyHardware]
The private network only hardware contained within a virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**  



</div>
<div class="prop-row">

-----
[projectedOverBandwidthAllocationFlag]: #projectedoverbandwidthallocationflag
#### [projectedOverBandwidthAllocationFlag]
Whether the bandwidth usage for this bandwidth pool for the current billing cycle is projected to exceed the allocation.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[projectedPublicBandwidthUsage]: #projectedpublicbandwidthusage
#### [projectedPublicBandwidthUsage]
The projected public outbound bandwidth for this virtual server for the current billing cycle.  
<span class="type-label">Type: </span>**float**  



</div>
<div class="prop-row">

-----
[serviceProvider]: #serviceprovider
#### [serviceProvider]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Service_Provider'>SoftLayer_Service_Provider </a>**  



</div>
<div class="prop-row">

-----
[totalBandwidthAllocated]: #totalbandwidthallocated
#### [totalBandwidthAllocated]
The combined allocated bandwidth for all servers in a virtual rack.  
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[virtualGuests]: #virtualguests
#### [virtualGuests]
The Virtual Server contained within a virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[activeDetailCount]: #activedetailcount
#### [activeDetailCount]
A count of the bandwidth allotment detail records associated with this virtual rack.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[applicationDeliveryControllerCount]: #applicationdeliverycontrollercount
#### [applicationDeliveryControllerCount]
A count of the Application Delivery Controller contained within a virtual rack.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[bareMetalInstanceCount]: #baremetalinstancecount
#### [bareMetalInstanceCount]
A count of the bare metal server instances contained within a virtual rack.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[billingCycleBandwidthUsageCount]: #billingcyclebandwidthusagecount
#### [billingCycleBandwidthUsageCount]
A count of a virtual rack's raw bandwidth usage data for an account's current billing cycle. One object is returned for each network this server is attached to.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[detailCount]: #detailcount
#### [detailCount]
A count of the bandwidth allotment detail records associated with this virtual rack.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[hardwareCount]: #hardwarecount
#### [hardwareCount]
A count of the hardware contained within a virtual rack.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[managedBareMetalInstanceCount]: #managedbaremetalinstancecount
#### [managedBareMetalInstanceCount]
A count of the managed bare metal server instances contained within a virtual rack.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[managedHardwareCount]: #managedhardwarecount
#### [managedHardwareCount]
A count of the managed hardware contained within a virtual rack.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[managedVirtualGuestCount]: #managedvirtualguestcount
#### [managedVirtualGuestCount]
A count of the managed Virtual Server contained within a virtual rack.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[privateNetworkOnlyHardwareCount]: #privatenetworkonlyhardwarecount
#### [privateNetworkOnlyHardwareCount]
A count of the private network only hardware contained within a virtual rack.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[virtualGuestCount]: #virtualguestcount
#### [virtualGuestCount]
A count of the Virtual Server contained within a virtual rack.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


