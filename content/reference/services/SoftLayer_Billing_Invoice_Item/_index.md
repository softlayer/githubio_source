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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getAssociatedChildren'> getAssociatedChildren</a> </span>
            <div class='views-field-body'>Retrieve an Invoice Item's associated child invoice items. Only parent invoice items have associated children. For instance, a server invoice item may have associated children.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getAssociatedInvoiceItem'> getAssociatedInvoiceItem</a> </span>
            <div class='views-field-body'>Retrieve an Invoice Item's associated invoice item. If this is populated, it means this is an orphaned invoice item, but logically belongs to the associated invoice item.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getBillingItem'> getBillingItem</a> </span>
            <div class='views-field-body'>Retrieve an Invoice Item's billing item, from which this item was generated.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getCategory'> getCategory</a> </span>
            <div class='views-field-body'>Retrieve this invoice item's "item category". </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getChildren'> getChildren</a> </span>
            <div class='views-field-body'>Retrieve an Invoice Item's child invoice items. Only parent invoice items have children. For instance, a server invoice item will have children.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getFilteredAssociatedChildren'> getFilteredAssociatedChildren</a> </span>
            <div class='views-field-body'>Retrieve an Invoice Item's associated child invoice items, excluding some items with a $0.00 recurring fee. Only parent invoice items have associated children. For instance, a server invoice item may have associated children.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getHourlyFlag'> getHourlyFlag</a> </span>
            <div class='views-field-body'>Retrieve indicating whether this invoice item is billed on an hourly basis.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getInvoice'> getInvoice</a> </span>
            <div class='views-field-body'>Retrieve the invoice to which this item belongs.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getLocation'> getLocation</a> </span>
            <div class='views-field-body'>Retrieve an invoice item's location, if one exists.'</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getNonZeroAssociatedChildren'> getNonZeroAssociatedChildren</a> </span>
            <div class='views-field-body'>Retrieve an Invoice Item's associated child invoice items, excluding ALL items with a $0.00 recurring fee. Only parent invoice items have associated children. For instance, a server invoice item may have associated children.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Billing_Invoice_Item record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getParent'> getParent</a> </span>
            <div class='views-field-body'>Retrieve every item tied to a server should have a parent invoice item which is the server line item. This is how we associate items to a server.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getProduct'> getProduct</a> </span>
            <div class='views-field-body'>Retrieve the entry in the product catalog that a invoice item is based upon.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getTopLevelProductGroupName'> getTopLevelProductGroupName</a> </span>
            <div class='views-field-body'>Retrieve a string representing the name of parent level product group of an invoice item.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getTotalOneTimeAmount'> getTotalOneTimeAmount</a> </span>
            <div class='views-field-body'>Retrieve an invoice Item's total, including any child invoice items if they exist.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getTotalOneTimeTaxAmount'> getTotalOneTimeTaxAmount</a> </span>
            <div class='views-field-body'>Retrieve an invoice Item's total, including any child invoice items if they exist.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getTotalRecurringAmount'> getTotalRecurringAmount</a> </span>
            <div class='views-field-body'>Retrieve an invoice Item's total, including any child invoice items if they exist.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getTotalRecurringTaxAmount'> getTotalRecurringTaxAmount</a> </span>
            <div class='views-field-body'>Retrieve a Billing Item's total, including any child billing items if they exist.'</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Invoice_Item/getUsageChargeFlag'> getUsageChargeFlag</a> </span>
            <div class='views-field-body'>Retrieve indicating whether this invoice item is for the usage charge.</div>
        </div>
        </div>
</div>

