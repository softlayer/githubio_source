---
title: "SoftLayer_Billing_Item_Network_PerformanceStorage_Iscsi"
description: "The SoftLayer_Billing_Item_Network_PerformanceStorage_Iscsi data type contains general information relating to a single... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Network_PerformanceStorage_Iscsi"
---

# SoftLayer_Billing_Item_Network_PerformanceStorage_Iscsi
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Item_Network_PerformanceStorage_Iscsi' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Billing_Item_Network_PerformanceStorage_Iscsi data type contains general information relating to a single SoftLayer billing item whose item category code is 'performance_storage_iscsi' 





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
[allowCancellationFlag]: #allowcancellationflag
#### [allowCancellationFlag]
Flag to check if a billing item can be cancelled. 1 = yes. 0 = no.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[associatedBillingItemId]: #associatedbillingitemid
#### [associatedBillingItemId]
This is sometimes populated for orphan billing items that are not attached to servers. Billing items like secondary portable IP addresses fit into this category. A user may set an association by calling [SoftLayer_Billing_Item::setAssociationId]({{<ref "reference/services/SoftLayer_Billing_Item/setAssociationId">}}). This will cause this orphan item to appear under its associated server billing item on future invoices. You may only attach orphaned billing items to server billing items without cancellation dates set.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[cancellationDate]: #cancellationdate
#### [cancellationDate]
A billing item's cancellation date. A billing item with a cancellation date in the past is not charged on your SoftLayer invoice. Cancellation dates in the future indicate the current billing item is active, but will be cancelled and not charged for in the future. A billing item with a null cancellation date is also considered an active billing item and is charged once every billing cycle.   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[categoryCode]: #categorycode
#### [categoryCode]
The category code of this billing item. It is used to tell us the difference between a primary disk and a secondary disk, for instance.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date the billing item was created. You can see this date on the invoice.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[currentHourlyCharge]: #currenthourlycharge
#### [currentHourlyCharge]
This is the total charge for the billing item for this billing item. It is calculated based on the hourlyRecurringFee * hoursUsed.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[cycleStartDate]: #cyclestartdate
#### [cycleStartDate]
The last time this billing item was charged.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
A brief description of a billing item.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[domainName]: #domainname
#### [domainName]
The domain name is provided for server billing items.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[hostName]: #hostname
#### [hostName]
The hostname is provided for server billing items  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[hourlyRecurringFee]: #hourlyrecurringfee
#### [hourlyRecurringFee]
The amount of money charged per hour for a billing item, if applicable. hourlyRecurringFee is measured in US Dollars ($USD).   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[hoursUsed]: #hoursused
#### [hoursUsed]
This is the number of hours the hourly billing item has been in use this billing period. For virtual servers, this means running, paused or stopped.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique identifier for this billing item.  
<span class="type-label">Type: </span>**integer**


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
[lastBillDate]: #lastbilldate
#### [lastBillDate]
The last time this billing item was charged.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date that a billing item was last modified.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[nextBillDate]: #nextbilldate
#### [nextBillDate]
The date on which your account will be charged for this billing item.   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
Extra information provided to help you identify this billing item. This is often a username or something to help identify items that customers have more than one of.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[oneTimeFee]: #onetimefee
#### [oneTimeFee]
The amount of money charged as a one-time charge for a billing item, if applicable. oneTimeFee is measured in US Dollars ($USD).   
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
[orderItemId]: #orderitemid
#### [orderItemId]
the SoftLayer_Billing_Order_Item ID. This is a reference to the original order item from which this billing item was originally created.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[parentId]: #parentid
#### [parentId]
The unique identifier of the parent of this billing item.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[recurringFee]: #recurringfee
#### [recurringFee]
The amount of money charged per month for a billing item, if applicable. recurringFee is measured in US Dollars ($USD).   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[recurringFeeTaxRate]: #recurringfeetaxrate
#### [recurringFeeTaxRate]
The rate at which recurring fees are taxed if you are a taxable customer.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[recurringMonths]: #recurringmonths
#### [recurringMonths]
The number of months in which the recurring fees will be incurred.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[serviceProviderId]: #serviceproviderid
#### [serviceProviderId]
This is the service provider for this billing item.   
<span class="type-label">Type: </span>**integer**


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
[setupFeeTaxRate]: #setupfeetaxrate
#### [setupFeeTaxRate]
The rate at which setup fees are taxed if you are a taxable customer.  
<span class="type-label">Type: </span>**decimal**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account that a billing item belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[activeAgreement]: #activeagreement
#### [activeAgreement]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Agreement'>SoftLayer_Account_Agreement </a>**


