---
title: "Ordering with KeyNames"
description: "Examples on how to order anything in the catalog with the proper package and item names."
date: "2018-01-15"
classes: 
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Item"
    - "SoftLayer_Product_Order"
tags:
    - "order"
    - "pricing"
    - "hardware"
    - "package"
    - "bare-metal"
---

Version  [5.4.0](https://github.com/softlayer/softlayer-python/releases/tag/v5.4.0) of the Softlayer-python project introducted some managers and CLI functions that greatly simplify the ordering processes via the api.

Building a package still requires a few steps however.

### 1. Find the package name

```
slcli order package-list
```

The most common packages are the following:

|Description | Package KeyName | Package Type |
| --- | --- | --- |
| Additional Products | ADDITIONAL_PRODUCTS | ADDITIONAL_SERVICES |
| Cloud Server | CLOUD_SERVER | VIRTUAL_SERVER_INSTANCE|
|Network Gateway Appliance|NETWORK_GATEWAY_APPLIANCE |BARE_METAL_GATEWAY |
|Load Balancers|LOAD_BALANCERS|ADDITIONAL_SERVICES_LOAD_BALANCER |
|Bare Metal Server| BARE_METAL_SERVER|BARE_METAL_CPU_FAST_PROVISION|
|POWER8 TULETA|IBM_POWER_8 |BARE_METAL_POWER_CPU|
|Object Storage| OBJECT_STORAGE|ADDITIONAL_SERVICES_OBJECT_STORAGE|
|Firewall |FIREWALL |ADDITIONAL_SERVICES_FIREWALL|
|Storage As A Service (StaaS) |STORAGE_AS_A_SERVICE_STAAS |STORAGE_AS_A_SERVICE |
|Load Balancer As A Service (LBaaS) |LBAAS |LOAD_BALANCER_AS_A_SERVICE|
|Dedicated Host |DEDICATED_HOST |DEDICATED_HOST |
|Public Virtual Server  |PUBLIC_CLOUD_SERVER |VIRTUAL_SERVER_INSTANCE|
  
Once we have selected a package we need to find out where we can order this package.

### 2. Package locations
```
slcli order package-locations BARE_METAL_SERVER
```

| id | short name | description | keyName |
| --- | --- | --- | --- |
|265592  | ams01 | AMS01 - Amsterdam   |    AMSTERDAM
|814994 |  ams03 | AMS03 - Amsterdam  |     AMSTERDAM03
|1004997 | che01 | CHE01 - Chennai    |     CHENNAI

Find the keyName for the location you want to order in. Packages may still be sold out in a location, so be on the lookout for that.

### 3. Items and Categories
Every package has certain item categories that need to be included in an order. You can find these with 
```
slcli order category-list BARE_METAL_SERVER
```

Then find the actual items in the category.

```
slcli order item-list BARE_METAL_SERVER
```

Create a list of items you want to order. If you want multiple disks (or GPU), you should have 1 item in your list per disk you want to add. Disks are attached in order that they appear on the order form.

#### Presets
BARE_METAL_SERVER orders require a preset. These can be ordered hourly.

```
slcli order preset-list BARE_METAL_SERVER
```


### 4. Getting ready to order.
The last thing to note is the --extras and --complex-type options.

--Extras are going to match up to things like Vlans, subnets, ssh keys etc. Basically anything in the order container that ISN'T prices. Supported fields correstpond to the SoftLayer_Container_Product_Order data type. Needs to be valid JSON

```
--extras '{"hardware": [{"hostname" : "testOrder1", "domain": "cgallo.com"}], "sshKeys" : [87634], "tags": "cgallo, test"}'
```

--complex-type should match up with something that starts with SoftLayer_Container_Product_Order_

[SoftLayer_Container_Product_Order_Hardware_Server](http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server) for bare metal servers, but there are others that may need to be selected. SLDN has a complete list of all supported containers.


### 5. Testing an order.

the --verify option will not actually place an order, just insure the order is mostly correct. You may still run into when actually placing the order however. Such as being unable to find IDs for ssh keys, vlans, etc, or being out of stock of an offering.

```bash
slcli --really order place --verify --preset D2620V4_64GB_2X1TB_SATA_RAID_1 BARE_METAL_SERVER  TORONTO  \
    OS_UBUNTU_16_04_LTS_XENIAL_XERUS_64_BIT \
    BANDWIDTH_0_GB_2  \
    1_GBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS  \
    REBOOT_KVM_OVER_IP 1_IP_ADDRESS  \
    UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT \
    --extras '{"hardware": [{"hostname" : "testOrder1", "domain": "cgallo.com"}], "sshKeys" : [87634], "tags": "cgallo, test"}' \
     --complex-type SoftLayer_Container_Product_Order_Hardware_Server
```


An example without using a preset
```bash
slcli order place --verify --billing monthly DUAL_E52600_V4_4_DRIVES DALLAS13 \
    BANDWIDTH_500_GB \
    HARD_DRIVE_1_00_TB_SATA_2 \
    DISK_CONTROLLER_NONRAID \
    MONITORING_HOST_PING \
    NOTIFICATION_EMAIL_AND_TICKET \
    OS_CENTOS_7_X_64_BIT \
    1_GBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS \
    1_IP_ADDRESS \
    1_IPV6_ADDRESS  \
    RAM_128_GB_DDR4_2133_ECC_REG \
    REBOOT_KVM_OVER_IP \
    AUTOMATED_NOTIFICATION \
    INTEL_INTEL_XEON_E52690_V4_2_60 \
    UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT \
    NESSUS_VULNERABILITY_ASSESSMENT_REPORTING \
    --extras '{"hardware": [{"hostname" : "testOrder1", "domain": "cgallo.com"}], "sshKeys" : [87634], "tags": "cgallo, test"}'  \
    --complex-type SoftLayer_Container_Product_Order_Hardware_Server
```
