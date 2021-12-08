---
title: "SoftLayer_Billing_Item"
description: "Every individual item that a SoftLayer customer is billed for is recorded in the SoftLayer_Billing_Item data type. Billi... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item"
---
# SoftLayer_Billing_Item
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Billing_Item' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Item' >Datatype</a></li>
    </ul>
</div>

## Description


Every individual item that a SoftLayer customer is billed for is recorded in the SoftLayer_Billing_Item data type. Billing items range from server chassis to hard drives to control panels, bandwidth quota upgrades and port upgrade charges. Softlayer [SoftLayer_Billing_Invoice]({{<ref "reference/datatypes/SoftLayer_Billing_Invoice">}}) are generated from the cost of a customer's billing items. Billing items are copied from the product catalog as they're ordered by customers to create a reference between an account and the billable items they own. 

Billing items exist in a tree relationship. Items are associated with each other by parent/child relationships. Component items such as CPU's, RAM, and software each have a parent billing item for the server chassis they're associated with. Billing Items with a null parent item do not have an associated parent item. 



        
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

#### [cancelItem](/reference/services/SoftLayer_Billing_Item/cancelItem)
Cancel a service or resource.

</div>

<div class="method-row">

#### [cancelService](/reference/services/SoftLayer_Billing_Item/cancelService)
Cancel a service or resource immediately. This does not include bare metal servers. 

</div>

<div class="method-row">

#### [cancelServiceOnAnniversaryDate](/reference/services/SoftLayer_Billing_Item/cancelServiceOnAnniversaryDate)
Cancel a service or resource on the next bill date

</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Billing_Item/getAccount)
Retrieve the account that a billing item belongs to.

</div>

<div class="method-row">

#### [getActiveAgreement](/reference/services/SoftLayer_Billing_Item/getActiveAgreement)


</div>

<div class="method-row">

#### [getActiveAgreementFlag](/reference/services/SoftLayer_Billing_Item/getActiveAgreementFlag)
Retrieve a flag indicating that the billing item is under an active agreement.

</div>

<div class="method-row">

#### [getActiveAssociatedChildren](/reference/services/SoftLayer_Billing_Item/getActiveAssociatedChildren)
Retrieve a billing item's active associated child billing items. This includes "floating" items that are not necessarily child items of this billing item.

</div>

<div class="method-row">

#### [getActiveAssociatedGuestDiskBillingItems](/reference/services/SoftLayer_Billing_Item/getActiveAssociatedGuestDiskBillingItems)


</div>

<div class="method-row">

#### [getActiveBundledItems](/reference/services/SoftLayer_Billing_Item/getActiveBundledItems)
Retrieve a Billing Item's active bundled billing items.

</div>

<div class="method-row">

#### [getActiveCancellationItem](/reference/services/SoftLayer_Billing_Item/getActiveCancellationItem)
Retrieve a service cancellation request item that corresponds to the billing item.

</div>

<div class="method-row">

#### [getActiveChildren](/reference/services/SoftLayer_Billing_Item/getActiveChildren)
Retrieve a Billing Item's active child billing items.

</div>

<div class="method-row">

#### [getActiveFlag](/reference/services/SoftLayer_Billing_Item/getActiveFlag)


</div>

<div class="method-row">

#### [getActiveSparePoolAssociatedGuestDiskBillingItems](/reference/services/SoftLayer_Billing_Item/getActiveSparePoolAssociatedGuestDiskBillingItems)


</div>

<div class="method-row">

#### [getActiveSparePoolBundledItems](/reference/services/SoftLayer_Billing_Item/getActiveSparePoolBundledItems)
Retrieve a Billing Item's spare pool bundled billing items.

</div>

<div class="method-row">

#### [getAssociatedBillingItem](/reference/services/SoftLayer_Billing_Item/getAssociatedBillingItem)
Retrieve a billing item's associated parent. This is to be used for billing items that are "floating", and therefore are not child items of any parent billing item. If it is desired to associate an item to another, populate this with the SoftLayer_Billing_Item ID of that associated parent item.

</div>

<div class="method-row">

#### [getAssociatedBillingItemHistory](/reference/services/SoftLayer_Billing_Item/getAssociatedBillingItemHistory)
Retrieve a history of billing items which a billing item has been associated with.

</div>

<div class="method-row">

