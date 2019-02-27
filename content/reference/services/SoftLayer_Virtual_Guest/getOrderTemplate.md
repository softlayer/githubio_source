---
title: "getOrderTemplate"
description: "Obtain an order container that is ready to be sent to the [[SoftLayer_Product_Order#placeOrder|SoftLayer_Product_Order::... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/getOrderTemplate"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::getOrderTemplate

Obtain an order container that is ready to be sent to the [[SoftLayer_Product_Order#placeOrder|SoftLayer_Product_Order::placeOrder]] method.


## Overview 
Obtain an order container that is ready to be sent to the [[SoftLayer_Product_Order#placeOrder|SoftLayer_Product_Order::placeOrder]] method. This container will include all services that the selected computing instance has. If desired you may remove prices which were returned. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|billingType| string| <ul type="xsd:string"> <li title="Monthly Billing">MONTHLY</li> <li title="Hourly Billing">HOURLY</li> </ul>|
|orderPrices| <a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>| This is a list of prices that could replace options that are normally selected by matching the items to the existing virtual server.|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>




