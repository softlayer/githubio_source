---
title: "SoftLayer_Product_Item_Price"
description: "The SoftLayer_Product_Item_Price data type contains general information relating to a single SoftLayer product item pric... "
layout: "datatype"
tags:
    - "datatype"
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
The SoftLayer_Product_Item_Price data type contains general information relating to a single SoftLayer product item price. You can find out what packages each price is in as well as which category under which this price is sold. All prices are returned in floating point values measured in US Dollars ($USD). 



### seeAlso

* [SoftLayer_Product_Item (type)](/reference/datatypes/SoftLayer_Product_Item (type) )


* [SoftLayer_Product_Item_Category](/reference/datatypes/SoftLayer_Product_Item_Category )




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
[currentPriceFlag]: #currentpriceflag
#### [currentPriceFlag]
This flag is used by the getUpgradeItemPrices methods available on various resources to indicate if a product price is used for the current billing item.   
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[hourlyRecurringFee]: #hourlyrecurringfee
#### [hourlyRecurringFee]
The hourly price for this item, should this item be part of an hourly pricing package.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique identifier of a Product Item Price.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[itemId]: #itemid
#### [itemId]
The unique identifier for a product Item  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[laborFee]: #laborfee
#### [laborFee]
The labor fee for a product item price.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[locationGroupId]: #locationgroupid
#### [locationGroupId]
The id of the [SoftLayer_Location_Group_Pricing]({{<ref "reference/datatypes/SoftLayer_Location_Group_Pricing">}}) that this price is part of. If set to null, the price is considered a standard price, which can be used with any location when ordering. 

During order [SoftLayer_Product_Order::verifyOrder]({{<ref "reference/services/SoftLayer_Product_Order/verifyOrder">}}), if a standard price is used, that price may be replaced with a location based price, which does not have this property set to null. The location based price must be part of a [SoftLayer_Location_Group_Pricing]({{<ref "reference/datatypes/SoftLayer_Location_Group_Pricing">}}) that has the location being ordered in order for this to happen.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[onSaleFlag]: #onsaleflag
#### [onSaleFlag]
On sale flag.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[oneTimeFee]: #onetimefee
#### [oneTimeFee]
The one time fee for a product item price.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[oneTimeFeeTax]: #onetimefeetax
#### [oneTimeFeeTax]
A price's total tax amount of the one time fees (oneTimeFee, laborFee, and setupFee). This is only populated after the order is verified via SoftLayer_Product_Order::verifyOrder()  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[orderOptions]: #orderoptions
#### [orderOptions]
Order options for the category that this price is associated with.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category_Order_Option_Type'>SoftLayer_Product_Item_Category_Order_Option_Type[] </a>**


</div>
<div class="prop-row">

-----
[proratedRecurringFee]: #proratedrecurringfee
#### [proratedRecurringFee]
A recurring fee is a fee that happens every billing period. This fee is represented as a floating point decimal in US dollars ($USD).  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[proratedRecurringFeeTax]: #proratedrecurringfeetax
#### [proratedRecurringFeeTax]
A price's tax amount of the recurring fee. This is only populated after the order is verified via SoftLayer_Product_Order::verifyOrder()  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[quantity]: #quantity
#### [quantity]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[recurringFee]: #recurringfee
#### [recurringFee]
A recurring fee is a fee that happens every billing period. This fee is represented as a floating point decimal in US dollars ($USD).  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[recurringFeeTax]: #recurringfeetax
#### [recurringFeeTax]
A price's tax amount of the recurring fee. This is only populated after the order is verified via SoftLayer_Product_Order::verifyOrder()  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[setupFee]: #setupfee
#### [setupFee]
The setup fee associated with a product item price.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[sort]: #sort
#### [sort]
Used for ordering items on sales orders.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[termLength]: #termlength
#### [termLength]
The number of months a term lasts for a term-based price  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[tierMinimumThreshold]: #tierminimumthreshold
#### [tierMinimumThreshold]
The minimum threshold for which this tiered usage price begins to apply.  The unit for the price is defined by the item to which this belongs, see [[SoftLayer_Product_Item::$units]].   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[usageRate]: #usagerate
#### [usageRate]
The rate for a usage based item  
<span class="type-label">Type: </span>**decimal**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[accountRestrictions]: #accountrestrictions
#### [accountRestrictions]
The account that the item price is restricted to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price_Account_Restriction'>SoftLayer_Product_Item_Price_Account_Restriction[] </a>**


</div>
<div class="prop-row">

-----
[attributes]: #attributes
#### [attributes]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price_Attribute'>SoftLayer_Product_Item_Price_Attribute[] </a>**


