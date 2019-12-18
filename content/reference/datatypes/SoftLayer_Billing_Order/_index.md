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


### associatedMethods

*  [SoftLayer_Billing_Order::getObject](/reference/services/SoftLayer_Billing_Order/getObject )



### seeAlso

* [SoftLayer_Account (type)](/reference/datatypes/SoftLayer_Account (type) )




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

## Local
-----
[accountId]: #accountid
#### [accountId]
The account ID to which an order belongs.  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
The point in time at which a billing item was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
*  
<span class="type-label">Type: </span>**integer**

-----
[impersonatingUserRecordId]: #impersonatinguserrecordid
#### [impersonatingUserRecordId]
The SoftLayer_User_Customer id of the portal or API user who impersonated the user which submitted an order.  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The last time an order was updated.  
<span class="type-label">Type: </span>**dateTime**

-----
[orderQuoteId]: #orderquoteid
#### [orderQuoteId]
The SoftLayer_Billing_Order_Quote id of the quote's user who finalized an order.  
<span class="type-label">Type: </span>**integer**

-----
[orderTypeId]: #ordertypeid
#### [orderTypeId]
The SoftLayer_Billing_Order_Type id of the order.  
<span class="type-label">Type: </span>**integer**

-----
[presaleEventId]: #presaleeventid
#### [presaleEventId]
  
<span class="type-label">Type: </span>**integer**

-----
[privateCloudOrderFlag]: #privatecloudorderflag
#### [privateCloudOrderFlag]
Flag indicating a private cloud solution order (Deprecated)  
<span class="type-label">Type: </span>**boolean**

-----
[status]: #status
#### [status]
Purchaser current status e.i. Approved, Pending_Approval  
<span class="type-label">Type: </span>**string**

-----
[userRecordId]: #userrecordid
#### [userRecordId]
The SoftLayer_User_Customer id of the portal or API user who submitted an order.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) to which an order belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[brand]: #brand
#### [brand]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand'>SoftLayer_Brand </a>**

-----
[cart]: #cart
#### [cart]
A cart is similar to a quote, except that it can be continually modified by the customer and does not have locked-in prices. Not all orders will have a cart associated with them. See [SoftLayer_Billing_Order_Cart]({{<ref "reference/datatypes/SoftLayer_Billing_Order_Cart">}}) for more information.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Cart'>SoftLayer_Billing_Order_Cart </a>**

-----
[coreRestrictedItems]: #corerestricteditems
#### [coreRestrictedItems]
The [SoftLayer_Billing_Order_Item]({{<ref "reference/datatypes/SoftLayer_Billing_Order_Item">}}) that are core restricted  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item[] </a>**

-----
[creditCardTransactions]: #creditcardtransactions
#### [creditCardTransactions]
All credit card transactions associated with this order. If this order was not placed with a credit card, this will be empty.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Payment_Card_Transaction'>SoftLayer_Billing_Payment_Card_Transaction[] </a>**

-----
[exchangeRate]: #exchangerate
#### [exchangeRate]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Currency_ExchangeRate'>SoftLayer_Billing_Currency_ExchangeRate </a>**

-----
[initialInvoice]: #initialinvoice
#### [initialInvoice]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Invoice'>SoftLayer_Billing_Invoice </a>**

-----
[items]: #items
#### [items]
The SoftLayer_Billing_Order_items included in an order.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item[] </a>**

-----
[orderApprovalDate]: #orderapprovaldate
#### [orderApprovalDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[orderNonServerMonthlyAmount]: #ordernonservermonthlyamount
#### [orderNonServerMonthlyAmount]
An order's non-server items total monthly fee.  
<span class="type-label">Type: </span>**decimal**

-----
[orderServerMonthlyAmount]: #orderservermonthlyamount
#### [orderServerMonthlyAmount]
An order's server items total monthly fee.  
<span class="type-label">Type: </span>**decimal**

-----
[orderTopLevelItems]: #ordertoplevelitems
#### [orderTopLevelItems]
An order's top level items. This normally includes the server line item and any non-server additional services such as NAS or ISCSI.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item[] </a>**

-----
[orderTotalAmount]: #ordertotalamount
#### [orderTotalAmount]
This amount represents the order's initial charge including set up fee and taxes.  
<span class="type-label">Type: </span>**decimal**

-----
[orderTotalOneTime]: #ordertotalonetime
#### [orderTotalOneTime]
An order's total one time amount summing all the set up fees, the labor fees and the one time fees. Taxes will be applied for non-tax-exempt. This amount represents the initial fees that will be charged.  
<span class="type-label">Type: </span>**decimal**

