---
title: "SoftLayer_Scale_Group_Status"
description: "The status of a scale group. This status affects what actions can occur on a group. The values can be: 


* ACTIVE - The... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Group_Status"
---
# SoftLayer_Scale_Group_Status
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Scale_Group_Status' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Scale_Group_Status' >Datatype</a></li>
    </ul>
</div>

## Description
The status of a scale group. This status affects what actions can occur on a group. The values can be: 


* ACTIVE - There are no actions execution for any members or assets of any type.
* BUSY - There is an action executing for one of the members or assets, but that action is not a scaling action.
* SCALING - At least one of the members is in the process of being created or destroyed.
* SUSPENDED - The group has been placed in a suspended state by a user. It may only be resumed by a user. While in a
suspended state, a scale group cannot have any members added or deleted, or change settings of that group that would invoke such an action. 
        
        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group_Status/getAllObjects'> getAllObjects</a> </span>
            <div class='views-field-body'>Get all group statuses</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Group_Status/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Scale_Group_Status record.</div>
        </div>
        </div>
</div>

