---
title: "SoftLayer_Billing_Invoice_Item"
description: "Every invoice item is defined in the SoftLayer_Billing_Invoice_Item service. Softlayer billing invoice items have detail... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice_Item"
---
# SoftLayer_Billing_Invoice_Item
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Billing_Invoice_Item' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item' >Datatype</a></li>
    </ul>
</div>

## Description
Every invoice item is defined in the SoftLayer_Billing_Invoice_Item service. Softlayer billing invoice items have details about the items that reside within an invoice. These items detail, for instance, the recurring and one time charges for each item billed. 



        
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

#### [getAssociatedChildren](/reference/services/SoftLayer_Billing_Invoice_Item/getAssociatedChildren)
Retrieve an Invoice Item's associated child invoice items. Only parent invoice items have associated children. For instance, a server invoice item may have associated children.

#### [getAssociatedInvoiceItem](/reference/services/SoftLayer_Billing_Invoice_Item/getAssociatedInvoiceItem)
Retrieve an Invoice Item's associated invoice item. If this is populated, it means this is an orphaned invoice item, but logically belongs to the associated invoice item.

#### [getBillingItem](/reference/services/SoftLayer_Billing_Invoice_Item/getBillingItem)
Retrieve an Invoice Item's billing item, from which this item was generated.

#### [getCategory](/reference/services/SoftLayer_Billing_Invoice_Item/getCategory)
Retrieve this invoice item's "item category". 

#### [getChildren](/reference/services/SoftLayer_Billing_Invoice_Item/getChildren)
Retrieve an Invoice Item's child invoice items. Only parent invoice items have children. For instance, a server invoice item will have children.

#### [getFilteredAssociatedChildren](/reference/services/SoftLayer_Billing_Invoice_Item/getFilteredAssociatedChildren)
Retrieve an Invoice Item's associated child invoice items, excluding some items with a $0.00 recurring fee. Only parent invoice items have associated children. For instance, a server invoice item may have associated children.

#### [getHourlyFlag](/reference/services/SoftLayer_Billing_Invoice_Item/getHourlyFlag)
Retrieve indicating whether this invoice item is billed on an hourly basis.

#### [getInvoice](/reference/services/SoftLayer_Billing_Invoice_Item/getInvoice)
Retrieve the invoice to which this item belongs.

#### [getLocation](/reference/services/SoftLayer_Billing_Invoice_Item/getLocation)
Retrieve an invoice item's location, if one exists.'

#### [getNonZeroAssociatedChildren](/reference/services/SoftLayer_Billing_Invoice_Item/getNonZeroAssociatedChildren)
Retrieve an Invoice Item's associated child invoice items, excluding ALL items with a $0.00 recurring fee. Only parent invoice items have associated children. For instance, a server invoice item may have associated children.

#### [getObject](/reference/services/SoftLayer_Billing_Invoice_Item/getObject)
Retrieve a SoftLayer_Billing_Invoice_Item record.

#### [getParent](/reference/services/SoftLayer_Billing_Invoice_Item/getParent)
Retrieve every item tied to a server should have a parent invoice item which is the server line item. This is how we associate items to a server.

#### [getProduct](/reference/services/SoftLayer_Billing_Invoice_Item/getProduct)
Retrieve the entry in the product catalog that a invoice item is based upon.

#### [getTopLevelProductGroupName](/reference/services/SoftLayer_Billing_Invoice_Item/getTopLevelProductGroupName)
Retrieve a string representing the name of parent level product group of an invoice item.

#### [getTotalOneTimeAmount](/reference/services/SoftLayer_Billing_Invoice_Item/getTotalOneTimeAmount)
Retrieve an invoice Item's total, including any child invoice items if they exist.

#### [getTotalOneTimeTaxAmount](/reference/services/SoftLayer_Billing_Invoice_Item/getTotalOneTimeTaxAmount)
Retrieve an invoice Item's total, including any child invoice items if they exist.

#### [getTotalRecurringAmount](/reference/services/SoftLayer_Billing_Invoice_Item/getTotalRecurringAmount)
Retrieve an invoice Item's total, including any child invoice items if they exist.

#### [getTotalRecurringTaxAmount](/reference/services/SoftLayer_Billing_Invoice_Item/getTotalRecurringTaxAmount)
Retrieve a Billing Item's total, including any child billing items if they exist.'

#### [getUsageChargeFlag](/reference/services/SoftLayer_Billing_Invoice_Item/getUsageChargeFlag)
Retrieve indicating whether this invoice item is for the usage charge.

</div>

