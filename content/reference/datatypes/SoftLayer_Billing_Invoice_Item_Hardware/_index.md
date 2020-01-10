---
title: "SoftLayer_Billing_Invoice_Item_Hardware"
description: "The SoftLayer_Billing_Invoice_Item_Hardware data type contains a 'resource'. This resource is a link to the hardware tie... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice_Item_Hardware"
---

# SoftLayer_Billing_Invoice_Item_Hardware
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item_Hardware' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Billing_Invoice_Item_Hardware data type contains a "resource". This resource is a link to the hardware tied to a SoftLayer_Billing_item whose category code is "server". 





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
[associatedInvoiceItemId]: #associatedinvoiceitemid
#### [associatedInvoiceItemId]
The associated invoice Item ID.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[billingItemId]: #billingitemid
#### [billingItemId]
The billing item from which this invoice item was generated.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[categoryCode]: #categorycode
#### [categoryCode]
The item category of the invoice item being invoiced.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date the invoice item was created.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
The item description for this invoice item.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[domainName]: #domainname
#### [domainName]
The domain name of the invoiced item. This is only used on invoice items whose category is "server".  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[hostName]: #hostname
#### [hostName]
The Host name of the invoiced item. This is only used on invoice items whose category is "server".  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[hourlyRecurringFee]: #hourlyrecurringfee
#### [hourlyRecurringFee]
The hourly recurring fee of the invoice item represented by a floating point decimal in US Dollars ($USD)  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The ID of the invoice item.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[invoiceId]: #invoiceid
#### [invoiceId]
The invoice to which this invoice item belongs.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[laborAfterTaxAmount]: #laboraftertaxamount
#### [laborAfterTaxAmount]
An invoice item's labor fee total after taxes. This does not include any child invoice items.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[laborFee]: #laborfee
#### [laborFee]
This also a one-time fee of a special type.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[laborFeeTaxRate]: #laborfeetaxrate
#### [laborFeeTaxRate]
The tax rate at which the labor fee is taxed.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[laborTaxAmount]: #labortaxamount
#### [laborTaxAmount]
An invoice item's labor tax amount. This does not include any child invoice items.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
A note to help describe more about the item. This normally holds usernames, or some other bit of extra information.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[oneTimeAfterTaxAmount]: #onetimeaftertaxamount
#### [oneTimeAfterTaxAmount]
An invoice item's one-time fee total after taxes. This does not include any child invoice items.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[oneTimeFee]: #onetimefee
#### [oneTimeFee]
If there are any one-time charges assessed, it will show up here represented by a floating point decimal in US Dollars ($USD)  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[oneTimeFeeTaxRate]: #onetimefeetaxrate
#### [oneTimeFeeTaxRate]
The rate at which the one-time fee is taxed.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[oneTimeTaxAmount]: #onetimetaxamount
#### [oneTimeTaxAmount]
An invoice item's one-time tax amount. This does not include any child invoice items.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[parentId]: #parentid
#### [parentId]
The parent invoice item, usually the server invoice item.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[productItemId]: #productitemid
#### [productItemId]
The entry in the product catalog that a invoice item is based upon.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[recurringAfterTaxAmount]: #recurringaftertaxamount
#### [recurringAfterTaxAmount]
An invoice item's recurring fee total after taxes. This does not include any child invoice items.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[recurringFee]: #recurringfee
#### [recurringFee]
The recurring fee of the invoice item represented by a floating point decimal in US Dollars ($USD)  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[recurringFeeTaxRate]: #recurringfeetaxrate
#### [recurringFeeTaxRate]
the rate at which the recurring fee is taxed.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[recurringTaxAmount]: #recurringtaxamount
#### [recurringTaxAmount]
An invoice item's recurring tax amount. This does not include any child invoice items.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[resourceTableId]: #resourcetableid
#### [resourceTableId]
The unique Identifier of the hardware attached to an invoice item.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[serviceProviderId]: #serviceproviderid
#### [serviceProviderId]
The service provider for the invoice item.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[setupAfterTaxAmount]: #setupaftertaxamount
#### [setupAfterTaxAmount]
An invoice item's setup fee total after taxes. This does not include any child invoice items.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[setupFee]: #setupfee
#### [setupFee]
If there were any setup fees they will show up here. These are normally a one-time fee.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[setupFeeDeferralMonths]: #setupfeedeferralmonths
#### [setupFeeDeferralMonths]
The number of months the setup fee is being deferred.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[setupFeeTaxRate]: #setupfeetaxrate
#### [setupFeeTaxRate]
The tax rate at which the setup fee is taxed.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[setupTaxAmount]: #setuptaxamount
#### [setupTaxAmount]
An invoice item's setup tax amount. This does not include any child invoice items.  
<span class="type-label">Type: </span>**decimal**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[associatedChildren]: #associatedchildren
#### [associatedChildren]
An Invoice Item's associated child invoice items. Only parent invoice items have associated children. For instance, a server invoice item may have associated children.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a>**


