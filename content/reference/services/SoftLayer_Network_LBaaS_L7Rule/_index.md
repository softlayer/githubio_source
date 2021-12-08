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

#### [addL7Rules](/reference/services/SoftLayer_Network_LBaaS_L7Rule/addL7Rules)
Create and add a L7 Rule to a given L7 policy with the provided rules details. 

</div>

<div class="method-row">

#### [deleteL7Rules](/reference/services/SoftLayer_Network_LBaaS_L7Rule/deleteL7Rules)
Delete one or more rules associated with the same policy. 

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_LBaaS_L7Rule/getObject)
Retrieve a SoftLayer_Network_LBaaS_L7Rule record.

</div>

<div class="method-row">

#### [updateL7Rules](/reference/services/SoftLayer_Network_LBaaS_L7Rule/updateL7Rules)
Update one or more rules associated with the same policy. 

</div>
</div>

</div>

