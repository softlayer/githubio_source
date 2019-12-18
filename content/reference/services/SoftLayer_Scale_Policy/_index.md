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
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [createObject](/reference/services/SoftLayer_Scale_Policy/createObject)
Add a policy to a group.

#### [deleteObject](/reference/services/SoftLayer_Scale_Policy/deleteObject)
Delete this policy from the group.

#### [editObject](/reference/services/SoftLayer_Scale_Policy/editObject)
Edit this policy's name.

#### [getActions](/reference/services/SoftLayer_Scale_Policy/getActions)
Retrieve the actions to perform upon any trigger hit. Currently this must be a single value.

#### [getObject](/reference/services/SoftLayer_Scale_Policy/getObject)
Retrieve a SoftLayer_Scale_Policy record.

#### [getOneTimeTriggers](/reference/services/SoftLayer_Scale_Policy/getOneTimeTriggers)
Retrieve the one-time triggers to check for this group.

#### [getRepeatingTriggers](/reference/services/SoftLayer_Scale_Policy/getRepeatingTriggers)
Retrieve the repeating triggers to check for this group.

#### [getResourceUseTriggers](/reference/services/SoftLayer_Scale_Policy/getResourceUseTriggers)
Retrieve the resource-use triggers to check for this group.

#### [getScaleActions](/reference/services/SoftLayer_Scale_Policy/getScaleActions)
Retrieve the scale actions to perform upon any trigger hit. Currently this must be a single value.

#### [getScaleGroup](/reference/services/SoftLayer_Scale_Policy/getScaleGroup)
Retrieve the group this policy is on.

#### [getTriggers](/reference/services/SoftLayer_Scale_Policy/getTriggers)
Retrieve the triggers to check for this group.

#### [trigger](/reference/services/SoftLayer_Scale_Policy/trigger)
Manually trigger the actions on this policy. 

</div>

