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





<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
    <div id="localProperties" class="prop-content" >
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#guestId" name=guestId>guestId</a></span>
            <div class='views-field-body'>The ID of the Virtual Guest associated with the security group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The unique ID for a security group, order, binding </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderId" name=orderId>orderId</a></span>
            <div class='views-field-body'>The ID of the order associated with the security group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#securityGroupId" name=securityGroupId>securityGroupId</a></span>
            <div class='views-field-body'>The ID of the security group that is associated with the order. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#guest" name=guest>guest</a></span>
            <div class='views-field-body'>The virtual guest associated with the binding </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#order" name=order>order</a></span>
            <div class='views-field-body'>The order associated with the binding </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#securityGroup" name=securityGroup>securityGroup</a></span>
            <div class='views-field-body'>The security group associated with the order </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_SecurityGroup'>SoftLayer_Network_SecurityGroup </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


