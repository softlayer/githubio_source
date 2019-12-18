---
title: "SoftLayer_Billing_Order_Quote"
description: "The SoftLayer_Billing_Order_Quote service controls the quoted orders that are created whenever a SoftLayer customer's pl... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Quote"
---
# SoftLayer_Billing_Order_Quote
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Billing_Order_Quote' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Order_Quote' >Datatype</a></li>
    </ul>
</div>

## Description
The SoftLayer_Billing_Order_Quote service controls the quoted orders that are created whenever a SoftLayer customer's places a purchase. Quotes exist in several states. The ones of concern are: 
*'''PENDING''': Quotes which have not been paid yet. Quotes pending approval from a Softlayer customer.


Once an order is placed from a quote it moves from PENDING to EXPIRED state 2 days after its creation and it is removed from the system after 5 days unless otherwise the SoftLayer customer saved the quote. 

Quotes could are created with contact information duplicated from the [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) or by manual entry. We do this in order to maintain a history of an account's contact information as quotes are generated. 

Query the [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) service to get a list of quotes for your account. 



        
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

#### [claim](/reference/services/SoftLayer_Billing_Order_Quote/claim)
Claim an anonymous quote

#### [deleteQuote](/reference/services/SoftLayer_Billing_Order_Quote/deleteQuote)
Delete the quote of an order

#### [getAccount](/reference/services/SoftLayer_Billing_Order_Quote/getAccount)
Retrieve a quote's corresponding account.

#### [getDoNotContactFlag](/reference/services/SoftLayer_Billing_Order_Quote/getDoNotContactFlag)
Retrieve indicates whether the owner of the quote chosen to no longer be contacted.

#### [getObject](/reference/services/SoftLayer_Billing_Order_Quote/getObject)
Retrieve a SoftLayer_Billing_Order_Quote record.

#### [getOrder](/reference/services/SoftLayer_Billing_Order_Quote/getOrder)
Retrieve this order contains the records for which products were selected for this quote.

#### [getOrdersFromQuote](/reference/services/SoftLayer_Billing_Order_Quote/getOrdersFromQuote)
Retrieve these are all the orders that were created from this quote.

#### [getPdf](/reference/services/SoftLayer_Billing_Order_Quote/getPdf)
Retrieve a PDF copy of a quote.

#### [getQuoteByQuoteKey](/reference/services/SoftLayer_Billing_Order_Quote/getQuoteByQuoteKey)
Retrieve a [SoftLayer_Billing_Order_Quote]({{<ref "reference/datatypes/SoftLayer_Billing_Order_Quote">}}) by the quote key specified.

#### [getRecalculatedOrderContainer](/reference/services/SoftLayer_Billing_Order_Quote/getRecalculatedOrderContainer)
Generate an [SoftLayer_Container_Product_Order]({{<ref "reference/datatypes/SoftLayer_Container_Product_Order">}}) from the previously-created quote. 

#### [placeOrder](/reference/services/SoftLayer_Billing_Order_Quote/placeOrder)
Place an order

#### [placeQuote](/reference/services/SoftLayer_Billing_Order_Quote/placeQuote)
Saves changes to a quote

#### [saveQuote](/reference/services/SoftLayer_Billing_Order_Quote/saveQuote)
Save the quote of an order

#### [verifyOrder](/reference/services/SoftLayer_Billing_Order_Quote/verifyOrder)
Verify an order

#### [withdrawGdprAcceptance](/reference/services/SoftLayer_Billing_Order_Quote/withdrawGdprAcceptance)
Withdraws the users acceptance of the GDPR terms.

</div>

