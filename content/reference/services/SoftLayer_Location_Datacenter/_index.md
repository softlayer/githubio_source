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
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [getActiveItemPresaleEvents](/reference/services/SoftLayer_Location_Datacenter/getActiveItemPresaleEvents)


#### [getActivePresaleEvents](/reference/services/SoftLayer_Location_Datacenter/getActivePresaleEvents)


#### [getAvailableObjectStorageDatacenters](/reference/services/SoftLayer_Location_Datacenter/getAvailableObjectStorageDatacenters)
Get the datacenters where object storage is available

#### [getBackboneDependents](/reference/services/SoftLayer_Location_Datacenter/getBackboneDependents)


#### [getBackendHardwareRouters](/reference/services/SoftLayer_Location_Datacenter/getBackendHardwareRouters)


#### [getBoundSubnets](/reference/services/SoftLayer_Location_Datacenter/getBoundSubnets)
Retrieve subnets which are directly bound to one or more routers in a given datacenter, and currently allow routing.

#### [getBrandCountryRestrictions](/reference/services/SoftLayer_Location_Datacenter/getBrandCountryRestrictions)
Retrieve this references relationship between brands, locations and countries associated with a user's account that are ineligible when ordering products. For example, the India datacenter may not be available on this brand for customers that live in Great Britain.

#### [getDatacenters](/reference/services/SoftLayer_Location_Datacenter/getDatacenters)
Retrieve all datacenter locations

#### [getDatacentersWithVirtualImageStoreServiceResourceRecord](/reference/services/SoftLayer_Location_Datacenter/getDatacentersWithVirtualImageStoreServiceResourceRecord)


#### [getEuCompliantFlag](/reference/services/SoftLayer_Location_Datacenter/getEuCompliantFlag)
Retrieve a flag indicating whether or not the datacenter/location is EU compliant.

#### [getFrontendHardwareRouters](/reference/services/SoftLayer_Location_Datacenter/getFrontendHardwareRouters)


#### [getGroups](/reference/services/SoftLayer_Location_Datacenter/getGroups)
Retrieve a location can be a member of 1 or more groups. This will show which groups to which a location belongs.

#### [getHardwareFirewalls](/reference/services/SoftLayer_Location_Datacenter/getHardwareFirewalls)


#### [getHardwareRouters](/reference/services/SoftLayer_Location_Datacenter/getHardwareRouters)


#### [getLocationAddress](/reference/services/SoftLayer_Location_Datacenter/getLocationAddress)
Retrieve a location's physical address.

#### [getLocationAddresses](/reference/services/SoftLayer_Location_Datacenter/getLocationAddresses)
Retrieve a location's physical addresses.

#### [getLocationReservationMember](/reference/services/SoftLayer_Location_Datacenter/getLocationReservationMember)
Retrieve a location's Dedicated Rack member

#### [getLocationStatus](/reference/services/SoftLayer_Location_Datacenter/getLocationStatus)
Retrieve the current locations status.

#### [getNetworkConfigurationAttribute](/reference/services/SoftLayer_Location_Datacenter/getNetworkConfigurationAttribute)


#### [getObject](/reference/services/SoftLayer_Location_Datacenter/getObject)
Retrieve a SoftLayer_Location_Datacenter record.

#### [getOnlinePptpVpnUserCount](/reference/services/SoftLayer_Location_Datacenter/getOnlinePptpVpnUserCount)
Retrieve the total number of users online using SoftLayer's PPTP VPN service for a location.

#### [getOnlineSslVpnUserCount](/reference/services/SoftLayer_Location_Datacenter/getOnlineSslVpnUserCount)
Retrieve the total number of users online using SoftLayer's SSL VPN service for a location.

#### [getPathString](/reference/services/SoftLayer_Location_Datacenter/getPathString)


#### [getPresaleEvents](/reference/services/SoftLayer_Location_Datacenter/getPresaleEvents)


#### [getPriceGroups](/reference/services/SoftLayer_Location_Datacenter/getPriceGroups)
Retrieve a location can be a member of 1 or more Price Groups. This will show which groups to which a location belongs.

#### [getRegionalGroup](/reference/services/SoftLayer_Location_Datacenter/getRegionalGroup)
Retrieve the regional group this datacenter belongs to.

#### [getRegionalInternetRegistry](/reference/services/SoftLayer_Location_Datacenter/getRegionalInternetRegistry)


#### [getRegions](/reference/services/SoftLayer_Location_Datacenter/getRegions)
Retrieve a location can be a member of 1 or more regions. This will show which regions to which a location belongs.

#### [getRoutableBoundSubnets](/reference/services/SoftLayer_Location_Datacenter/getRoutableBoundSubnets)
Retrieve retrieve all subnets that are eligible to be routed; those which the account has permission to associate with a vlan.

#### [getStatisticsGraphImage](/reference/services/SoftLayer_Location_Datacenter/getStatisticsGraphImage)
Retrieve a graph of a SoftLayer datacenter's last 48 hours of network activity.

#### [getTimezone](/reference/services/SoftLayer_Location_Datacenter/getTimezone)


#### [getVdrGroup](/reference/services/SoftLayer_Location_Datacenter/getVdrGroup)
Retrieve a location can be a member of 1 Bandwidth Pooling Group. This will show which group to which a location belongs.

#### [getViewableDatacenters](/reference/services/SoftLayer_Location_Datacenter/getViewableDatacenters)
Retrieve all datacenter locations

#### [getViewablePopsAndDataCenters](/reference/services/SoftLayer_Location_Datacenter/getViewablePopsAndDataCenters)
Retrieve viewable pops and datacenters in a combined list.

#### [getViewablepointOfPresence](/reference/services/SoftLayer_Location_Datacenter/getViewablepointOfPresence)
Retrieve viewable network locations

#### [getpointOfPresence](/reference/services/SoftLayer_Location_Datacenter/getpointOfPresence)
Retrieve all points of presence locations

</div>

