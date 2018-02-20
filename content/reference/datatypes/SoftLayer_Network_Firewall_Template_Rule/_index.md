---
title: "SoftLayer_Network_Firewall_Template_Rule"
description: "The SoftLayer_Network_Component_Firewall_Rule type contains general information relating to a single SoftLayer firewall... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Template_Rule"
---

# SoftLayer_Network_Firewall_Template_Rule
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Firewall_Template_Rule' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Component_Firewall_Rule type contains general information relating to a single SoftLayer firewall template rule. Use the [[SoftLayer Network Component Firewall]] service to view current rules. Use the [[SoftLayer Network Firewall Update Request]] service to submit a firewall update request. 
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
            <span class='views-field-title'><a href="#action" name=action>action</a></span>
            <div class='views-field-body'>The action that this template rule is to take [permit or deny]. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#destinationIpAddress" name=destinationIpAddress>destinationIpAddress</a></span>
            <div class='views-field-body'>The destination IP address considered for determining rule application. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#destinationIpSubnetMask" name=destinationIpSubnetMask>destinationIpSubnetMask</a></span>
            <div class='views-field-body'>The destination IP subnet mask considered for determining rule application. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#destinationPortRangeEnd" name=destinationPortRangeEnd>destinationPortRangeEnd</a></span>
            <div class='views-field-body'>The ending (upper end of range) destination port considered for determining rule application. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#destinationPortRangeStart" name=destinationPortRangeStart>destinationPortRangeStart</a></span>
            <div class='views-field-body'>The starting (lower end of range) destination port considered for determining rule application. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#firewallTemplateId" name=firewallTemplateId>firewallTemplateId</a></span>
            <div class='views-field-body'>The unique identifier of the firewall template that a firewall template rule is associated with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A Firewall template rule's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#notes" name=notes>notes</a></span>
            <div class='views-field-body'>The notes field for the firewall template rule. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderValue" name=orderValue>orderValue</a></span>
            <div class='views-field-body'>The numeric value describing the order in which the rule set should be applied. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#protocol" name=protocol>protocol</a></span>
            <div class='views-field-body'>The protocol considered for determining rule application. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#sourceIpAddress" name=sourceIpAddress>sourceIpAddress</a></span>
            <div class='views-field-body'>The source IP address considered for determining rule application. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#sourceIpSubnetMask" name=sourceIpSubnetMask>sourceIpSubnetMask</a></span>
            <div class='views-field-body'>The source IP subnet mask considered for determining rule application. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#firewallTemplate" name=firewallTemplate>firewallTemplate</a></span>
            <div class='views-field-body'>The firewall template that this rule is attached to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Firewall_Template'>SoftLayer_Network_Firewall_Template </a></p></div>
        </div>
            </div>
</div>


