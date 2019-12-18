---
title: "SoftLayer_Product_Package_Preset"
description: ""
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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




        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [getAllObjects](/reference/services/SoftLayer_Product_Package_Preset/getAllObjects)
Get all active package presets

#### [getAvailableStorageUnits](/reference/services/SoftLayer_Product_Package_Preset/getAvailableStorageUnits)


#### [getBareMetalReservedFlag](/reference/services/SoftLayer_Product_Package_Preset/getBareMetalReservedFlag)
Retrieve when true this preset is for ordering a Bare Metal Reserved server.

#### [getCategories](/reference/services/SoftLayer_Product_Package_Preset/getCategories)
Retrieve the item categories that are included in this package preset configuration.

#### [getComputeGroup](/reference/services/SoftLayer_Product_Package_Preset/getComputeGroup)
Retrieve the compute family this configuration belongs to.

#### [getConfiguration](/reference/services/SoftLayer_Product_Package_Preset/getConfiguration)
Retrieve the preset configuration (category and price).

#### [getDisallowedComputeGroupUpgradeFlag](/reference/services/SoftLayer_Product_Package_Preset/getDisallowedComputeGroupUpgradeFlag)
Retrieve when true this preset is only allowed to upgrade/downgrade to other presets in the same compute family.

#### [getFixedConfigurationFlag](/reference/services/SoftLayer_Product_Package_Preset/getFixedConfigurationFlag)
Retrieve a package preset with this flag set will not allow the price's defined in the preset configuration to be overriden during order placement.

#### [getLocations](/reference/services/SoftLayer_Product_Package_Preset/getLocations)
Retrieve the locations this preset configuration is available in. If empty the preset is available in all locations the package is available in.

#### [getLowestPresetServerPrice](/reference/services/SoftLayer_Product_Package_Preset/getLowestPresetServerPrice)
Retrieve the lowest server prices related to this package preset.

#### [getObject](/reference/services/SoftLayer_Product_Package_Preset/getObject)
Retrieve a SoftLayer_Product_Package_Preset record.

#### [getPackage](/reference/services/SoftLayer_Product_Package_Preset/getPackage)
Retrieve the package this preset belongs to.

#### [getPackageConfiguration](/reference/services/SoftLayer_Product_Package_Preset/getPackageConfiguration)
Retrieve the item categories associated with a package preset, including information detailing which item categories are required as part of a SoftLayer product order.

#### [getPrices](/reference/services/SoftLayer_Product_Package_Preset/getPrices)
Retrieve the item prices that are included in this package preset configuration.

#### [getStorageGroupTemplateArrays](/reference/services/SoftLayer_Product_Package_Preset/getStorageGroupTemplateArrays)
Retrieve describes how all disks in this preset will be configured.

#### [getTotalMinimumHourlyFee](/reference/services/SoftLayer_Product_Package_Preset/getTotalMinimumHourlyFee)
Retrieve the starting hourly price for this configuration. Additional options not defined in the preset may increase the cost.

#### [getTotalMinimumRecurringFee](/reference/services/SoftLayer_Product_Package_Preset/getTotalMinimumRecurringFee)
Retrieve the starting monthly price for this configuration. Additional options not defined in the preset may increase the cost.

</div>

