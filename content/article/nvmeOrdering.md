---
title: "Mirrored M.2 Ordering Examples"
description: "An explanation of the required settings for ordering a Mirrored M.2 server from the API."
date: "2025-06-10"
tags:
    - "article"
    - "sldn"
    - "order"
    - "package"
    - "slcli"
---

*NOTE*: This article is for [slcli v6.2.7](https://github.com/softlayer/softlayer-python/releases/tag/v6.2.7) and [ibmcloud sl v1.5.7](https://github.com/softlayer/softlayer-cli/releases/tag/v1.5.7)


# Basics

Ordering a server with a mirrored NVMe M.2 boot drive is a little tricky. There are 2 main difference between this setup and a normal order.

1. `storageGroups` need to be defined with the NVMe array first
2. NVMe array needs to set `hardDriveCategoryCodes` and `diskControllerIndex: 1`

> The `0th` index storageGroup will be what the server boots from. It will not match the order the raid cards are ordered in.

3. You will need to have DISK_CONTROLLER_RAID (`diskControllerIndex: 0`) in your order, before DISK_CONTROLLER_RAID_1_MIRRORED_NMVE_M_2 (`diskControllerIndex: 1`). DISK_CONTROLLER_RAID uses the `disk_controller` category price, and DISK_CONTROLLER_RAID_1_MIRRORED_NMVE_M_2 uses `disk_controller1` category price when both are present in an order.

This ordering is important because otherwise the SLCLI will pick the incorrect price id, and you will get one of the errors listed below.

4. A basic order will look like this:

```bash
./slcli -v order place --verify 2U_DUAL_INTEL_XEON_SAPPHIRE_RAPIDS_FAMILY_16_DRIVES DALLAS13 \
--complex-type SoftLayer_Container_Product_Order_Hardware_Server --billing monthly \
--extras '{"hardware":[{"hostname":"test1nvme","domain":"ibm.com"}],"storageGroups":[{"arraySize":480,"arrayTypeId":2, "diskControllerIndex":1,"hardDriveCategoryCodes":["secondary_pcie_slot0","secondary_pcie_slot1"]}, {"arraySize":1920,"arrayTypeId":2,"diskControllerIndex": 0,"hardDrives":[0,1]}]}' \
AUTOMATED_NOTIFICATION MONITORING_HOST_PING NOTIFICATION_EMAIL_AND_TICKET REBOOT_KVM_OVER_IP \
UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT BANDWIDTH_0_GB 1_IP_ADDRESS \
1_GBPS_REDUNDANT_PRIVATE_NETWORK_UPLINKS DISK_CONTROLLER_RAID \
DISK_CONTROLLER_RAID_1_MIRRORED_NMVE_M_2 \
MIRRORED_NVME_M_2_OS_BOOT_480GB  256_GB_RAM_DDR5 OS_CENTOS_STREAM_9_X_64_BIT \
INTEL_INTEL_XEON_6416_UEFI_BOOT_MODE_2_70 REDUNDANT_POWER_SUPPLY  HARD_DRIVE_1_9_TB_SSD \
HARD_DRIVE_1_9_TB_SSD
```

```bash
Calling: SoftLayer_Product_Order::verifyOrder(id=None, mask='', filter='None', args=({'orderContainers': [{
'hardware': [{'hostname': 'test1nvme', 'domain': 'ibm.com'}],
'storageGroups': [
    {
        'arraySize': 480,'arrayTypeId': 2, 'diskControllerIndex': 1,
        'hardDriveCategoryCodes': ['secondary_pcie_slot0', 'secondary_pcie_slot1']
    },{
        'arraySize': 1920, 'arrayTypeId': 2, 'diskControllerIndex': 0, 'hardDrives': [0, 1]
}],
'packageId': 3137,
'quantity': 1,
'location': 1854895,
'useHourlyPricing': False,
'complexType': 'SoftLayer_Container_Product_Order_Hardware_Server',
'prices': [
    {'id': 58, 'categories': [{'categoryCode': 'response'}], 'item': {'keyName': 'AUTOMATED_NOTIFICATION'}},
    {'id': 55, 'categories': [{'categoryCode': 'monitoring'}], 'item': {'keyName': 'MONITORING_HOST_PING'}},
    {'id': 57, 'categories': [{'categoryCode': 'notification'}], 'item': {'keyName': 'NOTIFICATION_EMAIL_AND_TICKET'}},
    {'id': 906, 'categories': [{'categoryCode': 'remote_management'}], 'item': {'keyName': 'REBOOT_KVM_OVER_IP'}}, 
    {'id': 420, 'categories': [{'categoryCode': 'vpn_management'}], 'item': {'keyName': 'UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT'}}, 
    {'id': 22505, 'categories': [{'categoryCode': 'bandwidth'}], 'item': {'keyName': 'BANDWIDTH_0_GB'}}, 
    {'id': 21, 'categories': [{'categoryCode': 'pri_ip_addresses'}], 'item': {'keyName': '1_IP_ADDRESS'}}, 
    {'id': 14023, 'categories': [{'categoryCode': 'port_speed'}], 'item': {'keyName': '1_GBPS_REDUNDANT_PRIVATE_NETWORK_UPLINKS'}}, 
    {'id': 22484, 'categories': [{'categoryCode': 'disk_controller'}], 'item': {'keyName': 'DISK_CONTROLLER_RAID'}}, 
    {'id': 306531, 'categories': [{'categoryCode': 'disk_controller1'}], 'item': {'keyName': 'DISK_CONTROLLER_RAID_1_MIRRORED_NMVE_M_2'}}, 
    {'id': 311834, 'categories': [{'categoryCode': 'pcie_slot0'}], 'item': {'keyName': 'MIRRORED_NVME_M_2_OS_BOOT_480GB'}}, 
    {'id': 301502, 'categories': [{'categoryCode': 'ram'}], 'item': {'keyName': '256_GB_RAM_DDR5'}}, 
    {'id': 307539, 'categories': [{'categoryCode': 'os'}], 'item': {'keyName': 'OS_CENTOS_STREAM_9_X_64_BIT'}}, 
    {'id': 313326, 'categories': [{'categoryCode': 'server'}], 'item': {'keyName': 'INTEL_INTEL_XEON_6416_UEFI_BOOT_MODE_2_70'}}, 
    {'id': 50221, 'categories': [{'categoryCode': 'power_supply'}], 'item': {'keyName': 'REDUNDANT_POWER_SUPPLY'}}, 
    {'id': 300316, 'categories': [{'categoryCode': 'disk0'}], 'item': {'keyName': 'HARD_DRIVE_1_9_TB_SSD'}}, 
    {'id': 300316, 'categories': [{'categoryCode': 'disk0'}], 'item': {'keyName': 'HARD_DRIVE_1_9_TB_SSD'}}
]
}]}) limit=None, offset=None)

┌─────────────────────────────────────────────────────┬────────────────────────────────────────────────┬──────┐
│                       keyName                       │                  description                   │ cost │
├─────────────────────────────────────────────────────┼────────────────────────────────────────────────┼──────┤
│               AUTOMATED_NOTIFICATION                │             Automated Notification             │  0   │
│                MONITORING_HOST_PING                 │                   Host Ping                    │  0   │
│            NOTIFICATION_EMAIL_AND_TICKET            │                Email and Ticket                │  0   │
│                 REBOOT_KVM_OVER_IP                  │              Reboot / KVM over IP              │  0   │
│ UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT │            Unlimited SSL VPN Users             │  0   │
│                   BANDWIDTH_0_GB                    │            0 GB Bandwidth Allotment            │  0   │
│                    1_IP_ADDRESS                     │                  1 IP Address                  │  0   │
│      1_GBPS_REDUNDANT_PRIVATE_NETWORK_UPLINKS       │    1 Gbps Redundant Private Network Uplinks    │  0   │
│                DISK_CONTROLLER_RAID                 │                      RAID                      │  0   │
│      DISK_CONTROLLER_RAID_1_MIRRORED_NMVE_M_2       │           RAID 1 (Mirrored NVMe M.2)           │  0   │
│           MIRRORED_NVME_M_2_OS_BOOT_480GB           │     Mirrored NVMe M.2 for OS Boot (480GB)      │  0   │
│                   256_GB_RAM_DDR5                   │                   256 GB RAM                   │  0   │
│             OS_CENTOS_STREAM_9_X_64_BIT             │           CentOS Stream 9.x (64 bit)           │  0   │
│      INTEL_INTEL_XEON_6416_UEFI_BOOT_MODE_2_70      │ Dual Intel Xeon Gold 6416H (24 Cores, 2.7 GHz) │  0   │
│               REDUNDANT_POWER_SUPPLY                │             Redundant Power Supply             │  0   │
│                HARD_DRIVE_1_9_TB_SSD                │                   1.9TB SSD                    │  0   │
│                HARD_DRIVE_1_9_TB_SSD                │                   1.9TB SSD                    │  0   │
└─────────────────────────────────────────────────────┴────────────────────────────────────────────────┴──────┘
```

From there you can customize your server how you like.

# Extras Explained

Here I have 2 raid arrays. 

0. Is the NVMe array in RAID1. I have to specify `secondary_pcie_slot0` / `secondary_pcie_slot1` to let the API know what drives to attach to this card. `diskControllerIndex` is 1, because I want it to use the second raid card on my order, `DISK_CONTROLLER_RAID_1_MIRRORED_NMVE_M_2` in this case.
1. This is for my other drives I'm adding, again in a RAID1. `diskControllerIndex` is 0, because I want it to use the first raid card on my order, `DISK_CONTROLLER_RAID` in this case.
2. [Advanced Bare Metal Ordering](https://sldn.softlayer.com/python/orderBareMetal/) has some more example of how to setup raid arrays.


```json
{
    "hardware": [
        {
            "hostname": "test1nvme",
            "domain": "ibm.com"
        }
    ],
    "storageGroups": [
        {
            "arraySize": 480,
            "arrayTypeId": 2,
            "diskControllerIndex": 1,
            "hardDriveCategoryCodes": [
                "secondary_pcie_slot0",
                "secondary_pcie_slot1"
            ]
        },
        {
            "arraySize": 1920,
            "arrayTypeId": 2,
            "diskControllerIndex": 0,
            "hardDrives": [0,1]
        }
    ]
}
```


# Common Errors

## Only 1 RAID card

This order works, but since it only specifies 1 raid card, the other drives will not get attached properly, and will lilely require Datacenter manual intervention to fix this order. Or the drives will be in a JBOD array.


```bash
slcli -v order place --verify 2U_DUAL_INTEL_XEON_SAPPHIRE_RAPIDS_FAMILY_16_DRIVES DALLAS13 \
--complex-type SoftLayer_Container_Product_Order_Hardware_Server --billing monthly \
--extras '{"hardware":[{"hostname":"test1nvme","domain":"ibm.com"}],"storageGroups":[{"arraySize":480,"arrayTypeId":2,"diskControllerIndex":0,"hardDriveCategoryCodes":["secondary_pcie_slot0","secondary_pcie_slot1"]},{"arraySize":1920,"arrayTypeId":2, "hardDrives":[0,1]}]}' \
AUTOMATED_NOTIFICATION MONITORING_HOST_PING NOTIFICATION_EMAIL_AND_TICKET REBOOT_KVM_OVER_IP \
UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT BANDWIDTH_0_GB 1_IP_ADDRESS \
1_GBPS_REDUNDANT_PRIVATE_NETWORK_UPLINKS DISK_CONTROLLER_RAID_1_MIRRORED_NMVE_M_2 \
MIRRORED_NVME_M_2_OS_BOOT_480GB  256_GB_RAM_DDR5 OS_CENTOS_STREAM_9_X_64_BIT \
INTEL_INTEL_XEON_6416_UEFI_BOOT_MODE_2_70 REDUNDANT_POWER_SUPPLY  HARD_DRIVE_1_9_TB_SSD \
HARD_DRIVE_1_9_TB_SSD
```
```
┌─────────────────────────────────────────────────────┬────────────────────────────────────────────────┬──────┐
│                       keyName                       │                  description                   │ cost │
├─────────────────────────────────────────────────────┼────────────────────────────────────────────────┼──────┤
│               AUTOMATED_NOTIFICATION                │             Automated Notification             │  0   │
│                MONITORING_HOST_PING                 │                   Host Ping                    │  0   │
│            NOTIFICATION_EMAIL_AND_TICKET            │                Email and Ticket                │  0   │
│                 REBOOT_KVM_OVER_IP                  │              Reboot / KVM over IP              │  0   │
│ UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT │            Unlimited SSL VPN Users             │  0   │
│                   BANDWIDTH_0_GB                    │            0 GB Bandwidth Allotment            │  0   │
│                    1_IP_ADDRESS                     │                  1 IP Address                  │  0   │
│      1_GBPS_REDUNDANT_PRIVATE_NETWORK_UPLINKS       │    1 Gbps Redundant Private Network Uplinks    │  0   │
│      DISK_CONTROLLER_RAID_1_MIRRORED_NMVE_M_2       │           RAID 1 (Mirrored NVMe M.2)           │  0   │
│           MIRRORED_NVME_M_2_OS_BOOT_480GB           │     Mirrored NVMe M.2 for OS Boot (480GB)      │  0   │
│                   256_GB_RAM_DDR5                   │                   256 GB RAM                   │  0   │
│             OS_CENTOS_STREAM_9_X_64_BIT             │           CentOS Stream 9.x (64 bit)           │  0   │
│      INTEL_INTEL_XEON_6416_UEFI_BOOT_MODE_2_70      │ Dual Intel Xeon Gold 6416H (24 Cores, 2.7 GHz) │  0   │
│               REDUNDANT_POWER_SUPPLY                │             Redundant Power Supply             │  0   │
│                HARD_DRIVE_1_9_TB_SSD                │                   1.9TB SSD                    │  0   │
│                HARD_DRIVE_1_9_TB_SSD                │                   1.9TB SSD                    │  0   │
└─────────────────────────────────────────────────────┴────────────────────────────────────────────────┴──────┘
```
##  Disk controller #1 is used by storage groups but it does not have a price.

`DISK_CONTROLLER_RAID` is missing from the order

```bash
slcli -v order place --verify 2U_DUAL_INTEL_XEON_SAPPHIRE_RAPIDS_FAMILY_16_DRIVES DALLAS13 \
--complex-type SoftLayer_Container_Product_Order_Hardware_Server --billing monthly \
--extras '{"hardware":[{"hostname":"test1nvme","domain":"ibm.com"}],"storageGroups":[{"arraySize":1920,"arrayTypeId":2,"diskControllerIndex": 0,"hardDrives":[0,1]},{"arraySize":480,"arrayTypeId":2,"diskControllerIndex":1,"hardDriveCategoryCodes":["secondary_pcie_slot0","secondary_pcie_slot1"]}]}' \
AUTOMATED_NOTIFICATION MONITORING_HOST_PING NOTIFICATION_EMAIL_AND_TICKET REBOOT_KVM_OVER_IP \
UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT BANDWIDTH_0_GB 1_IP_ADDRESS \
1_GBPS_REDUNDANT_PRIVATE_NETWORK_UPLINKS DISK_CONTROLLER_RAID_1_MIRRORED_NMVE_M_2 \
MIRRORED_NVME_M_2_OS_BOOT_480GB  256_GB_RAM_DDR5 OS_CENTOS_STREAM_9_X_64_BIT \
INTEL_INTEL_XEON_6416_UEFI_BOOT_MODE_2_70 REDUNDANT_POWER_SUPPLY  HARD_DRIVE_1_9_TB_SSD \
HARD_DRIVE_1_9_TB_SSD
```
SoftLayerAPIError(500): Disk controller #1 is used by storage groups but it does not have a price.


## Unable to add RAID because a Disk Controller price has already been added.

This is caused because older versions of the `slcli`/`ibmcloud sl` are not able to lookup the correct price if there are 2 raid cards in an order.

```bash
./slcli -v order place --verify 2U_DUAL_INTEL_XEON_SAPPHIRE_RAPIDS_FAMILY_16_DRIVES DALLAS13 \
--complex-type SoftLayer_Container_Product_Order_Hardware_Server --billing monthly \
--extras '{"hardware":[{"hostname":"test1nvme","domain":"ibm.com"}],"storageGroups":[{"arraySize":1920,"arrayTypeId":2,"diskControllerIndex": 0,"hardDrives":[0,1]},{"arraySize":480,"arrayTypeId":2,"diskControllerIndex":1,"hardDriveCategoryCodes":["secondary_pcie_slot0","secondary_pcie_slot1"]}]}' \
AUTOMATED_NOTIFICATION MONITORING_HOST_PING NOTIFICATION_EMAIL_AND_TICKET REBOOT_KVM_OVER_IP \
UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT BANDWIDTH_0_GB 1_IP_ADDRESS \
1_GBPS_REDUNDANT_PRIVATE_NETWORK_UPLINKS DISK_CONTROLLER_RAID \
DISK_CONTROLLER_RAID_1_MIRRORED_NMVE_M_2 \
MIRRORED_NVME_M_2_OS_BOOT_480GB  256_GB_RAM_DDR5 OS_CENTOS_STREAM_9_X_64_BIT \
INTEL_INTEL_XEON_6416_UEFI_BOOT_MODE_2_70 REDUNDANT_POWER_SUPPLY  HARD_DRIVE_1_9_TB_SSD \
HARD_DRIVE_1_9_TB_SSD 
```
SoftLayerAPIError(500): Unable to add RAID because a Disk Controller price has already been added.


## SoftLayerAPIError(500): A storage group with M.2 drive(s) must be the primary storage group.

Storage groups are in the wrong order.
```bash
slcli -v order place --verify 2U_DUAL_INTEL_XEON_SAPPHIRE_RAPIDS_FAMILY_16_DRIVES DALLAS13 \
--complex-type SoftLayer_Container_Product_Order_Hardware_Server --billing monthly \
--extras '{"hardware":[{"hostname":"test1nvme","domain":"ibm.com"}],"storageGroups":[{"arraySize":1920,"arrayTypeId":2,"diskControllerIndex": 0,"hardDrives":[0,1]},{"arraySize":480,"arrayTypeId":2,"diskControllerIndex":1,"hardDriveCategoryCodes":["secondary_pcie_slot0","secondary_pcie_slot1"]}]}' \
AUTOMATED_NOTIFICATION MONITORING_HOST_PING NOTIFICATION_EMAIL_AND_TICKET REBOOT_KVM_OVER_IP \
UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT BANDWIDTH_0_GB 1_IP_ADDRESS \
1_GBPS_REDUNDANT_PRIVATE_NETWORK_UPLINKS DISK_CONTROLLER_RAID \
DISK_CONTROLLER_RAID_1_MIRRORED_NMVE_M_2 \
MIRRORED_NVME_M_2_OS_BOOT_480GB  256_GB_RAM_DDR5 OS_CENTOS_STREAM_9_X_64_BIT \
INTEL_INTEL_XEON_6416_UEFI_BOOT_MODE_2_70 REDUNDANT_POWER_SUPPLY  HARD_DRIVE_1_9_TB_SSD \
HARD_DRIVE_1_9_TB_SSD
```
SoftLayerAPIError(500): A storage group with M.2 drive(s) must be the primary storage group.
