---
title: "SoftLayer_Container_Product_Order_Receipt"
description: "When an order is placed (SoftLayer_Product_Order::placeOrder), a receipt is returned when the order is created successfu... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Product_Order_Receipt"
---

# SoftLayer_Container_Product_Order_Receipt
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Product_Order_Receipt' >Datatype</a></li>
    </ul>
</div>

## Description 
When an order is placed (SoftLayer_Product_Order::placeOrder), a receipt is returned when the order is created successfully. The information in the receipt helps explain information about the order. It's order ID, and all the data within the order as well. 

For PayPal Orders, an URL is also returned to the user so that the user can complete the transaction. Users paying with PayPal must continue on to this URL, login and pay. When doing this, PayPal will redirect the user back to a SoftLayer page which will then "finalize" the authorization process. From here, Sales will verify the order by contacting the user in some way, unless sales has already spoken to the user about approving the order. 

For users paying with a credit card, a receipt means the order has gone to sales and is awaiting approval. 





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
[externalPaymentCheckoutUrl]: #externalpaymentcheckouturl
#### [externalPaymentCheckoutUrl]
This URL refers to the location where you will visit to complete the payment authorization for an external service, such as PayPal. This property is associated with <code>externalPaymentToken</code> and will only be populated when purchasing products with an external service. 

Once you visit this location, you will be presented with the options to confirm payment or deny payment. If you confirm payment, you will be redirected back to the receipt for your order. If you deny, you will be redirected back to the cancel order page where you do not need to take any additional action. 

Until you confirm payment with the external service, your products will not be provisioned or accessible for your consumption. Upon successfully confirming payment, our system will be notified and the order approval and provisioning systems will begin processing. After provisioning is complete, your services will be available.   
<span class="type-label">Type: </span>**string**

-----
[externalPaymentToken]: #externalpaymenttoken
#### [externalPaymentToken]
This token refers to the identifier for the external payment authorization. This token is associated with the <code>externalPaymentCheckoutUrl</code> and is only populated when purchasing products with an external service like PayPal.   
<span class="type-label">Type: </span>**string**

-----
[orderDate]: #orderdate
#### [orderDate]
The date when SoftLayer received the order.  
<span class="type-label">Type: </span>**dateTime**

-----
[orderDetails]: #orderdetails
#### [orderDetails]
This is a copy of the order container (SoftLayer_Container_Product_Order) which holds all the data related to an order. This will only return when an order is processed successfully. It will contain all the items in an order as well as the order totals.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>**

-----
[orderId]: #orderid
#### [orderId]
SoftLayer's unique identifier for the order.  
<span class="type-label">Type: </span>**integer**

-----
[paypalCheckoutUrl]: #paypalcheckouturl
#### [paypalCheckoutUrl]
Deprecation notice: use <code>externalPaymentCheckoutUrl</code> instead of this property. 

This URL refers to the location where you will visit to complete the payment authorization for PayPal. This property is associated with <code>paypalToken</code> and will only be populated when purchasing products with PayPal. 

Once you visit PayPal's site, you will be presented with the options to confirm payment or deny payment. If you confirm payment, you will be redirected back to the receipt for your order. If you deny, you will be redirected back to the cancel order page where you do not need to take any additional action. 

Until you confirm payment with PayPal, your products will not be provisioned or accessible for your consumption. Upon successfully confirming payment, our system will be notified and the order approval and provisioning systems will begin processing. After provisioning is complete, your services will be available.   
<span class="type-label">Type: </span>**string**

-----
[paypalToken]: #paypaltoken
#### [paypalToken]
Deprecation notice: use <code>externalPaymentToken</code> instead of this property. 

This token refers to the identifier provided when payment is processed via PayPal. This token is associated with the <code>paypalCheckoutUrl</code>.   
<span class="type-label">Type: </span>**string**

-----
[placedOrder]: #placedorder
#### [placedOrder]
This is a copy of the order that was successfully placed (SoftLayer_Billing_Order). This will only return when an order is processed successfully.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order </a>**

-----
[quote]: #quote
#### [quote]
This is a copy of the quote container (SoftLayer_Billing_Order_Quote) which holds all the data related to a quote. This will only return when a quote is processed successfully.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Quote'>SoftLayer_Billing_Order_Quote </a>**

</div>
<!-- LOCAL PROPERTY END -->

</div>


