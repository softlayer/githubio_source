---
title: "upgrade"
description: "Convert the VLAN to a paid resource. This can be done for any VLAN which was automatically allocated. Upgrading an exist... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
aliases:
    - "/reference/services/softlayer_network_vlan/upgrade"
---
# [SoftLayer_Network_Vlan](/reference/services/SoftLayer_Network_Vlan)::upgrade




## Overview 
Convert the VLAN to a paid resource. This can be done for any VLAN which was automatically allocated. Upgrading an existing VLAN provides the same benefits as a purchased VLAN. A purchased VLAN will remain on the account until cancelled. This operation cannot be undone! Once a VLAN is purchased, it can only be cancelled which will result in it being reclaimed. 

This operation is a convenience for utilizing the SoftLayer_Product_Order.placeOrder operation. It will place an order to upgrade the VLAN it is executed against. It will take a few moments for the order to be processed and the upgrade to complete. Note that the order is placed in such a way that any account state which prevents automatic order approval will prevent the order from being placed. Thus, if no error is received, the order was placed and approved, and the VLAN will be upgraded shortly. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_VlanInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Product_Order_Network_Vlan'>SoftLayer_Container_Product_Order_Network_Vlan </a>



### Error Handling

* SoftLayer_Exception 

> If the VLAN is already considered purchased. 

* SoftLayer_Exception 

> If the VLAN is ineligible for purchase, such as a Transit VLAN. 



