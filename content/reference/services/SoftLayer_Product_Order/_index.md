---
title: "SoftLayer_Product_Order"
description: "All orders (servers, virtual servers and services) pass through the [[SoftLayer_Product_Order]] service. This service pr... "
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
All orders (servers, virtual servers and services) pass through the [[SoftLayer_Product_Order]] service. This service provides the entry point for placing orders and quotes with SoftLayer. To place orders using these services, you must provide the appropriate container type as defined by [[SoftLayer_Container_Product_Order]]. For server orders, you would use [[SoftLayer_Container_Product_Order_Hardware_Server]]. For virtual server orders, you would use [[SoftLayer_Container_Product_Order_Virtual_Guest]]. For additional service orders, it will depend on the additional service (e.g., network attached storage, object storage, global load balancer) being purchased. See the data types documentation to get a list of all the available container types beginning with <code>SoftLayer_Container_Product_Order_*</code>. 

There are several main entry points associated with ordering: 

<ul> <li>[[SoftLayer_Product_Order/placeOrder|placeOrder]] - Order servers and services. Your credit card or PayPal account will get charged when successfully placed.</li> <li>[[SoftLayer_Product_Order/verifyOrder|verifyOrder]] - Run verification on your order before it's actually placed to get additional information, like your total monthly or hourly recurring charges. You may also call this service to help ensure that your call to [[SoftLayer_Product_Order/placeOrder|placeOrder]] will succeed. <strong>This service is called internally, so it is not required to verify before you call <code>placeOrder</code>.</strong> No credit card or PayPal charges result from this call.</li> <li>[[SoftLayer_Product_Order/placeQuote|placeQuote]] - Create a quote only. Subsequent orders may be placed from this quote. See [[SoftLayer_Billing_Order_Quote/placeOrder]] for details on how to order from a quote.</li> <li>[[SoftLayer_Product_Order/getVlans|getVlans]] - Get a list of available VLANs that can be supplied when placing an order.</li> </ul> 

While this service provides detailed customization for ordering, some customers may find the simplified ordering system sufficient for their needs. For more information, see the following: 

<ul> <li>[[SoftLayer_Virtual_Guest/createObject]] - Simplified virtual server ordering</li> <li>[[SoftLayer_Hardware/createObject]] - Simplified bare metal server ordering</li> </ul> 



        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Order/checkItemAvailability'> checkItemAvailability</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Order/checkItemAvailabilityForImageTemplate'> checkItemAvailabilityForImageTemplate</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Order/checkItemConflicts'> checkItemConflicts</a> </span>
            <div class='views-field-body'>Check order items for conflicts</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Order/getExternalPaymentAuthorizationReceipt'> getExternalPaymentAuthorizationReceipt</a> </span>
            <div class='views-field-body'>Returns an order receipt for a completed external (PayPal) payment authorization.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Order/getNetworks'> getNetworks</a> </span>
            <div class='views-field-body'>Retrieve the networks that are available during ordering.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Order/getResellerOrder'> getResellerOrder</a> </span>
            <div class='views-field-body'>Get External Reseller pricing where applicable</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Order/getTaxCalculationResult'> getTaxCalculationResult</a> </span>
            <div class='views-field-body'>Get the results of a tax calculation.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Order/getVlans'> getVlans</a> </span>
            <div class='views-field-body'>Get the VLANs that are available during ordering</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Order/placeOrder'> placeOrder</a> </span>
            <div class='views-field-body'>Place an order using the [[SoftLayer_Container_Product_Order]] data type.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Order/placeQuote'> placeQuote</a> </span>
            <div class='views-field-body'>Place a quote</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Order/processExternalPaymentAuthorization'> processExternalPaymentAuthorization</a> </span>
            <div class='views-field-body'>Process an external (PayPal) payment authorization.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Order/requiredItems'> requiredItems</a> </span>
            <div class='views-field-body'>Get list of items that are required with the item prices provided</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Product_Order/verifyOrder'> verifyOrder</a> </span>
            <div class='views-field-body'>Verify that an order may be successfully placed with the details provided.</div>
        </div>
        </div>
</div>

