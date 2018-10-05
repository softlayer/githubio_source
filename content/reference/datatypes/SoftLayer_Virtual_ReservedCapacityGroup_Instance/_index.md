---
title: "SoftLayer_Virtual_ReservedCapacityGroup_Instance"
description: "This data type presents the structure for a virtual reserved capacity group instance."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_ReservedCapacityGroup_Instance"
---

# SoftLayer_Virtual_ReservedCapacityGroup_Instance
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Virtual_ReservedCapacityGroup_Instance' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_ReservedCapacityGroup_Instance' >Datatype</a></li>
    </ul>
</div>

## Description 
This data type presents the structure for a virtual reserved capacity group instance. 





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
            <span class='views-field-title'>
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>The date that the reserved capacity group instance was created.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#guestId" name=guestId>guestId</a>
            </span>
            <div class='views-field-body'>The virtual guest ID associated with this reserved capacity group instance.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The reserved capacity group instance's associated unique ID.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>The date that the reserved capacity group instance was last modified.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#reservedCapacityGroupId" name=reservedCapacityGroupId>reservedCapacityGroupId</a>
            </span>
            <div class='views-field-body'>The ID of the reserved capacity group this instance is associated with.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#availableFlag" name=availableFlag>availableFlag</a>
            </span>
            <div class='views-field-body'>Flag to indecate whether or not the reserved instance is available or not. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingItem" name=billingItem>billingItem</a>
            </span>
            <div class='views-field-body'>The billing item for the reserved capacity group instance. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#guest" name=guest>guest</a>
            </span>
            <div class='views-field-body'>The virtual guest associated with this reserved capacity group instance. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#reservedCapacityGroup" name=reservedCapacityGroup>reservedCapacityGroup</a>
            </span>
            <div class='views-field-body'>The reserved instances that are members of this reserved capacity group. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Virtual_ReservedCapacityGroup'>SoftLayer_Virtual_ReservedCapacityGroup </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


