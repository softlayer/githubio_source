---
title: "SoftLayer_Network_Customer_Subnet_IpAddress"
description: "The SoftLayer_Network_Customer_Subnet_IpAddress data type contains general information relating to a single Customer Sub... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Customer_Subnet_IpAddress"
---

# SoftLayer_Network_Customer_Subnet_IpAddress
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Customer_Subnet_IpAddress' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Customer_Subnet_IpAddress data type contains general information relating to a single Customer Subnet (Remote) IPv4 address. 





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
            <div class='views-field-body'>Unique identifier for an ip address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ipAddress" name=ipAddress>ipAddress</a></span>
            <div class='views-field-body'>An IP address expressed in dotted quad format. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#notes" name=notes>notes</a></span>
            <div class='views-field-body'>An IP address' user defined note. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#subnetId" name=subnetId>subnetId</a></span>
            <div class='views-field-body'>The unique identifier for the customer subnet (remote) the ip address belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#subnet" name=subnet>subnet</a></span>
            <div class='views-field-body'>The customer subnet (remote) that the ip address belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Customer_Subnet'>SoftLayer_Network_Customer_Subnet </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#translations" name=translations>translations</a></span>
            <div class='views-field-body'>All the address translations that are tied to an IP address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context_Address_Translation'>SoftLayer_Network_Tunnel_Module_Context_Address_Translation[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#translationCount" name=translationCount>translationCount</a></span>
            <div class='views-field-body'>A count of all the address translations that are tied to an IP address. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


