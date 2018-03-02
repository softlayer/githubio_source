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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/createObject'> createObject</a> </span>
            <div class='views-field-body'>Create a scale group. If minimumMemberCount is greater than zero or desiredMemberCount is present, guest members will be created right away. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Delete this group. This can only be done on an empty, active group. This means that minimumMemberCount must be 0 since it is the only way for a group to have no group members. To delete a group and all of its members at the same time, use forceDeleteObject. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit this group. The name can be edited at any time. The minimumMemberCount and maximumMemberCount fields can also be edited at any time provided they don't force a scale up or scale down to bring the group into the proper range. Otherwise, the group's status must be active to set those fields. If the group member count is less than the new minimumMemberCount and the group is active, it will scale up the group members to reach the new minimum. Similarly if the group member count is greater than the new maximumMemberCount and the group is active, it will scale down the group members to reach the new maximum. 

When editing an active group, a special field can be provided: desiredMemberCount. When given, the group members are automatically scaled up or down to reach that number. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/forceDeleteObject'> forceDeleteObject</a> </span>
            <div class='views-field-body'>Delete this group and destroy all members of it.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the account for this scaling group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/getAvailableHourlyInstanceLimit'> getAvailableHourlyInstanceLimit</a> </span>
            <div class='views-field-body'>This returns the number of hourly instances an account can add from this point. It is essentially the same as [[SoftLayer_Account/hourlyInstanceLimit|hourlyInstanceLimit]] minus existing hourly instances and ones spoken for as part of a scaling group (as determined by the group's maximum). This number can be used to help determine a maximum member count for a new group to ensure it won't go over the account limit. This can return a negative value if the current hourly instance count combined with the unused-but-possible count (based on other scale group maximums) is over the limit. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/getAvailableRegionalGroups'> getAvailableRegionalGroups</a> </span>
            <div class='views-field-body'>Get the regional groups available for use by scaling groups. This also includes datacenter children that are available. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/getLoadBalancers'> getLoadBalancers</a> </span>
            <div class='views-field-body'>Retrieve collection of load balancers for this auto scale group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/getLogs'> getLogs</a> </span>
            <div class='views-field-body'>Retrieve collection of log entries for this group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/getNetworkVlans'> getNetworkVlans</a> </span>
            <div class='views-field-body'>Retrieve collection of VLANs for this auto scale group. VLANs are optional. This can contain a public or private VLAN or both. When a single VLAN for a public/private type is given it can be a non-purchased VLAN only if the minimumMemberCount on the group is >= 1. This can also contain any number of public/private purchased VLANs and members are staggered across them when scaled up.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Scale_Group record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/getPolicies'> getPolicies</a> </span>
            <div class='views-field-body'>Retrieve collection of policies for this group. This can be empty.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/getRegionalGroup'> getRegionalGroup</a> </span>
            <div class='views-field-body'>Retrieve the regional group for this scale group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/getStatus'> getStatus</a> </span>
            <div class='views-field-body'>Retrieve the status for this scale group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/getTerminationPolicy'> getTerminationPolicy</a> </span>
            <div class='views-field-body'>Retrieve the termination policy for this scaling group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/getVirtualGuestAssets'> getVirtualGuestAssets</a> </span>
            <div class='views-field-body'>Retrieve collection of guests that have been pinned to this group. Guest assets are only used for certain trigger checks such as resource watches. They do not count towards the auto scaling guest counts of this group in anyway and are never automatically added or removed.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/getVirtualGuestMembers'> getVirtualGuestMembers</a> </span>
            <div class='views-field-body'>Retrieve collection of guests that have been scaled with the group. When this group is active, the count of guests here is guaranteed to be between minimumMemberCount and maximumMemberCount inclusively.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/resume'> resume</a> </span>
            <div class='views-field-body'>Resume this group. The group must be in a suspended status to do this. By doing this, the group's status will become active. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/scale'> scale</a> </span>
            <div class='views-field-body'>Scale this group up or down by the amount given. If the number is negative, the given amount of guest members are removed. Similarly, if the number is positive, the given amount of guest members are added. Note, this call will add or remove as much as asked for, but will NOT go beyond the limits set by minimumMemberCount and maximumMemberCount. The result is a collection of SoftLayer_Scale_Member instances that were either removed or added. This call can only be invoked on an active group and does not respect cooldown (i.e. even if in a cooldown period, the scaling will still occur). </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/scaleTo'> scaleTo</a> </span>
            <div class='views-field-body'>Scale this group up or down to the number given. This call will add or remove as many guests as necessary, but will NOT go beyond the limits set by minimumMemberCount and maximumMemberCount. This call and its result are the equivalent of calling scale(number - virtualGuestMemberCount). This call can only be invoked on an active group and does not respect cooldown (i.e. even if in a cooldown period, the scaling will still occur). </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group/suspend'> suspend</a> </span>
            <div class='views-field-body'>Suspend this group. The group must be in an active status to do this. While suspended, a group cannot add or remove guest members for any reason. Changes to group settings that will cause a member to be added or deleted is also not allowed. </div>
        </div>
        </div>
</div>

