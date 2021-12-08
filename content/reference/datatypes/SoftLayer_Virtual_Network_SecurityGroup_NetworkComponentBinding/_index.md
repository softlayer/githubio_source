---
title: "SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding"
description: "The SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding data type contains general information for a single... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding"
---

# SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding data type contains general information for a single binding. A binding associates a [SoftLayer_Virtual_Guest_Network_Component]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Network_Component">}}) with a [SoftLayer_Network_SecurityGroup]({{<ref "reference/datatypes/SoftLayer_Network_SecurityGroup">}}). 





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
The unique ID for a binding.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[networkComponentId]: #networkcomponentid
#### [networkComponentId]
The ID of the network component.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[securityGroupId]: #securitygroupid
#### [securityGroupId]
The ID of the security group.  
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
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component'>SoftLayer_Virtual_Guest_Network_Component </a>**  



</div>
<div class="prop-row">

-----
[securityGroup]: #securitygroup
#### [securityGroup]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_SecurityGroup'>SoftLayer_Network_SecurityGroup </a>**  



</div>

## Count
</div>


