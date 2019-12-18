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

## Local
-----
[customerIpAddress]: #customeripaddress
#### [customerIpAddress]
The ip address record that will receive the encrypted traffic.  
<span class="type-label">Type: </span>**string**

-----
[customerIpAddressId]: #customeripaddressid
#### [customerIpAddressId]
The unique identifier for the ip address record that will receive the encrypted traffic.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
An address translation's unique identifier.  
<span class="type-label">Type: </span>**integer**

-----
[internalIpAddress]: #internalipaddress
#### [internalIpAddress]
The ip address record that will deliver the encrypted traffic.  
<span class="type-label">Type: </span>**string**

-----
[internalIpAddressId]: #internalipaddressid
#### [internalIpAddressId]
The unique identifier for the ip address record that will deliver the encrypted traffic.  
<span class="type-label">Type: </span>**integer**

-----
[networkTunnelContextId]: #networktunnelcontextid
#### [networkTunnelContextId]
An address translation's network tunnel identifier.  
<span class="type-label">Type: </span>**integer**

-----
[notes]: #notes
#### [notes]
A name or description given to an address translation to help identify the address translation.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[customerIpAddressRecord]: #customeripaddressrecord
#### [customerIpAddressRecord]
The ip address record for the ip that will receive the encrypted traffic from the IPSec network tunnel.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Customer_Subnet_IpAddress'>SoftLayer_Network_Customer_Subnet_IpAddress </a>**

-----
[internalIpAddressRecord]: #internalipaddressrecord
#### [internalIpAddressRecord]
The ip address record for the ip that will deliver the encrypted traffic from the IPSec network tunnel.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**

-----
[networkTunnelContext]: #networktunnelcontext
#### [networkTunnelContext]
The IPSec network tunnel an address translation belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context'>SoftLayer_Network_Tunnel_Module_Context </a>**


## Count
</div>


