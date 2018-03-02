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
Every individual item that a SoftLayer customer is billed for is recorded in the SoftLayer_Billing_Item data type. Billing items range from server chassis to hard drives to control panels, bandwidth quota upgrades and port upgrade charges. Softlayer [[SoftLayer_Billing_Invoice|invoices]] are generated from the cost of a customer's billing items. Billing items are copied from the product catalog as they're ordered by customers to create a reference between an account and the billable items they own. 

Billing items exist in a tree relationship. Items are associated with each other by parent/child relationships. Component items such as CPU's, RAM, and software each have a parent billing item for the server chassis they're associated with. Billing Items with a null parent item do not have an associated parent item. 



        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/cancelItem'> cancelItem</a> </span>
            <div class='views-field-body'>Cancel a service or resource.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/cancelService'> cancelService</a> </span>
            <div class='views-field-body'>Cancel a service or resource immediately. This does not include bare metal servers. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/cancelServiceOnAnniversaryDate'> cancelServiceOnAnniversaryDate</a> </span>
            <div class='views-field-body'>Cancel a service or resource on the next bill date</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the account that a billing item belongs to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getActiveAgreement'> getActiveAgreement</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getActiveAgreementFlag'> getActiveAgreementFlag</a> </span>
            <div class='views-field-body'>Retrieve a flag indicating that the billing item is under an active agreement.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getActiveAssociatedChildren'> getActiveAssociatedChildren</a> </span>
            <div class='views-field-body'>Retrieve a billing item's active associated child billing items. This includes "floating" items that are not necessarily child items of this billing item.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getActiveAssociatedGuestDiskBillingItems'> getActiveAssociatedGuestDiskBillingItems</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getActiveBundledItems'> getActiveBundledItems</a> </span>
            <div class='views-field-body'>Retrieve a Billing Item's active bundled billing items.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getActiveCancellationItem'> getActiveCancellationItem</a> </span>
            <div class='views-field-body'>Retrieve a service cancellation request item that corresponds to the billing item.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getActiveChildren'> getActiveChildren</a> </span>
            <div class='views-field-body'>Retrieve a Billing Item's active child billing items.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getActiveFlag'> getActiveFlag</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getActiveSparePoolAssociatedGuestDiskBillingItems'> getActiveSparePoolAssociatedGuestDiskBillingItems</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getActiveSparePoolBundledItems'> getActiveSparePoolBundledItems</a> </span>
            <div class='views-field-body'>Retrieve a Billing Item's spare pool bundled billing items.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getAssociatedBillingItem'> getAssociatedBillingItem</a> </span>
            <div class='views-field-body'>Retrieve a billing item's associated parent. This is to be used for billing items that are "floating", and therefore are not child items of any parent billing item. If it is desired to associate an item to another, populate this with the SoftLayer_Billing_Item ID of that associated parent item.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getAssociatedBillingItemHistory'> getAssociatedBillingItemHistory</a> </span>
            <div class='views-field-body'>Retrieve a history of billing items which a billing item has been associated with.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getAssociatedChildren'> getAssociatedChildren</a> </span>
            <div class='views-field-body'>Retrieve a Billing Item's associated child billing items. This includes "floating" items that are not necessarily child billing items of this billing item.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getAssociatedParent'> getAssociatedParent</a> </span>
            <div class='views-field-body'>Retrieve a billing item's associated parent billing item. This object will be the same as the parent billing item if parentId is set.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getAvailableMatchingVlans'> getAvailableMatchingVlans</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getBandwidthAllocation'> getBandwidthAllocation</a> </span>
            <div class='views-field-body'>Retrieve the bandwidth allocation for a billing item.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getBillableChildren'> getBillableChildren</a> </span>
            <div class='views-field-body'>Retrieve a billing item's recurring child items that have once been billed and are scheduled to be billed in the future.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getBundleItems'> getBundleItems</a> </span>
            <div class='views-field-body'>Retrieve a Billing Item's bundled billing items</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getBundledItems'> getBundledItems</a> </span>
            <div class='views-field-body'>Retrieve a Billing Item's bundled billing items'</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getCanceledChildren'> getCanceledChildren</a> </span>
            <div class='views-field-body'>Retrieve a Billing Item's active child billing items.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getCancellationReason'> getCancellationReason</a> </span>
            <div class='views-field-body'>Retrieve the billing item's cancellation reason.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getCancellationRequests'> getCancellationRequests</a> </span>
            <div class='views-field-body'>Retrieve this will return any cancellation requests that are associated with this billing item.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getCategory'> getCategory</a> </span>
            <div class='views-field-body'>Retrieve the item category to which the billing item's item belongs. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getChildren'> getChildren</a> </span>
            <div class='views-field-body'>Retrieve a Billing Item's child billing items'</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getChildrenWithActiveAgreement'> getChildrenWithActiveAgreement</a> </span>
            <div class='views-field-body'>Retrieve a Billing Item's active child billing items.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getDowngradeItems'> getDowngradeItems</a> </span>
            <div class='views-field-body'>Retrieve for product items which have a downgrade path defined, this will return those product items.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getFilteredNextInvoiceChildren'> getFilteredNextInvoiceChildren</a> </span>
            <div class='views-field-body'>Retrieve a Billing Item's associated child billing items, excluding some items with a $0.00 recurring fee.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getHourlyFlag'> getHourlyFlag</a> </span>
            <div class='views-field-body'>Retrieve a flag that will reflect whether this billing item is billed on an hourly basis or not.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getInvoiceItem'> getInvoiceItem</a> </span>
            <div class='views-field-body'>Retrieve invoice items associated with this billing item</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getInvoiceItems'> getInvoiceItems</a> </span>
            <div class='views-field-body'>Retrieve all invoice items associated with the billing item</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getItem'> getItem</a> </span>
            <div class='views-field-body'>Retrieve the entry in the SoftLayer product catalog that a billing item is based upon.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getLocation'> getLocation</a> </span>
            <div class='views-field-body'>Retrieve the location of the billing item. Some billing items have physical properties such as the server itself. For items such as these, we provide location information.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getNextInvoiceChildren'> getNextInvoiceChildren</a> </span>
            <div class='views-field-body'>Retrieve a Billing Item's child billing items and associated items'</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getNextInvoiceTotalOneTimeAmount'> getNextInvoiceTotalOneTimeAmount</a> </span>
            <div class='views-field-body'>Retrieve a Billing Item's total, including any child billing items if they exist.'</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getNextInvoiceTotalOneTimeTaxAmount'> getNextInvoiceTotalOneTimeTaxAmount</a> </span>
            <div class='views-field-body'>Retrieve a Billing Item's total, including any child billing items if they exist.'</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getNextInvoiceTotalRecurringAmount'> getNextInvoiceTotalRecurringAmount</a> </span>
            <div class='views-field-body'>Retrieve a Billing Item's total, including any child billing items and associated billing items if they exist.'</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getNextInvoiceTotalRecurringTaxAmount'> getNextInvoiceTotalRecurringTaxAmount</a> </span>
            <div class='views-field-body'>Retrieve this is deprecated and will always be zero. Because tax is calculated in real-time, previewing the next recurring invoice is pre-tax only.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getNonZeroNextInvoiceChildren'> getNonZeroNextInvoiceChildren</a> </span>
            <div class='views-field-body'>Retrieve a Billing Item's associated child billing items, excluding ALL items with a $0.00 recurring fee.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Billing_Item record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getOrderItem'> getOrderItem</a> </span>
            <div class='views-field-body'>Retrieve a billing item's original order item. Simply a reference to the original order from which this billing item was created.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getOriginalLocation'> getOriginalLocation</a> </span>
            <div class='views-field-body'>Retrieve the original physical location for this billing item--may differ from current.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getPackage'> getPackage</a> </span>
            <div class='views-field-body'>Retrieve the package under which this billing item was sold. A Package is the general grouping of products as seen on our order forms.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getParent'> getParent</a> </span>
            <div class='views-field-body'>Retrieve a billing item's parent item. If a billing item has no parent item then this value is null.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getParentVirtualGuestBillingItem'> getParentVirtualGuestBillingItem</a> </span>
            <div class='views-field-body'>Retrieve a billing item's parent item. If a billing item has no parent item then this value is null.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getPendingCancellationFlag'> getPendingCancellationFlag</a> </span>
            <div class='views-field-body'>Retrieve this flag indicates whether a billing item is scheduled to be canceled or not.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getPendingOrderItem'> getPendingOrderItem</a> </span>
            <div class='views-field-body'>Retrieve the new order item that will replace this billing item.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getProvisionTransaction'> getProvisionTransaction</a> </span>
            <div class='views-field-body'>Retrieve provisioning transaction for this billing item</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getServiceBillingItemsByCategory'> getServiceBillingItemsByCategory</a> </span>
            <div class='views-field-body'>Returns billing item in a given category code. Use this method to retrieve service billing items that you wish to cancel.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getSoftwareDescription'> getSoftwareDescription</a> </span>
            <div class='views-field-body'>Retrieve a friendly description of software component</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getUpgradeItem'> getUpgradeItem</a> </span>
            <div class='views-field-body'>Retrieve billing items whose product item has an upgrade path defined in our system will return the next product item in the upgrade path.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/getUpgradeItems'> getUpgradeItems</a> </span>
            <div class='views-field-body'>Retrieve billing items whose product item has an upgrade path defined in our system will return all the product items in the upgrade path.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/removeAssociationId'> removeAssociationId</a> </span>
            <div class='views-field-body'>Remove an association from an orphan billing item.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/setAssociationId'> setAssociationId</a> </span>
            <div class='views-field-body'>Set the associated billing item for an orphan billing item.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Item/voidCancelService'> voidCancelService</a> </span>
            <div class='views-field-body'>Void a service cancellation that was previously made.</div>
        </div>
        </div>
</div>

