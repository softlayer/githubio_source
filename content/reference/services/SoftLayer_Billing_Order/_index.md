---
title: "SoftLayer_Billing_Order"
description: "The SoftLayer_Billing_Order service controls the orders that are created whenever a SoftLayer customer's places a purcha... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order"
---
# SoftLayer_Billing_Order
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Billing_Order' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Order' >Datatype</a></li>
    </ul>
</div>

## Description
The SoftLayer_Billing_Order service controls the orders that are created whenever a SoftLayer customer's places a purchase. Orders exist in several states. The ones of concern are: 
*'''QUOTE_PENDING''': Orders which have not been paid yet. Orders pending approval from a Softlayer customer.


Once an order is paid it moves from QUOTE_PENDING to PENDING_APPROVAL state. 

Orders are created with contact information duplicated from the [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) or by manual entry. We do this in order to maintain a history of an account's contact information as orders are generated. 

Query the [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) service to get a list of orders for your account. 


### associatedMethods

*  [SoftLayer_Account::getBalance](/reference/services/SoftLayer_Account/getBalance )
*  [SoftLayer_Account::getInvoices](/reference/services/SoftLayer_Account/getInvoices )



        
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

#### [approveModifiedOrder](/reference/services/SoftLayer_Billing_Order/approveModifiedOrder)
Approve the changes of a modified order

#### [getAccount](/reference/services/SoftLayer_Billing_Order/getAccount)
Retrieve the [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) to which an order belongs.

#### [getAllObjects](/reference/services/SoftLayer_Billing_Order/getAllObjects)
Get all billing orders for your account

#### [getBrand](/reference/services/SoftLayer_Billing_Order/getBrand)


#### [getCart](/reference/services/SoftLayer_Billing_Order/getCart)
Retrieve a cart is similar to a quote, except that it can be continually modified by the customer and does not have locked-in prices. Not all orders will have a cart associated with them. See [SoftLayer_Billing_Order_Cart]({{<ref "reference/datatypes/SoftLayer_Billing_Order_Cart">}}) for more information.

#### [getCoreRestrictedItems](/reference/services/SoftLayer_Billing_Order/getCoreRestrictedItems)
Retrieve the [SoftLayer_Billing_Order_Item]({{<ref "reference/datatypes/SoftLayer_Billing_Order_Item">}}) that are core restricted

#### [getCreditCardTransactions](/reference/services/SoftLayer_Billing_Order/getCreditCardTransactions)
Retrieve all credit card transactions associated with this order. If this order was not placed with a credit card, this will be empty.

#### [getExchangeRate](/reference/services/SoftLayer_Billing_Order/getExchangeRate)


#### [getInitialInvoice](/reference/services/SoftLayer_Billing_Order/getInitialInvoice)


#### [getItems](/reference/services/SoftLayer_Billing_Order/getItems)
Retrieve the SoftLayer_Billing_Order_items included in an order.

#### [getObject](/reference/services/SoftLayer_Billing_Order/getObject)
Retrieve a SoftLayer_Billing_Order record.

#### [getOrderApprovalDate](/reference/services/SoftLayer_Billing_Order/getOrderApprovalDate)


#### [getOrderNonServerMonthlyAmount](/reference/services/SoftLayer_Billing_Order/getOrderNonServerMonthlyAmount)
Retrieve an order's non-server items total monthly fee.

#### [getOrderServerMonthlyAmount](/reference/services/SoftLayer_Billing_Order/getOrderServerMonthlyAmount)
Retrieve an order's server items total monthly fee.

#### [getOrderStatuses](/reference/services/SoftLayer_Billing_Order/getOrderStatuses)
Get a list of SoftLayer_Container_Billing_Order_Status objects.

#### [getOrderTopLevelItems](/reference/services/SoftLayer_Billing_Order/getOrderTopLevelItems)
Retrieve an order's top level items. This normally includes the server line item and any non-server additional services such as NAS or ISCSI.

