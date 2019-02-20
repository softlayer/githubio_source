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


* [SoftLayer_Product_Item_Category](/reference/services/SoftLayer_Product_Item_Category )




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
                <a href="#currentPriceFlag" name=currentPriceFlag>currentPriceFlag</a>
            </span>
            <div class='views-field-body'>This flag is used by the [[SoftLayer_Hardware::getUpgradeItems|getUpgradeItems]] method to indicate if a product price is used for the current billing item.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hourlyRecurringFee" name=hourlyRecurringFee>hourlyRecurringFee</a>
            </span>
            <div class='views-field-body'>The hourly price for this item, should this item be part of an hourly pricing package.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The unique identifier of a Product Item Price. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemId" name=itemId>itemId</a>
            </span>
            <div class='views-field-body'>The unique identifier for a product Item </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#laborFee" name=laborFee>laborFee</a>
            </span>
            <div class='views-field-body'>The labor fee for a product item price. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#locationGroupId" name=locationGroupId>locationGroupId</a>
            </span>
            <div class='views-field-body'>The id of the [[SoftLayer_Location_Group_Pricing]] that this price is part of. If set to null, the price is considered a standard price, which can be used with any location when ordering. 

During order [[SoftLayer_Product_Order/verifyOrder|verification]] and [[SoftLayer_Product_Order/placeOrder|placement]], if a standard price is used, that price may be replaced with a location based price, which does not have this property set to null. The location based price must be part of a [[SoftLayer_Location_Group_Pricing]] that has the location being ordered in order for this to happen.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#onSaleFlag" name=onSaleFlag>onSaleFlag</a>
            </span>
            <div class='views-field-body'>On sale flag. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#oneTimeFee" name=oneTimeFee>oneTimeFee</a>
            </span>
            <div class='views-field-body'>The one time fee for a product item price. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#oneTimeFeeTax" name=oneTimeFeeTax>oneTimeFeeTax</a>
            </span>
            <div class='views-field-body'>A price's total tax amount of the one time fees (oneTimeFee, laborFee, and setupFee). This is only populated after the order is verified via SoftLayer_Product_Order::verifyOrder() </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#orderOptions" name=orderOptions>orderOptions</a>
            </span>
            <div class='views-field-body'>Order options for the category that this price is associated with.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Category_Order_Option_Type'>SoftLayer_Product_Item_Category_Order_Option_Type[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#proratedRecurringFee" name=proratedRecurringFee>proratedRecurringFee</a>
            </span>
            <div class='views-field-body'>A recurring fee is a fee that happens every billing period. This fee is represented as a floating point decimal in US dollars ($USD). </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#proratedRecurringFeeTax" name=proratedRecurringFeeTax>proratedRecurringFeeTax</a>
            </span>
            <div class='views-field-body'>A price's tax amount of the recurring fee. This is only populated after the order is verified via SoftLayer_Product_Order::verifyOrder() </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#quantity" name=quantity>quantity</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#recurringFee" name=recurringFee>recurringFee</a>
            </span>
            <div class='views-field-body'>A recurring fee is a fee that happens every billing period. This fee is represented as a floating point decimal in US dollars ($USD). </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#recurringFeeTax" name=recurringFeeTax>recurringFeeTax</a>
            </span>
            <div class='views-field-body'>A price's tax amount of the recurring fee. This is only populated after the order is verified via SoftLayer_Product_Order::verifyOrder() </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#setupFee" name=setupFee>setupFee</a>
            </span>
            <div class='views-field-body'>The setup fee associated with a product item price. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#sort" name=sort>sort</a>
            </span>
            <div class='views-field-body'>Used for ordering items on sales orders. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#tierMinimumThreshold" name=tierMinimumThreshold>tierMinimumThreshold</a>
            </span>
            <div class='views-field-body'>The minimum threshold for which this tiered usage price begins to apply.  The unit for the price is defined by the item to which this belongs, see [[SoftLayer_Product_Item::$units]].  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#usageRate" name=usageRate>usageRate</a>
            </span>
            <div class='views-field-body'>The rate for a usage based item </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#accountRestrictions" name=accountRestrictions>accountRestrictions</a>
            </span>
            <div class='views-field-body'>The account that the item price is restricted to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Price_Account_Restriction'>SoftLayer_Product_Item_Price_Account_Restriction[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#attributes" name=attributes>attributes</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Price_Attribute'>SoftLayer_Product_Item_Price_Attribute[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#bareMetalReservedCapacityFlag" name=bareMetalReservedCapacityFlag>bareMetalReservedCapacityFlag</a>
            </span>
            <div class='views-field-body'>Signifies pricing that is only available on a bare metal reserved capacity order. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#bigDataOsJournalDiskFlag" name=bigDataOsJournalDiskFlag>bigDataOsJournalDiskFlag</a>
            </span>
            <div class='views-field-body'>Whether the price is for Big Data OS/Journal disks only. (Deprecated) </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#bundleReferences" name=bundleReferences>bundleReferences</a>
            </span>
            <div class='views-field-body'>cross reference for bundles </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Bundles'>SoftLayer_Product_Item_Bundles[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#capacityRestrictionMaximum" name=capacityRestrictionMaximum>capacityRestrictionMaximum</a>
            </span>
            <div class='views-field-body'>The maximum capacity value for which this price is suitable. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#capacityRestrictionMinimum" name=capacityRestrictionMinimum>capacityRestrictionMinimum</a>
            </span>
            <div class='views-field-body'>The minimum capacity value for which this price is suitable. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#capacityRestrictionType" name=capacityRestrictionType>capacityRestrictionType</a>
            </span>
            <div class='views-field-body'>The type of capacity restriction by which this price must abide. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#categories" name=categories>categories</a>
            </span>
            <div class='views-field-body'>All categories which this item is a member. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#dedicatedHostInstanceFlag" name=dedicatedHostInstanceFlag>dedicatedHostInstanceFlag</a>
            </span>
            <div class='views-field-body'>Signifies pricing that is only available on a dedicated host virtual server order. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#definedSoftwareLicenseFlag" name=definedSoftwareLicenseFlag>definedSoftwareLicenseFlag</a>
            </span>
            <div class='views-field-body'>Whether this price defines a software license for its product item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#eligibilityStrategy" name=eligibilityStrategy>eligibilityStrategy</a>
            </span>
            <div class='views-field-body'>Eligibility strategy to assess if a customer can order using this price. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#item" name=item>item</a>
            </span>
            <div class='views-field-body'>The product item a price is tied to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#orderPremiums" name=orderPremiums>orderPremiums</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Price_Premium'>SoftLayer_Product_Item_Price_Premium[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#packageReferences" name=packageReferences>packageReferences</a>
            </span>
            <div class='views-field-body'>cross reference for packages </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Package_Item_Prices'>SoftLayer_Product_Package_Item_Prices[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#packages" name=packages>packages</a>
            </span>
            <div class='views-field-body'>A price's packages under which this item is sold. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#presetConfigurations" name=presetConfigurations>presetConfigurations</a>
            </span>
            <div class='views-field-body'>A list of preset configurations this price is used in.' </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Package_Preset_Configuration'>SoftLayer_Product_Package_Preset_Configuration[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#priceType" name=priceType>priceType</a>
            </span>
            <div class='views-field-body'>The type keyname of this price which can be STANDARD or TIERED. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#pricingLocationGroup" name=pricingLocationGroup>pricingLocationGroup</a>
            </span>
            <div class='views-field-body'>The pricing location group that this price is applicable for. Prices that have a pricing location group will only be available for ordering with the locations specified on the location group. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Location_Group_Pricing'>SoftLayer_Location_Group_Pricing </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#requiredCoreCount" name=requiredCoreCount>requiredCoreCount</a>
            </span>
            <div class='views-field-body'>The number of server cores required to order this item. This is deprecated. Use [[SoftLayer_Product_Item_Price/getCapacityRestrictionMinimum|getCapacityRestrictionMinimum]] and [[SoftLayer_Product_Item_Price/getCapacityRestrictionMaximum|getCapacityRestrictionMaximum]] </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#reservedCapacityInstanceFlag" name=reservedCapacityInstanceFlag>reservedCapacityInstanceFlag</a>
            </span>
            <div class='views-field-body'>Signifies pricing that is only available on a reserved capacity virtual server order. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#accountRestrictionCount" name=accountRestrictionCount>accountRestrictionCount</a>
            </span>
            <div class='views-field-body'>A count of the account that the item price is restricted to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#attributeCount" name=attributeCount>attributeCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#bundleReferenceCount" name=bundleReferenceCount>bundleReferenceCount</a>
            </span>
            <div class='views-field-body'>A count of cross reference for bundles </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#categoryCount" name=categoryCount>categoryCount</a>
            </span>
            <div class='views-field-body'>A count of all categories which this item is a member. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#orderPremiumCount" name=orderPremiumCount>orderPremiumCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#packageCount" name=packageCount>packageCount</a>
            </span>
            <div class='views-field-body'>A count of a price's packages under which this item is sold. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#packageReferenceCount" name=packageReferenceCount>packageReferenceCount</a>
            </span>
            <div class='views-field-body'>A count of cross reference for packages </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#presetConfigurationCount" name=presetConfigurationCount>presetConfigurationCount</a>
            </span>
            <div class='views-field-body'>A count of a list of preset configurations this price is used in.' </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


