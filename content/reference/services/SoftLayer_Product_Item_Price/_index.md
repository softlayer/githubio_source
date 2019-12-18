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

#### [getAccountRestrictions](/reference/services/SoftLayer_Product_Item_Price/getAccountRestrictions)
Retrieve the account that the item price is restricted to.

#### [getAttributes](/reference/services/SoftLayer_Product_Item_Price/getAttributes)


#### [getBareMetalReservedCapacityFlag](/reference/services/SoftLayer_Product_Item_Price/getBareMetalReservedCapacityFlag)
Retrieve signifies pricing that is only available on a bare metal reserved capacity order.

#### [getBigDataOsJournalDiskFlag](/reference/services/SoftLayer_Product_Item_Price/getBigDataOsJournalDiskFlag)
Retrieve whether the price is for Big Data OS/Journal disks only. (Deprecated)

#### [getBundleReferences](/reference/services/SoftLayer_Product_Item_Price/getBundleReferences)
Retrieve cross reference for bundles

#### [getCapacityRestrictionMaximum](/reference/services/SoftLayer_Product_Item_Price/getCapacityRestrictionMaximum)
Retrieve the maximum capacity value for which this price is suitable.

#### [getCapacityRestrictionMinimum](/reference/services/SoftLayer_Product_Item_Price/getCapacityRestrictionMinimum)
Retrieve the minimum capacity value for which this price is suitable.

#### [getCapacityRestrictionType](/reference/services/SoftLayer_Product_Item_Price/getCapacityRestrictionType)
Retrieve the type of capacity restriction by which this price must abide.

#### [getCategories](/reference/services/SoftLayer_Product_Item_Price/getCategories)
Retrieve all categories which this item is a member.

#### [getDedicatedHostInstanceFlag](/reference/services/SoftLayer_Product_Item_Price/getDedicatedHostInstanceFlag)
Retrieve signifies pricing that is only available on a dedicated host virtual server order.

#### [getDefinedSoftwareLicenseFlag](/reference/services/SoftLayer_Product_Item_Price/getDefinedSoftwareLicenseFlag)
Retrieve whether this price defines a software license for its product item.

#### [getEligibilityStrategy](/reference/services/SoftLayer_Product_Item_Price/getEligibilityStrategy)
Retrieve eligibility strategy to assess if a customer can order using this price.

#### [getItem](/reference/services/SoftLayer_Product_Item_Price/getItem)
Retrieve the product item a price is tied to.

#### [getObject](/reference/services/SoftLayer_Product_Item_Price/getObject)
Retrieve a SoftLayer_Product_Item_Price record.

#### [getOrderPremiums](/reference/services/SoftLayer_Product_Item_Price/getOrderPremiums)


#### [getPackageReferences](/reference/services/SoftLayer_Product_Item_Price/getPackageReferences)
Retrieve cross reference for packages

#### [getPackages](/reference/services/SoftLayer_Product_Item_Price/getPackages)
Retrieve a price's packages under which this item is sold.

#### [getPresetConfigurations](/reference/services/SoftLayer_Product_Item_Price/getPresetConfigurations)
Retrieve a list of preset configurations this price is used in.'

#### [getPriceType](/reference/services/SoftLayer_Product_Item_Price/getPriceType)
Retrieve the type keyname of this price which can be STANDARD or TIERED.

#### [getPricingLocationGroup](/reference/services/SoftLayer_Product_Item_Price/getPricingLocationGroup)
Retrieve the pricing location group that this price is applicable for. Prices that have a pricing location group will only be available for ordering with the locations specified on the location group.

#### [getRequiredCoreCount](/reference/services/SoftLayer_Product_Item_Price/getRequiredCoreCount)
Retrieve the number of server cores required to order this item. This is deprecated. Use [SoftLayer_Product_Item_Price::getCapacityRestrictionMinimum]({{<ref "reference/services/SoftLayer_Product_Item_Price/getCapacityRestrictionMinimum">}})

#### [getReservedCapacityInstanceFlag](/reference/services/SoftLayer_Product_Item_Price/getReservedCapacityInstanceFlag)
Retrieve signifies pricing that is only available on a reserved capacity virtual server order.

#### [getUsageRatePrices](/reference/services/SoftLayer_Product_Item_Price/getUsageRatePrices)
Get all the rate-based prices for the location and items specified. 

</div>

