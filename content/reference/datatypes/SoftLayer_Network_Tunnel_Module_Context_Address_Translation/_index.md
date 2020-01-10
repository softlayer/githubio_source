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
[customerIpAddress]: #customeripaddress
#### [customerIpAddress]
The ip address record that will receive the encrypted traffic.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[customerIpAddressId]: #customeripaddressid
#### [customerIpAddressId]
The unique identifier for the ip address record that will receive the encrypted traffic.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
An address translation's unique identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[internalIpAddress]: #internalipaddress
#### [internalIpAddress]
The ip address record that will deliver the encrypted traffic.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[internalIpAddressId]: #internalipaddressid
#### [internalIpAddressId]
The unique identifier for the ip address record that will deliver the encrypted traffic.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[networkTunnelContextId]: #networktunnelcontextid
#### [networkTunnelContextId]
An address translation's network tunnel identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
A name or description given to an address translation to help identify the address translation.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[customerIpAddressRecord]: #customeripaddressrecord
#### [customerIpAddressRecord]
The ip address record for the ip that will receive the encrypted traffic from the IPSec network tunnel.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Customer_Subnet_IpAddress'>SoftLayer_Network_Customer_Subnet_IpAddress </a>**


</div>
<div class="prop-row">

-----
[internalIpAddressRecord]: #internalipaddressrecord
#### [internalIpAddressRecord]
The ip address record for the ip that will deliver the encrypted traffic from the IPSec network tunnel.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**


</div>
<div class="prop-row">

-----
[networkTunnelContext]: #networktunnelcontext
#### [networkTunnelContext]
The IPSec network tunnel an address translation belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context'>SoftLayer_Network_Tunnel_Module_Context </a>**


</div>

## Count
</div>


