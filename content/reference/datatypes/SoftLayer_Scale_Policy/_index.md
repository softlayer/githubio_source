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
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Scale_Policy' >Datatype</a></li>
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
            <span class='views-field-title'><a href="#cooldown" name=cooldown>cooldown</a></span>
            <div class='views-field-body'>The number of seconds this policy will wait after lastActionDate on group before performing another action. If not present, the group's cooldown value is used.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>When this policy was created. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#deleteFlag" name=deleteFlag>deleteFlag</a></span>
            <div class='views-field-body'>When set and true any edit that happens on this object, be it calling edit on this directly or setting as a child while editing a parent object, will end up being a deletion.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A policy's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>When this policy was last modified. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>The name of this policy. It must be unique within the group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#scaleGroupId" name=scaleGroupId>scaleGroupId</a></span>
            <div class='views-field-body'>The identifier of the group this member belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#actions" name=actions>actions</a></span>
            <div class='views-field-body'>The actions to perform upon any trigger hit. Currently this must be a single value. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_Policy_Action'>SoftLayer_Scale_Policy_Action[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#oneTimeTriggers" name=oneTimeTriggers>oneTimeTriggers</a></span>
            <div class='views-field-body'>The one-time triggers to check for this group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_Policy_Trigger'>SoftLayer_Scale_Policy_Trigger[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#repeatingTriggers" name=repeatingTriggers>repeatingTriggers</a></span>
            <div class='views-field-body'>The repeating triggers to check for this group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_Policy_Trigger'>SoftLayer_Scale_Policy_Trigger[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#resourceUseTriggers" name=resourceUseTriggers>resourceUseTriggers</a></span>
            <div class='views-field-body'>The resource-use triggers to check for this group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_Policy_Trigger'>SoftLayer_Scale_Policy_Trigger[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#scaleActions" name=scaleActions>scaleActions</a></span>
            <div class='views-field-body'>The scale actions to perform upon any trigger hit. Currently this must be a single value. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_Policy_Action'>SoftLayer_Scale_Policy_Action[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#scaleGroup" name=scaleGroup>scaleGroup</a></span>
            <div class='views-field-body'>The group this policy is on. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_Group'>SoftLayer_Scale_Group </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#triggers" name=triggers>triggers</a></span>
            <div class='views-field-body'>The triggers to check for this group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_Policy_Trigger'>SoftLayer_Scale_Policy_Trigger[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#actionCount" name=actionCount>actionCount</a></span>
            <div class='views-field-body'>A count of the actions to perform upon any trigger hit. Currently this must be a single value. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#oneTimeTriggerCount" name=oneTimeTriggerCount>oneTimeTriggerCount</a></span>
            <div class='views-field-body'>A count of the one-time triggers to check for this group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#repeatingTriggerCount" name=repeatingTriggerCount>repeatingTriggerCount</a></span>
            <div class='views-field-body'>A count of the repeating triggers to check for this group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#resourceUseTriggerCount" name=resourceUseTriggerCount>resourceUseTriggerCount</a></span>
            <div class='views-field-body'>A count of the resource-use triggers to check for this group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#scaleActionCount" name=scaleActionCount>scaleActionCount</a></span>
            <div class='views-field-body'>A count of the scale actions to perform upon any trigger hit. Currently this must be a single value. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#triggerCount" name=triggerCount>triggerCount</a></span>
            <div class='views-field-body'>A count of the triggers to check for this group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


