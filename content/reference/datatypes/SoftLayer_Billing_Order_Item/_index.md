---
title: "SoftLayer_Billing_Order_Item"
description: "Every individual item that a SoftLayer customer is billed for is recorded in the SoftLayer_Billing_Item data type. Billi... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Item"
---

# SoftLayer_Billing_Order_Item
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Billing_Order_Item' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Order_Item' >Datatype</a></li>
    </ul>
</div>

## Description 
Every individual item that a SoftLayer customer is billed for is recorded in the SoftLayer_Billing_Item data type. Billing items range from server chassis to hard drives to control panels, bandwidth quota upgrades and port upgrade charges. Softlayer [[SoftLayer_Billing_Invoice|invoices]] are generated from the cost of a customer's billing items. Billing items are copied from the product catalog as they're ordered by customers to create a reference between an account and the billable items they own. 

Billing items exist in a tree relationship. Items are associated with each other by parent/child relationships. Component items such as CPU's, RAM, and software each have a parent billing item for the server chassis they're associated with. Billing Items with a null parent item do not have an associated parent item. 


### associatedMethods

*  [SoftLayer_Network_Storage::getBillingItem](/reference/services/SoftLayer_Network_Storage/getBillingItem )
*  [SoftLayer_Network_LoadBalancer_VirtualIpAddress::getBillingItem](/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/getBillingItem )



### seeAlso

* [SoftLayer_Billing_Item_Hardware](/reference/datatypes/SoftLayer_Billing_Item_Hardware )


