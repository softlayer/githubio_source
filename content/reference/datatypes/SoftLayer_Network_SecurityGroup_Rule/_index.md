---
title: "SoftLayer_Network_SecurityGroup_Rule"
description: "The SoftLayer_Network_SecurityGroup_Rule data type contains general information for a single rule that belongs to a [[So... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_SecurityGroup_Rule"
---

# SoftLayer_Network_SecurityGroup_Rule
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_SecurityGroup_Rule' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_SecurityGroup_Rule data type contains general information for a single rule that belongs to a [[SoftLayer_Network_SecurityGroup|security group]]. By default, all traffic (both inbound and  outbound) to a virtual server instance is blocked. Security group rules are permissive, and define the allowed incoming (ingress) and outgoing (egress) traffic to both the public and private interfaces of a  virtual server instance. The order of rules within a security group does not matter and priority always falls to the least restrictive rule. 





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
            <span class='views-field-title'>
                <a href="#direction" name=direction>direction</a>
            </span>
            <div class='views-field-body'>The direction of traffic (ingress or egress). </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ethertype" name=ethertype>ethertype</a>
            </span>
            <div class='views-field-body'>IPv4 or IPv6. If the remoteIp or ethertype properties are not specified, the default is IPv4.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The unique ID for a rule. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#portRangeMax" name=portRangeMax>portRangeMax</a>
            </span>
            <div class='views-field-body'>The end of the port range for allowed traffic. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#portRangeMin" name=portRangeMin>portRangeMin</a>
            </span>
            <div class='views-field-body'>The start of the port range for allowed traffic. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#protocol" name=protocol>protocol</a>
            </span>
            <div class='views-field-body'>The protocol of packets (icmp, tcp, or udp). </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#remoteGroupId" name=remoteGroupId>remoteGroupId</a>
            </span>
            <div class='views-field-body'>The ID of the remote security group allowed as part of the rule. This property is mutually exclusive with the remoteIp property.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#remoteIp" name=remoteIp>remoteIp</a>
            </span>
            <div class='views-field-body'>CIDR or IP address for allowed connections. This property is mutually exclusive with the remoteGroupId property.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#securityGroupId" name=securityGroupId>securityGroupId</a>
            </span>
            <div class='views-field-body'>The ID of the security group that owns the rule. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#remoteGroup" name=remoteGroup>remoteGroup</a>
            </span>
            <div class='views-field-body'>The remote security group allowed as part of this rule. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_SecurityGroup'>SoftLayer_Network_SecurityGroup </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#securityGroup" name=securityGroup>securityGroup</a>
            </span>
            <div class='views-field-body'>The security group of this rule. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_SecurityGroup'>SoftLayer_Network_SecurityGroup </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