</div>
<div class="prop-row">

-----
[activeAgreementFlag]: #activeagreementflag
#### [activeAgreementFlag]
A flag indicating that the billing item is under an active agreement.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Agreement'>SoftLayer_Account_Agreement </a>**


</div>
<div class="prop-row">

-----
[activeAssociatedChildren]: #activeassociatedchildren
#### [activeAssociatedChildren]
A billing item's active associated child billing items. This includes "floating" items that are not necessarily child items of this billing item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[activeAssociatedGuestDiskBillingItems]: #activeassociatedguestdiskbillingitems
#### [activeAssociatedGuestDiskBillingItems]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[activeBundledItems]: #activebundleditems
#### [activeBundledItems]
A Billing Item's active bundled billing items.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[activeCancellationItem]: #activecancellationitem
#### [activeCancellationItem]
A service cancellation request item that corresponds to the billing item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request_Item'>SoftLayer_Billing_Item_Cancellation_Request_Item </a>**


</div>
<div class="prop-row">

-----
[activeChildren]: #activechildren
#### [activeChildren]
A Billing Item's active child billing items.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[activeFlag]: #activeflag
#### [activeFlag]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[activeSparePoolAssociatedGuestDiskBillingItems]: #activesparepoolassociatedguestdiskbillingitems
#### [activeSparePoolAssociatedGuestDiskBillingItems]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[activeSparePoolBundledItems]: #activesparepoolbundleditems
#### [activeSparePoolBundledItems]
A Billing Item's spare pool bundled billing items.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[associatedBillingItem]: #associatedbillingitem
#### [associatedBillingItem]
A billing item's associated parent. This is to be used for billing items that are "floating", and therefore are not child items of any parent billing item. If it is desired to associate an item to another, populate this with the SoftLayer_Billing_Item ID of that associated parent item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>
<div class="prop-row">

-----
[associatedBillingItemHistory]: #associatedbillingitemhistory
#### [associatedBillingItemHistory]
A history of billing items which a billing item has been associated with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Association_History'>SoftLayer_Billing_Item_Association_History[] </a>**


</div>
<div class="prop-row">

-----
[associatedChildren]: #associatedchildren
#### [associatedChildren]
A Billing Item's associated child billing items. This includes "floating" items that are not necessarily child billing items of this billing item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[associatedParent]: #associatedparent
#### [associatedParent]
A billing item's associated parent billing item. This object will be the same as the parent billing item if parentId is set.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[availableMatchingVlans]: #availablematchingvlans
#### [availableMatchingVlans]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>**


</div>
<div class="prop-row">

-----
[bandwidthAllocation]: #bandwidthallocation
#### [bandwidthAllocation]
The bandwidth allocation for a billing item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allocation'>SoftLayer_Network_Bandwidth_Version1_Allocation </a>**


</div>
<div class="prop-row">

-----
[billableChildren]: #billablechildren
#### [billableChildren]
A billing item's recurring child items that have once been billed and are scheduled to be billed in the future.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[bundleItems]: #bundleitems
#### [bundleItems]
A Billing Item's bundled billing items  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Bundles'>SoftLayer_Product_Item_Bundles[] </a>**


</div>
<div class="prop-row">

-----
[bundledItems]: #bundleditems
#### [bundledItems]
A Billing Item's bundled billing items'  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[canceledChildren]: #canceledchildren
#### [canceledChildren]
A Billing Item's active child billing items.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[cancellationReason]: #cancellationreason
#### [cancellationReason]
The billing item's cancellation reason.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Reason'>SoftLayer_Billing_Item_Cancellation_Reason </a>**


</div>
<div class="prop-row">

-----
[cancellationRequests]: #cancellationrequests
#### [cancellationRequests]
This will return any cancellation requests that are associated with this billing item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request'>SoftLayer_Billing_Item_Cancellation_Request[] </a>**


</div>
<div class="prop-row">

-----
[category]: #category
#### [category]
The item category to which the billing item's item belongs.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a>**


</div>
<div class="prop-row">

