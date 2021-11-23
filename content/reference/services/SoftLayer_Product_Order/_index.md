---
title: "SoftLayer_Product_Order"
description: "All orders (servers, virtual servers and services) pass through the [[SoftLayer_Product_Order]] service. This service provides the entry point for placing orders and quotes with SoftLayer. To place orders using these services, you must provide the appropriate container type as defined by [[SoftLayer_Container_Product_Order]]. For server orders, you would use [[SoftLayer_Container_Product_Order_Hardware_Server]]. For virtual server orders, you would use [[SoftLayer_Container_Product_Order_Virtual_Guest]]. For additional service orders, it will depend on the additional service (e.g., network attached storage, object storage) being purchased. See the data types documentation to get a list of all the available container types beginning with `SoftLayer_Container_Product_Order_*`. 

There are several main entry points associated with ordering: 

- [[SoftLayer_Product_Order/placeOrder]] Order servers and services. Your credit card or PayPal account will get charged when successfully placed. 

- [[SoftLayer_Product_Order/verifyOrder]] Run verification on your order before it's actually placed to get additional information, like your total monthly or hourly recurring charges. You may also call this service to help ensure that your call to [[SoftLayer_Product_Order/placeOrder]] will succeed. **This service is called internally, so it is not required to verify before you call `placeOrder`.** No credit card or PayPal charges result from this call. 

- [[SoftLayer_Product_Order/placeQuote]] Create a quote only. Subsequent orders may be placed from this quote. See [[SoftLayer_Billing_Order_Quote/placeOrder]] for details on how to order from a quote. 

- [[SoftLayer_Product_Order/getVlans]] Get a list of available VLANs that can be supplied when placing an order. 

While this service provides detailed customization for ordering, some customers may find the simplified ordering system sufficient for their needs. For more information, see the following: 

- [[SoftLayer_Virtual_Guest/createObject]] - Simplified virtual server ordering 

- [[SoftLayer_Hardware/createObject]] - Simplified bare metal server ordering "
date: "2018-02-12"
tags:
    - "service"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
type: "reference"
layout: "service"
mainService : "SoftLayer_Product_Order"
---