* [SoftLayer_Billing_Invoice](/reference/services/SoftLayer_Billing_Invoice )




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
                <a href="#categoryCode" name=categoryCode>categoryCode</a>
            </span>
            <div class='views-field-body'>The category code for the order item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#description" name=description>description</a>
            </span>
            <div class='views-field-body'>friendly description of purchase item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#domainName" name=domainName>domainName</a>
            </span>
            <div class='views-field-body'>The domain name of the server as designated by the purchaser at the time of order placement. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hostName" name=hostName>hostName</a>
            </span>
            <div class='views-field-body'>The hostname of the server as designated by the purchaser at the time of order placement. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hourlyRecurringFee" name=hourlyRecurringFee>hourlyRecurringFee</a>
            </span>
            <div class='views-field-body'>The amount of money charged per hourly for an order item, if applicable, and only if it was ordered this day. hourlyRecurringFee is measured in US Dollars ($USD).  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemId" name=itemId>itemId</a>
            </span>
            <div class='views-field-body'>The SoftLayer_Product_Item ID for this order item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemPriceId" name=itemPriceId>itemPriceId</a>
            </span>
            <div class='views-field-body'>the item price id (SoftLayer_Product_Item_Price->id) of the ordered item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#laborAfterTaxAmount" name=laborAfterTaxAmount>laborAfterTaxAmount</a>
            </span>
            <div class='views-field-body'>An order item's labor fee total after taxes. This does not include any child invoice items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#laborFee" name=laborFee>laborFee</a>
            </span>
            <div class='views-field-body'>The labor fee, if any. This is a one time charge. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#laborFeeTaxRate" name=laborFeeTaxRate>laborFeeTaxRate</a>
            </span>
            <div class='views-field-body'>The rate at which labor fees are taxed if you are a taxable customer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#laborTaxAmount" name=laborTaxAmount>laborTaxAmount</a>
            </span>
            <div class='views-field-body'>An order item's labor tax amount. This does not include any child invoice items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#oneTimeAfterTaxAmount" name=oneTimeAfterTaxAmount>oneTimeAfterTaxAmount</a>
            </span>
            <div class='views-field-body'>An order item's one-time fee total after taxes. This does not include any child invoice items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#oneTimeFee" name=oneTimeFee>oneTimeFee</a>
            </span>
            <div class='views-field-body'>The amount of money charged as a one-time charge for an order item, if applicable. oneTimeFee is measured in US Dollars ($USD).  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#oneTimeFeeTaxRate" name=oneTimeFeeTaxRate>oneTimeFeeTaxRate</a>
            </span>
            <div class='views-field-body'>The rate at which one time fees are taxed if you are a taxable customer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#oneTimeTaxAmount" name=oneTimeTaxAmount>oneTimeTaxAmount</a>
            </span>
            <div class='views-field-body'>An order item's one-time tax amount. This does not include any child invoice items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#parentId" name=parentId>parentId</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#presetId" name=presetId>presetId</a>
            </span>
            <div class='views-field-body'>The id for the preset configuration ordered. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#promoCodeId" name=promoCodeId>promoCodeId</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#quantity" name=quantity>quantity</a>
            </span>
            <div class='views-field-body'>the quantity of the ordered item in a quote. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#recurringAfterTaxAmount" name=recurringAfterTaxAmount>recurringAfterTaxAmount</a>
            </span>
            <div class='views-field-body'>An order item's recurring fee total after taxes. This does not include any child invoice items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#recurringFee" name=recurringFee>recurringFee</a>
            </span>
            <div class='views-field-body'>The amount of money charged per month for an order item, if applicable. recurringFee is measured in US Dollars ($USD).  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#recurringTaxAmount" name=recurringTaxAmount>recurringTaxAmount</a>
            </span>
            <div class='views-field-body'>An order item's recurring tax amount. This does not include any child invoice items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#setupAfterTaxAmount" name=setupAfterTaxAmount>setupAfterTaxAmount</a>
            </span>
            <div class='views-field-body'>An order item's setup fee total after taxes. This does not include any child invoice items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#setupFee" name=setupFee>setupFee</a>
            </span>
            <div class='views-field-body'>The setup fee, if any. This is a one time charge. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#setupFeeDeferralMonths" name=setupFeeDeferralMonths>setupFeeDeferralMonths</a>
            </span>
            <div class='views-field-body'>The month set up fee deferral. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#setupFeeTaxRate" name=setupFeeTaxRate>setupFeeTaxRate</a>
            </span>
            <div class='views-field-body'>The rate at which setup fees are taxed if you are a taxable customer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#setupTaxAmount" name=setupTaxAmount>setupTaxAmount</a>
            </span>
            <div class='views-field-body'>An order item's setup tax amount. This does not include any child invoice items. </div>
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
                <a href="#billingItem" name=billingItem>billingItem</a>
            </span>
            <div class='views-field-body'>The SoftLayer_Billing_Item tied to the order item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#bundledItems" name=bundledItems>bundledItems</a>
            </span>
            <div class='views-field-body'>The other items included with an ordered item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#category" name=category>category</a>
            </span>
            <div class='views-field-body'>The item category tied to an order item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#children" name=children>children</a>
            </span>
            <div class='views-field-body'>The child order items for an order item. All server order items should have children. These children are considered a part of the server. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#globalIdentifier" name=globalIdentifier>globalIdentifier</a>
            </span>
            <div class='views-field-body'>A hardware's universally unique identifier. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardwareGenericComponent" name=hardwareGenericComponent>hardwareGenericComponent</a>
            </span>
            <div class='views-field-body'>The component type tied to an order item. All hardware-specific items should have a generic hardware component. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Generic'>SoftLayer_Hardware_Component_Model_Generic </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#item" name=item>item</a>
            </span>
            <div class='views-field-body'>The SoftLayer_Product_Item tied to an order item. The item is the actual definition of the product being sold. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemCategoryAnswers" name=itemCategoryAnswers>itemCategoryAnswers</a>
            </span>
            <div class='views-field-body'>This is an item's category answers. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Order_Item_Category_Answer'>SoftLayer_Billing_Order_Item_Category_Answer[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemPrice" name=itemPrice>itemPrice</a>
            </span>
            <div class='views-field-body'>The SoftLayer_Product_Item_Price tied to an order item. The item price object describes the cost of an item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#location" name=location>location</a>
            </span>
            <div class='views-field-body'>The location of an ordered item. This is usually the same as the server it is being ordered with. Otherwise it describes the location of the additional service being ordered. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#nextOrderChildren" name=nextOrderChildren>nextOrderChildren</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#oldBillingItem" name=oldBillingItem>oldBillingItem</a>
            </span>
            <div class='views-field-body'>This is only populated when an upgrade order is placed. The old billing item represents what the billing was before the upgrade happened. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#order" name=order>order</a>
            </span>
            <div class='views-field-body'>The order to which this item belongs. The order contains all the information related to the items included in an order </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#orderApprovalDate" name=orderApprovalDate>orderApprovalDate</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#package" name=package>package</a>
            </span>
            <div class='views-field-body'>The SoftLayer_Product_Package an order item is a part of. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#parent" name=parent>parent</a>
            </span>
            <div class='views-field-body'>The parent order item ID for an item. Items that are associated with a server will have a parent. The parent will be the server item itself. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#preset" name=preset>preset</a>
            </span>
            <div class='views-field-body'>The SoftLayer_Product_Package_Preset related to this order item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Package_Preset'>SoftLayer_Product_Package_Preset </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#promoCode" name=promoCode>promoCode</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Promotion'>SoftLayer_Product_Promotion </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#redundantPowerSupplyCount" name=redundantPowerSupplyCount>redundantPowerSupplyCount</a>
            </span>
            <div class='views-field-body'>A count of power supplies contained within this SoftLayer_Billing_Order </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsigned integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#softwareDescription" name=softwareDescription>softwareDescription</a>
            </span>
            <div class='views-field-body'>For ordered items that are software items, a full description of that software can be found with this property.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#storageGroups" name=storageGroups>storageGroups</a>
            </span>
            <div class='views-field-body'>The drive storage groups that are attached to this billing order item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group_Order'>SoftLayer_Configuration_Storage_Group_Order[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#totalRecurringAmount" name=totalRecurringAmount>totalRecurringAmount</a>
            </span>
            <div class='views-field-body'>The recurring fee of an ordered item. This amount represents the fees that will be charged on a recurring (usually monthly) basis. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#upgradeItem" name=upgradeItem>upgradeItem</a>
            </span>
            <div class='views-field-body'>The next SoftLayer_Product_Item in the upgrade path for this order item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#bundledItemCount" name=bundledItemCount>bundledItemCount</a>
            </span>
            <div class='views-field-body'>A count of the other items included with an ordered item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#childrenCount" name=childrenCount>childrenCount</a>
            </span>
            <div class='views-field-body'>A count of the child order items for an order item. All server order items should have children. These children are considered a part of the server. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemCategoryAnswerCount" name=itemCategoryAnswerCount>itemCategoryAnswerCount</a>
            </span>
            <div class='views-field-body'>A count of this is an item's category answers. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#nextOrderChildrenCount" name=nextOrderChildrenCount>nextOrderChildrenCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#storageGroupCount" name=storageGroupCount>storageGroupCount</a>
            </span>
            <div class='views-field-body'>A count of the drive storage groups that are attached to this billing order item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