#### [getOrderTotalAmount](/reference/services/SoftLayer_Billing_Order/getOrderTotalAmount)
Retrieve this amount represents the order's initial charge including set up fee and taxes.

#### [getOrderTotalOneTime](/reference/services/SoftLayer_Billing_Order/getOrderTotalOneTime)
Retrieve an order's total one time amount summing all the set up fees, the labor fees and the one time fees. Taxes will be applied for non-tax-exempt. This amount represents the initial fees that will be charged.

#### [getOrderTotalOneTimeAmount](/reference/services/SoftLayer_Billing_Order/getOrderTotalOneTimeAmount)
Retrieve an order's total one time amount. This amount represents the initial fees before tax.

#### [getOrderTotalOneTimeTaxAmount](/reference/services/SoftLayer_Billing_Order/getOrderTotalOneTimeTaxAmount)
Retrieve an order's total one time tax amount. This amount represents the tax that will be applied to the total charge, if the SoftLayer_Account tied to a SoftLayer_Billing_Order is a taxable account.

#### [getOrderTotalRecurring](/reference/services/SoftLayer_Billing_Order/getOrderTotalRecurring)
Retrieve an order's total recurring amount. Taxes will be applied for non-tax-exempt. This amount represents the fees that will be charged on a recurring (usually monthly) basis.

#### [getOrderTotalRecurringAmount](/reference/services/SoftLayer_Billing_Order/getOrderTotalRecurringAmount)
Retrieve an order's total recurring amount. This amount represents the fees that will be charged on a recurring (usually monthly) basis.

#### [getOrderTotalRecurringTaxAmount](/reference/services/SoftLayer_Billing_Order/getOrderTotalRecurringTaxAmount)
Retrieve the total tax amount of the recurring fees, if the SoftLayer_Account tied to a SoftLayer_Billing_Order is a taxable account.

#### [getOrderTotalSetupAmount](/reference/services/SoftLayer_Billing_Order/getOrderTotalSetupAmount)
Retrieve an order's total setup fee.

#### [getOrderType](/reference/services/SoftLayer_Billing_Order/getOrderType)
Retrieve the type of an order. This lets you know where this order was generated from.

#### [getPaypalTransactions](/reference/services/SoftLayer_Billing_Order/getPaypalTransactions)
Retrieve all PayPal transactions associated with this order. If this order was not placed with PayPal, this will be empty.

#### [getPdf](/reference/services/SoftLayer_Billing_Order/getPdf)
Retrieve a PDF copy of a quote.

#### [getPdfFilename](/reference/services/SoftLayer_Billing_Order/getPdfFilename)
Retrieve the default name of the PDF

#### [getPresaleEvent](/reference/services/SoftLayer_Billing_Order/getPresaleEvent)


#### [getQuote](/reference/services/SoftLayer_Billing_Order/getQuote)
Retrieve the quote of an order. This quote holds information about its expiration date, creation date, name and status. This information is tied to an order having the status 'QUOTE'

#### [getRecalculatedOrderContainer](/reference/services/SoftLayer_Billing_Order/getRecalculatedOrderContainer)
Generate an [SoftLayer_Container_Product_Order]({{<ref "reference/datatypes/SoftLayer_Container_Product_Order">}}) from a billing order. 

#### [getReceipt](/reference/services/SoftLayer_Billing_Order/getReceipt)
Generate and return an order receipt.

#### [getReferralPartner](/reference/services/SoftLayer_Billing_Order/getReferralPartner)
Retrieve the Referral Partner who referred this order. (Only necessary for new customer orders)

#### [getUpgradeRequestFlag](/reference/services/SoftLayer_Billing_Order/getUpgradeRequestFlag)
Retrieve this flag indicates an order is an upgrade.

#### [getUserRecord](/reference/services/SoftLayer_Billing_Order/getUserRecord)
Retrieve the SoftLayer_User_Customer object tied to an order.

#### [isPendingEditApproval](/reference/services/SoftLayer_Billing_Order/isPendingEditApproval)
Determine if the existing order is pending edit approval

</div>

