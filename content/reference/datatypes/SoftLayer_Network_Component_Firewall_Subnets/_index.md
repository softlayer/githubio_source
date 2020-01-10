---
title: "SoftLayer_Network_Component_Firewall_Subnets"
description: "A SoftLayer_Network_Component_Firewall_Subnets object type represents the current linked subnets and contains relative i... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component_Firewall_Subnets"
---

# SoftLayer_Network_Component_Firewall_Subnets
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Component_Firewall_Subnets' >Datatype</a></li>
    </ul>
</div>

## Description 
A SoftLayer_Network_Component_Firewall_Subnets object type represents the current linked subnets and contains relative information. Use the [[SoftLayer Network Firewall Update Request]] service to submit a firewall update request. Use the [[SoftLayer Network Firewall Template]] service to pull SoftLayer recommended rule set templates. 

### External Links


* [Firewall at Wikipedia](http://en.wikipedia.org/wiki/Firewall_(networking))






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
[applyServerRulesFlag]: #applyserverrulesflag
#### [applyServerRulesFlag]
A boolean flag that indicates whether the subnet should receive all the rules intended for the host on this context slot.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[subnetId]: #subnetid
#### [subnetId]
The unique identifier of the subnet being linked to the network component firewall.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[networkComponentFirewall]: #networkcomponentfirewall
#### [networkComponentFirewall]
The network component firewall that write rules for this subnet.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component_Firewall'>SoftLayer_Network_Component_Firewall </a>**


</div>
<div class="prop-row">

-----
[subnet]: #subnet
#### [subnet]
The subnet that this link binds to the network component firewall.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>**


</div>

## Count
</div>


