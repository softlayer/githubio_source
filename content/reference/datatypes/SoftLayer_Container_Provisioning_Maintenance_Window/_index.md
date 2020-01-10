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
[classificationIds]: #classificationids
#### [classificationIds]
Maintenance classifications.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Maintenance_Classification'>SoftLayer_Provisioning_Maintenance_Classification[] </a>**


</div>
<div class="prop-row">

-----
[itemCategoryIds]: #itemcategoryids
#### [itemCategoryIds]
Maintenance classifications.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category[] </a>**


</div>
<div class="prop-row">

-----
[maintenanceWindowId]: #maintenancewindowid
#### [maintenanceWindowId]
The maintenance window id  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[ticketId]: #ticketid
#### [ticketId]
Maintenance window ticket id  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[windowMaintenanceDate]: #windowmaintenancedate
#### [windowMaintenanceDate]
Maintenance window date  
<span class="type-label">Type: </span>**dateTime**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