-----
[orderTotalOneTimeAmount]: #ordertotalonetimeamount
#### [orderTotalOneTimeAmount]
An order's total one time amount. This amount represents the initial fees before tax.  
<span class="type-label">Type: </span>**decimal**

-----
[orderTotalOneTimeTaxAmount]: #ordertotalonetimetaxamount
#### [orderTotalOneTimeTaxAmount]
An order's total one time tax amount. This amount represents the tax that will be applied to the total charge, if the SoftLayer_Account tied to a SoftLayer_Billing_Order is a taxable account.  
<span class="type-label">Type: </span>**decimal**

-----
[orderTotalRecurring]: #ordertotalrecurring
#### [orderTotalRecurring]
An order's total recurring amount. Taxes will be applied for non-tax-exempt. This amount represents the fees that will be charged on a recurring (usually monthly) basis.  
<span class="type-label">Type: </span>**decimal**

-----
[orderTotalRecurringAmount]: #ordertotalrecurringamount
#### [orderTotalRecurringAmount]
An order's total recurring amount. This amount represents the fees that will be charged on a recurring (usually monthly) basis.  
<span class="type-label">Type: </span>**decimal**

-----
[orderTotalRecurringTaxAmount]: #ordertotalrecurringtaxamount
#### [orderTotalRecurringTaxAmount]
The total tax amount of the recurring fees, if the SoftLayer_Account tied to a SoftLayer_Billing_Order is a taxable account.  
<span class="type-label">Type: </span>**decimal**

-----
[orderTotalSetupAmount]: #ordertotalsetupamount
#### [orderTotalSetupAmount]
An order's total setup fee.  
<span class="type-label">Type: </span>**decimal**

-----
[orderType]: #ordertype
#### [orderType]
The type of an order. This lets you know where this order was generated from.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Type'>SoftLayer_Billing_Order_Type </a>**

-----
[paypalTransactions]: #paypaltransactions
#### [paypalTransactions]
All PayPal transactions associated with this order. If this order was not placed with PayPal, this will be empty.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Payment_PayPal_Transaction'>SoftLayer_Billing_Payment_PayPal_Transaction[] </a>**

-----
[presaleEvent]: #presaleevent
#### [presaleEvent]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Sales_Presale_Event'>SoftLayer_Sales_Presale_Event </a>**

-----
[quote]: #quote
#### [quote]
The quote of an order. This quote holds information about its expiration date, creation date, name and status. This information is tied to an order having the status 'QUOTE'  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Quote'>SoftLayer_Billing_Order_Quote </a>**

-----
[referralPartner]: #referralpartner
#### [referralPartner]
The Referral Partner who referred this order. (Only necessary for new customer orders)  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[upgradeRequestFlag]: #upgraderequestflag
#### [upgradeRequestFlag]
This flag indicates an order is an upgrade.  
<span class="type-label">Type: </span>**boolean**

-----
[userRecord]: #userrecord
#### [userRecord]
The SoftLayer_User_Customer object tied to an order.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**


## Count

-----
[coreRestrictedItemCount]: #corerestricteditemcount
#### [coreRestrictedItemCount]
A count of the [SoftLayer_Billing_Order_Item]({{<ref "reference/datatypes/SoftLayer_Billing_Order_Item">}}) that are core restricted   
<span class="type-label">Type: </span>**unsigned long**


-----
[creditCardTransactionCount]: #creditcardtransactioncount
#### [creditCardTransactionCount]
A count of all credit card transactions associated with this order. If this order was not placed with a credit card, this will be empty.   
<span class="type-label">Type: </span>**unsigned long**


-----
[itemCount]: #itemcount
#### [itemCount]
A count of the SoftLayer_Billing_Order_items included in an order.   
<span class="type-label">Type: </span>**unsigned long**


-----
[orderTopLevelItemCount]: #ordertoplevelitemcount
#### [orderTopLevelItemCount]
A count of an order's top level items. This normally includes the server line item and any non-server additional services such as NAS or ISCSI.   
<span class="type-label">Type: </span>**unsigned long**


-----
[paypalTransactionCount]: #paypaltransactioncount
#### [paypalTransactionCount]
A count of all PayPal transactions associated with this order. If this order was not placed with PayPal, this will be empty.   
<span class="type-label">Type: </span>**unsigned long**

</div>


