---
title: "SoftLayer_Network_Component_Firewall_Subnets"
description: "A SoftLayer_Network_Component_Firewall_Subnets object type represents the current linked subnets and contains relative i... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component_Firewall_Subnets"
---

# SoftLayer_Network_Component_Firewall_Subnets
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Component_Firewall_Subnets' >Datatype</a></li>
    </ul>
</div>

## Description 
A SoftLayer_Network_Component_Firewall_Subnets object type represents the current linked subnets and contains relative information. Use the [[SoftLayer Network Firewall Update Request]] service to submit a firewall update request. Use the [[SoftLayer Network Firewall Template]] service to pull SoftLayer recommended rule set templates. 
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
            <span class='views-field-title'><a href="#applyServerRulesFlag" name=applyServerRulesFlag>applyServerRulesFlag</a></span>
            <div class='views-field-body'>A boolean flag that indicates whether the subnet should receive all the rules intended for the host on this context slot. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#subnetId" name=subnetId>subnetId</a></span>
            <div class='views-field-body'>The unique identifier of the subnet being linked to the network component firewall. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkComponentFirewall" name=networkComponentFirewall>networkComponentFirewall</a></span>
            <div class='views-field-body'>The network component firewall that write rules for this subnet. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component_Firewall'>SoftLayer_Network_Component_Firewall </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#subnet" name=subnet>subnet</a></span>
            <div class='views-field-body'>The subnet that this link binds to the network component firewall. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a></p></div>
        </div>
            </div>
</div>


