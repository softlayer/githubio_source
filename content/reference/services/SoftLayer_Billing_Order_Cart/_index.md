---
title: "SoftLayer_Billing_Order_Cart"
description: "The [[SoftLayer_Billing_Order_Cart]] service allows customers to save their order in a state that can be continually mod... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Cart"
---
# SoftLayer_Billing_Order_Cart
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Billing_Order_Cart' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Order_Cart' >Datatype</a></li>
    </ul>
</div>

## Description
The [[SoftLayer_Billing_Order_Cart]] service allows customers to save their order in a state that can be continually modified. The difference between a cart and a quote is that a quote has locked-in prices while a cart does not. This allows customers to save their order configuration for up to 30 days. After 30 days, the cart is deleted and cannot be retrieved again. 



        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/claim'> claim</a> </span>
            <div class='views-field-body'>Claim an anonymous quote</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/createCart'> createCart</a> </span>
            <div class='views-field-body'>Create a new cart from the order data provided</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/deleteCart'> deleteCart</a> </span>
            <div class='views-field-body'>Delete an existing cart</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/deleteQuote'> deleteQuote</a> </span>
            <div class='views-field-body'>Delete the quote of an order</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve a quote's corresponding account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/getCartByCartKey'> getCartByCartKey</a> </span>
            <div class='views-field-body'>Retrieve a cart.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/getDoNotContactFlag'> getDoNotContactFlag</a> </span>
            <div class='views-field-body'>Retrieve indicates whether the owner of the quote chosen to no longer be contacted.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Billing_Order_Cart record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/getOrder'> getOrder</a> </span>
            <div class='views-field-body'>Retrieve this order contains the records for which products were selected for this quote.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/getOrdersFromQuote'> getOrdersFromQuote</a> </span>
            <div class='views-field-body'>Retrieve these are all the orders that were created from this quote.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/getPdf'> getPdf</a> </span>
            <div class='views-field-body'>Retrieve a PDF copy of the cart.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/getQuoteByQuoteKey'> getQuoteByQuoteKey</a> </span>
            <div class='views-field-body'>Retrieve a [[SoftLayer_Billing_Order_Quote]] by the quote key specified.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/getRecalculatedOrderContainer'> getRecalculatedOrderContainer</a> </span>
            <div class='views-field-body'>Retrieve order container from a saved cart</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/placeOrder'> placeOrder</a> </span>
            <div class='views-field-body'>Place an order</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/placeQuote'> placeQuote</a> </span>
            <div class='views-field-body'>Saves changes to a quote</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/saveQuote'> saveQuote</a> </span>
            <div class='views-field-body'>Save the quote of an order</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/updateCart'> updateCart</a> </span>
            <div class='views-field-body'>Update an existing cart with the modified order data</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/verifyOrder'> verifyOrder</a> </span>
            <div class='views-field-body'>Verify an order</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Billing_Order_Cart/withdrawGdprAcceptance'> withdrawGdprAcceptance</a> </span>
            <div class='views-field-body'>Withdraws the users acceptance of the GDPR terms.</div>
        </div>
        </div>
</div>