#### [getAssociatedChildren](/reference/services/SoftLayer_Billing_Item/getAssociatedChildren)
Retrieve a Billing Item's associated child billing items. This includes "floating" items that are not necessarily child billing items of this billing item.

</div>

<div class="method-row">

#### [getAssociatedParent](/reference/services/SoftLayer_Billing_Item/getAssociatedParent)
Retrieve a billing item's associated parent billing item. This object will be the same as the parent billing item if parentId is set.

</div>

<div class="method-row">

#### [getAvailableMatchingVlans](/reference/services/SoftLayer_Billing_Item/getAvailableMatchingVlans)


</div>

<div class="method-row">

#### [getBandwidthAllocation](/reference/services/SoftLayer_Billing_Item/getBandwidthAllocation)
Retrieve the bandwidth allocation for a billing item.

</div>

<div class="method-row">

#### [getBillableChildren](/reference/services/SoftLayer_Billing_Item/getBillableChildren)
Retrieve a billing item's recurring child items that have once been billed and are scheduled to be billed in the future.

</div>

<div class="method-row">

#### [getBundleItems](/reference/services/SoftLayer_Billing_Item/getBundleItems)
Retrieve (DEPRECATED) Do not use.

</div>

<div class="method-row">

#### [getBundledItems](/reference/services/SoftLayer_Billing_Item/getBundledItems)
Retrieve a Billing Item's bundled billing items.

</div>

<div class="method-row">

#### [getCanceledChildren](/reference/services/SoftLayer_Billing_Item/getCanceledChildren)
Retrieve a Billing Item's active child billing items.

</div>

<div class="method-row">

#### [getCancellationReason](/reference/services/SoftLayer_Billing_Item/getCancellationReason)
Retrieve the billing item's cancellation reason.

</div>

<div class="method-row">

#### [getCancellationRequests](/reference/services/SoftLayer_Billing_Item/getCancellationRequests)
Retrieve this will return any cancellation requests that are associated with this billing item.

</div>

<div class="method-row">

#### [getCategory](/reference/services/SoftLayer_Billing_Item/getCategory)
Retrieve the item category to which the billing item's item belongs. 

</div>

<div class="method-row">

#### [getChildren](/reference/services/SoftLayer_Billing_Item/getChildren)
Retrieve a Billing Item's child billing items'

</div>

<div class="method-row">

#### [getChildrenWithActiveAgreement](/reference/services/SoftLayer_Billing_Item/getChildrenWithActiveAgreement)
Retrieve a Billing Item's active child billing items.

</div>

<div class="method-row">

#### [getDowngradeItems](/reference/services/SoftLayer_Billing_Item/getDowngradeItems)
Retrieve for product items which have a downgrade path defined, this will return those product items.

</div>

<div class="method-row">

#### [getFilteredNextInvoiceChildren](/reference/services/SoftLayer_Billing_Item/getFilteredNextInvoiceChildren)
Retrieve a Billing Item's associated child billing items, excluding some items with a $0.00 recurring fee.

</div>

<div class="method-row">

#### [getHourlyFlag](/reference/services/SoftLayer_Billing_Item/getHourlyFlag)
Retrieve a flag that will reflect whether this billing item is billed on an hourly basis or not.

</div>

<div class="method-row">

#### [getInvoiceItem](/reference/services/SoftLayer_Billing_Item/getInvoiceItem)
Retrieve invoice items associated with this billing item

</div>

<div class="method-row">

#### [getInvoiceItems](/reference/services/SoftLayer_Billing_Item/getInvoiceItems)
Retrieve all invoice items associated with the billing item

</div>

<div class="method-row">

#### [getItem](/reference/services/SoftLayer_Billing_Item/getItem)
Retrieve the entry in the SoftLayer product catalog that a billing item is based upon.

</div>

<div class="method-row">

#### [getLocation](/reference/services/SoftLayer_Billing_Item/getLocation)
Retrieve the location of the billing item. Some billing items have physical properties such as the server itself. For items such as these, we provide location information.

</div>

<div class="method-row">

#### [getNextInvoiceChildren](/reference/services/SoftLayer_Billing_Item/getNextInvoiceChildren)
Retrieve a Billing Item's child billing items and associated items'

</div>

<div class="method-row">

#### [getNextInvoiceTotalOneTimeAmount](/reference/services/SoftLayer_Billing_Item/getNextInvoiceTotalOneTimeAmount)
Retrieve a Billing Item's total, including any child billing items if they exist.'

