---
title: "SoftLayer_Scale_Network_Vlan"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Network_Vlan"
---

# SoftLayer_Scale_Network_Vlan
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Scale_Network_Vlan' >Datatype</a></li>
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
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>When this network VLAN reference was created. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#deleteFlag" name=deleteFlag>deleteFlag</a></span>
            <div class='views-field-body'>When set and true any edit that happens on this object, be it calling edit on this directly or setting as a child while editing a parent object, will end up being a deletion.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The network VLAN reference's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkVlanId" name=networkVlanId>networkVlanId</a></span>
            <div class='views-field-body'>The identifier for the VLAN to scale with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#scaleGroupId" name=scaleGroupId>scaleGroupId</a></span>
            <div class='views-field-body'>The identifier of the group this network VLAN reference applies to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkVlan" name=networkVlan>networkVlan</a></span>
            <div class='views-field-body'>The network VLAN to scale with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#scaleGroup" name=scaleGroup>scaleGroup</a></span>
            <div class='views-field-body'>The group this network VLAN is for. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Scale_Group'>SoftLayer_Scale_Group </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


