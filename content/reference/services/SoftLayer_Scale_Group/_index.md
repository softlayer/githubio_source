---
title: "SoftLayer_Scale_Group"
description: "A scale group can contain a number of guest members which can fluctuate up and down, staying within a defined range, man... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Group"
---
# SoftLayer_Scale_Group
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Scale_Group' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Scale_Group' >Datatype</a></li>
    </ul>
</div>

## Description
A scale group can contain a number of guest members which can fluctuate up and down, staying within a defined range, manually or automatically based on policies given. Groups are set of VLANs to be placed behind. Groups can also have static hardware/guests pinned to the group. These static resources can be used to effect things like moving averages for policy triggers but are not counted as group members and are not subject to automatic reclaim. 



        
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

#### [createObject](/reference/services/SoftLayer_Scale_Group/createObject)
Create a scale group. 

#### [deleteObject](/reference/services/SoftLayer_Scale_Group/deleteObject)
Delete this group. This can only be done on an empty, active group. 

#### [editObject](/reference/services/SoftLayer_Scale_Group/editObject)
Edit this group. 

#### [forceDeleteObject](/reference/services/SoftLayer_Scale_Group/forceDeleteObject)
Delete this group and destroy all members of it.

#### [getAccount](/reference/services/SoftLayer_Scale_Group/getAccount)
Retrieve the account for this scaling group.

#### [getAvailableHourlyInstanceLimit](/reference/services/SoftLayer_Scale_Group/getAvailableHourlyInstanceLimit)
This returns the number of hourly instances an account can add from this point. 

#### [getAvailableRegionalGroups](/reference/services/SoftLayer_Scale_Group/getAvailableRegionalGroups)
Get the regional groups available for use by scaling groups. This also includes datacenter children that are available. 

#### [getLoadBalancers](/reference/services/SoftLayer_Scale_Group/getLoadBalancers)
Retrieve collection of load balancers for this auto scale group.

#### [getLogs](/reference/services/SoftLayer_Scale_Group/getLogs)
Retrieve collection of log entries for this group.

#### [getNetworkVlans](/reference/services/SoftLayer_Scale_Group/getNetworkVlans)
Retrieve collection of VLANs for this auto scale group. VLANs are optional. This can contain a public or private VLAN or both. When a single VLAN for a public/private type is given it can be a non-purchased VLAN only if the minimumMemberCount on the group is >= 1. This can also contain any number of public/private purchased VLANs and members are staggered across them when scaled up.

#### [getObject](/reference/services/SoftLayer_Scale_Group/getObject)
Retrieve a SoftLayer_Scale_Group record.

#### [getPolicies](/reference/services/SoftLayer_Scale_Group/getPolicies)
Retrieve collection of policies for this group. This can be empty.

#### [getRegionalGroup](/reference/services/SoftLayer_Scale_Group/getRegionalGroup)
Retrieve the regional group for this scale group.

#### [getStatus](/reference/services/SoftLayer_Scale_Group/getStatus)
Retrieve the status for this scale group.

#### [getTerminationPolicy](/reference/services/SoftLayer_Scale_Group/getTerminationPolicy)
Retrieve the termination policy for this scaling group.

#### [getVirtualGuestAssets](/reference/services/SoftLayer_Scale_Group/getVirtualGuestAssets)
Retrieve collection of guests that have been pinned to this group. Guest assets are only used for certain trigger checks such as resource watches. They do not count towards the auto scaling guest counts of this group in anyway and are never automatically added or removed.

#### [getVirtualGuestMembers](/reference/services/SoftLayer_Scale_Group/getVirtualGuestMembers)
Retrieve collection of guests that have been scaled with the group. When this group is active, the count of guests here is guaranteed to be between minimumMemberCount and maximumMemberCount inclusively.

#### [resume](/reference/services/SoftLayer_Scale_Group/resume)
Resume this group. 

#### [scale](/reference/services/SoftLayer_Scale_Group/scale)
Scale this group up or down by the amount given. 

#### [scaleTo](/reference/services/SoftLayer_Scale_Group/scaleTo)
Scale this group up or down to the number given. 

#### [suspend](/reference/services/SoftLayer_Scale_Group/suspend)
Suspend this group. 

</div>

