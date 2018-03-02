---
title: "SoftLayer_Network_Firewall_Update_Request_Rule"
description: "The SoftLayer_Network_Firewall_Update_Request_Rule type contains information relating to a SoftLayer network firewall up... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Update_Request_Rule"
---

# SoftLayer_Network_Firewall_Update_Request_Rule
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request_Rule' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Firewall_Update_Request_Rule type contains information relating to a SoftLayer network firewall update request rule. This rule is a member of a [[SoftLayer Network Firewall Update Request]]. Use the [[SoftLayer Network Component Firewall]] service to view current rules. Use the [[SoftLayer Network Firewall Template]] service to pull SoftLayer recommended rule set templates. 

### External Links


* [Firewall at Wikipedia](http://en.wikipedia.org/wiki/Firewall_(networking))






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
            <div class='views-field-body'>The action that this update request rule is to take [permit or deny]. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#destinationIpAddress" name=destinationIpAddress>destinationIpAddress</a></span>
            <div class='views-field-body'>The destination IP address considered for determining rule application. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#destinationIpCidr" name=destinationIpCidr>destinationIpCidr</a></span>
            <div class='views-field-body'>The CIDR is used for determining rule application. This value will </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
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
            <span class='views-field-title'><a href="#firewallUpdateRequestId" name=firewallUpdateRequestId>firewallUpdateRequestId</a></span>
            <div class='views-field-body'>The unique identifier of the firewall update request that a firewall update request rule is associated with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A Firewall update request rule's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#notes" name=notes>notes</a></span>
            <div class='views-field-body'>The notes field for the firewall update request rule. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderValue" name=orderValue>orderValue</a></span>
            <div class='views-field-body'>The numeric value describing the order in which the rule should be applied. </div>
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
            <span class='views-field-title'><a href="#sourceIpCidr" name=sourceIpCidr>sourceIpCidr</a></span>
            <div class='views-field-body'>The CIDR is used for determining rule application. This value will </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#sourceIpSubnetMask" name=sourceIpSubnetMask>sourceIpSubnetMask</a></span>
            <div class='views-field-body'>The source IP subnet mask considered for determining rule application. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#version" name=version>version</a></span>
            <div class='views-field-body'>Whether this rule is an IPv4 rule or an IPv6 rule. If </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#firewallUpdateRequest" name=firewallUpdateRequest>firewallUpdateRequest</a></span>
            <div class='views-field-body'>The update request that this rule belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request'>SoftLayer_Network_Firewall_Update_Request </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


