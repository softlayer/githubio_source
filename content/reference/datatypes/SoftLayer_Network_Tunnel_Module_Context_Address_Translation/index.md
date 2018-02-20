---
title: "SoftLayer_Network_Tunnel_Module_Context_Address_Translation"
description: "The SoftLayer_Network_Tunnel_Module_Context_Address_Translation data type contains general information relating to a sin... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context_Address_Translation"
---

# SoftLayer_Network_Tunnel_Module_Context_Address_Translation
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context_Address_Translation' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Tunnel_Module_Context_Address_Translation data type contains general information relating to a single address translation. Information such as notes, ip addresses, along with record information, and network tunnel data may be retrieved. 
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
            <span class='views-field-title'><a href="#customerIpAddress" name=customerIpAddress>customerIpAddress</a></span>
            <div class='views-field-body'>The ip address record that will receive the encrypted traffic. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#customerIpAddressId" name=customerIpAddressId>customerIpAddressId</a></span>
            <div class='views-field-body'>The unique identifier for the ip address record that will receive the encrypted traffic. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>An address translation's unique identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#internalIpAddress" name=internalIpAddress>internalIpAddress</a></span>
            <div class='views-field-body'>The ip address record that will deliver the encrypted traffic. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#internalIpAddressId" name=internalIpAddressId>internalIpAddressId</a></span>
            <div class='views-field-body'>The unique identifier for the ip address record that will deliver the encrypted traffic. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkTunnelContextId" name=networkTunnelContextId>networkTunnelContextId</a></span>
            <div class='views-field-body'>An address translation's network tunnel identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#notes" name=notes>notes</a></span>
            <div class='views-field-body'>A name or description given to an address translation to help identify the address translation. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#customerIpAddressRecord" name=customerIpAddressRecord>customerIpAddressRecord</a></span>
            <div class='views-field-body'>The ip address record for the ip that will receive the encrypted traffic from the IPSec network tunnel. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Customer_Subnet_IpAddress'>SoftLayer_Network_Customer_Subnet_IpAddress </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#internalIpAddressRecord" name=internalIpAddressRecord>internalIpAddressRecord</a></span>
            <div class='views-field-body'>The ip address record for the ip that will deliver the encrypted traffic from the IPSec network tunnel. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkTunnelContext" name=networkTunnelContext>networkTunnelContext</a></span>
            <div class='views-field-body'>The IPSec network tunnel an address translation belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context'>SoftLayer_Network_Tunnel_Module_Context </a></p></div>
        </div>
            </div>
</div>


