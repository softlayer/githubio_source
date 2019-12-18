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
All orders (servers, virtual servers and services) pass through the [SoftLayer_Product_Order]({{<ref "reference/datatypes/SoftLayer_Product_Order">}}) service. This service provides the entry point for placing orders and quotes with SoftLayer. To place orders using these services, you must provide the appropriate container type as defined by [SoftLayer_Container_Product_Order]({{<ref "reference/datatypes/SoftLayer_Container_Product_Order">}}). For server orders, you would use [SoftLayer_Container_Product_Order_Hardware_Server]({{<ref "reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server">}}). For virtual server orders, you would use [SoftLayer_Container_Product_Order_Virtual_Guest]({{<ref "reference/datatypes/SoftLayer_Container_Product_Order_Virtual_Guest">}}). For additional service orders, it will depend on the additional service (e.g., network attached storage, object storage, global load balancer) being purchased. See the data types documentation to get a list of all the available container types beginning with <code>SoftLayer_Container_Product_Order_*</code>. 

There are several main entry points associated with ordering: 

<ul> <li>[SoftLayer_Product_Order::placeOrder]({{<ref "reference/services/SoftLayer_Product_Order/placeOrder">}}) - Get a list of available VLANs that can be supplied when placing an order.</li> </ul> 

While this service provides detailed customization for ordering, some customers may find the simplified ordering system sufficient for their needs. For more information, see the following: 

<ul> <li>[SoftLayer_Virtual_Guest::createObject]({{<ref "reference/services/SoftLayer_Virtual_Guest/createObject">}}) - Simplified virtual server ordering</li> <li>[SoftLayer_Hardware::createObject]({{<ref "reference/services/SoftLayer_Hardware/createObject">}}) - Simplified bare metal server ordering</li> </ul> 



        
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

#### [checkItemAvailability](/reference/services/SoftLayer_Product_Order/checkItemAvailability)


#### [checkItemAvailabilityForImageTemplate](/reference/services/SoftLayer_Product_Order/checkItemAvailabilityForImageTemplate)


#### [checkItemConflicts](/reference/services/SoftLayer_Product_Order/checkItemConflicts)
Check order items for conflicts

#### [getExternalPaymentAuthorizationReceipt](/reference/services/SoftLayer_Product_Order/getExternalPaymentAuthorizationReceipt)
Returns an order receipt for a completed external (PayPal) payment authorization.

#### [getNetworks](/reference/services/SoftLayer_Product_Order/getNetworks)
Retrieve the networks that are available during ordering.

#### [getResellerOrder](/reference/services/SoftLayer_Product_Order/getResellerOrder)
Get External Reseller pricing where applicable

#### [getTaxCalculationResult](/reference/services/SoftLayer_Product_Order/getTaxCalculationResult)
Get the results of a tax calculation.

#### [getVlans](/reference/services/SoftLayer_Product_Order/getVlans)
Get the VLANs that are available during ordering

#### [placeOrder](/reference/services/SoftLayer_Product_Order/placeOrder)
Place an order using the [SoftLayer_Container_Product_Order]({{<ref "reference/datatypes/SoftLayer_Container_Product_Order">}}) data type.

#### [placeQuote](/reference/services/SoftLayer_Product_Order/placeQuote)
Place a quote

#### [processExternalPaymentAuthorization](/reference/services/SoftLayer_Product_Order/processExternalPaymentAuthorization)
Process an external (PayPal) payment authorization.

#### [requiredItems](/reference/services/SoftLayer_Product_Order/requiredItems)
Get list of items that are required with the item prices provided

#### [verifyOrder](/reference/services/SoftLayer_Product_Order/verifyOrder)
Verify that an order may be successfully placed with the details provided.

</div>

