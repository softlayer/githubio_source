---
title: "SoftLayer_Network_Gateway_Member"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway_Member"
---

# SoftLayer_Network_Gateway_Member
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Gateway_Member' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Gateway_Member' >Datatype</a></li>
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
[hardwareId]: #hardwareid
#### [hardwareId]
The internal identifier of the hardware for this member.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A gateway member's internal identifier.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[networkGatewayId]: #networkgatewayid
#### [networkGatewayId]
The internal identifier of the gateway this member belongs to.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[priority]: #priority
#### [priority]
The priority for this gateway member. This is set internally and cannot be provided on create.   
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[attributes]: #attributes
#### [attributes]
The attributes for this member.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway_Member_Attribute'>SoftLayer_Network_Gateway_Member_Attribute </a>**  



</div>
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
The device for this member.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**  



</div>
<div class="prop-row">

-----
[networkGateway]: #networkgateway
#### [networkGateway]
The gateway this member belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway </a>**  



</div>

## Count
</div>


