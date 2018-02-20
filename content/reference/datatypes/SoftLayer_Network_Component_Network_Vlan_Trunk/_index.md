---
title: "SoftLayer_Network_Component_Network_Vlan_Trunk"
description: "Represents the association between a Network_Component and Network_Vlan in the manner of a 'trunk'. Trunking a VLAN to a... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component_Network_Vlan_Trunk"
---

# SoftLayer_Network_Component_Network_Vlan_Trunk
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Component_Network_Vlan_Trunk' >Datatype</a></li>
    </ul>
</div>

## Description 
Represents the association between a Network_Component and Network_Vlan in the manner of a 'trunk'. Trunking a VLAN to a port allows that ports to receive and send packets tagged with the corresponding VLAN number. 
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
            <span class='views-field-title'><a href="#networkComponentId" name=networkComponentId>networkComponentId</a></span>
            <div class='views-field-body'>The network component's identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkVlanId" name=networkVlanId>networkVlanId</a></span>
            <div class='views-field-body'>The identifier of the network VLAN that is a trunk on the network component. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkComponent" name=networkComponent>networkComponent</a></span>
            <div class='views-field-body'>The network component that the VLAN is being trunked to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkVlan" name=networkVlan>networkVlan</a></span>
            <div class='views-field-body'>The VLAN that is being trunked to the network component. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a></p></div>
        </div>
            </div>
</div>


