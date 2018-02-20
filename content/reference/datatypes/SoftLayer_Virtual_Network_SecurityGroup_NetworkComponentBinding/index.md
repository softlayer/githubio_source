---
title: "SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding"
description: "The SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding data type contains general information for a single... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding"
---

# SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding data type contains general information for a single binding. A binding associates a [[SoftLayer_Virtual_Guest_Network_Component]] with a [[SoftLayer_Network_SecurityGroup]]. 
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
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The unique ID for a binding. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkComponentId" name=networkComponentId>networkComponentId</a></span>
            <div class='views-field-body'>The ID of the network component. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#securityGroupId" name=securityGroupId>securityGroupId</a></span>
            <div class='views-field-body'>The ID of the security group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkComponent" name=networkComponent>networkComponent</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component'>SoftLayer_Virtual_Guest_Network_Component </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#securityGroup" name=securityGroup>securityGroup</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_SecurityGroup'>SoftLayer_Network_SecurityGroup </a></p></div>
        </div>
            </div>
</div>


