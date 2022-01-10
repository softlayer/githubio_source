---
title: "SoftLayer_Network_Component_Network_Vlan_Trunk"
description: "Represents the association between a Network_Component and Network_Vlan in the manner of a 'trunk'. Trunking a VLAN to a... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component_Network_Vlan_Trunk"
---

# SoftLayer_Network_Component_Network_Vlan_Trunk
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Component_Network_Vlan_Trunk' >Datatype</a></li>
    </ul>
</div>

## Description 


Represents the association between a Network_Component and Network_Vlan in the manner of a 'trunk'. Trunking a VLAN to a port allows that ports to receive and send packets tagged with the corresponding VLAN number. 

### External Links


* [Virtual LAN at Wikipedia](http://en.wikipedia.org/wiki/Virtual_LAN)






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
[networkComponentId]: #networkcomponentid
#### [networkComponentId]
The network component's identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[networkVlanId]: #networkvlanid
#### [networkVlanId]
The identifier of the network VLAN that is a trunk on the network component.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[networkComponent]: #networkcomponent
#### [networkComponent]
The network component that the VLAN is being trunked to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>**  



</div>
<div class="prop-row">

-----
[networkVlan]: #networkvlan
#### [networkVlan]
The VLAN that is being trunked to the network component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>**  



</div>

## Count
</div>


