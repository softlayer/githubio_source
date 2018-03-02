---
title: "SoftLayer_Scale_Group"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Group"
---

# SoftLayer_Scale_Group
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Scale_Group' >Datatype</a></li>
    </ul>
</div>

## Description 






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
            <div class='views-field-body'>The identifier of the account assigned to this group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#balancedTerminationFlag" name=balancedTerminationFlag>balancedTerminationFlag</a></span>
            <div class='views-field-body'>If this is true, this group will scale down members in a way to preserve the balance across VLANs. If there is ambiguity about which member to use to maintain balance, the terminationPolicy is used to resolve it. This is false by default and can only be set to true if there are multiple VLANs that are being balanced across.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cooldown" name=cooldown>cooldown</a></span>
            <div class='views-field-body'>The number of seconds this group will wait after lastActionDate before performing another action. Be advised, this can be overridden per policy. While strongly discouraged, a value of 0 effectively disables cooldown.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>When this group was created. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#desiredMemberCount" name=desiredMemberCount>desiredMemberCount</a></span>
            <div class='views-field-body'>This value is only available on the template for creating and editing a group. It will be null when retrieved. When this value is provided on create or edit, guests will be scaled up or down to meet this number. This number must be in the range provided by minimumMemberCount and maximumMemberCount. This value can only be present during create or edit when this group is active. Note, guests that are created as a result of this value can possibly be removed after cooldown by a policy.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A group's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#lastActionDate" name=lastActionDate>lastActionDate</a></span>
            <div class='views-field-body'>The date of the last action on this group or its create date </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#maximumMemberCount" name=maximumMemberCount>maximumMemberCount</a></span>
            <div class='views-field-body'>The greatest number of virtual guest members that are allowed on this group. Any attempts to add a guest member will fail if it will result in the total guest member count of this group to be above this number. If this number is edited and is less than the current guest member count, guests will be removed to at least be no greater than this number.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#minimumMemberCount" name=minimumMemberCount>minimumMemberCount</a></span>
            <div class='views-field-body'>The fewest number of virtual guest members that are allowed on this group. Any attempts to remove a guest member will fail if it will result in the total guest member count of this group to be below this number. If this number is edited and is larger than the current guest member count, guests will be added to at least reach this number.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>When this group was last modified. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>The name of this scale group. It must be unique on the account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#regionalGroupId" name=regionalGroupId>regionalGroupId</a></span>
            <div class='views-field-body'>The identifier of the regional group this scaling group is assigned to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#suspendedFlag" name=suspendedFlag>suspendedFlag</a></span>
            <div class='views-field-body'>If true, this group is suspended. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#terminationPolicyId" name=terminationPolicyId>terminationPolicyId</a></span>
            <div class='views-field-body'>The termination policy for the group. This determines which member to choose to delete when scaling downwards.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#virtualGuestMemberTemplate" name=virtualGuestMemberTemplate>virtualGuestMemberTemplate</a></span>
            <div class='views-field-body'>This is the template to create guest members with. This is the same template accepted by the createObject call on SoftLayer_Virtual_Guest with some caveats. The hostname provided will have an arbitrary value appended to it for each guest created. Also, hourlyBillingFlag cannot be false, and if the datacenter is provided it must be in the region of this group. Finally, VLANs cannot be provided for the template, it will use VLANs provided to this group instead. 

Note, if this template is edited on an existing group the previous template values are not kept and are not considered during termination. This means a group's guest members could effectively be a hybrid of multiple templates because this value was changed after some guest members were created but before others were created.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a></p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>The account for this scaling group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#loadBalancers" name=loadBalancers>loadBalancers</a></span>
            <div class='views-field-body'>Collection of load balancers for this auto scale group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_LoadBalancer'>SoftLayer_Scale_LoadBalancer[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#logs" name=logs>logs</a></span>
            <div class='views-field-body'>Collection of log entries for this group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_Group_Log'>SoftLayer_Scale_Group_Log[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkVlans" name=networkVlans>networkVlans</a></span>
            <div class='views-field-body'>Collection of VLANs for this auto scale group. VLANs are optional. This can contain a public or private VLAN or both. When a single VLAN for a public/private type is given it can be a non-purchased VLAN only if the minimumMemberCount on the group is >= 1. This can also contain any number of public/private purchased VLANs and members are staggered across them when scaled up. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_Network_Vlan'>SoftLayer_Scale_Network_Vlan[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#policies" name=policies>policies</a></span>
            <div class='views-field-body'>Collection of policies for this group. This can be empty. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_Policy'>SoftLayer_Scale_Policy[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#regionalGroup" name=regionalGroup>regionalGroup</a></span>
            <div class='views-field-body'>The regional group for this scale group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Location_Group_Regional'>SoftLayer_Location_Group_Regional </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#status" name=status>status</a></span>
            <div class='views-field-body'>The status for this scale group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_Group_Status'>SoftLayer_Scale_Group_Status </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#terminationPolicy" name=terminationPolicy>terminationPolicy</a></span>
            <div class='views-field-body'>The termination policy for this scaling group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_Termination_Policy'>SoftLayer_Scale_Termination_Policy </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#virtualGuestAssets" name=virtualGuestAssets>virtualGuestAssets</a></span>
            <div class='views-field-body'>Collection of guests that have been pinned to this group. Guest assets are only used for certain trigger checks such as resource watches. They do not count towards the auto scaling guest counts of this group in anyway and are never automatically added or removed. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_Asset'>SoftLayer_Scale_Asset[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#virtualGuestMembers" name=virtualGuestMembers>virtualGuestMembers</a></span>
            <div class='views-field-body'>Collection of guests that have been scaled with the group. When this group is active, the count of guests here is guaranteed to be between minimumMemberCount and maximumMemberCount inclusively. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_Member'>SoftLayer_Scale_Member[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#loadBalancerCount" name=loadBalancerCount>loadBalancerCount</a></span>
            <div class='views-field-body'>A count of collection of load balancers for this auto scale group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#logCount" name=logCount>logCount</a></span>
            <div class='views-field-body'>A count of collection of log entries for this group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkVlanCount" name=networkVlanCount>networkVlanCount</a></span>
            <div class='views-field-body'>A count of collection of VLANs for this auto scale group. VLANs are optional. This can contain a public or private VLAN or both. When a single VLAN for a public/private type is given it can be a non-purchased VLAN only if the minimumMemberCount on the group is >= 1. This can also contain any number of public/private purchased VLANs and members are staggered across them when scaled up. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#policyCount" name=policyCount>policyCount</a></span>
            <div class='views-field-body'>A count of collection of policies for this group. This can be empty. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#virtualGuestAssetCount" name=virtualGuestAssetCount>virtualGuestAssetCount</a></span>
            <div class='views-field-body'>A count of collection of guests that have been pinned to this group. Guest assets are only used for certain trigger checks such as resource watches. They do not count towards the auto scaling guest counts of this group in anyway and are never automatically added or removed. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#virtualGuestMemberCount" name=virtualGuestMemberCount>virtualGuestMemberCount</a></span>
            <div class='views-field-body'>A count of collection of guests that have been scaled with the group. When this group is active, the count of guests here is guaranteed to be between minimumMemberCount and maximumMemberCount inclusively. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


