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
[accountId]: #accountid
#### [accountId]
The user account identifier associated with this allotment.  
<span class="type-label">Type: </span>**integer**

-----
[bandwidthAllotmentTypeId]: #bandwidthallotmenttypeid
#### [bandwidthAllotmentTypeId]
An identifier marking this allotment as a virtual private rack (1) or a bandwidth pooling(2).  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
Creation date for an allotment.  
<span class="type-label">Type: </span>**dateTime**

-----
[endDate]: #enddate
#### [endDate]
End date for an allotment.  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
A virtual rack's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[locationGroupId]: #locationgroupid
#### [locationGroupId]
Location Group Id for an allotment  
<span class="type-label">Type: </span>**integer**

-----
[name]: #name
#### [name]
Text A virtual rack's name.  
<span class="type-label">Type: </span>**string**

-----
[serviceProviderId]: #serviceproviderid
#### [serviceProviderId]
Service Provider Id for an allotment  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account associated with this virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[activeDetails]: #activedetails
#### [activeDetails]
The bandwidth allotment detail records associated with this virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment_Detail'>SoftLayer_Network_Bandwidth_Version1_Allotment_Detail[] </a>**

-----
[applicationDeliveryControllers]: #applicationdeliverycontrollers
#### [applicationDeliveryControllers]
The Application Delivery Controller contained within a virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller'>SoftLayer_Network_Application_Delivery_Controller[] </a>**

-----
[averageDailyPublicBandwidthUsage]: #averagedailypublicbandwidthusage
#### [averageDailyPublicBandwidthUsage]
The average daily public bandwidth usage for the current billing cycle.  
<span class="type-label">Type: </span>**float**

-----
[bandwidthAllotmentType]: #bandwidthallotmenttype
#### [bandwidthAllotmentType]
The bandwidth allotment type of this virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment_Type'>SoftLayer_Network_Bandwidth_Version1_Allotment_Type </a>**

-----
[bareMetalInstances]: #baremetalinstances
#### [bareMetalInstances]
The bare metal server instances contained within a virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[billingCycleBandwidthUsage]: #billingcyclebandwidthusage
#### [billingCycleBandwidthUsage]
A virtual rack's raw bandwidth usage data for an account's current billing cycle. One object is returned for each network this server is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a>**

-----
[billingCyclePrivateBandwidthUsage]: #billingcycleprivatebandwidthusage
#### [billingCyclePrivateBandwidthUsage]
A virtual rack's raw private network bandwidth usage data for an account's current billing cycle.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage </a>**

-----
[billingCyclePublicBandwidthUsage]: #billingcyclepublicbandwidthusage
#### [billingCyclePublicBandwidthUsage]
A virtual rack's raw public network bandwidth usage data for an account's current billing cycle.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage </a>**

-----
[billingCyclePublicUsageTotal]: #billingcyclepublicusagetotal
#### [billingCyclePublicUsageTotal]
The total public bandwidth used in this virtual rack for an account's current billing cycle.  
<span class="type-label">Type: </span>**unsigned integer**

-----
[billingItem]: #billingitem
#### [billingItem]
A virtual rack's billing item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**

-----
[currentBandwidthSummary]: #currentbandwidthsummary
#### [currentBandwidthSummary]
An object that provides commonly used bandwidth summary components for the current billing cycle.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Bandwidth_Summary'>SoftLayer_Metric_Tracking_Object_Bandwidth_Summary </a>**

-----
[details]: #details
#### [details]
The bandwidth allotment detail records associated with this virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment_Detail'>SoftLayer_Network_Bandwidth_Version1_Allotment_Detail[] </a>**

-----
[hardware]: #hardware
#### [hardware]
The hardware contained within a virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[inboundPublicBandwidthUsage]: #inboundpublicbandwidthusage
#### [inboundPublicBandwidthUsage]
The total public inbound bandwidth used in this virtual rack for an account's current billing cycle.  
<span class="type-label">Type: </span>**decimal**

-----
[locationGroup]: #locationgroup
#### [locationGroup]
The location group associated with this virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Group'>SoftLayer_Location_Group </a>**

-----
[managedBareMetalInstances]: #managedbaremetalinstances
#### [managedBareMetalInstances]
The managed bare metal server instances contained within a virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[managedHardware]: #managedhardware
#### [managedHardware]
The managed hardware contained within a virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[managedVirtualGuests]: #managedvirtualguests
#### [managedVirtualGuests]
The managed Virtual Server contained within a virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[metricTrackingObject]: #metrictrackingobject
#### [metricTrackingObject]
A virtual rack's metric tracking object. This object records all periodic polled data available to this rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_VirtualDedicatedRack'>SoftLayer_Metric_Tracking_Object_VirtualDedicatedRack </a>**

