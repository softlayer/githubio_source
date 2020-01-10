---
title: "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress_SecureTransportProtocol"
description: "Links a SSL transport protocol with a virtual IP address instance. Instances of this class are immutable and should refl... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress_SecureTransportProtocol"
---

# SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress_SecureTransportProtocol
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress_SecureTransportProtocol' >Datatype</a></li>
    </ul>
</div>

## Description 
Links a SSL transport protocol with a virtual IP address instance. Instances of this class are immutable and should reflect a protocol that is configurable on a load balancer device. 





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
[id]: #id
#### [id]
Unique identifier for the protocol instance  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[keyName]: #keyname
#### [keyName]
Identifier for the associated communication protocol  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[virtualIpAddressId]: #virtualipaddressid
#### [virtualIpAddressId]
Identifier for the associated [SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress]({{<ref "reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress">}}) instance   
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[virtualIpAddress]: #virtualipaddress
#### [virtualIpAddress]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress </a>**


</div>

## Count
</div>


