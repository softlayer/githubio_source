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

Quotes could are created with contact information duplicated from the [[SoftLayer_Account (type)|SoftLayer_Account data type]] or by manual entry. We do this in order to maintain a history of an account's contact information as quotes are generated. 

Query the [[SoftLayer_Account]] service to get a list of quotes for your account. 
        
        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Quote/claim'> claim</a> </span>
            <div class='views-field-body'>Claim an anonymous quote</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Quote/deleteQuote'> deleteQuote</a> </span>
            <div class='views-field-body'>Delete the quote of an order</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Quote/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve a quote's corresponding account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Quote/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Billing_Order_Quote record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Quote/getOrder'> getOrder</a> </span>
            <div class='views-field-body'>Retrieve this order contains the records for which products were selected for this quote.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Quote/getOrdersFromQuote'> getOrdersFromQuote</a> </span>
            <div class='views-field-body'>Retrieve these are all the orders that were created from this quote.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Quote/getPdf'> getPdf</a> </span>
            <div class='views-field-body'>Retrieve a PDF copy of a quote.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Quote/getQuoteByQuoteKey'> getQuoteByQuoteKey</a> </span>
            <div class='views-field-body'>Retrieve a [[SoftLayer_Billing_Order_Quote]] by the quote key specified.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Quote/getRecalculatedOrderContainer'> getRecalculatedOrderContainer</a> </span>
            <div class='views-field-body'>Generate an [[SoftLayer_Container_Product_Order|order container]] from the previously-created quote. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Quote/placeOrder'> placeOrder</a> </span>
            <div class='views-field-body'>Place an order</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Quote/placeQuote'> placeQuote</a> </span>
            <div class='views-field-body'>Saves changes to a quote</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Quote/saveQuote'> saveQuote</a> </span>
            <div class='views-field-body'>Save the quote of an order</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Quote/verifyOrder'> verifyOrder</a> </span>
            <div class='views-field-body'>Verify an order</div>
        </div>
        </div>
</div>

