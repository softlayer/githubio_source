---
title: "SoftLayer_Provisioning_Maintenance_Window"
description: "The SoftLayer_Provisioning_Maintenance_Window represent a time window that SoftLayer performs a hardware or software mai... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Provisioning"
classes:
    - "SoftLayer_Provisioning_Maintenance_Window"
---

# SoftLayer_Provisioning_Maintenance_Window
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Provisioning_Maintenance_Window' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Provisioning_Maintenance_Window' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Provisioning_Maintenance_Window represent a time window that SoftLayer performs a hardware or software maintenance and upgrades. 


### associatedMethods

*  [SoftLayer_Provisioning_Maintenance_Window::getMaintenanceWindows](/reference/services/SoftLayer_Provisioning_Maintenance_Window/getMaintenanceWindows )



### seeAlso

* [SoftLayer_Product_Order_Upgrade_Request](/reference/datatypes/SoftLayer_Product_Order_Upgrade_Request )




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
                <a href="#beginDate" name=beginDate>beginDate</a>
            </span>
            <div class='views-field-body'>The date and time a maintenance window is scheduled to begin. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#dayOfWeek" name=dayOfWeek>dayOfWeek</a>
            </span>
            <div class='views-field-body'>An ISO-8601 numeric representation of the day of the week that a maintenance window is performed. 1: Monday, 7: Sunday </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#endDate" name=endDate>endDate</a>
            </span>
            <div class='views-field-body'>The date and time a maintenance window is scheduled to end. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>Id of the maintenance window </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#locationId" name=locationId>locationId</a>
            </span>
            <div class='views-field-body'>An internal identifier of the location (data center) record that a maintenance window takes place in. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#portalTzId" name=portalTzId>portalTzId</a>
            </span>
            <div class='views-field-body'>An internal identifier of the datacenter timezone. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
    </div>


