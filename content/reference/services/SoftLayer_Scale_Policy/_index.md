---
title: "SoftLayer_Scale_Policy"
description: "A scale policy is a combination of triggers and actions that can occur on a scale group. When any trigger is satisfied (... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Policy"
---
# SoftLayer_Scale_Policy
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Scale_Policy' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Scale_Policy' >Datatype</a></li>
    </ul>
</div>

## Description


A scale policy is a combination of triggers and actions that can occur on a scale group. When any trigger is satisfied (or the policy is manually triggered) the actions will be executed. 



        
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

#### [createObject](/reference/services/SoftLayer_Scale_Policy/createObject)
Add a policy to a group.

</div>

<div class="method-row">

#### [deleteObject](/reference/services/SoftLayer_Scale_Policy/deleteObject)
Delete this policy from the group.

</div>

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_Scale_Policy/editObject)
Edit this policy's name.

</div>

<div class="method-row">

#### [getActions](/reference/services/SoftLayer_Scale_Policy/getActions)
Retrieve the actions to perform upon any trigger hit. Currently this must be a single value.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Scale_Policy/getObject)
Retrieve a SoftLayer_Scale_Policy record.

</div>

<div class="method-row">

#### [getOneTimeTriggers](/reference/services/SoftLayer_Scale_Policy/getOneTimeTriggers)
Retrieve the one-time triggers to check for this group.

</div>

<div class="method-row">

#### [getRepeatingTriggers](/reference/services/SoftLayer_Scale_Policy/getRepeatingTriggers)
Retrieve the repeating triggers to check for this group.

</div>

<div class="method-row">

#### [getResourceUseTriggers](/reference/services/SoftLayer_Scale_Policy/getResourceUseTriggers)
Retrieve the resource-use triggers to check for this group.

</div>

<div class="method-row">

#### [getScaleActions](/reference/services/SoftLayer_Scale_Policy/getScaleActions)
Retrieve the scale actions to perform upon any trigger hit. Currently this must be a single value.

</div>

<div class="method-row">

#### [getScaleGroup](/reference/services/SoftLayer_Scale_Policy/getScaleGroup)
Retrieve the group this policy is on.

</div>

<div class="method-row">

#### [getTriggers](/reference/services/SoftLayer_Scale_Policy/getTriggers)
Retrieve the triggers to check for this group.

</div>

<div class="method-row">

#### [trigger](/reference/services/SoftLayer_Scale_Policy/trigger)
Manually trigger the actions on this policy. 

</div>
</div>

</div>

