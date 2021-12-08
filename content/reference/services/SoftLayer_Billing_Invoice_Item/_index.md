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
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [getAssociatedChildren](/reference/services/SoftLayer_Billing_Invoice_Item/getAssociatedChildren)
Retrieve an Invoice Item's associated child invoice items. Only parent invoice items have associated children. For instance, a server invoice item may have associated children.

</div>

<div class="method-row">

#### [getAssociatedInvoiceItem](/reference/services/SoftLayer_Billing_Invoice_Item/getAssociatedInvoiceItem)
Retrieve an Invoice Item's associated invoice item. If this is populated, it means this is an orphaned invoice item, but logically belongs to the associated invoice item.

</div>

<div class="method-row">

#### [getBillingItem](/reference/services/SoftLayer_Billing_Invoice_Item/getBillingItem)
Retrieve an Invoice Item's billing item, from which this item was generated.

</div>

<div class="method-row">

#### [getCategory](/reference/services/SoftLayer_Billing_Invoice_Item/getCategory)
Retrieve this invoice item's "item category". 

</div>

<div class="method-row">

#### [getChildren](/reference/services/SoftLayer_Billing_Invoice_Item/getChildren)
Retrieve an Invoice Item's child invoice items. Only parent invoice items have children. For instance, a server invoice item will have children.

</div>

<div class="method-row">

#### [getFilteredAssociatedChildren](/reference/services/SoftLayer_Billing_Invoice_Item/getFilteredAssociatedChildren)
Retrieve an Invoice Item's associated child invoice items, excluding some items with a $0.00 recurring fee. Only parent invoice items have associated children. For instance, a server invoice item may have associated children.

</div>

<div class="method-row">

#### [getHourlyFlag](/reference/services/SoftLayer_Billing_Invoice_Item/getHourlyFlag)
Retrieve indicating whether this invoice item is billed on an hourly basis.

</div>

<div class="method-row">

#### [getInvoice](/reference/services/SoftLayer_Billing_Invoice_Item/getInvoice)
Retrieve the invoice to which this item belongs.

</div>

<div class="method-row">

#### [getLocation](/reference/services/SoftLayer_Billing_Invoice_Item/getLocation)
Retrieve an invoice item's location, if one exists.'

</div>

<div class="method-row">

#### [getNonZeroAssociatedChildren](/reference/services/SoftLayer_Billing_Invoice_Item/getNonZeroAssociatedChildren)
Retrieve an Invoice Item's associated child invoice items, excluding ALL items with a $0.00 recurring fee. Only parent invoice items have associated children. For instance, a server invoice item may have associated children.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Billing_Invoice_Item/getObject)
Retrieve a SoftLayer_Billing_Invoice_Item record.

</div>

<div class="method-row">

#### [getParent](/reference/services/SoftLayer_Billing_Invoice_Item/getParent)
Retrieve every item tied to a server should have a parent invoice item which is the server line item. This is how we associate items to a server.

</div>

<div class="method-row">

#### [getProduct](/reference/services/SoftLayer_Billing_Invoice_Item/getProduct)
Retrieve the entry in the product catalog that a invoice item is based upon.

</div>

<div class="method-row">

#### [getTopLevelProductGroupName](/reference/services/SoftLayer_Billing_Invoice_Item/getTopLevelProductGroupName)
Retrieve a string representing the name of parent level product group of an invoice item.

</div>

<div class="method-row">

#### [getTotalOneTimeAmount](/reference/services/SoftLayer_Billing_Invoice_Item/getTotalOneTimeAmount)
Retrieve an invoice Item's total, including any child invoice items if they exist.

</div>

<div class="method-row">

#### [getTotalOneTimeTaxAmount](/reference/services/SoftLayer_Billing_Invoice_Item/getTotalOneTimeTaxAmount)
Retrieve an invoice Item's total, including any child invoice items if they exist.

</div>

<div class="method-row">

#### [getTotalRecurringAmount](/reference/services/SoftLayer_Billing_Invoice_Item/getTotalRecurringAmount)
Retrieve an invoice Item's total, including any child invoice items if they exist.

</div>

<div class="method-row">

#### [getTotalRecurringTaxAmount](/reference/services/SoftLayer_Billing_Invoice_Item/getTotalRecurringTaxAmount)
Retrieve a Billing Item's total, including any child billing items if they exist.'

</div>

<div class="method-row">

#### [getUsageChargeFlag](/reference/services/SoftLayer_Billing_Invoice_Item/getUsageChargeFlag)
Retrieve indicating whether this invoice item is for the usage charge.

</div>
</div>

</div>

