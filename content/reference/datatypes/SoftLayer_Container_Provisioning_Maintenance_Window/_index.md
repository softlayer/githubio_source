---
title: "SoftLayer_Container_Provisioning_Maintenance_Window"
description: "This is the datatype that needs to be populated and sent to SoftLayer_Provisioning_Maintenance_Window::addCustomerUpgrad... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Provisioning_Maintenance_Window"
---

# SoftLayer_Container_Provisioning_Maintenance_Window
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Provisioning_Maintenance_Window' >Datatype</a></li>
    </ul>
</div>

## Description 
This is the datatype that needs to be populated and sent to SoftLayer_Provisioning_Maintenance_Window::addCustomerUpgradeWindow. This datatype has everything required to place an order with SoftLayer. 





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
                <a href="#classificationIds" name=classificationIds>classificationIds</a>
            </span>
            <div class='views-field-body'>Maintenance classifications. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Provisioning_Maintenance_Classification'>SoftLayer_Provisioning_Maintenance_Classification[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemCategoryIds" name=itemCategoryIds>itemCategoryIds</a>
            </span>
            <div class='views-field-body'>Maintenance classifications. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#maintenanceWindowId" name=maintenanceWindowId>maintenanceWindowId</a>
            </span>
            <div class='views-field-body'>The maintenance window id </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ticketId" name=ticketId>ticketId</a>
            </span>
            <div class='views-field-body'>Maintenance window ticket id </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#windowMaintenanceDate" name=windowMaintenanceDate>windowMaintenanceDate</a>
            </span>
            <div class='views-field-body'>Maintenance window date </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
            </div>
    </div>


