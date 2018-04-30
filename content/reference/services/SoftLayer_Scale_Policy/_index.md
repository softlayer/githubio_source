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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Policy/createObject'> createObject</a> </span>
            <div class='views-field-body'>Add a policy to a group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Policy/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Delete this policy from the group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Policy/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit this policy's name.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Policy/getActions'> getActions</a> </span>
            <div class='views-field-body'>Retrieve the actions to perform upon any trigger hit. Currently this must be a single value.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Policy/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Scale_Policy record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Policy/getOneTimeTriggers'> getOneTimeTriggers</a> </span>
            <div class='views-field-body'>Retrieve the one-time triggers to check for this group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Policy/getRepeatingTriggers'> getRepeatingTriggers</a> </span>
            <div class='views-field-body'>Retrieve the repeating triggers to check for this group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Policy/getResourceUseTriggers'> getResourceUseTriggers</a> </span>
            <div class='views-field-body'>Retrieve the resource-use triggers to check for this group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Policy/getScaleActions'> getScaleActions</a> </span>
            <div class='views-field-body'>Retrieve the scale actions to perform upon any trigger hit. Currently this must be a single value.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Policy/getScaleGroup'> getScaleGroup</a> </span>
            <div class='views-field-body'>Retrieve the group this policy is on.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Policy/getTriggers'> getTriggers</a> </span>
            <div class='views-field-body'>Retrieve the triggers to check for this group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Policy/trigger'> trigger</a> </span>
            <div class='views-field-body'>Manually trigger the actions on this policy. </div>
        </div>
        </div>
</div>

