---
title: "SoftLayer_Scale_Network_Vlan"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Network_Vlan"
---

# SoftLayer_Scale_Network_Vlan
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Scale_Network_Vlan' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Scale_Network_Vlan' >Datatype</a></li>
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
[createDate]: #createdate
#### [createDate]
When this network VLAN reference was created.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[deleteFlag]: #deleteflag
#### [deleteFlag]
When set and true any edit that happens on this object, be it calling edit on this directly or setting as a child while editing a parent object, will end up being a deletion.   
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The network VLAN reference's internal identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[networkVlanId]: #networkvlanid
#### [networkVlanId]
The identifier for the VLAN to scale with.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[scaleGroupId]: #scalegroupid
#### [scaleGroupId]
The identifier of the group this network VLAN reference applies to.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[networkVlan]: #networkvlan
#### [networkVlan]
The network VLAN to scale with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>**


</div>
<div class="prop-row">

-----
[scaleGroup]: #scalegroup
#### [scaleGroup]
The group this network VLAN is for.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Group'>SoftLayer_Scale_Group </a>**


</div>

## Count
</div>