-----
[children]: #children
#### [children]
A Billing Item's child billing items'  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[childrenWithActiveAgreement]: #childrenwithactiveagreement
#### [childrenWithActiveAgreement]
A Billing Item's active child billing items.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[downgradeItems]: #downgradeitems
#### [downgradeItems]
For product items which have a downgrade path defined, this will return those product items.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>**


</div>
<div class="prop-row">

-----
[filteredNextInvoiceChildren]: #filterednextinvoicechildren
#### [filteredNextInvoiceChildren]
A Billing Item's associated child billing items, excluding some items with a $0.00 recurring fee.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[hourlyFlag]: #hourlyflag
#### [hourlyFlag]
A flag that will reflect whether this billing item is billed on an hourly basis or not.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[invoiceItem]: #invoiceitem
#### [invoiceItem]
Invoice items associated with this billing item  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item </a>**


</div>
<div class="prop-row">

-----
[invoiceItems]: #invoiceitems
#### [invoiceItems]
All invoice items associated with the billing item  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a>**


</div>
<div class="prop-row">

-----
[item]: #item
#### [item]
The entry in the SoftLayer product catalog that a billing item is based upon.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**


</div>
<div class="prop-row">

-----
[location]: #location
#### [location]
The location of the billing item. Some billing items have physical properties such as the server itself. For items such as these, we provide location information.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[nextInvoiceChildren]: #nextinvoicechildren
#### [nextInvoiceChildren]
A Billing Item's child billing items and associated items'  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[nextInvoiceTotalOneTimeAmount]: #nextinvoicetotalonetimeamount
#### [nextInvoiceTotalOneTimeAmount]
A Billing Item's total, including any child billing items if they exist.'  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[nextInvoiceTotalOneTimeTaxAmount]: #nextinvoicetotalonetimetaxamount
#### [nextInvoiceTotalOneTimeTaxAmount]
A Billing Item's total, including any child billing items if they exist.'  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[nextInvoiceTotalRecurringAmount]: #nextinvoicetotalrecurringamount
#### [nextInvoiceTotalRecurringAmount]
A Billing Item's total, including any child billing items and associated billing items if they exist.'  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[nextInvoiceTotalRecurringTaxAmount]: #nextinvoicetotalrecurringtaxamount
#### [nextInvoiceTotalRecurringTaxAmount]
This is deprecated and will always be zero. Because tax is calculated in real-time, previewing the next recurring invoice is pre-tax only.  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[nonZeroNextInvoiceChildren]: #nonzeronextinvoicechildren
#### [nonZeroNextInvoiceChildren]
A Billing Item's associated child billing items, excluding ALL items with a $0.00 recurring fee.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


</div>
<div class="prop-row">

-----
[orderItem]: #orderitem
#### [orderItem]
A billing item's original order item. Simply a reference to the original order from which this billing item was created.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item </a>**


</div>
<div class="prop-row">

-----
[originalLocation]: #originallocation
#### [originalLocation]
The original physical location for this billing item--may differ from current.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[package]: #package
#### [package]
The package under which this billing item was sold. A Package is the general grouping of products as seen on our order forms.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a>**


</div>
<div class="prop-row">

-----
[parent]: #parent
#### [parent]
A billing item's parent item. If a billing item has no parent item then this value is null.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>
<div class="prop-row">

-----
[parentVirtualGuestBillingItem]: #parentvirtualguestbillingitem
#### [parentVirtualGuestBillingItem]
A billing item's parent item. If a billing item has no parent item then this value is null.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Virtual_Guest'>SoftLayer_Billing_Item_Virtual_Guest </a>**


</div>
<div class="prop-row">

-----
[pendingCancellationFlag]: #pendingcancellationflag
#### [pendingCancellationFlag]
This flag indicates whether a billing item is scheduled to be canceled or not.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[pendingOrderItem]: #pendingorderitem
#### [pendingOrderItem]
The new order item that will replace this billing item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item </a>**


</div>
<div class="prop-row">

-----
[provisionTransaction]: #provisiontransaction
#### [provisionTransaction]
Provisioning transaction for this billing item  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>**


</div>
<div class="prop-row">

-----
[resource]: #resource
#### [resource]
The StorageLayer account that a network storage billing item is associated with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>**


</div>
<div class="prop-row">

