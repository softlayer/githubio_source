---
title: "getVlans"
description: "Return collections of public and private VLANs that are available during ordering. If a location ID is provided, the res... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
---
# SoftLayer_Product_Order::getVlans
## Overview 
Return collections of public and private VLANs that are available during ordering. If a location ID is provided, the resulting VLANs will be limited to that location. If the Virtual Server package id (46) is provided, the VLANs will be narrowed down to those locations that contain routers with the VIRTUAL_IMAGE_STORE data attribute. 

For the selectedItems parameter, this is a comma-separated string of category codes and item values. For example: 

<ul> <li><code>port_speed=10,guest_disk0=LOCAL_DISK</code></li> <li><code>port_speed=100,disk0=SAN_DISK</code></li> <li><code>port_speed=100,private_network_only=1,guest_disk0=LOCAL_DISK</code></li> </ul> 

This parameter is used to narrow the available results down even further. It's not necessary when selecting a VLAN, but it will help avoid errors when attempting to place an order. The only acceptable category codes are: 

<ul> <li><code>port_speed</code></li> <li>A disk category, such as <code>guest_disk0</code> or <code>disk0</code>, with values of either <code>LOCAL_DISK</code> or <code>SAN_DISK</code></li> <li><code>private_network_only</code></li> <li><code>dual_path_network</code></li> </ul> 

For most customers, it's sufficient to only provide the first 2 parameters. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|locationId| integer| Narrow the VLANs down by this datacenter. This value should match the datacenter selected for the order container.|
|packageId| integer| Optional, but recommended package id for the order container.|
|selectedItems| string| A string of existing items selected on the order - see the method overview for more details.|
|vlanIds| array of integers| If provided, the results will be limited to these VLANs.|
|subnetIds| array of integers| If provided, the results will be limited to VLANs that contain these subnets.|
|accountId| integer| For authenticated users, this optional parameter will be ignored.|
|orderContainer| <a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>| Optionally filter VLANs relating to the <code>prices</code> specified on the order container.|
|hardwareFirewallOrderedFlag| boolean| Provided when ordering a hardware firewall, will cause results to exclude inside VLANs and VLANs w/ dedicated firewall attached|


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Product_Order_Network_Vlans'>SoftLayer_Container_Product_Order_Network_Vlans </a>

