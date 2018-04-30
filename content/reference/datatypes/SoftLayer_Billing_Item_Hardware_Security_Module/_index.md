---
title: "SoftLayer_Billing_Item_Hardware_Security_Module"
description: "The SoftLayer_Billing_Item_Hardware_Security_Module data type contains general information relating to a single SoftLaye... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Hardware_Security_Module"
---

# SoftLayer_Billing_Item_Hardware_Security_Module
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Item_Hardware_Security_Module' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Billing_Item_Hardware_Security_Module data type contains general information relating to a single SoftLayer billing item for a hardware security module. 





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
                <a href="#allowCancellationFlag" name=allowCancellationFlag>allowCancellationFlag</a>
            </span>
            <div class='views-field-body'>Flag to check if a billing item can be cancelled. 1 = yes. 0 = no.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#associatedBillingItemId" name=associatedBillingItemId>associatedBillingItemId</a>
            </span>
            <div class='views-field-body'>This is sometimes populated for orphan billing items that are not attached to servers. Billing items like secondary portable IP addresses fit into this category. A user may set an association by calling [[SoftLayer_Billing_Item::setAssociationId]]. This will cause this orphan item to appear under its associated server billing item on future invoices. You may only attach orphaned billing items to server billing items without cancellation dates set.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#cancellationDate" name=cancellationDate>cancellationDate</a>
            </span>
            <div class='views-field-body'>A billing item's cancellation date. A billing item with a cancellation date in the past is not charged on your SoftLayer invoice. Cancellation dates in the future indicate the current billing item is active, but will be cancelled and not charged for in the future. A billing item with a null cancellation date is also considered an active billing item and is charged once every billing cycle.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#categoryCode" name=categoryCode>categoryCode</a>
            </span>
            <div class='views-field-body'>The category code of this billing item. It is used to tell us the difference between a primary disk and a secondary disk, for instance. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>The date the billing item was created. You can see this date on the invoice. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#currentHourlyCharge" name=currentHourlyCharge>currentHourlyCharge</a>
            </span>
            <div class='views-field-body'>This is the total charge for the billing item for this billing item. It is calculated based on the hourlyRecurringFee * hoursUsed.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#cycleStartDate" name=cycleStartDate>cycleStartDate</a>
            </span>
            <div class='views-field-body'>The last time this billing item was charged. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#description" name=description>description</a>
            </span>
            <div class='views-field-body'>A brief description of a billing item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#domainName" name=domainName>domainName</a>
            </span>
            <div class='views-field-body'>The domain name is provided for server billing items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hostName" name=hostName>hostName</a>
            </span>
            <div class='views-field-body'>The hostname is provided for server billing items </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hourlyRecurringFee" name=hourlyRecurringFee>hourlyRecurringFee</a>
            </span>
            <div class='views-field-body'>The amount of money charged per hour for a billing item, if applicable. hourlyRecurringFee is measured in US Dollars ($USD).  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hoursUsed" name=hoursUsed>hoursUsed</a>
            </span>
            <div class='views-field-body'>This is the number of hours the hourly billing item has been in use this billing period. For virtual servers, this means running, paused or stopped.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The unique identifier for this billing item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#laborFee" name=laborFee>laborFee</a>
            </span>
            <div class='views-field-body'>The labor fee, if any. This is a one time charge. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#laborFeeTaxRate" name=laborFeeTaxRate>laborFeeTaxRate</a>
            </span>
            <div class='views-field-body'>The rate at which labor fees are taxed if you are a taxable customer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#lastBillDate" name=lastBillDate>lastBillDate</a>
            </span>
            <div class='views-field-body'>The last time this billing item was charged. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>The date that a billing item was last modified. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#nextBillDate" name=nextBillDate>nextBillDate</a>
            </span>
            <div class='views-field-body'>The date on which your account will be charged for this billing item.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notes" name=notes>notes</a>
            </span>
            <div class='views-field-body'>Extra information provided to help you identify this billing item. This is often a username or something to help identify items that customers have more than one of. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#oneTimeFee" name=oneTimeFee>oneTimeFee</a>
            </span>
            <div class='views-field-body'>The amount of money charged as a one-time charge for a billing item, if applicable. oneTimeFee is measured in US Dollars ($USD).  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#oneTimeFeeTaxRate" name=oneTimeFeeTaxRate>oneTimeFeeTaxRate</a>
            </span>
            <div class='views-field-body'>The rate at which one time fees are taxed if you are a taxable customer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#orderItemId" name=orderItemId>orderItemId</a>
            </span>
            <div class='views-field-body'>the SoftLayer_Billing_Order_Item ID. This is a reference to the original order item from which this billing item was originally created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#parentId" name=parentId>parentId</a>
            </span>
            <div class='views-field-body'>The unique identifier of the parent of this billing item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#recurringFee" name=recurringFee>recurringFee</a>
            </span>
            <div class='views-field-body'>The amount of money charged per month for a billing item, if applicable. recurringFee is measured in US Dollars ($USD).  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#recurringFeeTaxRate" name=recurringFeeTaxRate>recurringFeeTaxRate</a>
            </span>
            <div class='views-field-body'>The rate at which recurring fees are taxed if you are a taxable customer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#recurringMonths" name=recurringMonths>recurringMonths</a>
            </span>
            <div class='views-field-body'>The number of months in which the recurring fees will be incurred. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#resourceTableId" name=resourceTableId>resourceTableId</a>
            </span>
            <div class='views-field-body'>The resource (unique identifier) for a server billing item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#serviceProviderId" name=serviceProviderId>serviceProviderId</a>
            </span>
            <div class='views-field-body'>This is the service provider for this billing item.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#setupFee" name=setupFee>setupFee</a>
            </span>
            <div class='views-field-body'>The setup fee, if any. This is a one time charge. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#setupFeeTaxRate" name=setupFeeTaxRate>setupFeeTaxRate</a>
            </span>
            <div class='views-field-body'>The rate at which setup fees are taxed if you are a taxable customer. </div>
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
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'>The account that a billing item belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activeAgreement" name=activeAgreement>activeAgreement</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account_Agreement'>SoftLayer_Account_Agreement </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activeAgreementFlag" name=activeAgreementFlag>activeAgreementFlag</a>
            </span>
            <div class='views-field-body'>A flag indicating that the billing item is under an active agreement. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account_Agreement'>SoftLayer_Account_Agreement </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activeAssociatedChildren" name=activeAssociatedChildren>activeAssociatedChildren</a>
            </span>
            <div class='views-field-body'>A billing item's active associated child billing items. This includes "floating" items that are not necessarily child items of this billing item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activeAssociatedGuestDiskBillingItems" name=activeAssociatedGuestDiskBillingItems>activeAssociatedGuestDiskBillingItems</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activeBundledItems" name=activeBundledItems>activeBundledItems</a>
            </span>
            <div class='views-field-body'>A Billing Item's active bundled billing items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activeCancellationItem" name=activeCancellationItem>activeCancellationItem</a>
            </span>
            <div class='views-field-body'>A service cancellation request item that corresponds to the billing item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request_Item'>SoftLayer_Billing_Item_Cancellation_Request_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activeChildren" name=activeChildren>activeChildren</a>
            </span>
            <div class='views-field-body'>A Billing Item's active child billing items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activeFlag" name=activeFlag>activeFlag</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activeSparePoolAssociatedGuestDiskBillingItems" name=activeSparePoolAssociatedGuestDiskBillingItems>activeSparePoolAssociatedGuestDiskBillingItems</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activeSparePoolBundledItems" name=activeSparePoolBundledItems>activeSparePoolBundledItems</a>
            </span>
            <div class='views-field-body'>A Billing Item's spare pool bundled billing items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#associatedBillingItem" name=associatedBillingItem>associatedBillingItem</a>
            </span>
            <div class='views-field-body'>A billing item's associated parent. This is to be used for billing items that are "floating", and therefore are not child items of any parent billing item. If it is desired to associate an item to another, populate this with the SoftLayer_Billing_Item ID of that associated parent item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#associatedBillingItemHistory" name=associatedBillingItemHistory>associatedBillingItemHistory</a>
            </span>
            <div class='views-field-body'>A history of billing items which a billing item has been associated with. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item_Association_History'>SoftLayer_Billing_Item_Association_History[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#associatedChildren" name=associatedChildren>associatedChildren</a>
            </span>
            <div class='views-field-body'>A Billing Item's associated child billing items. This includes "floating" items that are not necessarily child billing items of this billing item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#associatedParent" name=associatedParent>associatedParent</a>
            </span>
            <div class='views-field-body'>A billing item's associated parent billing item. This object will be the same as the parent billing item if parentId is set. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#availableMatchingVlans" name=availableMatchingVlans>availableMatchingVlans</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#bandwidthAllocation" name=bandwidthAllocation>bandwidthAllocation</a>
            </span>
            <div class='views-field-body'>The bandwidth allocation for a billing item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allocation'>SoftLayer_Network_Bandwidth_Version1_Allocation </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billableChildren" name=billableChildren>billableChildren</a>
            </span>
            <div class='views-field-body'>A billing item's recurring child items that have once been billed and are scheduled to be billed in the future. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCycleBandwidthUsage" name=billingCycleBandwidthUsage>billingCycleBandwidthUsage</a>
            </span>
            <div class='views-field-body'>The raw bandwidth usage data for the current billing cycle. One object will be returned for each network this server is attached to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePrivateBandwidthUsage" name=billingCyclePrivateBandwidthUsage>billingCyclePrivateBandwidthUsage</a>
            </span>
            <div class='views-field-body'>The raw private bandwidth usage data for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePrivateUsageIn" name=billingCyclePrivateUsageIn>billingCyclePrivateUsageIn</a>
            </span>
            <div class='views-field-body'>The total private inbound bandwidth for this hardware for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePrivateUsageOut" name=billingCyclePrivateUsageOut>billingCyclePrivateUsageOut</a>
            </span>
            <div class='views-field-body'>The total private outbound bandwidth for this hardware for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePrivateUsageTotal" name=billingCyclePrivateUsageTotal>billingCyclePrivateUsageTotal</a>
            </span>
            <div class='views-field-body'>The total private bandwidth for this hardware for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsigned integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePublicBandwidthUsage" name=billingCyclePublicBandwidthUsage>billingCyclePublicBandwidthUsage</a>
            </span>
            <div class='views-field-body'>The raw public bandwidth usage data for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePublicUsageIn" name=billingCyclePublicUsageIn>billingCyclePublicUsageIn</a>
            </span>
            <div class='views-field-body'>The total public inbound bandwidth for this hardware for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePublicUsageOut" name=billingCyclePublicUsageOut>billingCyclePublicUsageOut</a>
            </span>
            <div class='views-field-body'>The total public outbound bandwidth for this hardware for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>decimal</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePublicUsageTotal" name=billingCyclePublicUsageTotal>billingCyclePublicUsageTotal</a>
            </span>
            <div class='views-field-body'>The total public bandwidth for this hardware for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsigned integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#bundleItems" name=bundleItems>bundleItems</a>
            </span>
            <div class='views-field-body'>A Billing Item's bundled billing items </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Bundles'>SoftLayer_Product_Item_Bundles[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#bundledItems" name=bundledItems>bundledItems</a>
            </span>
            <div class='views-field-body'>A Billing Item's bundled billing items' </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#canceledChildren" name=canceledChildren>canceledChildren</a>
            </span>
            <div class='views-field-body'>A Billing Item's active child billing items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#cancellationReason" name=cancellationReason>cancellationReason</a>
            </span>
            <div class='views-field-body'>The billing item's cancellation reason. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Reason'>SoftLayer_Billing_Item_Cancellation_Reason </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#cancellationRequests" name=cancellationRequests>cancellationRequests</a>
            </span>
            <div class='views-field-body'>This will return any cancellation requests that are associated with this billing item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request'>SoftLayer_Billing_Item_Cancellation_Request[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#category" name=category>category</a>
            </span>
            <div class='views-field-body'>The item category to which the billing item's item belongs.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#children" name=children>children</a>
            </span>
            <div class='views-field-body'>A Billing Item's child billing items' </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#childrenWithActiveAgreement" name=childrenWithActiveAgreement>childrenWithActiveAgreement</a>
            </span>
            <div class='views-field-body'>A Billing Item's active child billing items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#downgradeItems" name=downgradeItems>downgradeItems</a>
            </span>
            <div class='views-field-body'>For product items which have a downgrade path defined, this will return those product items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#filteredNextInvoiceChildren" name=filteredNextInvoiceChildren>filteredNextInvoiceChildren</a>
            </span>
            <div class='views-field-body'>A Billing Item's associated child billing items, excluding some items with a $0.00 recurring fee. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hourlyFlag" name=hourlyFlag>hourlyFlag</a>
            </span>
            <div class='views-field-body'>A flag that will reflect whether this billing item is billed on an hourly basis or not. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoiceItem" name=invoiceItem>invoiceItem</a>
            </span>
            <div class='views-field-body'>Invoice items associated with this billing item </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoiceItems" name=invoiceItems>invoiceItems</a>
            </span>
            <div class='views-field-body'>All invoice items associated with the billing item </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Invoice_Item'>SoftLayer_Billing_Invoice_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#item" name=item>item</a>
            </span>
            <div class='views-field-body'>The entry in the SoftLayer product catalog that a billing item is based upon. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#location" name=location>location</a>
            </span>
            <div class='views-field-body'>The location of the billing item. Some billing items have physical properties such as the server itself. For items such as these, we provide location information. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#lockboxNetworkStorage" name=lockboxNetworkStorage>lockboxNetworkStorage</a>
            </span>
            <div class='views-field-body'>A lockbox account associated with a server. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item_Network_Storage'>SoftLayer_Billing_Item_Network_Storage </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#monitoringBillingItems" name=monitoringBillingItems>monitoringBillingItems</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#nextInvoiceChildren" name=nextInvoiceChildren>nextInvoiceChildren</a>
            </span>
            <div class='views-field-body'>A Billing Item's child billing items and associated items' </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#nextInvoiceTotalOneTimeAmount" name=nextInvoiceTotalOneTimeAmount>nextInvoiceTotalOneTimeAmount</a>
            </span>
            <div class='views-field-body'>A Billing Item's total, including any child billing items if they exist.' </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#nextInvoiceTotalOneTimeTaxAmount" name=nextInvoiceTotalOneTimeTaxAmount>nextInvoiceTotalOneTimeTaxAmount</a>
            </span>
            <div class='views-field-body'>A Billing Item's total, including any child billing items if they exist.' </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#nextInvoiceTotalRecurringAmount" name=nextInvoiceTotalRecurringAmount>nextInvoiceTotalRecurringAmount</a>
            </span>
            <div class='views-field-body'>A Billing Item's total, including any child billing items and associated billing items if they exist.' </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#nextInvoiceTotalRecurringTaxAmount" name=nextInvoiceTotalRecurringTaxAmount>nextInvoiceTotalRecurringTaxAmount</a>
            </span>
            <div class='views-field-body'>This is deprecated and will always be zero. Because tax is calculated in real-time, previewing the next recurring invoice is pre-tax only. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#nonZeroNextInvoiceChildren" name=nonZeroNextInvoiceChildren>nonZeroNextInvoiceChildren</a>
            </span>
            <div class='views-field-body'>A Billing Item's associated child billing items, excluding ALL items with a $0.00 recurring fee. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#orderItem" name=orderItem>orderItem</a>
            </span>
            <div class='views-field-body'>A billing item's original order item. Simply a reference to the original order from which this billing item was created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#originalLocation" name=originalLocation>originalLocation</a>
            </span>
            <div class='views-field-body'>The original physical location for this billing item--may differ from current. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#package" name=package>package</a>
            </span>
            <div class='views-field-body'>The package under which this billing item was sold. A Package is the general grouping of products as seen on our order forms. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#parent" name=parent>parent</a>
            </span>
            <div class='views-field-body'>A billing item's parent item. If a billing item has no parent item then this value is null. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#parentVirtualGuestBillingItem" name=parentVirtualGuestBillingItem>parentVirtualGuestBillingItem</a>
            </span>
            <div class='views-field-body'>A billing item's parent item. If a billing item has no parent item then this value is null. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item_Virtual_Guest'>SoftLayer_Billing_Item_Virtual_Guest </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#pendingCancellationFlag" name=pendingCancellationFlag>pendingCancellationFlag</a>
            </span>
            <div class='views-field-body'>This flag indicates whether a billing item is scheduled to be canceled or not. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#pendingOrderItem" name=pendingOrderItem>pendingOrderItem</a>
            </span>
            <div class='views-field-body'>The new order item that will replace this billing item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#provisionTransaction" name=provisionTransaction>provisionTransaction</a>
            </span>
            <div class='views-field-body'>Provisioning transaction for this billing item </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#resource" name=resource>resource</a>
            </span>
            <div class='views-field-body'>The resource for a hardware security module billing item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Hardware_SecurityModule'>SoftLayer_Hardware_SecurityModule </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#softwareDescription" name=softwareDescription>softwareDescription</a>
            </span>
            <div class='views-field-body'>A friendly description of software component </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#upgradeItem" name=upgradeItem>upgradeItem</a>
            </span>
            <div class='views-field-body'>Billing items whose product item has an upgrade path defined in our system will return the next product item in the upgrade path. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#upgradeItems" name=upgradeItems>upgradeItems</a>
            </span>
            <div class='views-field-body'>Billing items whose product item has an upgrade path defined in our system will return all the product items in the upgrade path. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activeAssociatedChildrenCount" name=activeAssociatedChildrenCount>activeAssociatedChildrenCount</a>
            </span>
            <div class='views-field-body'>A count of a billing item's active associated child billing items. This includes "floating" items that are not necessarily child items of this billing item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activeAssociatedGuestDiskBillingItemCount" name=activeAssociatedGuestDiskBillingItemCount>activeAssociatedGuestDiskBillingItemCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activeBundledItemCount" name=activeBundledItemCount>activeBundledItemCount</a>
            </span>
            <div class='views-field-body'>A count of a Billing Item's active bundled billing items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activeChildrenCount" name=activeChildrenCount>activeChildrenCount</a>
            </span>
            <div class='views-field-body'>A count of a Billing Item's active child billing items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activeSparePoolAssociatedGuestDiskBillingItemCount" name=activeSparePoolAssociatedGuestDiskBillingItemCount>activeSparePoolAssociatedGuestDiskBillingItemCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activeSparePoolBundledItemCount" name=activeSparePoolBundledItemCount>activeSparePoolBundledItemCount</a>
            </span>
            <div class='views-field-body'>A count of a Billing Item's spare pool bundled billing items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#associatedBillingItemHistoryCount" name=associatedBillingItemHistoryCount>associatedBillingItemHistoryCount</a>
            </span>
            <div class='views-field-body'>A count of a history of billing items which a billing item has been associated with. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#associatedChildrenCount" name=associatedChildrenCount>associatedChildrenCount</a>
            </span>
            <div class='views-field-body'>A count of a Billing Item's associated child billing items. This includes "floating" items that are not necessarily child billing items of this billing item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#associatedParentCount" name=associatedParentCount>associatedParentCount</a>
            </span>
            <div class='views-field-body'>A count of a billing item's associated parent billing item. This object will be the same as the parent billing item if parentId is set. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#availableMatchingVlanCount" name=availableMatchingVlanCount>availableMatchingVlanCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billableChildrenCount" name=billableChildrenCount>billableChildrenCount</a>
            </span>
            <div class='views-field-body'>A count of a billing item's recurring child items that have once been billed and are scheduled to be billed in the future. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCycleBandwidthUsageCount" name=billingCycleBandwidthUsageCount>billingCycleBandwidthUsageCount</a>
            </span>
            <div class='views-field-body'>A count of the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this server is attached to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePrivateBandwidthUsageCount" name=billingCyclePrivateBandwidthUsageCount>billingCyclePrivateBandwidthUsageCount</a>
            </span>
            <div class='views-field-body'>A count of the raw private bandwidth usage data for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCyclePublicBandwidthUsageCount" name=billingCyclePublicBandwidthUsageCount>billingCyclePublicBandwidthUsageCount</a>
            </span>
            <div class='views-field-body'>A count of the raw public bandwidth usage data for the current billing cycle. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#bundleItemCount" name=bundleItemCount>bundleItemCount</a>
            </span>
            <div class='views-field-body'>A count of a Billing Item's bundled billing items </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#bundledItemCount" name=bundledItemCount>bundledItemCount</a>
            </span>
            <div class='views-field-body'>A count of a Billing Item's bundled billing items' </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#canceledChildrenCount" name=canceledChildrenCount>canceledChildrenCount</a>
            </span>
            <div class='views-field-body'>A count of a Billing Item's active child billing items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#cancellationRequestCount" name=cancellationRequestCount>cancellationRequestCount</a>
            </span>
            <div class='views-field-body'>A count of this will return any cancellation requests that are associated with this billing item. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#childrenCount" name=childrenCount>childrenCount</a>
            </span>
            <div class='views-field-body'>A count of a Billing Item's child billing items' </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#childrenWithActiveAgreementCount" name=childrenWithActiveAgreementCount>childrenWithActiveAgreementCount</a>
            </span>
            <div class='views-field-body'>A count of a Billing Item's active child billing items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#downgradeItemCount" name=downgradeItemCount>downgradeItemCount</a>
            </span>
            <div class='views-field-body'>A count of for product items which have a downgrade path defined, this will return those product items. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#filteredNextInvoiceChildrenCount" name=filteredNextInvoiceChildrenCount>filteredNextInvoiceChildrenCount</a>
            </span>
            <div class='views-field-body'>A count of a Billing Item's associated child billing items, excluding some items with a $0.00 recurring fee. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#invoiceItemCount" name=invoiceItemCount>invoiceItemCount</a>
            </span>
            <div class='views-field-body'>A count of all invoice items associated with the billing item </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#monitoringBillingItemCount" name=monitoringBillingItemCount>monitoringBillingItemCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#nextInvoiceChildrenCount" name=nextInvoiceChildrenCount>nextInvoiceChildrenCount</a>
            </span>
            <div class='views-field-body'>A count of a Billing Item's child billing items and associated items' </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#nonZeroNextInvoiceChildrenCount" name=nonZeroNextInvoiceChildrenCount>nonZeroNextInvoiceChildrenCount</a>
            </span>
            <div class='views-field-body'>A count of a Billing Item's associated child billing items, excluding ALL items with a $0.00 recurring fee. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#upgradeItemCount" name=upgradeItemCount>upgradeItemCount</a>
            </span>
            <div class='views-field-body'>A count of billing items whose product item has an upgrade path defined in our system will return all the product items in the upgrade path. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