-----
[softwareDescription]: #softwaredescription
#### [softwareDescription]
A friendly description of software component  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a>**


</div>
<div class="prop-row">

-----
[upgradeItem]: #upgradeitem
#### [upgradeItem]
Billing items whose product item has an upgrade path defined in our system will return the next product item in the upgrade path.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**


</div>
<div class="prop-row">

-----
[upgradeItems]: #upgradeitems
#### [upgradeItems]
Billing items whose product item has an upgrade path defined in our system will return all the product items in the upgrade path.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>**


</div>

## Count
<div class="prop-row">

-----
[activeAssociatedChildrenCount]: #activeassociatedchildrencount
#### [activeAssociatedChildrenCount]
A count of a billing item's active associated child billing items. This includes "floating" items that are not necessarily child items of this billing item.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeAssociatedGuestDiskBillingItemCount]: #activeassociatedguestdiskbillingitemcount
#### [activeAssociatedGuestDiskBillingItemCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeBundledItemCount]: #activebundleditemcount
#### [activeBundledItemCount]
A count of a Billing Item's active bundled billing items.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeChildrenCount]: #activechildrencount
#### [activeChildrenCount]
A count of a Billing Item's active child billing items.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeSparePoolAssociatedGuestDiskBillingItemCount]: #activesparepoolassociatedguestdiskbillingitemcount
#### [activeSparePoolAssociatedGuestDiskBillingItemCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[activeSparePoolBundledItemCount]: #activesparepoolbundleditemcount
#### [activeSparePoolBundledItemCount]
A count of a Billing Item's spare pool bundled billing items.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[associatedBillingItemHistoryCount]: #associatedbillingitemhistorycount
#### [associatedBillingItemHistoryCount]
A count of a history of billing items which a billing item has been associated with.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[associatedChildrenCount]: #associatedchildrencount
#### [associatedChildrenCount]
A count of a Billing Item's associated child billing items. This includes "floating" items that are not necessarily child billing items of this billing item.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[associatedParentCount]: #associatedparentcount
#### [associatedParentCount]
A count of a billing item's associated parent billing item. This object will be the same as the parent billing item if parentId is set.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[availableMatchingVlanCount]: #availablematchingvlancount
#### [availableMatchingVlanCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[billableChildrenCount]: #billablechildrencount
#### [billableChildrenCount]
A count of a billing item's recurring child items that have once been billed and are scheduled to be billed in the future.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[bundleItemCount]: #bundleitemcount
#### [bundleItemCount]
A count of a Billing Item's bundled billing items   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[bundledItemCount]: #bundleditemcount
#### [bundledItemCount]
A count of a Billing Item's bundled billing items'   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[canceledChildrenCount]: #canceledchildrencount
#### [canceledChildrenCount]
A count of a Billing Item's active child billing items.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[cancellationRequestCount]: #cancellationrequestcount
#### [cancellationRequestCount]
A count of this will return any cancellation requests that are associated with this billing item.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[childrenCount]: #childrencount
#### [childrenCount]
A count of a Billing Item's child billing items'   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[childrenWithActiveAgreementCount]: #childrenwithactiveagreementcount
#### [childrenWithActiveAgreementCount]
A count of a Billing Item's active child billing items.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[downgradeItemCount]: #downgradeitemcount
#### [downgradeItemCount]
A count of for product items which have a downgrade path defined, this will return those product items.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[filteredNextInvoiceChildrenCount]: #filterednextinvoicechildrencount
#### [filteredNextInvoiceChildrenCount]
A count of a Billing Item's associated child billing items, excluding some items with a $0.00 recurring fee.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[invoiceItemCount]: #invoiceitemcount
#### [invoiceItemCount]
A count of all invoice items associated with the billing item   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[nextInvoiceChildrenCount]: #nextinvoicechildrencount
#### [nextInvoiceChildrenCount]
A count of a Billing Item's child billing items and associated items'   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[nonZeroNextInvoiceChildrenCount]: #nonzeronextinvoicechildrencount
#### [nonZeroNextInvoiceChildrenCount]
A count of a Billing Item's associated child billing items, excluding ALL items with a $0.00 recurring fee.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[upgradeItemCount]: #upgradeitemcount
#### [upgradeItemCount]
A count of billing items whose product item has an upgrade path defined in our system will return all the product items in the upgrade path.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


