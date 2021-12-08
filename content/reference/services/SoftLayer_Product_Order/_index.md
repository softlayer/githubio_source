---
title: "SoftLayer_Product_Order"
description: "All orders (servers, virtual servers and services) pass through the [SoftLayer_Product_Order]({{<ref 'reference/datatype... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
---
# SoftLayer_Product_Order
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Product_Order' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Order' >Datatype</a></li>
    </ul>
</div>

## Description


All orders (servers, virtual servers and services) pass through the [SoftLayer_Product_Order]({{<ref "reference/datatypes/SoftLayer_Product_Order">}}) service. This service provides the entry point for placing orders and quotes with SoftLayer. To place orders using these services, you must provide the appropriate container type as defined by [SoftLayer_Container_Product_Order]({{<ref "reference/datatypes/SoftLayer_Container_Product_Order">}}). For server orders, you would use [SoftLayer_Container_Product_Order_Hardware_Server]({{<ref "reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server">}}). For virtual server orders, you would use [SoftLayer_Container_Product_Order_Virtual_Guest]({{<ref "reference/datatypes/SoftLayer_Container_Product_Order_Virtual_Guest">}}). For additional service orders, it will depend on the additional service (e.g., network attached storage, object storage) being purchased. See the data types documentation to get a list of all the available container types beginning with `SoftLayer_Container_Product_Order_*`. 

There are several main entry points associated with ordering: 

- [SoftLayer_Product_Order::placeOrder]({{<ref "reference/services/SoftLayer_Product_Order/placeOrder">}}) Order servers and services. Your credit card or PayPal account will get charged when successfully placed. 

- [SoftLayer_Product_Order::verifyOrder]({{<ref "reference/services/SoftLayer_Product_Order/verifyOrder">}}) Run verification on your order before it's actually placed to get additional information, like your total monthly or hourly recurring charges. You may also call this service to help ensure that your call to [SoftLayer_Product_Order::placeOrder]({{<ref "reference/services/SoftLayer_Product_Order/placeOrder">}}) will succeed. **This service is called internally, so it is not required to verify before you call `placeOrder`.** No credit card or PayPal charges result from this call. 

- [SoftLayer_Product_Order::placeQuote]({{<ref "reference/services/SoftLayer_Product_Order/placeQuote">}}) Create a quote only. Subsequent orders may be placed from this quote. See [SoftLayer_Billing_Order_Quote::placeOrder]({{<ref "reference/services/SoftLayer_Billing_Order_Quote/placeOrder">}}) for details on how to order from a quote. 

- [SoftLayer_Product_Order::getVlans]({{<ref "reference/services/SoftLayer_Product_Order/getVlans">}}) Get a list of available VLANs that can be supplied when placing an order. 

While this service provides detailed customization for ordering, some customers may find the simplified ordering system sufficient for their needs. For more information, see the following: 

- [SoftLayer_Virtual_Guest::createObject]({{<ref "reference/services/SoftLayer_Virtual_Guest/createObject">}}) - Simplified virtual server ordering 

- [SoftLayer_Hardware::createObject]({{<ref "reference/services/SoftLayer_Hardware/createObject">}}) - Simplified bare metal server ordering 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [checkItemAvailability](/reference/services/SoftLayer_Product_Order/checkItemAvailability)


</div>

<div class="method-row">

#### [checkItemAvailabilityForImageTemplate](/reference/services/SoftLayer_Product_Order/checkItemAvailabilityForImageTemplate)


</div>

<div class="method-row">

#### [checkItemConflicts](/reference/services/SoftLayer_Product_Order/checkItemConflicts)
Check order items for conflicts

</div>

<div class="method-row">

#### [getExternalPaymentAuthorizationReceipt](/reference/services/SoftLayer_Product_Order/getExternalPaymentAuthorizationReceipt)
Returns an order receipt for a completed external (PayPal) payment authorization.

</div>

<div class="method-row deprecated">

#### [getNetworks](/reference/services/SoftLayer_Product_Order/getNetworks)
(DEPRECATED) Retrieve the networks that are available during ordering.

<span class="deprecation-label">Deprecated  </span>


</div>

<div class="method-row">

#### [getResellerOrder](/reference/services/SoftLayer_Product_Order/getResellerOrder)
Get External Reseller pricing where applicable

</div>

<div class="method-row">

#### [getTaxCalculationResult](/reference/services/SoftLayer_Product_Order/getTaxCalculationResult)
Get the results of a tax calculation.

</div>

<div class="method-row">

#### [getVlans](/reference/services/SoftLayer_Product_Order/getVlans)
Get the VLANs that are available during ordering

</div>

<div class="method-row">

#### [placeOrder](/reference/services/SoftLayer_Product_Order/placeOrder)
Place an order using the [SoftLayer_Container_Product_Order]({{<ref "reference/datatypes/SoftLayer_Container_Product_Order">}}) data type.

</div>

<div class="method-row">

#### [placeQuote](/reference/services/SoftLayer_Product_Order/placeQuote)
Place a quote

</div>

<div class="method-row">

#### [processExternalPaymentAuthorization](/reference/services/SoftLayer_Product_Order/processExternalPaymentAuthorization)
Process an external (PayPal) payment authorization.

</div>

<div class="method-row">

#### [requiredItems](/reference/services/SoftLayer_Product_Order/requiredItems)
Get list of items that are required with the item prices provided

</div>

<div class="method-row">

#### [verifyOrder](/reference/services/SoftLayer_Product_Order/verifyOrder)
Verify that an order may be successfully placed with the details provided.

</div>
</div>

</div>

