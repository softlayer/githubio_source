---
title: "SoftLayer_Container_Utility_Network_Firewall_Rule_Attribute"
description: "The SoftLayer_Container_Utility_Network_Firewall_Rule_Attribute data type contains information relating to a single fire... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Utility_Network_Firewall_Rule_Attribute"
---

# SoftLayer_Container_Utility_Network_Firewall_Rule_Attribute
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Utility_Network_Firewall_Rule_Attribute' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Utility_Network_Firewall_Rule_Attribute data type contains information relating to a single firewall rule. 
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
            <span class='views-field-title'><a href="#actions" name=actions>actions</a></span>
            <div class='views-field-body'>The valid actions for use with rules. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>array of strings</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#maximumRuleCount" name=maximumRuleCount>maximumRuleCount</a></span>
            <div class='views-field-body'>Maximum allowed number of rules. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#protocols" name=protocols>protocols</a></span>
            <div class='views-field-body'>The valid protocols for use with rules. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>array of strings</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#sourceIpSubnetMasks" name=sourceIpSubnetMasks>sourceIpSubnetMasks</a></span>
            <div class='views-field-body'>The valid source ip subnet masks for use with rules. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Container_Utility_Network_Subnet_Mask_Generic_Detail'>SoftLayer_Container_Utility_Network_Subnet_Mask_Generic_Detail[] </a></p></div>
        </div>
            </div>
    </div>