</div>
<div class="prop-row">

-----
[bareMetalReservedCapacityFlag]: #baremetalreservedcapacityflag
#### [bareMetalReservedCapacityFlag]
Signifies pricing that is only available on a bare metal reserved capacity order.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[bigDataOsJournalDiskFlag]: #bigdataosjournaldiskflag
#### [bigDataOsJournalDiskFlag]
Whether the price is for Big Data OS/Journal disks only. (Deprecated)  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[bundleReferences]: #bundlereferences
#### [bundleReferences]
cross reference for bundles  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Bundles'>SoftLayer_Product_Item_Bundles[] </a>**


</div>
<div class="prop-row">

-----
[capacityRestrictionMaximum]: #capacityrestrictionmaximum
#### [capacityRestrictionMaximum]
The maximum capacity value for which this price is suitable.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[capacityRestrictionMinimum]: #capacityrestrictionminimum
#### [capacityRestrictionMinimum]
The minimum capacity value for which this price is suitable.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[capacityRestrictionType]: #capacityrestrictiontype
#### [capacityRestrictionType]
The type of capacity restriction by which this price must abide.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[categories]: #categories
#### [categories]
All categories which this item is a member.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category[] </a>**


</div>
<div class="prop-row">

-----
[dedicatedHostInstanceFlag]: #dedicatedhostinstanceflag
#### [dedicatedHostInstanceFlag]
Signifies pricing that is only available on a dedicated host virtual server order.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[definedSoftwareLicenseFlag]: #definedsoftwarelicenseflag
#### [definedSoftwareLicenseFlag]
Whether this price defines a software license for its product item.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[eligibilityStrategy]: #eligibilitystrategy
#### [eligibilityStrategy]
Eligibility strategy to assess if a customer can order using this price.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[item]: #item
#### [item]
The product item a price is tied to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**


</div>
<div class="prop-row">

-----
[orderPremiums]: #orderpremiums
#### [orderPremiums]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price_Premium'>SoftLayer_Product_Item_Price_Premium[] </a>**


</div>
<div class="prop-row">

-----
[packageReferences]: #packagereferences
#### [packageReferences]
cross reference for packages  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Item_Prices'>SoftLayer_Product_Package_Item_Prices[] </a>**


</div>
<div class="prop-row">

-----
[packages]: #packages
#### [packages]
A price's packages under which this item is sold.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package[] </a>**


</div>
<div class="prop-row">

-----
[presetConfigurations]: #presetconfigurations
#### [presetConfigurations]
A list of preset configurations this price is used in.'  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Preset_Configuration'>SoftLayer_Product_Package_Preset_Configuration[] </a>**


</div>
<div class="prop-row">

-----
[priceType]: #pricetype
#### [priceType]
The type keyname of this price which can be STANDARD, TIERED, or TERM.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[pricingLocationGroup]: #pricinglocationgroup
#### [pricingLocationGroup]
The pricing location group that this price is applicable for. Prices that have a pricing location group will only be available for ordering with the locations specified on the location group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location_Group_Pricing'>SoftLayer_Location_Group_Pricing </a>**


</div>
<div class="prop-row">

-----
[requiredCoreCount]: #requiredcorecount
#### [requiredCoreCount]
The number of server cores required to order this item. This is deprecated. Use [SoftLayer_Product_Item_Price::getCapacityRestrictionMinimum]({{<ref "reference/services/SoftLayer_Product_Item_Price/getCapacityRestrictionMinimum">}})  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[reservedCapacityInstanceFlag]: #reservedcapacityinstanceflag
#### [reservedCapacityInstanceFlag]
Signifies pricing that is only available on a reserved capacity virtual server order.  
<span class="type-label">Type: </span>**boolean**


</div>

## Count
<div class="prop-row">

-----
[accountRestrictionCount]: #accountrestrictioncount
#### [accountRestrictionCount]
A count of the account that the item price is restricted to.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[bundleReferenceCount]: #bundlereferencecount
#### [bundleReferenceCount]
A count of cross reference for bundles   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[categoryCount]: #categorycount
#### [categoryCount]
A count of all categories which this item is a member.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[orderPremiumCount]: #orderpremiumcount
#### [orderPremiumCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[packageCount]: #packagecount
#### [packageCount]
A count of a price's packages under which this item is sold.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[packageReferenceCount]: #packagereferencecount
#### [packageReferenceCount]
A count of cross reference for packages   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[presetConfigurationCount]: #presetconfigurationcount
#### [presetConfigurationCount]
A count of a list of preset configurations this price is used in.'   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


