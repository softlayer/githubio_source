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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#description" name=description>description</a></span>
            <div class='views-field-body'>A description of the package preset. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A preset's internal identifier. Everything regarding a SoftLayer_Product_Package_Preset is tied back to this id. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#isActive" name=isActive>isActive</a></span>
            <div class='views-field-body'>The status of the package preset. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#keyName" name=keyName>keyName</a></span>
            <div class='views-field-body'>The key name of the package preset. For the base configuration of a package the preset key name is "DEFAULT". </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>The name of the package preset. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#packageId" name=packageId>packageId</a></span>
            <div class='views-field-body'>The package id for the package this preset belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#availableStorageUnits" name=availableStorageUnits>availableStorageUnits</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsigned integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#categories" name=categories>categories</a></span>
            <div class='views-field-body'>The item categories that are included in this package preset configuration. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#computeGroup" name=computeGroup>computeGroup</a></span>
            <div class='views-field-body'>The compute family this configuration belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Server_Group'>SoftLayer_Product_Item_Server_Group </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#configuration" name=configuration>configuration</a></span>
            <div class='views-field-body'>The preset configuration (category and price). </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package_Preset_Configuration'>SoftLayer_Product_Package_Preset_Configuration[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#disallowedComputeGroupUpgradeFlag" name=disallowedComputeGroupUpgradeFlag>disallowedComputeGroupUpgradeFlag</a></span>
            <div class='views-field-body'>When true this preset is only allowed to upgrade/downgrade to other presets in the same compute family. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#fixedConfigurationFlag" name=fixedConfigurationFlag>fixedConfigurationFlag</a></span>
            <div class='views-field-body'>A package preset with this flag set will not allow the price's defined in the preset configuration to be overriden during order placement. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#locations" name=locations>locations</a></span>
            <div class='views-field-body'>The locations this preset configuration is available in. If empty the preset is available in all locations the package is available in. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#lowestPresetServerPrice" name=lowestPresetServerPrice>lowestPresetServerPrice</a></span>
            <div class='views-field-body'>The lowest server prices related to this package preset. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#package" name=package>package</a></span>
            <div class='views-field-body'>The package this preset belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#packageConfiguration" name=packageConfiguration>packageConfiguration</a></span>
            <div class='views-field-body'>The item categories associated with a package preset, including information detailing which item categories are required as part of a SoftLayer product order. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Package_Order_Configuration'>SoftLayer_Product_Package_Order_Configuration[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#prices" name=prices>prices</a></span>
            <div class='views-field-body'>The item prices that are included in this package preset configuration. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#storageGroupTemplateArrays" name=storageGroupTemplateArrays>storageGroupTemplateArrays</a></span>
            <div class='views-field-body'>Describes how all disks in this preset will be configured. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group_Template_Group'>SoftLayer_Configuration_Storage_Group_Template_Group[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#totalMinimumHourlyFee" name=totalMinimumHourlyFee>totalMinimumHourlyFee</a></span>
            <div class='views-field-body'>The starting hourly price for this configuration. Additional options not defined in the preset may increase the cost. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#totalMinimumRecurringFee" name=totalMinimumRecurringFee>totalMinimumRecurringFee</a></span>
            <div class='views-field-body'>The starting monthly price for this configuration. Additional options not defined in the preset may increase the cost. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
            </div>
</div>


