---
title: "SoftLayer_Container_Network_Subnet_IpAddress"
description: "SoftLayer_Container_Subnet_IPAddress models an IP v4 address as it exists as a member of it's subnet, letting the user k... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_Subnet_IpAddress"
---

# SoftLayer_Container_Network_Subnet_IpAddress
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_Subnet_IpAddress' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_Subnet_IPAddress models an IP v4 address as it exists as a member of it's subnet, letting the user know if it is a network identifier, gateway, broadcast, or useable address. Addresses that are neither the network identifier nor the gateway nor the broadcast addresses are usable by SoftLayer servers. 

### External Links


* [Ip address at Wikipedia](http://en.wikipedia.org/wiki/Ip_address)


* [RFC791:Internet Protocol Specification at ietf.org](http://tools.ietf.org/html/rfc791)



### associatedMethods

*  [SoftLayer_Network_Subnet::getRoutableEndpointIpAddresses](/reference/services/SoftLayer_Network_Subnet/getRoutableEndpointIpAddresses )



### seeAlso

* [SoftLayer_Network_Subnet](/reference/services/SoftLayer_Network_Subnet )


* [SoftLayer_Network_Subnet_IpAddress](/reference/services/SoftLayer_Network_Subnet_IpAddress )


* [SoftLayer_Network_Vlan](/reference/services/SoftLayer_Network_Vlan )




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
                <a href="#hardware" name=hardware>hardware</a>
            </span>
            <div class='views-field-body'>The hardware that an IP address is associated with. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ipAddress" name=ipAddress>ipAddress</a>
            </span>
            <div class='views-field-body'>An IP address expressed in dotted-quad notation. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#isBroadcastAddress" name=isBroadcastAddress>isBroadcastAddress</a>
            </span>
            <div class='views-field-body'>Whether an IP address is its subnet's broadcast address. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#isGatewayAddress" name=isGatewayAddress>isGatewayAddress</a>
            </span>
            <div class='views-field-body'>Whether an IP address is its subnet's gateway address. Gateway addresses exist on SoftLayer's routers and many not be assigned to servers. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#isNetworkAddress" name=isNetworkAddress>isNetworkAddress</a>
            </span>
            <div class='views-field-body'>Whether an IP address is its subnet's network identifier address. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
            </div>
    </div>


