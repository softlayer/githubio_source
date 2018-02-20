---
title: "SoftLayer_Scale_Member_Virtual_Guest"
description: "A guest member is a scaled guest on a scale group. It is added either automatically or manually based on group settings.... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Member_Virtual_Guest"
---
# SoftLayer_Scale_Member_Virtual_Guest
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Scale_Member_Virtual_Guest' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Scale_Member_Virtual_Guest' >Datatype</a></li>
    </ul>
</div>

## Description
A guest member is a scaled guest on a scale group. It is added either automatically or manually based on group settings. It can be removed here, but is usually best removed using one of the scaling features of the group as a whole. 
        
        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Member_Virtual_Guest/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Delete this group member. Note, this can only be done on an active group when it wont cause the group to go below its minimumMemberCount. This is not the recommended way to delete members. Instead, users should invoke scale(-1) on SoftLayer_Scale_Group so it can choose the best guest member to remove. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Member_Virtual_Guest/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Scale_Member_Virtual_Guest record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Member_Virtual_Guest/getScaleGroup'> getScaleGroup</a> </span>
            <div class='views-field-body'>Retrieve the group this member belongs to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Member_Virtual_Guest/getVirtualGuest'> getVirtualGuest</a> </span>
            <div class='views-field-body'>Retrieve the guest for this member.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Member_Virtual_Guest/getVirtualGuestId'> getVirtualGuestId</a> </span>
            <div class='views-field-body'>Retrieve the identifier of the guest for this member.</div>
        </div>
        </div>
</div>

