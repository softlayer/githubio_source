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

## Local
-----
[description]: #description
#### [description]
A description of the package preset.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
A preset's internal identifier. Everything regarding a SoftLayer_Product_Package_Preset is tied back to this id.  
<span class="type-label">Type: </span>**integer**

-----
[isActive]: #isactive
#### [isActive]
The status of the package preset.  
<span class="type-label">Type: </span>**string**

-----
[keyName]: #keyname
#### [keyName]
The key name of the package preset. For the base configuration of a package the preset key name is "DEFAULT".  
<span class="type-label">Type: </span>**string**

-----
[name]: #name
#### [name]
The name of the package preset.  
<span class="type-label">Type: </span>**string**

-----
[packageId]: #packageid
#### [packageId]
The package id for the package this preset belongs to.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[availableStorageUnits]: #availablestorageunits
#### [availableStorageUnits]
  
<span class="type-label">Type: </span>**unsigned integer**

-----
[bareMetalReservedFlag]: #baremetalreservedflag
#### [bareMetalReservedFlag]
When true this preset is for ordering a Bare Metal Reserved server.  
<span class="type-label">Type: </span>**boolean**

-----
[categories]: #categories
#### [categories]
The item categories that are included in this package preset configuration.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category[] </a>**

-----
[computeGroup]: #computegroup
#### [computeGroup]
The compute family this configuration belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Server_Group'>SoftLayer_Product_Item_Server_Group </a>**

-----
[configuration]: #configuration
#### [configuration]
The preset configuration (category and price).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Preset_Configuration'>SoftLayer_Product_Package_Preset_Configuration[] </a>**

-----
[disallowedComputeGroupUpgradeFlag]: #disallowedcomputegroupupgradeflag
#### [disallowedComputeGroupUpgradeFlag]
When true this preset is only allowed to upgrade/downgrade to other presets in the same compute family.  
<span class="type-label">Type: </span>**boolean**

-----
[fixedConfigurationFlag]: #fixedconfigurationflag
#### [fixedConfigurationFlag]
A package preset with this flag set will not allow the price's defined in the preset configuration to be overriden during order placement.  
<span class="type-label">Type: </span>**boolean**

-----
[locations]: #locations
#### [locations]
The locations this preset configuration is available in. If empty the preset is available in all locations the package is available in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location[] </a>**

-----
[lowestPresetServerPrice]: #lowestpresetserverprice
#### [lowestPresetServerPrice]
The lowest server prices related to this package preset.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a>**

-----
[package]: #package
#### [package]
The package this preset belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a>**

-----
[packageConfiguration]: #packageconfiguration
#### [packageConfiguration]
The item categories associated with a package preset, including information detailing which item categories are required as part of a SoftLayer product order.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Order_Configuration'>SoftLayer_Product_Package_Order_Configuration[] </a>**

-----
[prices]: #prices
#### [prices]
The item prices that are included in this package preset configuration.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>**

-----
[storageGroupTemplateArrays]: #storagegrouptemplatearrays
#### [storageGroupTemplateArrays]
Describes how all disks in this preset will be configured.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group_Template_Group'>SoftLayer_Configuration_Storage_Group_Template_Group[] </a>**

-----
[totalMinimumHourlyFee]: #totalminimumhourlyfee
#### [totalMinimumHourlyFee]
The starting hourly price for this configuration. Additional options not defined in the preset may increase the cost.  
<span class="type-label">Type: </span>**decimal**

-----
[totalMinimumRecurringFee]: #totalminimumrecurringfee
#### [totalMinimumRecurringFee]
The starting monthly price for this configuration. Additional options not defined in the preset may increase the cost.  
<span class="type-label">Type: </span>**decimal**


## Count

-----
[categoryCount]: #categorycount
#### [categoryCount]
A count of the item categories that are included in this package preset configuration.   
<span class="type-label">Type: </span>**unsigned long**


-----
[configurationCount]: #configurationcount
#### [configurationCount]
A count of the preset configuration (category and price).   
<span class="type-label">Type: </span>**unsigned long**


-----
[locationCount]: #locationcount
#### [locationCount]
A count of the locations this preset configuration is available in. If empty the preset is available in all locations the package is available in.   
<span class="type-label">Type: </span>**unsigned long**


-----
[packageConfigurationCount]: #packageconfigurationcount
#### [packageConfigurationCount]
A count of the item categories associated with a package preset, including information detailing which item categories are required as part of a SoftLayer product order.   
<span class="type-label">Type: </span>**unsigned long**


-----
[priceCount]: #pricecount
#### [priceCount]
A count of the item prices that are included in this package preset configuration.   
<span class="type-label">Type: </span>**unsigned long**


-----
[storageGroupTemplateArrayCount]: #storagegrouptemplatearraycount
#### [storageGroupTemplateArrayCount]
A count of describes how all disks in this preset will be configured.   
<span class="type-label">Type: </span>**unsigned long**

</div>


