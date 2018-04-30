---
title: "SoftLayer_Layout_Profile"
description: "Layout profiles are the primary object used to tie customized portal experiences to the [[SoftLayer_User_Customer|user a... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Layout"
classes:
    - "SoftLayer_Layout_Profile"
---
# SoftLayer_Layout_Profile
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Layout_Profile' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Layout_Profile' >Datatype</a></li>
    </ul>
</div>

## Description
Layout profiles are the primary object used to tie customized portal experiences to the [[SoftLayer_User_Customer|user account]]. 

In order to take full advantage of the flexible customization of the portal, each user must be given one or more layout profiles. Each layout profile is then assigned one of the [[SoftLayer_Layout_Container|layout containers]], thereby giving the user all [[SoftLayer_Layout_Item|items]] and associated [[SoftLayer_Layout_Profile_Preferences|default preferences]]. These default preferences can be modified via the [[SoftLayer_Layout_Profile::modifyPreference()]] method, giving the user their own customized configuration. 



### seeAlso

* [SoftLayer_Layout_Profile_Preference](/reference/services/SoftLayer_Layout_Profile_Preference )


* [SoftLayer_Layout_Container](/reference/services/SoftLayer_Layout_Container )


* [SoftLayer_Layout_Preference](/reference/datatypes/SoftLayer_Layout_Preference )


* [SoftLayer_Layout_Profile_Containers](/reference/services/SoftLayer_Layout_Profile_Containers )


        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Layout_Profile/createObject'> createObject</a> </span>
            <div class='views-field-body'>Create a new layout profile</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Layout_Profile/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Delete a layout profile</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Layout_Profile/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit the layout profile object</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Layout_Profile/getLayoutContainers'> getLayoutContainers</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Layout_Profile/getLayoutPreferences'> getLayoutPreferences</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Layout_Profile/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Layout_Profile record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Layout_Profile/modifyPreference'> modifyPreference</a> </span>
            <div class='views-field-body'>Modifies an associated layout preference</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Layout_Profile/modifyPreferences'> modifyPreferences</a> </span>
            <div class='views-field-body'>Modifies a collection of associated preferences</div>
        </div>
        </div>
</div>

