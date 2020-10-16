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
Every individual item that a SoftLayer customer is billed for is recorded in the SoftLayer_Billing_Item data type. Billing items range from server chassis to hard drives to control panels, bandwidth quota upgrades and port upgrade charges. Softlayer [SoftLayer_Billing_Invoice]({{<ref "reference/datatypes/SoftLayer_Billing_Invoice">}}) are generated from the cost of a customer's billing items. Billing items are copied from the product catalog as they're ordered by customers to create a reference between an account and the billable items they own. 

Billing items exist in a tree relationship. Items are associated with each other by parent/child relationships. Component items such as CPU's, RAM, and software each have a parent billing item for the server chassis they're associated with. Billing Items with a null parent item do not have an associated parent item. 


### associatedMethods

*  [SoftLayer_Network_Storage::getBillingItem](/reference/services/SoftLayer_Network_Storage/getBillingItem )
*  [SoftLayer_Network_LoadBalancer_VirtualIpAddress::getBillingItem](/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress/getBillingItem )



### seeAlso

* [SoftLayer_Billing_Item_Hardware](/reference/datatypes/SoftLayer_Billing_Item_Hardware )


* [SoftLayer_Billing_Invoice](/reference/datatypes/SoftLayer_Billing_Invoice )




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
[categoryCode]: #categorycode
#### [categoryCode]
The category code for the order item.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
friendly description of purchase item.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[domainName]: #domainname
#### [domainName]
The domain name of the server as designated by the purchaser at the time of order placement.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[hostName]: #hostname
#### [hostName]
The hostname of the server as designated by the purchaser at the time of order placement.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[hourlyRecurringFee]: #hourlyrecurringfee
#### [hourlyRecurringFee]
The amount of money charged per hourly for an order item, if applicable, and only if it was ordered this day. hourlyRecurringFee is measured in US Dollars ($USD).   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[itemId]: #itemid
#### [itemId]
The SoftLayer_Product_Item ID for this order item.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[itemPriceId]: #itempriceid
#### [itemPriceId]
the item price id (SoftLayer_Product_Item_Price->id) of the ordered item.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[laborAfterTaxAmount]: #laboraftertaxamount
#### [laborAfterTaxAmount]
An order item's labor fee total after taxes. This does not include any child invoice items.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[laborFee]: #laborfee
#### [laborFee]
The labor fee, if any. This is a one time charge.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[laborFeeTaxRate]: #laborfeetaxrate
#### [laborFeeTaxRate]
The rate at which labor fees are taxed if you are a taxable customer.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[laborTaxAmount]: #labortaxamount
#### [laborTaxAmount]
An order item's labor tax amount. This does not include any child invoice items.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[oneTimeAfterTaxAmount]: #onetimeaftertaxamount
#### [oneTimeAfterTaxAmount]
An order item's one-time fee total after taxes. This does not include any child invoice items.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[oneTimeFee]: #onetimefee
#### [oneTimeFee]
The amount of money charged as a one-time charge for an order item, if applicable. oneTimeFee is measured in US Dollars ($USD).   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[oneTimeFeeTaxRate]: #onetimefeetaxrate
#### [oneTimeFeeTaxRate]
The rate at which one time fees are taxed if you are a taxable customer.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[oneTimeTaxAmount]: #onetimetaxamount
#### [oneTimeTaxAmount]
An order item's one-time tax amount. This does not include any child invoice items.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[parentId]: #parentid
#### [parentId]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[presetId]: #presetid
#### [presetId]
The id for the preset configuration ordered.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[promoCodeId]: #promocodeid
#### [promoCodeId]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[quantity]: #quantity
#### [quantity]
the quantity of the ordered item in a quote.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[recurringAfterTaxAmount]: #recurringaftertaxamount
#### [recurringAfterTaxAmount]
An order item's recurring fee total after taxes. This does not include any child invoice items.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[recurringFee]: #recurringfee
#### [recurringFee]
The amount of money charged per month for an order item, if applicable. recurringFee is measured in US Dollars ($USD).   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[recurringTaxAmount]: #recurringtaxamount
#### [recurringTaxAmount]
An order item's recurring tax amount. This does not include any child invoice items.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[setupAfterTaxAmount]: #setupaftertaxamount
#### [setupAfterTaxAmount]
An order item's setup fee total after taxes. This does not include any child invoice items.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[setupFee]: #setupfee
#### [setupFee]
The setup fee, if any. This is a one time charge.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[setupFeeDeferralMonths]: #setupfeedeferralmonths
#### [setupFeeDeferralMonths]
The month set up fee deferral.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[setupFeeTaxRate]: #setupfeetaxrate
#### [setupFeeTaxRate]
The rate at which setup fees are taxed if you are a taxable customer.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[setupTaxAmount]: #setuptaxamount
#### [setupTaxAmount]
An order item's setup tax amount. This does not include any child invoice items.  
<span class="type-label">Type: </span>**decimal**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The SoftLayer_Billing_Item tied to the order item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>
<div class="prop-row">

