---
title: "SoftLayer_Hardware_Status"
description: "SoftLayer_Hardware_Status models the inventory state of any piece of hardware in SoftLayer's inventory. Most of these st... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Status"
---

# SoftLayer_Hardware_Status
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Status' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Hardware_Status models the inventory state of any piece of hardware in SoftLayer's inventory. Most of these statuses are used by SoftLayer while a server is not provisioned or undergoing provisioning. SoftLayer uses the following status codes: 


*'''ACTIVE''': This server is active and in use.
*'''DEPLOY''': Used during server provisioning.
*'''DEPLOY2''': Used during server provisioning.
*'''MACWAIT''': Used during server provisioning.
*'''RECLAIM''': This server has been reclaimed by SoftLayer and is awaiting de-provisioning.


Servers in production and in use should stay in the ACTIVE state. If a server's status ever reads anything else then please contact SoftLayer support. 


### associatedMethods

*  [SoftLayer_Hardware::getHardwareStatus](/reference/services/SoftLayer_Hardware/getHardwareStatus )



### seeAlso

* [SoftLayer_Hardware](/reference/services/SoftLayer_Hardware )




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
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>A hardware status' internal identifier. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#status" name=status>status</a>
            </span>
            <div class='views-field-body'>A hardware's status code. See the SoftLayer_Hardware_Status Overview for ''status''' possible values. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


