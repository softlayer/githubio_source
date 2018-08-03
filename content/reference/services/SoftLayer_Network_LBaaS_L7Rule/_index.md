---
title: "SoftLayer_Network_LBaaS_L7Rule"
description: "The SoftLayer_Network_LBaaS_L7Rule service allows consumers to manage the Rules associated with a Policy.Polices have mu... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Rule"
---
# SoftLayer_Network_LBaaS_L7Rule
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LBaaS_L7Rule' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7Rule' >Datatype</a></li>
    </ul>
</div>

## Description
The SoftLayer_Network_LBaaS_L7Rule service allows consumers to manage the Rules associated with a Policy.Polices have multiple rules, each rule is evaluated to true or false. If all the rules of the policies are evaluated to true then action of that policy will be applied to the request. Rules have types, which can be HOST_NAME, FILE_TYPE, HEADER, COOKIE, PATH and rules also have a comparison type which indicates how how rules are evaluated. Rules can have following comparison types: REGEX, STARTS_WITH, ENDS_WITH, CONTAINS, and EQUAL_TO. 



        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LBaaS_L7Rule/addL7Rules'> addL7Rules</a> </span>
            <div class='views-field-body'>Create and add a L7 Rule to a given L7 policy with the provided rules details. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LBaaS_L7Rule/deleteL7Rules'> deleteL7Rules</a> </span>
            <div class='views-field-body'>Delete one or more rules associated with the same policy. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LBaaS_L7Rule/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_LBaaS_L7Rule record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_LBaaS_L7Rule/updateL7Rules'> updateL7Rules</a> </span>
            <div class='views-field-body'>Update one or more rules associated with the same policy. </div>
        </div>
        </div>
</div>

