---
title: "SoftLayer_Layout_Profile_Preference"
description: "The profile preferences are an aggregation of the default preferences and the customized preferences. 

For each [[SoftL... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Layout"
classes:
    - "SoftLayer_Layout_Profile_Preference"
---
# SoftLayer_Layout_Profile_Preference
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Layout_Profile_Preference' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Layout_Profile_Preference' >Datatype</a></li>
    </ul>
</div>

## Description
The profile preferences are an aggregation of the default preferences and the customized preferences. 

For each [[SoftLayer_Layout_Profile_Containers|associated container]] on a [[SoftLayer_Layout_Profile|profile]], the [[SoftLayer_Layout_Preference|default preferences]] are inherited through the profile preferences. However, any one of these may be overridden through the [[SoftLayer_Layout_Profile::modifyPreference()]] method. Rather than maintaining two different sets of preferences, all preferences are grouped together through the profile preferences, presenting the customized preferences in place of the default preferences they are overriding. 



### seeAlso

* [SoftLayer_Layout_Profile](/reference/datatypes/SoftLayer_Layout_Profile )


* [SoftLayer_Layout_Profile_Containers](/reference/services/SoftLayer_Layout_Profile_Containers )


* [SoftLayer_Layout_Preference](/reference/datatypes/SoftLayer_Layout_Preference )


        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Layout_Profile_Preference/getLayoutContainer'> getLayoutContainer</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Layout_Profile_Preference/getLayoutItem'> getLayoutItem</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Layout_Profile_Preference/getLayoutPreference'> getLayoutPreference</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Layout_Profile_Preference/getLayoutProfile'> getLayoutProfile</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Layout_Profile_Preference/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Layout_Profile_Preference record.</div>
        </div>
        </div>
</div>

