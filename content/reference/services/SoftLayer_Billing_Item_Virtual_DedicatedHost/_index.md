---
title: "SoftLayer_Billing_Item_Virtual_DedicatedHost"
description: ""
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Virtual_DedicatedHost"
---
# SoftLayer_Billing_Item_Virtual_DedicatedHost
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Item_Virtual_DedicatedHost' >Datatype</a></li>
    </ul>
</div>

## Description






        
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

#### [cancelItem](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/cancelItem)
Cancel a service or resource.

</div>

<div class="method-row">

#### [cancelService](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/cancelService)
Cancel a service or resource immediately. This does not include bare metal servers. 

</div>

<div class="method-row">

#### [cancelServiceOnAnniversaryDate](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/cancelServiceOnAnniversaryDate)
Cancel a service or resource on the next bill date

</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getAccount)
Retrieve the account that a billing item belongs to.

</div>

<div class="method-row">

#### [getActiveAgreement](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getActiveAgreement)


</div>

<div class="method-row">

#### [getActiveAgreementFlag](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getActiveAgreementFlag)
Retrieve a flag indicating that the billing item is under an active agreement.

</div>

<div class="method-row">

#### [getActiveAssociatedChildren](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getActiveAssociatedChildren)
Retrieve a billing item's active associated child billing items. This includes "floating" items that are not necessarily child items of this billing item.

</div>

<div class="method-row">

#### [getActiveAssociatedGuestDiskBillingItems](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getActiveAssociatedGuestDiskBillingItems)


</div>

<div class="method-row">

#### [getActiveBundledItems](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getActiveBundledItems)
Retrieve a Billing Item's active bundled billing items.

</div>

<div class="method-row">

#### [getActiveCancellationItem](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getActiveCancellationItem)
Retrieve a service cancellation request item that corresponds to the billing item.

</div>

<div class="method-row">

#### [getActiveChildren](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getActiveChildren)
Retrieve a Billing Item's active child billing items.

</div>

<div class="method-row">

#### [getActiveFlag](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getActiveFlag)


</div>

<div class="method-row">

#### [getActiveSparePoolAssociatedGuestDiskBillingItems](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getActiveSparePoolAssociatedGuestDiskBillingItems)


</div>

<div class="method-row">

#### [getActiveSparePoolBundledItems](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getActiveSparePoolBundledItems)
Retrieve a Billing Item's spare pool bundled billing items.

</div>

<div class="method-row">

#### [getAssociatedBillingItem](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getAssociatedBillingItem)
Retrieve a billing item's associated parent. This is to be used for billing items that are "floating", and therefore are not child items of any parent billing item. If it is desired to associate an item to another, populate this with the SoftLayer_Billing_Item ID of that associated parent item.

</div>

<div class="method-row">

#### [getAssociatedBillingItemHistory](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getAssociatedBillingItemHistory)
Retrieve a history of billing items which a billing item has been associated with.

</div>

<div class="method-row">

#### [getAssociatedChildren](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getAssociatedChildren)
Retrieve a Billing Item's associated child billing items. This includes "floating" items that are not necessarily child billing items of this billing item.

</div>

<div class="method-row">

#### [getAssociatedParent](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getAssociatedParent)
Retrieve a billing item's associated parent billing item. This object will be the same as the parent billing item if parentId is set.

</div>

<div class="method-row">

#### [getAvailableMatchingVlans](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getAvailableMatchingVlans)


</div>

<div class="method-row">

#### [getBandwidthAllocation](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getBandwidthAllocation)
Retrieve the bandwidth allocation for a billing item.

</div>

<div class="method-row">

#### [getBillableChildren](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getBillableChildren)
Retrieve a billing item's recurring child items that have once been billed and are scheduled to be billed in the future.

</div>

<div class="method-row">

#### [getBundleItems](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getBundleItems)
Retrieve a Billing Item's bundled billing items

</div>

<div class="method-row">

#### [getBundledItems](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getBundledItems)
Retrieve a Billing Item's bundled billing items'

</div>

<div class="method-row">

#### [getCanceledChildren](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getCanceledChildren)
Retrieve a Billing Item's active child billing items.

</div>

<div class="method-row">

#### [getCancellationReason](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getCancellationReason)
Retrieve the billing item's cancellation reason.

</div>

<div class="method-row">

#### [getCancellationRequests](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getCancellationRequests)
Retrieve this will return any cancellation requests that are associated with this billing item.

</div>

<div class="method-row">

#### [getCategory](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getCategory)
Retrieve the item category to which the billing item's item belongs. 

</div>

<div class="method-row">

#### [getChildren](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getChildren)
Retrieve a Billing Item's child billing items'

</div>

<div class="method-row">

#### [getChildrenWithActiveAgreement](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getChildrenWithActiveAgreement)
Retrieve a Billing Item's active child billing items.

</div>

<div class="method-row">

#### [getDowngradeItems](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getDowngradeItems)
Retrieve for product items which have a downgrade path defined, this will return those product items.

</div>

<div class="method-row">

