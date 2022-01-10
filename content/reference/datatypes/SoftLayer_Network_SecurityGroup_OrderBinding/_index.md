---
title: "SoftLayer_Network_SecurityGroup_OrderBinding"
description: "The SoftLayer_Network_SecurityGroup_OrderBinding data type contains links between security groups and product orders."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_SecurityGroup_OrderBinding"
---

# SoftLayer_Network_SecurityGroup_OrderBinding
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_SecurityGroup_OrderBinding' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Network_SecurityGroup_OrderBinding data type contains links between security groups and product orders. 





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
[guestId]: #guestid
#### [guestId]
The ID of the Virtual Guest associated with the security group.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique ID for a security group, order, binding  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[orderId]: #orderid
#### [orderId]
The ID of the order associated with the security group.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[securityGroupId]: #securitygroupid
#### [securityGroupId]
The ID of the security group that is associated with the order.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[guest]: #guest
#### [guest]
The virtual guest associated with the binding  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**  



</div>
<div class="prop-row">

-----
[order]: #order
#### [order]
The order associated with the binding  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order </a>**  



</div>
<div class="prop-row">

-----
[securityGroup]: #securitygroup
#### [securityGroup]
The security group associated with the order  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_SecurityGroup'>SoftLayer_Network_SecurityGroup </a>**  



</div>

## Count
</div>


