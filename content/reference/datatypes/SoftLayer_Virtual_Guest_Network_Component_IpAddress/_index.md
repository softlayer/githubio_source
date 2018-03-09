---
title: "SoftLayer_Virtual_Guest_Network_Component_IpAddress"
description: "The SoftLayer_Virtual_Guest_Network_Component_IpAddress data type contains general information relating to the binding o... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Network_Component_IpAddress"
---

# SoftLayer_Virtual_Guest_Network_Component_IpAddress
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component_IpAddress' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Virtual_Guest_Network_Component_IpAddress data type contains general information relating to the binding of a single network component to a single SoftLayer IP address. 


### associatedMethods

*  [SoftLayer_Network_Subnet_IpAddress::getObject](/reference/services/SoftLayer_Network_Subnet_IpAddress/getObject )
*  [SoftLayer_Network_Subnet_IpAddress::editObject](/reference/services/SoftLayer_Network_Subnet_IpAddress/editObject )





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
                <a href="#ipAddressId" name=ipAddressId>ipAddressId</a>
            </span>
            <div class='views-field-body'>The unique ID of the [[SoftLayer_Network_Subnet_ipAddress|ip address]] this virtual IP address is associated with.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#port" name=port>port</a>
            </span>
            <div class='views-field-body'>The port that a network component has reserved.  This field is only required for some IP address types.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#type" name=type>type</a>
            </span>
            <div class='views-field-body'>The type of IP that this IP address record references.  Some examples are PRIMARY for the network component's primary IP address and CONSOLE_PROXY which represents the IP information for logging into a computing instance's console.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ipAddress" name=ipAddress>ipAddress</a>
            </span>
            <div class='views-field-body'>The IP address associated with this object's network component. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#networkComponent" name=networkComponent>networkComponent</a>
            </span>
            <div class='views-field-body'>The network component associated with this object's IP address. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component'>SoftLayer_Virtual_Guest_Network_Component </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