#### [getFilteredNextInvoiceChildren](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getFilteredNextInvoiceChildren)
Retrieve a Billing Item's associated child billing items, excluding some items with a $0.00 recurring fee.

</div>

<div class="method-row">

#### [getHourlyFlag](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getHourlyFlag)
Retrieve a flag that will reflect whether this billing item is billed on an hourly basis or not.

</div>

<div class="method-row">

#### [getInvoiceItem](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getInvoiceItem)
Retrieve invoice items associated with this billing item

</div>

<div class="method-row">

#### [getInvoiceItems](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getInvoiceItems)
Retrieve all invoice items associated with the billing item

</div>

<div class="method-row">

#### [getItem](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getItem)
Retrieve the entry in the SoftLayer product catalog that a billing item is based upon.

</div>

<div class="method-row">

#### [getLocation](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getLocation)
Retrieve the location of the billing item. Some billing items have physical properties such as the server itself. For items such as these, we provide location information.

</div>

<div class="method-row">

#### [getNextInvoiceChildren](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getNextInvoiceChildren)
Retrieve a Billing Item's child billing items and associated items'

</div>

<div class="method-row">

#### [getNextInvoiceTotalOneTimeAmount](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getNextInvoiceTotalOneTimeAmount)
Retrieve a Billing Item's total, including any child billing items if they exist.'

</div>

<div class="method-row">

#### [getNextInvoiceTotalOneTimeTaxAmount](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getNextInvoiceTotalOneTimeTaxAmount)
Retrieve a Billing Item's total, including any child billing items if they exist.'

</div>

<div class="method-row">

#### [getNextInvoiceTotalRecurringAmount](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getNextInvoiceTotalRecurringAmount)
Retrieve a Billing Item's total, including any child billing items and associated billing items if they exist.'

</div>

<div class="method-row">

#### [getNextInvoiceTotalRecurringTaxAmount](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getNextInvoiceTotalRecurringTaxAmount)
Retrieve this is deprecated and will always be zero. Because tax is calculated in real-time, previewing the next recurring invoice is pre-tax only.

</div>

<div class="method-row">

#### [getNonZeroNextInvoiceChildren](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getNonZeroNextInvoiceChildren)
Retrieve a Billing Item's associated child billing items, excluding ALL items with a $0.00 recurring fee.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getObject)
Retrieve a SoftLayer_Billing_Item_Virtual_DedicatedHost record.

</div>

<div class="method-row">

#### [getOrderItem](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getOrderItem)
Retrieve a billing item's original order item. Simply a reference to the original order from which this billing item was created.

</div>

<div class="method-row">

#### [getOriginalLocation](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getOriginalLocation)
Retrieve the original physical location for this billing item--may differ from current.

</div>

<div class="method-row">

#### [getPackage](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getPackage)
Retrieve the package under which this billing item was sold. A Package is the general grouping of products as seen on our order forms.

</div>

<div class="method-row">

#### [getParent](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getParent)
Retrieve a billing item's parent item. If a billing item has no parent item then this value is null.

</div>

<div class="method-row">

#### [getParentVirtualGuestBillingItem](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getParentVirtualGuestBillingItem)
Retrieve a billing item's parent item. If a billing item has no parent item then this value is null.

</div>

<div class="method-row">

#### [getPendingCancellationFlag](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getPendingCancellationFlag)
Retrieve this flag indicates whether a billing item is scheduled to be canceled or not.

</div>

<div class="method-row">

#### [getPendingOrderItem](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getPendingOrderItem)
Retrieve the new order item that will replace this billing item.

</div>

<div class="method-row">

#### [getProvisionTransaction](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getProvisionTransaction)
Retrieve provisioning transaction for this billing item

</div>

<div class="method-row">

#### [getResource](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getResource)
Retrieve the resource for a virtual dedicated host billing item.

</div>

<div class="method-row">

#### [getServiceBillingItemsByCategory](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getServiceBillingItemsByCategory)
Returns billing item in a given category code. Use this method to retrieve service billing items that you wish to cancel.

</div>

<div class="method-row">

#### [getSoftwareDescription](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getSoftwareDescription)
Retrieve a friendly description of software component

</div>

<div class="method-row">

#### [getUpgradeItem](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getUpgradeItem)
Retrieve billing items whose product item has an upgrade path defined in our system will return the next product item in the upgrade path.

</div>

<div class="method-row">

#### [getUpgradeItems](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/getUpgradeItems)
Retrieve billing items whose product item has an upgrade path defined in our system will return all the product items in the upgrade path.

</div>

<div class="method-row">

#### [removeAssociationId](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/removeAssociationId)
Remove an association from an orphan billing item.

</div>

<div class="method-row">

#### [setAssociationId](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/setAssociationId)
Set the associated billing item for an orphan billing item.

</div>

<div class="method-row">

#### [voidCancelService](/reference/services/SoftLayer_Billing_Item_Virtual_DedicatedHost/voidCancelService)
Void a service cancellation that was previously made.

</div>
</div>

</div>

