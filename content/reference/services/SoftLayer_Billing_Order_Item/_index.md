---
title: "SoftLayer_Billing_Order_Item"
description: "The SoftLayer_Billing_Order_Item datatype provides information regarding a single ordered item. When a server order or a... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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
The SoftLayer_Billing_Order_Item datatype provides information regarding a single ordered item. When a server order or any other order is placed, the information about that order is stored as SoftLayer_Billing_Order_items. 

This also provides information about software or hardware related to an ordered item,what package the item is in, and all pricing information related to this ordered item. 



        
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

#### [getBillingItem](/reference/services/SoftLayer_Billing_Order_Item/getBillingItem)
Retrieve the SoftLayer_Billing_Item tied to the order item.

#### [getBundledItems](/reference/services/SoftLayer_Billing_Order_Item/getBundledItems)
Retrieve the other items included with an ordered item.

#### [getCategory](/reference/services/SoftLayer_Billing_Order_Item/getCategory)
Retrieve the item category tied to an order item.

#### [getChildren](/reference/services/SoftLayer_Billing_Order_Item/getChildren)
Retrieve the child order items for an order item. All server order items should have children. These children are considered a part of the server.

#### [getGlobalIdentifier](/reference/services/SoftLayer_Billing_Order_Item/getGlobalIdentifier)
Retrieve a hardware's universally unique identifier.

#### [getHardwareGenericComponent](/reference/services/SoftLayer_Billing_Order_Item/getHardwareGenericComponent)
Retrieve the component type tied to an order item. All hardware-specific items should have a generic hardware component.

#### [getItem](/reference/services/SoftLayer_Billing_Order_Item/getItem)
Retrieve the SoftLayer_Product_Item tied to an order item. The item is the actual definition of the product being sold.

#### [getItemCategoryAnswers](/reference/services/SoftLayer_Billing_Order_Item/getItemCategoryAnswers)
Retrieve this is an item's category answers.

#### [getItemPrice](/reference/services/SoftLayer_Billing_Order_Item/getItemPrice)
Retrieve the SoftLayer_Product_Item_Price tied to an order item. The item price object describes the cost of an item.

#### [getLocation](/reference/services/SoftLayer_Billing_Order_Item/getLocation)
Retrieve the location of an ordered item. This is usually the same as the server it is being ordered with. Otherwise it describes the location of the additional service being ordered.

#### [getNextOrderChildren](/reference/services/SoftLayer_Billing_Order_Item/getNextOrderChildren)


#### [getObject](/reference/services/SoftLayer_Billing_Order_Item/getObject)
Retrieve a SoftLayer_Billing_Order_Item record.

#### [getOldBillingItem](/reference/services/SoftLayer_Billing_Order_Item/getOldBillingItem)
Retrieve this is only populated when an upgrade order is placed. The old billing item represents what the billing was before the upgrade happened.

#### [getOrder](/reference/services/SoftLayer_Billing_Order_Item/getOrder)
Retrieve the order to which this item belongs. The order contains all the information related to the items included in an order

#### [getOrderApprovalDate](/reference/services/SoftLayer_Billing_Order_Item/getOrderApprovalDate)


#### [getPackage](/reference/services/SoftLayer_Billing_Order_Item/getPackage)
Retrieve the SoftLayer_Product_Package an order item is a part of.

#### [getParent](/reference/services/SoftLayer_Billing_Order_Item/getParent)
Retrieve the parent order item ID for an item. Items that are associated with a server will have a parent. The parent will be the server item itself.

#### [getPreset](/reference/services/SoftLayer_Billing_Order_Item/getPreset)
Retrieve the SoftLayer_Product_Package_Preset related to this order item.

#### [getPromoCode](/reference/services/SoftLayer_Billing_Order_Item/getPromoCode)


#### [getRedundantPowerSupplyCount](/reference/services/SoftLayer_Billing_Order_Item/getRedundantPowerSupplyCount)
Retrieve a count of power supplies contained within this SoftLayer_Billing_Order

#### [getSoftwareDescription](/reference/services/SoftLayer_Billing_Order_Item/getSoftwareDescription)
Retrieve for ordered items that are software items, a full description of that software can be found with this property. 

#### [getStorageGroups](/reference/services/SoftLayer_Billing_Order_Item/getStorageGroups)
Retrieve the drive storage groups that are attached to this billing order item.

#### [getTotalRecurringAmount](/reference/services/SoftLayer_Billing_Order_Item/getTotalRecurringAmount)
Retrieve the recurring fee of an ordered item. This amount represents the fees that will be charged on a recurring (usually monthly) basis.

#### [getUpgradeItem](/reference/services/SoftLayer_Billing_Order_Item/getUpgradeItem)
Retrieve the next SoftLayer_Product_Item in the upgrade path for this order item.

</div>

