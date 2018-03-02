---
title: "SoftLayer_Container_Product_Order_Network"
description: "This type contains the structure of network-related objects that may be specified when ordering services."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Product_Order_Network"
---

# SoftLayer_Container_Product_Order_Network
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Product_Order_Network' >Datatype</a></li>
    </ul>
</div>

## Description 
This type contains the structure of network-related objects that may be specified when ordering services. 





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
            <span class='views-field-title'><a href="#network" name=network>network</a></span>
            <div class='views-field-body'>The [[SoftLayer_Network]] object. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network'>SoftLayer_Network </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#publicVlans" name=publicVlans>publicVlans</a></span>
            <div class='views-field-body'>The list of public [[SoftLayer_Container_Product_Order_Network_Vlan|vlans]] available for ordering. Each VLAN will have list of public subnets that are accessible to the VLAN.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#subnets" name=subnets>subnets</a></span>
            <div class='views-field-body'>The list of private [[SoftLayer_Container_Product_Order_Network_Subnet|subnets]] available for ordering with a description of their available IP space.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order[] </a></p></div>
        </div>
            </div>
    </div>


