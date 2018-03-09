---
title: "SoftLayer_Billing_Invoice_Item"
description: "Each billing invoice item makes up a record within an invoice. This provides you with a detailed record of everything re... "
layout: "datatype"
tags:
    - "datatype"
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
Each billing invoice item makes up a record within an invoice. This provides you with a detailed record of everything related to an invoice item. When you are billed, our system takes active billing items and creates an invoice. These invoice items are a copy of your active billing items, and make up the contents of your invoice. 


### associatedMethods

*  [SoftLayer_Billing_Invoice_Item::getObject](/reference/services/SoftLayer_Billing_Invoice_Item/getObject )



### seeAlso

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
                <a href="#associatedInvoiceItemId" name=associatedInvoiceItemId>associatedInvoiceItemId</a>
            </span>
            <div class='views-field-body'>The associated invoice Item ID. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingItemId" name=billingItemId>billingItemId</a>
            </span>
            <div class='views-field-body'>The billing item from which this invoice item was generated. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#categoryCode" name=categoryCode>categoryCode</a>
            </span>
            <div class='views-field-body'>The item category of the invoice item being invoiced. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>The date the invoice item was created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#description" name=description>description</a>
            </span>
            <div class='views-field-body'>The item description for this invoice item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#domainName" name=domainName>domainName</a>
            </span>
            <div class='views-field-body'>The domain name of the invoiced item. This is only used on invoice items whose category is "server". </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hostName" name=hostName>hostName</a>
            </span>
            <div class='views-field-body'>The Host name of the invoiced item. This is only used on invoice items whose category is "server". </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hourlyRecurringFee" name=hourlyRecurringFee>hourlyRecurringFee</a>
            </span>
            <div class='views-field-body'>The hourly recurring fee of the invoice item represented by a floating point decimal in US Dollars ($USD) </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The ID of the invoice item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoiceId" name=invoiceId>invoiceId</a>
            </span>
            <div class='views-field-body'>The invoice to which this invoice item belongs. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#laborAfterTaxAmount" name=laborAfterTaxAmount>laborAfterTaxAmount</a>
            </span>
            <div class='views-field-body'>An invoice item's labor fee total after taxes. This does not include any child invoice items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#laborFee" name=laborFee>laborFee</a>
            </span>
            <div class='views-field-body'>This also a one-time fee of a special type. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#laborFeeTaxRate" name=laborFeeTaxRate>laborFeeTaxRate</a>
            </span>
            <div class='views-field-body'>The tax rate at which the labor fee is taxed. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#laborTaxAmount" name=laborTaxAmount>laborTaxAmount</a>
            </span>
            <div class='views-field-body'>An invoice item's labor tax amount. This does not include any child invoice items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notes" name=notes>notes</a>
            </span>
            <div class='views-field-body'>A note to help describe more about the item. This normally holds usernames, or some other bit of extra information. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#oneTimeAfterTaxAmount" name=oneTimeAfterTaxAmount>oneTimeAfterTaxAmount</a>
            </span>
            <div class='views-field-body'>An invoice item's one-time fee total after taxes. This does not include any child invoice items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#oneTimeFee" name=oneTimeFee>oneTimeFee</a>
            </span>
            <div class='views-field-body'>If there are any one-time charges assessed, it will show up here represented by a floating point decimal in US Dollars ($USD) </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#oneTimeFeeTaxRate" name=oneTimeFeeTaxRate>oneTimeFeeTaxRate</a>
            </span>
            <div class='views-field-body'>The rate at which the one-time fee is taxed. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#oneTimeTaxAmount" name=oneTimeTaxAmount>oneTimeTaxAmount</a>
            </span>
            <div class='views-field-body'>An invoice item's one-time tax amount. This does not include any child invoice items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#parentId" name=parentId>parentId</a>
            </span>
            <div class='views-field-body'>The parent invoice item, usually the server invoice item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#productItemId" name=productItemId>productItemId</a>
            </span>
            <div class='views-field-body'>The entry in the product catalog that a invoice item is based upon. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#recurringAfterTaxAmount" name=recurringAfterTaxAmount>recurringAfterTaxAmount</a>
            </span>
            <div class='views-field-body'>An invoice item's recurring fee total after taxes. This does not include any child invoice items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#recurringFee" name=recurringFee>recurringFee</a>
            </span>
            <div class='views-field-body'>The recurring fee of the invoice item represented by a floating point decimal in US Dollars ($USD) </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#recurringFeeTaxRate" name=recurringFeeTaxRate>recurringFeeTaxRate</a>
            </span>
            <div class='views-field-body'>the rate at which the recurring fee is taxed. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#recurringTaxAmount" name=recurringTaxAmount>recurringTaxAmount</a>
            </span>
            <div class='views-field-body'>An invoice item's recurring tax amount. This does not include any child invoice items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#resourceTableId" name=resourceTableId>resourceTableId</a>
            </span>
            <div class='views-field-body'>A unique identifier for a SoftLayer Service that is associated to an invoice item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#serviceProviderId" name=serviceProviderId>serviceProviderId</a>
            </span>
            <div class='views-field-body'>The service provider for the invoice item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#setupAfterTaxAmount" name=setupAfterTaxAmount>setupAfterTaxAmount</a>
            </span>
            <div class='views-field-body'>An invoice item's setup fee total after taxes. This does not include any child invoice items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#setupFee" name=setupFee>setupFee</a>
            </span>
            <div class='views-field-body'>If there were any setup fees they will show up here. These are normally a one-time fee. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#setupFeeTaxRate" name=setupFeeTaxRate>setupFeeTaxRate</a>
            </span>
            <div class='views-field-body'>The tax rate at which the setup fee is taxed. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#setupTaxAmount" name=setupTaxAmount>setupTaxAmount</a>
            </span>
            <div class='views-field-body'>An invoice item's setup tax amount. This does not include any child invoice items. </div>
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
                <a href="#associatedChildren" name=associatedChildren>associatedChildren</a>
            </span>
            <div class='views-field-body'>An Invoice Item's associated child invoice items. Only parent invoice items have associated children. For instance, a server invoice item may have associated children. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#associatedInvoiceItem" name=associatedInvoiceItem>associatedInvoiceItem</a>
            </span>
            <div class='views-field-body'>An Invoice Item's associated invoice item. If this is populated, it means this is an orphaned invoice item, but logically belongs to the associated invoice item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingItem" name=billingItem>billingItem</a>
            </span>
            <div class='views-field-body'>An Invoice Item's billing item, from which this item was generated. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#category" name=category>category</a>
            </span>
            <div class='views-field-body'>This invoice item's "item category".  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#children" name=children>children</a>
            </span>
            <div class='views-field-body'>An Invoice Item's child invoice items. Only parent invoice items have children. For instance, a server invoice item will have children. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#filteredAssociatedChildren" name=filteredAssociatedChildren>filteredAssociatedChildren</a>
            </span>
            <div class='views-field-body'>An Invoice Item's associated child invoice items, excluding some items with a $0.00 recurring fee. Only parent invoice items have associated children. For instance, a server invoice item may have associated children. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hourlyFlag" name=hourlyFlag>hourlyFlag</a>
            </span>
            <div class='views-field-body'>Indicating whether this invoice item is billed on an hourly basis. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoice" name=invoice>invoice</a>
            </span>
            <div class='views-field-body'>The invoice to which this item belongs. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#location" name=location>location</a>
            </span>
            <div class='views-field-body'>An invoice item's location, if one exists.' </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#nonZeroAssociatedChildren" name=nonZeroAssociatedChildren>nonZeroAssociatedChildren</a>
            </span>
            <div class='views-field-body'>An Invoice Item's associated child invoice items, excluding ALL items with a $0.00 recurring fee. Only parent invoice items have associated children. For instance, a server invoice item may have associated children. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#parent" name=parent>parent</a>
            </span>
            <div class='views-field-body'>Every item tied to a server should have a parent invoice item which is the server line item. This is how we associate items to a server. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#product" name=product>product</a>
            </span>
            <div class='views-field-body'>The entry in the product catalog that a invoice item is based upon. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#topLevelProductGroupName" name=topLevelProductGroupName>topLevelProductGroupName</a>
            </span>
            <div class='views-field-body'>A string representing the name of parent level product group of an invoice item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#totalOneTimeAmount" name=totalOneTimeAmount>totalOneTimeAmount</a>
            </span>
            <div class='views-field-body'>An invoice Item's total, including any child invoice items if they exist. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#totalOneTimeTaxAmount" name=totalOneTimeTaxAmount>totalOneTimeTaxAmount</a>
            </span>
            <div class='views-field-body'>An invoice Item's total, including any child invoice items if they exist. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#totalRecurringAmount" name=totalRecurringAmount>totalRecurringAmount</a>
            </span>
            <div class='views-field-body'>An invoice Item's total, including any child invoice items if they exist. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#totalRecurringTaxAmount" name=totalRecurringTaxAmount>totalRecurringTaxAmount</a>
            </span>
            <div class='views-field-body'>A Billing Item's total, including any child billing items if they exist.' </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#usageChargeFlag" name=usageChargeFlag>usageChargeFlag</a>
            </span>
            <div class='views-field-body'>Indicating whether this invoice item is for the usage charge. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#associatedChildrenCount" name=associatedChildrenCount>associatedChildrenCount</a>
            </span>
            <div class='views-field-body'>A count of an Invoice Item's associated child invoice items. Only parent invoice items have associated children. For instance, a server invoice item may have associated children. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#childrenCount" name=childrenCount>childrenCount</a>
            </span>
            <div class='views-field-body'>A count of an Invoice Item's child invoice items. Only parent invoice items have children. For instance, a server invoice item will have children. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#filteredAssociatedChildrenCount" name=filteredAssociatedChildrenCount>filteredAssociatedChildrenCount</a>
            </span>
            <div class='views-field-body'>A count of an Invoice Item's associated child invoice items, excluding some items with a $0.00 recurring fee. Only parent invoice items have associated children. For instance, a server invoice item may have associated children. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#nonZeroAssociatedChildrenCount" name=nonZeroAssociatedChildrenCount>nonZeroAssociatedChildrenCount</a>
            </span>
            <div class='views-field-body'>A count of an Invoice Item's associated child invoice items, excluding ALL items with a $0.00 recurring fee. Only parent invoice items have associated children. For instance, a server invoice item may have associated children. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


