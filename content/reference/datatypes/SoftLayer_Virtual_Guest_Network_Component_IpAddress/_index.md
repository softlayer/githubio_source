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
[ipAddressId]: #ipaddressid
#### [ipAddressId]
The unique ID of the [SoftLayer_Network_Subnet_ipAddress]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_ipAddress">}}) this virtual IP address is associated with.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[port]: #port
#### [port]
The port that a network component has reserved.  This field is only required for some IP address types.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The type of IP that this IP address record references.  Some examples are PRIMARY for the network component's primary IP address and CONSOLE_PROXY which represents the IP information for logging into a computing instance's console.   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[ipAddress]: #ipaddress
#### [ipAddress]
The IP address associated with this object's network component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**


</div>
<div class="prop-row">

-----
[networkComponent]: #networkcomponent
#### [networkComponent]
The network component associated with this object's IP address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component'>SoftLayer_Virtual_Guest_Network_Component </a>**


</div>

## Count
</div>


