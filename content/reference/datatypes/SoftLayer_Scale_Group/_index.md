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
    <li id='service'> <a href='/reference/services/SoftLayer_Scale_Group' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Scale_Group' >Datatype</a></li>
    </ul>
</div>

## Description 








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
The identifier of the account assigned to this group.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[balancedTerminationFlag]: #balancedterminationflag
#### [balancedTerminationFlag]
If this is true, this group will scale down members in a way to preserve the balance across VLANs. If there is ambiguity about which member to use to maintain balance, the terminationPolicy is used to resolve it. This is false by default and can only be set to true if there are multiple VLANs that are being balanced across.   
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[cooldown]: #cooldown
#### [cooldown]
The number of seconds this group will wait after lastActionDate before performing another action. Be advised, this can be overridden per policy. While strongly discouraged, a value of 0 effectively disables cooldown.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
When this group was created.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[desiredMemberCount]: #desiredmembercount
#### [desiredMemberCount]
This value is only available on the template for creating and editing a group. It will be null when retrieved. When this value is provided on create or edit, guests will be scaled up or down to meet this number. This number must be in the range provided by minimumMemberCount and maximumMemberCount. This value can only be present during create or edit when this group is active. Note, guests that are created as a result of this value can possibly be removed after cooldown by a policy.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A group's internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[lastActionDate]: #lastactiondate
#### [lastActionDate]
The date of the last action on this group or its create date  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[maximumMemberCount]: #maximummembercount
#### [maximumMemberCount]
The greatest number of virtual guest members that are allowed on this group. Any attempts to add a guest member will fail if it will result in the total guest member count of this group to be above this number. If this number is edited and is less than the current guest member count, guests will be removed to at least be no greater than this number.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[minimumMemberCount]: #minimummembercount
#### [minimumMemberCount]
The fewest number of virtual guest members that are allowed on this group. Any attempts to remove a guest member will fail if it will result in the total guest member count of this group to be below this number. If this number is edited and is larger than the current guest member count, guests will be added to at least reach this number.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
When this group was last modified.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The name of this scale group. It must be unique on the account.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[regionalGroupId]: #regionalgroupid
#### [regionalGroupId]
The identifier of the regional group this scaling group is assigned to.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[suspendedFlag]: #suspendedflag
#### [suspendedFlag]
If true, this group is suspended.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[terminationPolicyId]: #terminationpolicyid
#### [terminationPolicyId]
The termination policy for the group. This determines which member to choose to delete when scaling downwards.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[virtualGuestMemberTemplate]: #virtualguestmembertemplate
#### [virtualGuestMemberTemplate]
This is the template to create guest members with. This is the same template accepted by the createObject call on SoftLayer_Virtual_Guest with some caveats. The hostname provided will have an arbitrary value appended to it for each guest created. Also, hourlyBillingFlag cannot be false, and if the datacenter is provided it must be in the region of this group. Finally, VLANs cannot be provided for the template, it will use VLANs provided to this group instead. 

Note, if this template is edited on an existing group the previous template values are not kept and are not considered during termination. This means a group's guest members could effectively be a hybrid of multiple templates because this value was changed after some guest members were created but before others were created.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account for this scaling group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[loadBalancers]: #loadbalancers
#### [loadBalancers]
Collection of load balancers for this auto scale group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_LoadBalancer'>SoftLayer_Scale_LoadBalancer[] </a>**  



</div>
<div class="prop-row">

-----
[logs]: #logs
#### [logs]
Collection of log entries for this group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Group_Log'>SoftLayer_Scale_Group_Log[] </a>**  



</div>
<div class="prop-row">

-----
[networkVlans]: #networkvlans
#### [networkVlans]
Collection of VLANs for this auto scale group. VLANs are optional. This can contain a public or private VLAN or both. When a single VLAN for a public/private type is given it can be a non-purchased VLAN only if the minimumMemberCount on the group is >= 1. This can also contain any number of public/private purchased VLANs and members are staggered across them when scaled up.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Network_Vlan'>SoftLayer_Scale_Network_Vlan[] </a>**  



</div>
<div class="prop-row">

-----
[policies]: #policies
#### [policies]
Collection of policies for this group. This can be empty.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Policy'>SoftLayer_Scale_Policy[] </a>**  



</div>
<div class="prop-row">

-----
[regionalGroup]: #regionalgroup
#### [regionalGroup]
The regional group for this scale group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Group_Regional'>SoftLayer_Location_Group_Regional </a>**  



</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
The status for this scale group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Group_Status'>SoftLayer_Scale_Group_Status </a>**  



</div>
<div class="prop-row">

-----
[terminationPolicy]: #terminationpolicy
#### [terminationPolicy]
The termination policy for this scaling group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Termination_Policy'>SoftLayer_Scale_Termination_Policy </a>**  



</div>
<div class="prop-row">

-----
[virtualGuestAssets]: #virtualguestassets
#### [virtualGuestAssets]
Collection of guests that have been pinned to this group. Guest assets are only used for certain trigger checks such as resource watches. They do not count towards the auto scaling guest counts of this group in anyway and are never automatically added or removed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Asset'>SoftLayer_Scale_Asset[] </a>**  



</div>
<div class="prop-row">

-----
[virtualGuestMembers]: #virtualguestmembers
#### [virtualGuestMembers]
Collection of guests that have been scaled with the group. When this group is active, the count of guests here is guaranteed to be between minimumMemberCount and maximumMemberCount inclusively.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Member'>SoftLayer_Scale_Member[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[loadBalancerCount]: #loadbalancercount
#### [loadBalancerCount]
A count of collection of load balancers for this auto scale group.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[logCount]: #logcount
#### [logCount]
A count of collection of log entries for this group.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[networkVlanCount]: #networkvlancount
#### [networkVlanCount]
A count of collection of VLANs for this auto scale group. VLANs are optional. This can contain a public or private VLAN or both. When a single VLAN for a public/private type is given it can be a non-purchased VLAN only if the minimumMemberCount on the group is >= 1. This can also contain any number of public/private purchased VLANs and members are staggered across them when scaled up.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[policyCount]: #policycount
#### [policyCount]
A count of collection of policies for this group. This can be empty.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[virtualGuestAssetCount]: #virtualguestassetcount
#### [virtualGuestAssetCount]
A count of collection of guests that have been pinned to this group. Guest assets are only used for certain trigger checks such as resource watches. They do not count towards the auto scaling guest counts of this group in anyway and are never automatically added or removed.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[virtualGuestMemberCount]: #virtualguestmembercount
#### [virtualGuestMemberCount]
A count of collection of guests that have been scaled with the group. When this group is active, the count of guests here is guaranteed to be between minimumMemberCount and maximumMemberCount inclusively.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


