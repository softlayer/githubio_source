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




<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
The hardware that an IP address is associated with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**  



</div>
<div class="prop-row">

-----
[ipAddress]: #ipaddress
#### [ipAddress]
An IP address expressed in dotted-quad notation.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[isBroadcastAddress]: #isbroadcastaddress
#### [isBroadcastAddress]
Whether an IP address is its subnet's broadcast address.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[isGatewayAddress]: #isgatewayaddress
#### [isGatewayAddress]
Whether an IP address is its subnet's gateway address. Gateway addresses exist on SoftLayer's routers and many not be assigned to servers.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[isNetworkAddress]: #isnetworkaddress
#### [isNetworkAddress]
Whether an IP address is its subnet's network identifier address.  
<span class="type-label">Type: </span>**boolean**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


