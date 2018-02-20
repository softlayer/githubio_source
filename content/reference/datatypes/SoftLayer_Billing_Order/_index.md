---
title: "SoftLayer_Billing_Order"
description: "The SoftLayer_Billing_Order data type contains general information relating to an individual order applied to a SoftLaye... "
layout: "datatype"
tags:
    - "datatype"
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
The SoftLayer_Billing_Order data type contains general information relating to an individual order applied to a SoftLayer customer account or to a new customer. Personal information in this type such as names, addresses, and phone numbers are taken from the account's contact information at the time the order is generated for existing SoftLayer customer. 
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
            <span class='views-field-title'><a href="#accountId" name=accountId>accountId</a></span>
            <div class='views-field-body'>The account ID to which an order belongs. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The point in time at which a billing item was created. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>* </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#impersonatingUserRecordId" name=impersonatingUserRecordId>impersonatingUserRecordId</a></span>
            <div class='views-field-body'>The SoftLayer_User_Customer id of the portal or API user who impersonated the user which submitted an order. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>The last time an order was updated. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderQuoteId" name=orderQuoteId>orderQuoteId</a></span>
            <div class='views-field-body'>The SoftLayer_Billing_Order_Quote id of the quote's user who finalized an order. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderTypeId" name=orderTypeId>orderTypeId</a></span>
            <div class='views-field-body'>The SoftLayer_Billing_Order_Type id of the order. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#presaleEventId" name=presaleEventId>presaleEventId</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#privateCloudOrderFlag" name=privateCloudOrderFlag>privateCloudOrderFlag</a></span>
            <div class='views-field-body'>Flag indicating a private cloud solution order (Deprecated) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#status" name=status>status</a></span>
            <div class='views-field-body'>Purchaser current status e.i. Approved, Pending_Approval </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#userRecordId" name=userRecordId>userRecordId</a></span>
            <div class='views-field-body'>The SoftLayer_User_Customer id of the portal or API user who submitted an order. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>The [[SoftLayer_Account|account]] to which an order belongs. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#brand" name=brand>brand</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Brand'>SoftLayer_Brand </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#cart" name=cart>cart</a></span>
            <div class='views-field-body'>A cart is similar to a quote, except that it can be continually modified by the customer and does not have locked-in prices. Not all orders will have a cart associated with them. See [[SoftLayer_Billing_Order_Cart]] for more information. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Order_Cart'>SoftLayer_Billing_Order_Cart </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#coreRestrictedItems" name=coreRestrictedItems>coreRestrictedItems</a></span>
            <div class='views-field-body'>The [[SoftLayer_Billing_Order_Item (type)|order items]] that are core restricted </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#creditCardTransactions" name=creditCardTransactions>creditCardTransactions</a></span>
            <div class='views-field-body'>All credit card transactions associated with this order. If this order was not placed with a credit card, this will be empty. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Payment_Card_Transaction'>SoftLayer_Billing_Payment_Card_Transaction[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#exchangeRate" name=exchangeRate>exchangeRate</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Currency_ExchangeRate'>SoftLayer_Billing_Currency_ExchangeRate </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#initialInvoice" name=initialInvoice>initialInvoice</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#items" name=items>items</a></span>
            <div class='views-field-body'>The SoftLayer_Billing_Order_items included in an order. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderApprovalDate" name=orderApprovalDate>orderApprovalDate</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderNonServerMonthlyAmount" name=orderNonServerMonthlyAmount>orderNonServerMonthlyAmount</a></span>
            <div class='views-field-body'>An order's non-server items total monthly fee. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderServerMonthlyAmount" name=orderServerMonthlyAmount>orderServerMonthlyAmount</a></span>
            <div class='views-field-body'>An order's server items total monthly fee. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderTopLevelItems" name=orderTopLevelItems>orderTopLevelItems</a></span>
            <div class='views-field-body'>An order's top level items. This normally includes the server line item and any non-server additional services such as NAS or ISCSI. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderTotalAmount" name=orderTotalAmount>orderTotalAmount</a></span>
            <div class='views-field-body'>This amount represents the order's initial charge including set up fee and taxes. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderTotalOneTime" name=orderTotalOneTime>orderTotalOneTime</a></span>
            <div class='views-field-body'>An order's total one time amount summing all the set up fees, the labor fees and the one time fees. Taxes will be applied for non-tax-exempt. This amount represents the initial fees that will be charged. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderTotalOneTimeAmount" name=orderTotalOneTimeAmount>orderTotalOneTimeAmount</a></span>
            <div class='views-field-body'>An order's total one time amount. This amount represents the initial fees before tax. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderTotalOneTimeTaxAmount" name=orderTotalOneTimeTaxAmount>orderTotalOneTimeTaxAmount</a></span>
            <div class='views-field-body'>An order's total one time tax amount. This amount represents the tax that will be applied to the total charge, if the SoftLayer_Account tied to a SoftLayer_Billing_Order is a taxable account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderTotalRecurring" name=orderTotalRecurring>orderTotalRecurring</a></span>
            <div class='views-field-body'>An order's total recurring amount. Taxes will be applied for non-tax-exempt. This amount represents the fees that will be charged on a recurring (usually monthly) basis. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderTotalRecurringAmount" name=orderTotalRecurringAmount>orderTotalRecurringAmount</a></span>
            <div class='views-field-body'>An order's total recurring amount. This amount represents the fees that will be charged on a recurring (usually monthly) basis. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderTotalRecurringTaxAmount" name=orderTotalRecurringTaxAmount>orderTotalRecurringTaxAmount</a></span>
            <div class='views-field-body'>The total tax amount of the recurring fees, if the SoftLayer_Account tied to a SoftLayer_Billing_Order is a taxable account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderTotalSetupAmount" name=orderTotalSetupAmount>orderTotalSetupAmount</a></span>
            <div class='views-field-body'>An order's total setup fee. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderType" name=orderType>orderType</a></span>
            <div class='views-field-body'>The type of an order. This lets you know where this order was generated from. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Order_Type'>SoftLayer_Billing_Order_Type </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#paypalTransactions" name=paypalTransactions>paypalTransactions</a></span>
            <div class='views-field-body'>All PayPal transactions associated with this order. If this order was not placed with PayPal, this will be empty. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Payment_PayPal_Transaction'>SoftLayer_Billing_Payment_PayPal_Transaction[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#presaleEvent" name=presaleEvent>presaleEvent</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Sales_Presale_Event'>SoftLayer_Sales_Presale_Event </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#quote" name=quote>quote</a></span>
            <div class='views-field-body'>The quote of an order. This quote holds information about its expiration date, creation date, name and status. This information is tied to an order having the status 'QUOTE' </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Order_Quote'>SoftLayer_Billing_Order_Quote </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#referralPartner" name=referralPartner>referralPartner</a></span>
            <div class='views-field-body'>The Referral Partner who referred this order. (Only necessary for new customer orders) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#upgradeRequestFlag" name=upgradeRequestFlag>upgradeRequestFlag</a></span>
            <div class='views-field-body'>This flag indicates an order is an upgrade. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#userRecord" name=userRecord>userRecord</a></span>
            <div class='views-field-body'>The SoftLayer_User_Customer object tied to an order. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p></div>
        </div>
            </div>
</div>


