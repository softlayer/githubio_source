---
title: "SoftLayer_Network_Gateway_Vlan"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway_Vlan"
---

# SoftLayer_Network_Gateway_Vlan
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Gateway_Vlan' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Gateway_Vlan' >Datatype</a></li>
    </ul>
</div>

## Description 






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
[bypassFlag]: #bypassflag
#### [bypassFlag]
If true, this VLAN is bypassed. If false, it is routed through the gateway.   
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A gateway VLAN's internal identifier.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[networkGatewayId]: #networkgatewayid
#### [networkGatewayId]
The internal identifier of the gateway this VLAN is attached to.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[networkVlanId]: #networkvlanid
#### [networkVlanId]
The internal identifier of the network VLAN.   
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[networkGateway]: #networkgateway
#### [networkGateway]
The gateway this VLAN is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway </a>**


</div>
<div class="prop-row">

-----
[networkVlan]: #networkvlan
#### [networkVlan]
The network VLAN record.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>**


</div>

## Count
</div>