</div>
<div class="prop-row">

-----
[associatedInvoiceItem]: #associatedinvoiceitem
#### [associatedInvoiceItem]
An Invoice Item's associated invoice item. If this is populated, it means this is an orphaned invoice item, but logically belongs to the associated invoice item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item </a>**


</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
An Invoice Item's billing item, from which this item was generated.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>
<div class="prop-row">

-----
[category]: #category
#### [category]
This invoice item's "item category".   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a>**


</div>
<div class="prop-row">

-----
[children]: #children
#### [children]
An Invoice Item's child invoice items. Only parent invoice items have children. For instance, a server invoice item will have children.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a>**


</div>
<div class="prop-row">

-----
[filteredAssociatedChildren]: #filteredassociatedchildren
#### [filteredAssociatedChildren]
An Invoice Item's associated child invoice items, excluding some items with a $0.00 recurring fee. Only parent invoice items have associated children. For instance, a server invoice item may have associated children.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a>**


</div>
<div class="prop-row">

-----
[hourlyFlag]: #hourlyflag
#### [hourlyFlag]
Indicating whether this invoice item is billed on an hourly basis.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[invoice]: #invoice
#### [invoice]
The invoice to which this item belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a>**


</div>
<div class="prop-row">

-----
[location]: #location
#### [location]
An invoice item's location, if one exists.'  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[nonZeroAssociatedChildren]: #nonzeroassociatedchildren
#### [nonZeroAssociatedChildren]
An Invoice Item's associated child invoice items, excluding ALL items with a $0.00 recurring fee. Only parent invoice items have associated children. For instance, a server invoice item may have associated children.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a>**


</div>
<div class="prop-row">

-----
[parent]: #parent
#### [parent]
Every item tied to a server should have a parent invoice item which is the server line item. This is how we associate items to a server.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item </a>**


</div>
<div class="prop-row">

-----
[product]: #product
#### [product]
The entry in the product catalog that a invoice item is based upon.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**


</div>
<div class="prop-row">

-----
[resource]: #resource
#### [resource]
The resource for a server invoice item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**


</div>
<div class="prop-row">

-----
[topLevelProductGroupName]: #toplevelproductgroupname
#### [topLevelProductGroupName]
A string representing the name of parent level product group of an invoice item.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[totalOneTimeAmount]: #totalonetimeamount
#### [totalOneTimeAmount]
An invoice Item's total, including any child invoice items if they exist.  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[totalOneTimeTaxAmount]: #totalonetimetaxamount
#### [totalOneTimeTaxAmount]
An invoice Item's total, including any child invoice items if they exist.  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[totalRecurringAmount]: #totalrecurringamount
#### [totalRecurringAmount]
An invoice Item's total, including any child invoice items if they exist.  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[totalRecurringTaxAmount]: #totalrecurringtaxamount
#### [totalRecurringTaxAmount]
A Billing Item's total, including any child billing items if they exist.'  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[usageChargeFlag]: #usagechargeflag
#### [usageChargeFlag]
Indicating whether this invoice item is for the usage charge.  
<span class="type-label">Type: </span>**boolean**


</div>

## Count
<div class="prop-row">

-----
[associatedChildrenCount]: #associatedchildrencount
#### [associatedChildrenCount]
A count of an Invoice Item's associated child invoice items. Only parent invoice items have associated children. For instance, a server invoice item may have associated children.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[childrenCount]: #childrencount
#### [childrenCount]
A count of an Invoice Item's child invoice items. Only parent invoice items have children. For instance, a server invoice item will have children.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[filteredAssociatedChildrenCount]: #filteredassociatedchildrencount
#### [filteredAssociatedChildrenCount]
A count of an Invoice Item's associated child invoice items, excluding some items with a $0.00 recurring fee. Only parent invoice items have associated children. For instance, a server invoice item may have associated children.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[nonZeroAssociatedChildrenCount]: #nonzeroassociatedchildrencount
#### [nonZeroAssociatedChildrenCount]
A count of an Invoice Item's associated child invoice items, excluding ALL items with a $0.00 recurring fee. Only parent invoice items have associated children. For instance, a server invoice item may have associated children.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


