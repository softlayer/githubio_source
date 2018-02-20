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

Orders are created with contact information duplicated from the [[SoftLayer_Account (type)|SoftLayer_Account data type]] or by manual entry. We do this in order to maintain a history of an account's contact information as orders are generated. 

Query the [[SoftLayer_Account]] service to get a list of orders for your account. 
### associatedMethods

        SoftLayer_Account::getBalance1        SoftLayer_Account::getInvoices1        
        
        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/approveModifiedOrder'> approveModifiedOrder</a> </span>
            <div class='views-field-body'>Approve the changes of a modified order</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the [[SoftLayer_Account|account]] to which an order belongs.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getAllObjects'> getAllObjects</a> </span>
            <div class='views-field-body'>Get all billing orders for your account</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getBrand'> getBrand</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getCart'> getCart</a> </span>
            <div class='views-field-body'>Retrieve a cart is similar to a quote, except that it can be continually modified by the customer and does not have locked-in prices. Not all orders will have a cart associated with them. See [[SoftLayer_Billing_Order_Cart]] for more information.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getCoreRestrictedItems'> getCoreRestrictedItems</a> </span>
            <div class='views-field-body'>Retrieve the [[SoftLayer_Billing_Order_Item (type)|order items]] that are core restricted</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getCreditCardTransactions'> getCreditCardTransactions</a> </span>
            <div class='views-field-body'>Retrieve all credit card transactions associated with this order. If this order was not placed with a credit card, this will be empty.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getExchangeRate'> getExchangeRate</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getInitialInvoice'> getInitialInvoice</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getItems'> getItems</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Billing_Order_items included in an order.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Billing_Order record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getOrderApprovalDate'> getOrderApprovalDate</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getOrderNonServerMonthlyAmount'> getOrderNonServerMonthlyAmount</a> </span>
            <div class='views-field-body'>Retrieve an order's non-server items total monthly fee.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getOrderServerMonthlyAmount'> getOrderServerMonthlyAmount</a> </span>
            <div class='views-field-body'>Retrieve an order's server items total monthly fee.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getOrderStatuses'> getOrderStatuses</a> </span>
            <div class='views-field-body'>Get a list of SoftLayer_Container_Billing_Order_Status objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getOrderTopLevelItems'> getOrderTopLevelItems</a> </span>
            <div class='views-field-body'>Retrieve an order's top level items. This normally includes the server line item and any non-server additional services such as NAS or ISCSI.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getOrderTotalAmount'> getOrderTotalAmount</a> </span>
            <div class='views-field-body'>Retrieve this amount represents the order's initial charge including set up fee and taxes.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getOrderTotalOneTime'> getOrderTotalOneTime</a> </span>
            <div class='views-field-body'>Retrieve an order's total one time amount summing all the set up fees, the labor fees and the one time fees. Taxes will be applied for non-tax-exempt. This amount represents the initial fees that will be charged.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getOrderTotalOneTimeAmount'> getOrderTotalOneTimeAmount</a> </span>
            <div class='views-field-body'>Retrieve an order's total one time amount. This amount represents the initial fees before tax.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getOrderTotalOneTimeTaxAmount'> getOrderTotalOneTimeTaxAmount</a> </span>
            <div class='views-field-body'>Retrieve an order's total one time tax amount. This amount represents the tax that will be applied to the total charge, if the SoftLayer_Account tied to a SoftLayer_Billing_Order is a taxable account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getOrderTotalRecurring'> getOrderTotalRecurring</a> </span>
            <div class='views-field-body'>Retrieve an order's total recurring amount. Taxes will be applied for non-tax-exempt. This amount represents the fees that will be charged on a recurring (usually monthly) basis.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getOrderTotalRecurringAmount'> getOrderTotalRecurringAmount</a> </span>
            <div class='views-field-body'>Retrieve an order's total recurring amount. This amount represents the fees that will be charged on a recurring (usually monthly) basis.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getOrderTotalRecurringTaxAmount'> getOrderTotalRecurringTaxAmount</a> </span>
            <div class='views-field-body'>Retrieve the total tax amount of the recurring fees, if the SoftLayer_Account tied to a SoftLayer_Billing_Order is a taxable account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getOrderTotalSetupAmount'> getOrderTotalSetupAmount</a> </span>
            <div class='views-field-body'>Retrieve an order's total setup fee.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getOrderType'> getOrderType</a> </span>
            <div class='views-field-body'>Retrieve the type of an order. This lets you know where this order was generated from.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getPaypalTransactions'> getPaypalTransactions</a> </span>
            <div class='views-field-body'>Retrieve all PayPal transactions associated with this order. If this order was not placed with PayPal, this will be empty.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getPdf'> getPdf</a> </span>
            <div class='views-field-body'>Retrieve a PDF copy of a quote.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getPdfFilename'> getPdfFilename</a> </span>
            <div class='views-field-body'>Retrieve the default name of the PDF</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getPresaleEvent'> getPresaleEvent</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getQuote'> getQuote</a> </span>
            <div class='views-field-body'>Retrieve the quote of an order. This quote holds information about its expiration date, creation date, name and status. This information is tied to an order having the status 'QUOTE'</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getRecalculatedOrderContainer'> getRecalculatedOrderContainer</a> </span>
            <div class='views-field-body'>Generate an [[SoftLayer_Container_Product_Order|order container]] from a billing order. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getReceipt'> getReceipt</a> </span>
            <div class='views-field-body'>Generate and return an order receipt.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getReferralPartner'> getReferralPartner</a> </span>
            <div class='views-field-body'>Retrieve the Referral Partner who referred this order. (Only necessary for new customer orders)</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getUpgradeRequestFlag'> getUpgradeRequestFlag</a> </span>
            <div class='views-field-body'>Retrieve this flag indicates an order is an upgrade.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/getUserRecord'> getUserRecord</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_User_Customer object tied to an order.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order/isPendingEditApproval'> isPendingEditApproval</a> </span>
            <div class='views-field-body'>Determine if the existing order is pending edit approval</div>
        </div>
        </div>
</div>

