---
title: "getVlans"
description: "Return collections of public and private VLANs that are available during ordering. If a location ID is provided, the resulting VLANs will be limited to that location. If the Virtual Server package id (46) is provided, the VLANs will be narrowed down to those locations that contain routers with the VIRTUAL_IMAGE_STORE data attribute. 

For the selectedItems parameter, this is a comma-separated string of category codes and item values. For example: 

- `port_speed=10,guest_disk0=LOCAL_DISK` 

- `port_speed=100,disk0=SAN_DISK` 

- `port_speed=100,private_network_only=1,guest_disk0=LOCAL_DISK` 

This parameter is used to narrow the available results down even further. It's not necessary when selecting a VLAN, but it will help avoid errors when attempting to place an order. The only acceptable category codes are: 

- `port_speed` 

- A disk category, such as `guest_disk0` or `disk0`, with values of either `LOCAL_DISK` or `SAN_DISK` 

- `private_network_only` 

- `dual_path_network` 

For most customers, it's sufficient to only provide the first 2 parameters. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
type: "reference"
layout: "method"
mainService : "SoftLayer_Product_Order"
---
