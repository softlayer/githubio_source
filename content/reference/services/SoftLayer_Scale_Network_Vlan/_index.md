---
title: "SoftLayer_Scale_Network_Vlan"
description: "A scale network VLAN is a VLAN that scaled members will be placed on."
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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


A scale network VLAN is a VLAN that scaled members will be placed on.



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [createObject](/reference/services/SoftLayer_Scale_Network_Vlan/createObject)
Create a network VLAN for a scale group. Once created, the VLAN will be used to scale with. 

</div>

<div class="method-row">

#### [deleteObject](/reference/services/SoftLayer_Scale_Network_Vlan/deleteObject)
Delete this network VLAN reference. Note, this does not affect existing scaled members. Once deleted however, future scaled members will not be placed on this referenced VLAN. 

</div>

<div class="method-row">

#### [getNetworkVlan](/reference/services/SoftLayer_Scale_Network_Vlan/getNetworkVlan)
Retrieve the network VLAN to scale with.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Scale_Network_Vlan/getObject)
Retrieve a SoftLayer_Scale_Network_Vlan record.

</div>

<div class="method-row">

#### [getScaleGroup](/reference/services/SoftLayer_Scale_Network_Vlan/getScaleGroup)
Retrieve the group this network VLAN is for.

</div>
</div>

</div>

