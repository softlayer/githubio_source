---
title: "upgrade"
description: "Convert the VLAN this operation is executed against to a paid resource. This can be done for any Automatic VLAN. This op... "
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


Convert the VLAN to a paid resource. That is, from an Automatic to a Premium VLAN.


## Overview 
Convert the VLAN this operation is executed against to a paid resource. This can be done for any Automatic VLAN. This operation can only be executed on an Automatic VLAN, and will transition it to being a Premium VLAN. The VLAN will then provide the benefits of a Premium VLAN. A Premium VLAN will remain on the account until cancelled. This operation cannot be undone! Once a VLAN becomes Premium, it can only be removed through cancellation, which will result in it being reclaimed. 

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

* SoftLayer_Exception 

> If the Pod lacks capacity for new Premium VLANs on the respective network. 



