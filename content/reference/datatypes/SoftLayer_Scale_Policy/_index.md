---
title: "SoftLayer_Scale_Policy"
description: ""
layout: "datatype"
tags:
    - "datatype"
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
[cooldown]: #cooldown
#### [cooldown]
The number of seconds this policy will wait after lastActionDate on group before performing another action. If not present, the group's cooldown value is used.   
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
When this policy was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[deleteFlag]: #deleteflag
#### [deleteFlag]
When set and true any edit that happens on this object, be it calling edit on this directly or setting as a child while editing a parent object, will end up being a deletion.   
<span class="type-label">Type: </span>**boolean**

-----
[id]: #id
#### [id]
A policy's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
When this policy was last modified.  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
The name of this policy. It must be unique within the group.  
<span class="type-label">Type: </span>**string**

-----
[scaleGroupId]: #scalegroupid
#### [scaleGroupId]
The identifier of the group this member belongs to.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[actions]: #actions
#### [actions]
The actions to perform upon any trigger hit. Currently this must be a single value.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Policy_Action'>SoftLayer_Scale_Policy_Action[] </a>**

-----
[oneTimeTriggers]: #onetimetriggers
#### [oneTimeTriggers]
The one-time triggers to check for this group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Policy_Trigger'>SoftLayer_Scale_Policy_Trigger[] </a>**

-----
[repeatingTriggers]: #repeatingtriggers
#### [repeatingTriggers]
The repeating triggers to check for this group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Policy_Trigger'>SoftLayer_Scale_Policy_Trigger[] </a>**

-----
[resourceUseTriggers]: #resourceusetriggers
#### [resourceUseTriggers]
The resource-use triggers to check for this group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Policy_Trigger'>SoftLayer_Scale_Policy_Trigger[] </a>**

-----
[scaleActions]: #scaleactions
#### [scaleActions]
The scale actions to perform upon any trigger hit. Currently this must be a single value.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Policy_Action'>SoftLayer_Scale_Policy_Action[] </a>**

-----
[scaleGroup]: #scalegroup
#### [scaleGroup]
The group this policy is on.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Group'>SoftLayer_Scale_Group </a>**

-----
[triggers]: #triggers
#### [triggers]
The triggers to check for this group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Policy_Trigger'>SoftLayer_Scale_Policy_Trigger[] </a>**


## Count

-----
[actionCount]: #actioncount
#### [actionCount]
A count of the actions to perform upon any trigger hit. Currently this must be a single value.   
<span class="type-label">Type: </span>**unsigned long**


-----
[oneTimeTriggerCount]: #onetimetriggercount
#### [oneTimeTriggerCount]
A count of the one-time triggers to check for this group.   
<span class="type-label">Type: </span>**unsigned long**


-----
[repeatingTriggerCount]: #repeatingtriggercount
#### [repeatingTriggerCount]
A count of the repeating triggers to check for this group.   
<span class="type-label">Type: </span>**unsigned long**


-----
[resourceUseTriggerCount]: #resourceusetriggercount
#### [resourceUseTriggerCount]
A count of the resource-use triggers to check for this group.   
<span class="type-label">Type: </span>**unsigned long**


-----
[scaleActionCount]: #scaleactioncount
#### [scaleActionCount]
A count of the scale actions to perform upon any trigger hit. Currently this must be a single value.   
<span class="type-label">Type: </span>**unsigned long**


-----
[triggerCount]: #triggercount
#### [triggerCount]
A count of the triggers to check for this group.   
<span class="type-label">Type: </span>**unsigned long**

</div>