-----
[metricTrackingObjectId]: #metrictrackingobjectid
#### [metricTrackingObjectId]
The metric tracking object id for this allotment.  
<span class="type-label">Type: </span>**integer**

-----
[outboundPublicBandwidthUsage]: #outboundpublicbandwidthusage
#### [outboundPublicBandwidthUsage]
The total public outbound bandwidth used in this virtual rack for an account's current billing cycle.  
<span class="type-label">Type: </span>**decimal**

-----
[overBandwidthAllocationFlag]: #overbandwidthallocationflag
#### [overBandwidthAllocationFlag]
Whether the bandwidth usage for this bandwidth pool for the current billing cycle exceeds the allocation.  
<span class="type-label">Type: </span>**integer**

-----
[privateNetworkOnlyHardware]: #privatenetworkonlyhardware
#### [privateNetworkOnlyHardware]
The private network only hardware contained within a virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**

-----
[projectedOverBandwidthAllocationFlag]: #projectedoverbandwidthallocationflag
#### [projectedOverBandwidthAllocationFlag]
Whether the bandwidth usage for this bandwidth pool for the current billing cycle is projected to exceed the allocation.  
<span class="type-label">Type: </span>**integer**

-----
[projectedPublicBandwidthUsage]: #projectedpublicbandwidthusage
#### [projectedPublicBandwidthUsage]
The projected public outbound bandwidth for this virtual server for the current billing cycle.  
<span class="type-label">Type: </span>**float**

-----
[serviceProvider]: #serviceprovider
#### [serviceProvider]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Service_Provider'>SoftLayer_Service_Provider </a>**

-----
[totalBandwidthAllocated]: #totalbandwidthallocated
#### [totalBandwidthAllocated]
The combined allocated bandwidth for all servers in a virtual rack.  
<span class="type-label">Type: </span>**unsigned long**

-----
[virtualGuests]: #virtualguests
#### [virtualGuests]
The Virtual Server contained within a virtual rack.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


## Count

-----
[activeDetailCount]: #activedetailcount
#### [activeDetailCount]
A count of the bandwidth allotment detail records associated with this virtual rack.   
<span class="type-label">Type: </span>**unsigned long**


-----
[applicationDeliveryControllerCount]: #applicationdeliverycontrollercount
#### [applicationDeliveryControllerCount]
A count of the Application Delivery Controller contained within a virtual rack.   
<span class="type-label">Type: </span>**unsigned long**


-----
[bareMetalInstanceCount]: #baremetalinstancecount
#### [bareMetalInstanceCount]
A count of the bare metal server instances contained within a virtual rack.   
<span class="type-label">Type: </span>**unsigned long**


-----
[billingCycleBandwidthUsageCount]: #billingcyclebandwidthusagecount
#### [billingCycleBandwidthUsageCount]
A count of a virtual rack's raw bandwidth usage data for an account's current billing cycle. One object is returned for each network this server is attached to.   
<span class="type-label">Type: </span>**unsigned long**


-----
[detailCount]: #detailcount
#### [detailCount]
A count of the bandwidth allotment detail records associated with this virtual rack.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardwareCount]: #hardwarecount
#### [hardwareCount]
A count of the hardware contained within a virtual rack.   
<span class="type-label">Type: </span>**unsigned long**


-----
[managedBareMetalInstanceCount]: #managedbaremetalinstancecount
#### [managedBareMetalInstanceCount]
A count of the managed bare metal server instances contained within a virtual rack.   
<span class="type-label">Type: </span>**unsigned long**


-----
[managedHardwareCount]: #managedhardwarecount
#### [managedHardwareCount]
A count of the managed hardware contained within a virtual rack.   
<span class="type-label">Type: </span>**unsigned long**


-----
[managedVirtualGuestCount]: #managedvirtualguestcount
#### [managedVirtualGuestCount]
A count of the managed Virtual Server contained within a virtual rack.   
<span class="type-label">Type: </span>**unsigned long**


-----
[privateNetworkOnlyHardwareCount]: #privatenetworkonlyhardwarecount
#### [privateNetworkOnlyHardwareCount]
A count of the private network only hardware contained within a virtual rack.   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualGuestCount]: #virtualguestcount
#### [virtualGuestCount]
A count of the Virtual Server contained within a virtual rack.   
<span class="type-label">Type: </span>**unsigned long**

</div>


