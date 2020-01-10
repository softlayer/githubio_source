---
title: "SoftLayer_Product_Package_Preset"
description: "Package presets are used to simplify ordering by eliminating the need for price ids when submitting orders. 

Orders sub... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package_Preset"
---

# SoftLayer_Product_Package_Preset
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Product_Package_Preset' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Package_Preset' >Datatype</a></li>
    </ul>
</div>

## Description 
Package presets are used to simplify ordering by eliminating the need for price ids when submitting orders. 

Orders submitted with a preset id defined will use the prices included in the package preset. Prices submitted on an order with a preset id will replace the prices included in the package preset for that prices category. If the package preset has a fixed configuration flag <em>(fixedConfigurationFlag)</em> set then the prices included in the preset configuration cannot be replaced by prices submitted on the order. The only exception to the fixed configuration flag would be if a price submitted on the order is an account-restricted price for the same product item. 





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
[description]: #description
#### [description]
A description of the package preset.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A preset's internal identifier. Everything regarding a SoftLayer_Product_Package_Preset is tied back to this id.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[isActive]: #isactive
#### [isActive]
The status of the package preset.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[keyName]: #keyname
#### [keyName]
The key name of the package preset. For the base configuration of a package the preset key name is "DEFAULT".  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The name of the package preset.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[packageId]: #packageid
#### [packageId]
The package id for the package this preset belongs to.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[availableStorageUnits]: #availablestorageunits
#### [availableStorageUnits]
  
<span class="type-label">Type: </span>**unsigned integer**


</div>
<div class="prop-row">

-----
[bareMetalReservedFlag]: #baremetalreservedflag
#### [bareMetalReservedFlag]
When true this preset is for ordering a Bare Metal Reserved server.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[categories]: #categories
#### [categories]
The item categories that are included in this package preset configuration.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category[] </a>**


</div>
<div class="prop-row">

-----
[computeGroup]: #computegroup
#### [computeGroup]
The compute family this configuration belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Server_Group'>SoftLayer_Product_Item_Server_Group </a>**


</div>
<div class="prop-row">

-----
[configuration]: #configuration
#### [configuration]
The preset configuration (category and price).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Preset_Configuration'>SoftLayer_Product_Package_Preset_Configuration[] </a>**


</div>
<div class="prop-row">

-----
[disallowedComputeGroupUpgradeFlag]: #disallowedcomputegroupupgradeflag
#### [disallowedComputeGroupUpgradeFlag]
When true this preset is only allowed to upgrade/downgrade to other presets in the same compute family.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[fixedConfigurationFlag]: #fixedconfigurationflag
#### [fixedConfigurationFlag]
A package preset with this flag set will not allow the price's defined in the preset configuration to be overriden during order placement.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[locations]: #locations
#### [locations]
The locations this preset configuration is available in. If empty the preset is available in all locations the package is available in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location[] </a>**


</div>
<div class="prop-row">

-----
[lowestPresetServerPrice]: #lowestpresetserverprice
#### [lowestPresetServerPrice]
The lowest server prices related to this package preset.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a>**


</div>
<div class="prop-row">

-----
[package]: #package
#### [package]
The package this preset belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a>**


</div>
<div class="prop-row">

-----
[packageConfiguration]: #packageconfiguration
#### [packageConfiguration]
The item categories associated with a package preset, including information detailing which item categories are required as part of a SoftLayer product order.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Order_Configuration'>SoftLayer_Product_Package_Order_Configuration[] </a>**


</div>
<div class="prop-row">

-----
[prices]: #prices
#### [prices]
The item prices that are included in this package preset configuration.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>**


</div>
<div class="prop-row">

-----
[storageGroupTemplateArrays]: #storagegrouptemplatearrays
#### [storageGroupTemplateArrays]
Describes how all disks in this preset will be configured.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group_Template_Group'>SoftLayer_Configuration_Storage_Group_Template_Group[] </a>**


</div>
<div class="prop-row">

-----
[totalMinimumHourlyFee]: #totalminimumhourlyfee
#### [totalMinimumHourlyFee]
The starting hourly price for this configuration. Additional options not defined in the preset may increase the cost.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[totalMinimumRecurringFee]: #totalminimumrecurringfee
#### [totalMinimumRecurringFee]
The starting monthly price for this configuration. Additional options not defined in the preset may increase the cost.  
<span class="type-label">Type: </span>**decimal**


</div>

## Count
<div class="prop-row">

-----
[categoryCount]: #categorycount
#### [categoryCount]
A count of the item categories that are included in this package preset configuration.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[configurationCount]: #configurationcount
#### [configurationCount]
A count of the preset configuration (category and price).   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[locationCount]: #locationcount
#### [locationCount]
A count of the locations this preset configuration is available in. If empty the preset is available in all locations the package is available in.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[packageConfigurationCount]: #packageconfigurationcount
#### [packageConfigurationCount]
A count of the item categories associated with a package preset, including information detailing which item categories are required as part of a SoftLayer product order.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[priceCount]: #pricecount
#### [priceCount]
A count of the item prices that are included in this package preset configuration.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[storageGroupTemplateArrayCount]: #storagegrouptemplatearraycount
#### [storageGroupTemplateArrayCount]
A count of describes how all disks in this preset will be configured.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


