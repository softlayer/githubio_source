---
title: "SoftLayer_Location_Datacenter"
description: "SoftLayer_Location_Datacenter exposes functionality to access datacenter-specific portions of SoftLayer's backend networ... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Datacenter"
---
# SoftLayer_Location_Datacenter
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Location_Datacenter' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Location_Datacenter' >Datatype</a></li>
    </ul>
</div>

## Description


SoftLayer_Location_Datacenter exposes functionality to access datacenter-specific portions of SoftLayer's backend network. SoftLayer maintains datacenters within it's location hierarchy. Datacenters are located in city locations and each contain server room locations, racks, then slots. Each slot location houses a piece of SoftLayer hardware. 



### seeAlso

* [SoftLayer_Location](/reference/services/SoftLayer_Location )


        
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

#### [getActiveItemPresaleEvents](/reference/services/SoftLayer_Location_Datacenter/getActiveItemPresaleEvents)


</div>

<div class="method-row">

#### [getActivePresaleEvents](/reference/services/SoftLayer_Location_Datacenter/getActivePresaleEvents)


</div>

<div class="method-row">

#### [getAvailableObjectStorageDatacenters](/reference/services/SoftLayer_Location_Datacenter/getAvailableObjectStorageDatacenters)
Get the datacenters where object storage is available

</div>

<div class="method-row">

#### [getBackboneDependents](/reference/services/SoftLayer_Location_Datacenter/getBackboneDependents)


</div>

<div class="method-row">

#### [getBackendHardwareRouters](/reference/services/SoftLayer_Location_Datacenter/getBackendHardwareRouters)


</div>

<div class="method-row">

#### [getBnppCompliantFlag](/reference/services/SoftLayer_Location_Datacenter/getBnppCompliantFlag)
Retrieve a flag indicating whether or not the datacenter/location is BNPP compliant.

</div>

<div class="method-row">

#### [getBoundSubnets](/reference/services/SoftLayer_Location_Datacenter/getBoundSubnets)
Retrieve subnets which are directly bound to one or more routers in a given datacenter, and currently allow routing.

</div>

<div class="method-row">

#### [getBrandCountryRestrictions](/reference/services/SoftLayer_Location_Datacenter/getBrandCountryRestrictions)
Retrieve this references relationship between brands, locations and countries associated with a user's account that are ineligible when ordering products. For example, the India datacenter may not be available on this brand for customers that live in Great Britain.

</div>

<div class="method-row">

#### [getDatacenters](/reference/services/SoftLayer_Location_Datacenter/getDatacenters)
Retrieve all datacenter locations

</div>

<div class="method-row">

#### [getDatacentersWithVirtualImageStoreServiceResourceRecord](/reference/services/SoftLayer_Location_Datacenter/getDatacentersWithVirtualImageStoreServiceResourceRecord)


</div>

<div class="method-row">

#### [getEuCompliantFlag](/reference/services/SoftLayer_Location_Datacenter/getEuCompliantFlag)
Retrieve a flag indicating whether or not the datacenter/location is EU compliant.

</div>

<div class="method-row">

#### [getFrontendHardwareRouters](/reference/services/SoftLayer_Location_Datacenter/getFrontendHardwareRouters)


</div>

<div class="method-row">

#### [getGroups](/reference/services/SoftLayer_Location_Datacenter/getGroups)
Retrieve a location can be a member of 1 or more groups. This will show which groups to which a location belongs.

</div>

<div class="method-row">

#### [getHardwareFirewalls](/reference/services/SoftLayer_Location_Datacenter/getHardwareFirewalls)


</div>

<div class="method-row">

#### [getHardwareRouters](/reference/services/SoftLayer_Location_Datacenter/getHardwareRouters)


</div>

<div class="method-row">

#### [getLocationAddress](/reference/services/SoftLayer_Location_Datacenter/getLocationAddress)
Retrieve a location's physical address.

</div>

<div class="method-row">

#### [getLocationAddresses](/reference/services/SoftLayer_Location_Datacenter/getLocationAddresses)
Retrieve a location's physical addresses.

</div>

<div class="method-row">

#### [getLocationReservationMember](/reference/services/SoftLayer_Location_Datacenter/getLocationReservationMember)
Retrieve a location's Dedicated Rack member

</div>

<div class="method-row">

#### [getLocationStatus](/reference/services/SoftLayer_Location_Datacenter/getLocationStatus)
Retrieve the current locations status.

</div>

<div class="method-row">

#### [getNetworkConfigurationAttribute](/reference/services/SoftLayer_Location_Datacenter/getNetworkConfigurationAttribute)


</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Location_Datacenter/getObject)
Retrieve a SoftLayer_Location_Datacenter record.

</div>

<div class="method-row">

#### [getOnlineSslVpnUserCount](/reference/services/SoftLayer_Location_Datacenter/getOnlineSslVpnUserCount)
Retrieve the total number of users online using SoftLayer's SSL VPN service for a location.

</div>

<div class="method-row">

#### [getPathString](/reference/services/SoftLayer_Location_Datacenter/getPathString)


</div>

<div class="method-row">

#### [getPresaleEvents](/reference/services/SoftLayer_Location_Datacenter/getPresaleEvents)


</div>

<div class="method-row">

#### [getPriceGroups](/reference/services/SoftLayer_Location_Datacenter/getPriceGroups)
Retrieve a location can be a member of 1 or more Price Groups. This will show which groups to which a location belongs.

</div>

<div class="method-row">

#### [getRegionalGroup](/reference/services/SoftLayer_Location_Datacenter/getRegionalGroup)
Retrieve the regional group this datacenter belongs to.

</div>

<div class="method-row">

#### [getRegionalInternetRegistry](/reference/services/SoftLayer_Location_Datacenter/getRegionalInternetRegistry)


</div>

<div class="method-row">

#### [getRegions](/reference/services/SoftLayer_Location_Datacenter/getRegions)
Retrieve a location can be a member of 1 or more regions. This will show which regions to which a location belongs.

</div>

<div class="method-row">

#### [getRoutableBoundSubnets](/reference/services/SoftLayer_Location_Datacenter/getRoutableBoundSubnets)
Retrieve retrieve all subnets that are eligible to be routed; those which the account has permission to associate with a vlan.

</div>

<div class="method-row">

#### [getStatisticsGraphImage](/reference/services/SoftLayer_Location_Datacenter/getStatisticsGraphImage)
Retrieve a graph of a SoftLayer datacenter's last 48 hours of network activity.

</div>

<div class="method-row">

#### [getTimezone](/reference/services/SoftLayer_Location_Datacenter/getTimezone)


</div>

<div class="method-row">

#### [getVdrGroup](/reference/services/SoftLayer_Location_Datacenter/getVdrGroup)
Retrieve a location can be a member of 1 Bandwidth Pooling Group. This will show which group to which a location belongs.

</div>

<div class="method-row">

#### [getViewableDatacenters](/reference/services/SoftLayer_Location_Datacenter/getViewableDatacenters)
Retrieve all datacenter locations

</div>

<div class="method-row">

#### [getViewablePopsAndDataCenters](/reference/services/SoftLayer_Location_Datacenter/getViewablePopsAndDataCenters)
Retrieve viewable pops and datacenters in a combined list.

</div>

<div class="method-row">

#### [getViewablepointOfPresence](/reference/services/SoftLayer_Location_Datacenter/getViewablepointOfPresence)
Retrieve viewable network locations

</div>

<div class="method-row">

#### [getpointOfPresence](/reference/services/SoftLayer_Location_Datacenter/getpointOfPresence)
Retrieve all points of presence locations

</div>
</div>

</div>