</div>

<div class="method-row">

#### [getNextInvoiceTotalOneTimeTaxAmount](/reference/services/SoftLayer_Billing_Item/getNextInvoiceTotalOneTimeTaxAmount)
Retrieve a Billing Item's total, including any child billing items if they exist.'

</div>

<div class="method-row">

#### [getNextInvoiceTotalRecurringAmount](/reference/services/SoftLayer_Billing_Item/getNextInvoiceTotalRecurringAmount)
Retrieve a Billing Item's total, including any child billing items and associated billing items if they exist.'

</div>

<div class="method-row">

#### [getNextInvoiceTotalRecurringTaxAmount](/reference/services/SoftLayer_Billing_Item/getNextInvoiceTotalRecurringTaxAmount)
Retrieve this is deprecated and will always be zero. Because tax is calculated in real-time, previewing the next recurring invoice is pre-tax only.

</div>

<div class="method-row">

#### [getNonZeroNextInvoiceChildren](/reference/services/SoftLayer_Billing_Item/getNonZeroNextInvoiceChildren)
Retrieve a Billing Item's associated child billing items, excluding ALL items with a $0.00 recurring fee.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Billing_Item/getObject)
Retrieve a SoftLayer_Billing_Item record.

</div>

<div class="method-row">

#### [getOrderItem](/reference/services/SoftLayer_Billing_Item/getOrderItem)
Retrieve a billing item's original order item. Simply a reference to the original order from which this billing item was created.

</div>

<div class="method-row">

#### [getOriginalLocation](/reference/services/SoftLayer_Billing_Item/getOriginalLocation)
Retrieve the original physical location for this billing item--may differ from current.

</div>

<div class="method-row">

#### [getPackage](/reference/services/SoftLayer_Billing_Item/getPackage)
Retrieve the package under which this billing item was sold. A Package is the general grouping of products as seen on our order forms.

</div>

<div class="method-row">

#### [getParent](/reference/services/SoftLayer_Billing_Item/getParent)
Retrieve a billing item's parent item. If a billing item has no parent item then this value is null.

</div>

<div class="method-row">

#### [getParentVirtualGuestBillingItem](/reference/services/SoftLayer_Billing_Item/getParentVirtualGuestBillingItem)
Retrieve a billing item's parent item. If a billing item has no parent item then this value is null.

</div>

<div class="method-row">

#### [getPendingCancellationFlag](/reference/services/SoftLayer_Billing_Item/getPendingCancellationFlag)
Retrieve this flag indicates whether a billing item is scheduled to be canceled or not.

</div>

<div class="method-row">

#### [getPendingOrderItem](/reference/services/SoftLayer_Billing_Item/getPendingOrderItem)
Retrieve the new order item that will replace this billing item.

</div>

<div class="method-row">

#### [getProvisionTransaction](/reference/services/SoftLayer_Billing_Item/getProvisionTransaction)
Retrieve provisioning transaction for this billing item

</div>

<div class="method-row">

#### [getServiceBillingItemsByCategory](/reference/services/SoftLayer_Billing_Item/getServiceBillingItemsByCategory)
Returns billing item in a given category code. Use this method to retrieve service billing items that you wish to cancel.

</div>

<div class="method-row">

#### [getSoftwareDescription](/reference/services/SoftLayer_Billing_Item/getSoftwareDescription)
Retrieve a friendly description of software component

</div>

<div class="method-row">

#### [getUpgradeItem](/reference/services/SoftLayer_Billing_Item/getUpgradeItem)
Retrieve billing items whose product item has an upgrade path defined in our system will return the next product item in the upgrade path.

</div>

<div class="method-row">

#### [getUpgradeItems](/reference/services/SoftLayer_Billing_Item/getUpgradeItems)
Retrieve billing items whose product item has an upgrade path defined in our system will return all the product items in the upgrade path.

</div>

<div class="method-row">

#### [removeAssociationId](/reference/services/SoftLayer_Billing_Item/removeAssociationId)
Remove an association from an orphan billing item.

</div>

<div class="method-row">

#### [setAssociationId](/reference/services/SoftLayer_Billing_Item/setAssociationId)
Set the associated billing item for an orphan billing item.

</div>

<div class="method-row">

#### [voidCancelService](/reference/services/SoftLayer_Billing_Item/voidCancelService)
Void a service cancellation that was previously made.

</div>
</div>

</div>