-----
[bundledItems]: #bundleditems
#### [bundledItems]
The other items included with an ordered item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item[] </a>**


</div>
<div class="prop-row">

-----
[category]: #category
#### [category]
The item category tied to an order item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a>**


</div>
<div class="prop-row">

-----
[children]: #children
#### [children]
The child order items for an order item. All server order items should have children. These children are considered a part of the server.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item[] </a>**


</div>
<div class="prop-row">

-----
[globalIdentifier]: #globalidentifier
#### [globalIdentifier]
A hardware's universally unique identifier.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[hardwareGenericComponent]: #hardwaregenericcomponent
#### [hardwareGenericComponent]
The component type tied to an order item. All hardware-specific items should have a generic hardware component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Generic'>SoftLayer_Hardware_Component_Model_Generic </a>**


</div>
<div class="prop-row">

-----
[item]: #item
#### [item]
The SoftLayer_Product_Item tied to an order item. The item is the actual definition of the product being sold.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**


</div>
<div class="prop-row">

-----
[itemCategoryAnswers]: #itemcategoryanswers
#### [itemCategoryAnswers]
This is an item's category answers.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Item_Category_Answer'>SoftLayer_Billing_Order_Item_Category_Answer[] </a>**


</div>
<div class="prop-row">

-----
[itemPrice]: #itemprice
#### [itemPrice]
The SoftLayer_Product_Item_Price tied to an order item. The item price object describes the cost of an item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price </a>**


</div>
<div class="prop-row">

-----
[location]: #location
#### [location]
The location of an ordered item. This is usually the same as the server it is being ordered with. Otherwise it describes the location of the additional service being ordered.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[nextOrderChildren]: #nextorderchildren
#### [nextOrderChildren]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item[] </a>**


</div>
<div class="prop-row">

-----
[oldBillingItem]: #oldbillingitem
#### [oldBillingItem]
This is only populated when an upgrade order is placed. The old billing item represents what the billing was before the upgrade happened.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>
<div class="prop-row">

-----
[order]: #order
#### [order]
The order to which this item belongs. The order contains all the information related to the items included in an order  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order </a>**


</div>
<div class="prop-row">

-----
[orderApprovalDate]: #orderapprovaldate
#### [orderApprovalDate]
  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[package]: #package
#### [package]
The SoftLayer_Product_Package an order item is a part of.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a>**


</div>
<div class="prop-row">

-----
[parent]: #parent
#### [parent]
The parent order item ID for an item. Items that are associated with a server will have a parent. The parent will be the server item itself.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item </a>**


</div>
<div class="prop-row">

-----
[preset]: #preset
#### [preset]
The SoftLayer_Product_Package_Preset related to this order item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Preset'>SoftLayer_Product_Package_Preset </a>**


</div>
<div class="prop-row">

-----
[promoCode]: #promocode
#### [promoCode]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Promotion'>SoftLayer_Product_Promotion </a>**


</div>
<div class="prop-row">

-----
[redundantPowerSupplyCount]: #redundantpowersupplycount
#### [redundantPowerSupplyCount]
A count of power supplies contained within this SoftLayer_Billing_Order  
<span class="type-label">Type: </span>**unsigned integer**


</div>
<div class="prop-row">

-----
[softwareDescription]: #softwaredescription
#### [softwareDescription]
For ordered items that are software items, a full description of that software can be found with this property.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a>**


</div>
<div class="prop-row">

-----
[storageGroups]: #storagegroups
#### [storageGroups]
The drive storage groups that are attached to this billing order item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group_Order'>SoftLayer_Configuration_Storage_Group_Order[] </a>**


</div>
<div class="prop-row">

-----
[totalRecurringAmount]: #totalrecurringamount
#### [totalRecurringAmount]
The recurring fee of an ordered item. This amount represents the fees that will be charged on a recurring (usually monthly) basis.  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[upgradeItem]: #upgradeitem
#### [upgradeItem]
The next SoftLayer_Product_Item in the upgrade path for this order item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**


</div>

## Count
<div class="prop-row">

-----
[bundledItemCount]: #bundleditemcount
#### [bundledItemCount]
A count of the other items included with an ordered item.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[childrenCount]: #childrencount
#### [childrenCount]
A count of the child order items for an order item. All server order items should have children. These children are considered a part of the server.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[itemCategoryAnswerCount]: #itemcategoryanswercount
#### [itemCategoryAnswerCount]
A count of this is an item's category answers.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[nextOrderChildrenCount]: #nextorderchildrencount
#### [nextOrderChildrenCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[storageGroupCount]: #storagegroupcount
#### [storageGroupCount]
A count of the drive storage groups that are attached to this billing order item.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


