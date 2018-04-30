---
title: "SoftLayer_Product_Item_Price"
description: "The SoftLayer_Product_Item_Price contains general information relating to a single SoftLayer product item price. You can... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Price"
---
# SoftLayer_Product_Item_Price
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Product_Item_Price' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Item_Price' >Datatype</a></li>
    </ul>
</div>

## Description
The SoftLayer_Product_Item_Price contains general information relating to a single SoftLayer product item price. You can find out what packages each price is in as well as which category under which this price is sold. All prices are returned in floating point values measured in US Dollars ($USD). 



        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getAccountRestrictions'> getAccountRestrictions</a> </span>
            <div class='views-field-body'>Retrieve the account that the item price is restricted to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getAttributes'> getAttributes</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getBigDataOsJournalDiskFlag'> getBigDataOsJournalDiskFlag</a> </span>
            <div class='views-field-body'>Retrieve whether the price is for Big Data OS/Journal disks only. (Deprecated)</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getBundleReferences'> getBundleReferences</a> </span>
            <div class='views-field-body'>Retrieve cross reference for bundles</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getCapacityRestrictionMaximum'> getCapacityRestrictionMaximum</a> </span>
            <div class='views-field-body'>Retrieve the maximum capacity value for which this price is suitable.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getCapacityRestrictionMinimum'> getCapacityRestrictionMinimum</a> </span>
            <div class='views-field-body'>Retrieve the minimum capacity value for which this price is suitable.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getCapacityRestrictionType'> getCapacityRestrictionType</a> </span>
            <div class='views-field-body'>Retrieve the type of capacity restriction by which this price must abide.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getCategories'> getCategories</a> </span>
            <div class='views-field-body'>Retrieve all categories which this item is a member.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getDedicatedHostInstanceFlag'> getDedicatedHostInstanceFlag</a> </span>
            <div class='views-field-body'>Retrieve signifies pricing that is only available on a dedicated host virtual server order.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getDefinedSoftwareLicenseFlag'> getDefinedSoftwareLicenseFlag</a> </span>
            <div class='views-field-body'>Retrieve whether this price defines a software license for its product item.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getItem'> getItem</a> </span>
            <div class='views-field-body'>Retrieve the product item a price is tied to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Product_Item_Price record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getOrderPremiums'> getOrderPremiums</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getPackageReferences'> getPackageReferences</a> </span>
            <div class='views-field-body'>Retrieve cross reference for packages</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getPackages'> getPackages</a> </span>
            <div class='views-field-body'>Retrieve a price's packages under which this item is sold.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getPresetConfigurations'> getPresetConfigurations</a> </span>
            <div class='views-field-body'>Retrieve a list of preset configurations this price is used in.'</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getPriceType'> getPriceType</a> </span>
            <div class='views-field-body'>Retrieve the type keyname of this price which can be STANDARD or TIERED.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getPricingLocationGroup'> getPricingLocationGroup</a> </span>
            <div class='views-field-body'>Retrieve the pricing location group that this price is applicable for. Prices that have a pricing location group will only be available for ordering with the locations specified on the location group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getRequiredCoreCount'> getRequiredCoreCount</a> </span>
            <div class='views-field-body'>Retrieve the number of server cores required to order this item. This is deprecated. Use [[SoftLayer_Product_Item_Price/getCapacityRestrictionMinimum|getCapacityRestrictionMinimum]] and [[SoftLayer_Product_Item_Price/getCapacityRestrictionMaximum|getCapacityRestrictionMaximum]]</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Item_Price/getUsageRatePrices'> getUsageRatePrices</a> </span>
            <div class='views-field-body'>Get all the rate-based prices for the location and items specified. </div>
        </div>
        </div>
</div>

