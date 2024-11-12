---
title: "Understanding and building an order using the Softlayer order CLI"
description: "In version 5.4.0 of softlayer-python, there is a new slcli command for placing IaaS cloud server orders using the API. This command can also be used to place orders for products that are normally ordered through the IBM Cloud infrastructure customer portal."
date: "2018-03-12"
author: "rrossiter"
tags:
    - "article"
    - "slcli"
    - "ordering"
    - "order"
---


In version 5.4.0 of [softlayer-python](https://github.com/softlayer/softlayer-python), there is a new slcli command for placing IaaS cloud server orders using the API. This command can also be used to place orders for products that are normally ordered through the IBM Cloud infrastructure customer portal. There are multiple helpers to assist you in creating a specific order. In these examples, you will learn how to:

* Build an order
  1.  Understand the order structure
  2.  Search for server packages
  3. Identify categories of items
  4. Verify the order
  5. Place the order
* Place an order programmatically using Python.


## [Build an order](#build_order) {#build_order .anchor-link}

### Step 1: Understand the order structure

In the SoftLayer API, an order can consist of multiple order containers. For simplicity, the order CLI only works with one order container, so in these examples and explanations, the terms “order container” and “order” are synonymous.

A package is the first component to look for when placing an order. Packages are divided among the different top-level products available for ordering in SoftLayer. Some example packages are *CLOUD_SERVER* for VSIs, *BARE_METAL_SERVER* for bare metal servers, and *STORAGE_AS_A_SERVICE_STAAS* for Storage-as-a-Service. Within a package, there are items that are subdivided into categories. Some packages have presets for your convenience and others require that you specify items individually.  If a package’s category is required, an item from that category must be chosen to order the package.  Depending on the category, items within the category are mutually exclusive (for example, you can’t order both 8 GB and 16 GB of RAM for a VSI). Finally, each order must have an associated location (datacenter).

![packages](/img/articles/Order_Structure.png)

When using the order CLI, we build an order from the top (package) to the bottom (items). You can use the slcli order package-list to find the package you want to order. A --keyword option is provided to perform some simple searching for filtering out packages, making it easier to find the package you need. For this example we will build a bare metal server order.

{{< highlight shell >}}
$ slcli order package-list --help
Usage: slcli order package-list [OPTIONS]

  List packages that can be ordered via the placeOrder API.

  Example:
      # List out all packages for ordering
      slcli order package-list

  Keywords can also be used for some simple filtering functionality to help
  find a package easier.

  Example:
     # List out all packages with "server" in the name
      slcli order package-list --keyword server

Options:
  --keyword TEXT  A word (or string) used to filter package names.
  -h, --help      Show this message and exit.

{{< /highlight >}}


### Step 2: Search for server packages


We can use the “server” keyword to search for server packages:

```
$ slcli order package-list --keyword "Bare Metal"
:.....................:.....................:
:         name        :       keyName       :
:.....................:.....................:
: Bare Metal Instance : BARE_METAL_INSTANCE :
:  Bare Metal Server  :  BARE_METAL_SERVER  :
:.....................:.....................:
```

We will be using the *BARE_METAL_SERVER* package for this order. Bare metal servers offer preset configurations, so we will find and use one for our order. The preset-list command needs a package keyname (*BARE_METAL_SERVER*) for listing the presets. There is also a --keyword option for filtering the returned presets if needed.

```
$ slcli order preset-list BARE_METAL_SERVER
:.............................................:...............................................:.................................................................:
:                     name                    :                    keyName                    :                           description                           :
:.............................................:...............................................:.................................................................:
:         S1270 32GB 1X1TBSATA NORAID         :          S1270_32GB_1X1TBSATA_NORAID          :      Single Xeon 1270, 32GB Ram, 1x1TB SATA disks, Non-RAID     :
:         S1270 32GB 2X960GBSSD NORAID        :          S1270_32GB_2X960GBSSD_NORAID         :     Single Xeon 1270, 32GB Ram, 2x960GB SSD disks, Non-RAID     :
:         D2690 128GB 2X600GBSAS RAID1        :         D2690_128GB_2X600GBSAS_RAID1_2        :       Dual Xeon 2690, 128GB Ram, 2x600GB SAS disks, RAID1       :
:        D2690 256GB 4X600GBSAS RAID10        :     D2690_256GB_4X600GBSAS_RAID10_RAID_10     :       Dual Xeon 2690, 256GB Ram, 4x600GB SAS disks, RAID10      :
:        D2620v4 64GB 1X1TBSATA NORAID        :         D2620V4_64GB_1X1TBSATA_NORAID         :      Dual Xeon 2620v4, 64GB Ram, 1x1TB SATA disks, Non-RAID     :
:     D2620 128GB 2X1T SATA RAID 1xM60 GPU    :     D2620_128GB_2X1TB_SATA_RAID_1_M60_GPU1    : Dual Xeon 2620, 128GB Ram, 2X1TB SATA disks, RAID 1   1xM60 GPU :
:    D2690 256GB 2x4TB SATA RAID1 2xM60 GPU   : D2690_256GB_2X4TB_SATA_RAID1_2XM60_GPU_RAID_1 :        Dual Xeon 2690, 256GB Ram, 2X4TB SATA disk, RAID 1       :
:       D2690v4 128GB 2X600GB SAS RAID 1      :        D2690V4_128GB_2X600GB_SAS_RAID_1       :      Dual Xeon 2690v4, 128GB Ram, 2x600GB SAS disks, RAID1      :
:        D2620v4 64GB 2X1TB SATA RAID 1       :         D2620V4_64GB_2X1TB_SATA_RAID_1        :       Dual Xeon 2620v4, 64GB Ram, 2x1TB SATA disks, RAID1       :
: D2620v4 128GB 2X800GB SSD RAID 1 K80 GPU(2) :   D2620V4_128GB_2X800GB_SSD_RAID_1_K80_GPU2   :      Dual Xeon 2620v4, 128GB Ram, 2x800GB SSD disks, RAID1      :
:  D2690v4 128GB 2X4TB SATA RAID 1 K2 GPU(2)  :    D2690V4_128GB_2X4TB_SATA_RAID_1_K2_GPU2    :            D2690v4 128GB 2x4TB SATA RAID 1 K2 GPU(2)            :
:      D2690v4 256GB 4X600GB SAS RAID 10      :       D2690V4_256GB_4X600GB_SAS_RAID_10       :     Dual Xeon 2690v4, 256GB Ram, 4x600GB SAS disks, RAID 10     :
:.............................................:...............................................:.................................................................:

```


### Step 3: Identify categories of items


For this example, we will use the *S1270_32GB_1X1TBSATA_NORAID* preset. Now let’s find the categories of items we need to set for a bare metal order.

```
slcli order category-list BARE_METAL_SERVER
:........................................:.......................:............:
:                  name                  :      categoryCode     : isRequired :
:........................................:.......................:............:
:                 Server                 :         server        :     Y      :
:        New Cloud Customer Setup        :   new_customer_setup  :     N      :
:               Surcharges               :        premium        :     N      :
:            Operating System            :           os          :     Y      :
:                  RAM                   :          ram          :     Y      :
:            Disk Controller             :    disk_controller    :     Y      :
:            First Hard Drive            :         disk0         :     Y      :
:           Second Hard Drive            :         disk1         :     N      :
:            Third Hard Drive            :         disk2         :     N      :
:           Fourth Hard Drive            :         disk3         :     N      :
:            Public Bandwidth            :       bandwidth       :     Y      :
:           Uplink Port Speeds           :       port_speed      :     Y      :
:           Remote Management            :   remote_management   :     Y      :
:          Primary IP Addresses          :    pri_ip_addresses   :     Y      :
:     Public Secondary IP Addresses      :    sec_ip_addresses   :     N      :
:              Power Supply              :      power_supply     :     N      :
:      Public Static IPv6 Addresses      : static_ipv6_addresses :     N      :
:         Primary IPv6 Addresses         :   pri_ipv6_addresses  :     N      :
:                 EVault                 :         evault        :     N      :
:        Graphics Processing Unit        :          gpu0         :     N      :
:   Secondary Graphics Processing Unit   :          gpu1         :     N      :
:                 Other                  :         other         :     N      :
:    VPN Management - Private Network    :     vpn_management    :     Y      :
: Vulnerability Assessments & Management : vulnerability_scanner :     N      :
:........................................:.......................:............:
```

This is a minimal order, so we are only specifying items that are required for the order. To find the items we’re required to fill, we can use the --required option on the category-list command.

```
$ slcli order category-list BARE_METAL_SERVER --required
:..................................:...................:............:
:               name               :    categoryCode   : isRequired :
:..................................:...................:............:
:              Server              :       server      :     Y      :
:         Operating System         :         os        :     Y      :
:               RAM                :        ram        :     Y      :
:         Disk Controller          :  disk_controller  :     Y      :
:         First Hard Drive         :       disk0       :     Y      :
:         Public Bandwidth         :     bandwidth     :     Y      :
:        Uplink Port Speeds        :     port_speed    :     Y      :
:        Remote Management         : remote_management :     Y      :
:       Primary IP Addresses       :  pri_ip_addresses :     Y      :
: VPN Management - Private Network :   vpn_management  :     Y      :
:..................................:...................:............:
```


Most of these categories are already covered for us by the preset (Server, RAM, and Disk Controller, First Hard Drive). If you’re ever unsure of the required categories you may be missing in your order, you can use the place command with the --verify flag, and if any categories are missing, they will be printed out for you.

We can now select the rest of our items for our order using the item-list command. There are typically a lot of items to choose from in a package, so it is suggested to use the --category option to only retrieve the items from the category you are interested in.

```
$ slcli order item-list BARE_METAL_SERVER --category os
:.....................................................:..................................................................:
:                       keyName                       :                           description                            :
:.....................................................:..................................................................:
:       OS_RHEL_5_32_BIT_PER_PROCESSOR_LICENSING      : Red Hat Enterprise Linux 5.x (32 bit) (per-processor licensing)  :
:       OS_RHEL_6_64_BIT_PER_PROCESSOR_LICENSING      : Red Hat Enterprise Linux 6.x (64 bit) (per-processor licensing)  :
:                OS_FREEBSD_9_X_64_BIT                :                       FreeBSD 9.x (64 bit)                       :
:          OS_WINDOWS_2012_R2_FULL_STD_64_BIT         :         Windows Server 2012 R2 Standard Edition (64 bit)         :
:                OS_FREEBSD_10_X_64_BIT               :                      FreeBSD 10.x (64 bit)                       :
:                 OS_CENTOS_7_X_64_BIT                :                       CentOS 7.x (64 bit)                        :
:          OS_WINDOWS_2008_FULL_STD_64_BIT_R2         :         Windows Server 2008 R2 Standard Edition (64bit)          :
:                 OS_CENTOS_6_X_32_BIT                :                       CentOS 6.x (32 bit)                        :
:           OS_WINDOWS_2012_FULL_STD_64_BIT           :          Windows Server 2012 Standard Edition (64 bit)           :
:     OS_UBUNTU_12_04_LTS_PRECISE_PANGOLIN_64_BIT     :         Ubuntu Linux 12.04 LTS Precise Pangolin (64 bit)         :
:                OS_FREEBSD_10_X_32_BIT               :                      FreeBSD 10.x (32 bit)                       :
:                  OS_RHEL_7_1_64_BIT                 : Red Hat Enterprise Linux 7.x (64 bit)  (per-processor licensing) :
:       OS_UBUNTU_16_04_LTS_XENIAL_XERUS_64_BIT       :           Ubuntu Linux 16.04 LTS Xenial Xerus (64 bit)           :
:                 OS_CENTOS_6_X_64_BIT                :                       CentOS 6.x (64 bit)                        :
:            OS_CENTOS_7_X_MINIMAL_64_BIT_2           :              CentOS 7.x - Minimal Install (64 bit)               :
:     OS_UBUNTU_12_04_LTS_PRECISE_PANGOLIN_32_BIT     :         Ubuntu Linux 12.04 LTS Precise Pangolin (32 bit)         :
:                OS_NO_OPERATING_SYSTEM               :                       No Operating System                        :
:             OS_CENTOS_6_X_MINIMAL_64_BIT            :              CentOS 6.x - Minimal Install (64 bit)               :
:               OS_FREEBSD_9_X_32_BIT_2               :                       FreeBSD 9.x (32 bit)                       :
:        OS_UBUNTU_14_04_LTS_TRUSTY_TAHR_32_BIT       :           Ubuntu Linux 14.04 LTS Trusty Tahr (32 bit)            :
: OS_WINDOWS_SERVER_2012_STANDARD_EDITION_64_BIT_CORE :         Windows Server 2012 R2 Standard Edition (64 bit)         :
:        OS_WINDOWS_2008_FULL_WEB_64_BIT_R2_SP1       :            Windows Server 2008 R2 Web Edition (64bit)            :
:       OS_RHEL_5_64_BIT_PER_PROCESSOR_LICENSING      : Red Hat Enterprise Linux 5.x (64 bit) (per-processor licensing)  :
:       OS_RHEL_6_32_BIT_PER_PROCESSOR_LICENSING      : Red Hat Enterprise Linux 6.x (32 bit) (per-processor licensing)  :
:        OS_UBUNTU_14_04_LTS_TRUSTY_TAHR_64_BIT       :           Ubuntu Linux 14.04 LTS Trusty Tahr (64 bit)            :
:           OS_WINDOWS_2016_FULL_STD_64_BIT           :          Windows Server 2016 Standard Edition (64 bit)           :
:                OS_FREEBSD_11_X_64_BIT               :                      FreeBSD 11.x (64 bit)                       :
:.....................................................:..................................................................:
```


```
$slcli order item-list BARE_METAL_SERVER --category bandwidth
:.....................................:.......................................:
:               keyName               :              description              :
:.....................................:.......................................:
:            BANDWIDTH_0_GB           :             0 GB Bandwidth            :
:           BANDWIDTH_500_GB          :            500 GB Bandwidth           :
: BANDWIDTH_UNLIMITED_100_MBPS_UPLINK : Unlimited Bandwidth (100 Mbps Uplink) :
:          BANDWIDTH_1000_GB          :           1000 GB Bandwidth           :
:          BANDWIDTH_5000_GB          :           5000 GB Bandwidth           :
:          BANDWIDTH_10000_GB         :           10000 GB Bandwidth          :
:           BANDWIDTH_0_GB_2          :             0 GB Bandwidth            :
:          BANDWIDTH_20000_GB         :           20000 GB Bandwidth          :
:.....................................:.......................................:
```

```
$ slcli order item-list BARE_METAL_SERVER --category port_speed
:......................................................:..........................................................:
:                       keyName                        :                       description                        :
:......................................................:..........................................................:
:            1_GBPS_PRIVATE_NETWORK_UPLINK             :              1 Gbps Private Network Uplink               :
:           100_MBPS_PRIVATE_NETWORK_UPLINK            :             100 Mbps Private Network Uplink              :
:   10_GBPS_REDUNDANT_PUBLIC_PRIVATE_NETWORK_UPLINKS   :    10 Gbps Redundant Public & Private Network Uplinks    :
:    10_GBPS_DUAL_PRIVATE_NETWORK_UPLINKS_UNBONDED     :     10 Gbps Dual Private Network Uplinks (Unbonded)      :
:        10_MBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS        :         10 Mbps Public & Private Network Uplinks         :
:        1_GBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS         :         1 Gbps Public & Private Network Uplinks          :
:            10_MBPS_PRIVATE_NETWORK_UPLINK            :              10 Mbps Private Network Uplink              :
:      10_GBPS_REDUNDANT_PRIVATE_NETWORK_UPLINKS       :        10 Gbps Redundant Private Network Uplinks         :
:       100_MBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS        :        100 Mbps Public & Private Network Uplinks         :
:    1_GBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS_UNBONDED    :    1 Gbps Public & Private Network Uplinks (Unbonded)    :
: 10_GBPS_DUAL_PUBLIC_PRIVATE_NETWORK_UPLINKS_UNBONDED : 10 Gbps Dual Public & Private Network Uplinks (Unbonded) :
:......................................................:..........................................................:
```

```
$ slcli order item-list BARE_METAL_SERVER --category remote_management
:....................:......................:
:      keyName       :     description      :
:....................:......................:
: REBOOT_KVM_OVER_IP : Reboot / KVM over IP :
:....................:......................:
```

```
$ slcli order item-list BARE_METAL_SERVER --category pri_ip_addresses
:..............:..............:
:   keyName    : description  :
:..............:..............:
: 1_IP_ADDRESS : 1 IP Address :
:..............:..............:
```

```
$ slcli order item-list BARE_METAL_SERVER --category vpn_management
:.....................................................:.......................................................:
:                       keyName                       :                      description                      :
:.....................................................:.......................................................:
: UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT : Unlimited SSL VPN Users & 1 PPTP VPN User per account :
:.....................................................:.......................................................:
```


Some of these categories only have 1 item, so there isn’t much choice for those items. For this order, we will use the following items:

* OS_CENTOS_7_X_64_BIT
* BANDWIDTH_0_GB_2 
* 1_GBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS 
* REBOOT_KVM_OVER_IP, 1_IP_ADDRESS
* UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT


### Step 4: Verify the order


Now that we know the details of the bare metal server we will be ordering, we can try verifying the order we want to make. The place command takes in all the information for the order, and will attempt to verify the order (if --verify is specified) or place the order. We need the following information to verify our order:
 
1. Package (BARE_METAL_SERVER)
2. Location (DALLAS13)
3. Billing term (hourly)
4. Preset (S1270_32GB_1X1TBSATA_NORAID)
5. Type (SoftLayer_Container_Product_Order_Hardware_Server)

_Note_: The type information is used by the order API to determine the data that is needed in the order. For bare metal servers, this type is SoftLayer_Container_Product_Order_Hardware_Server. These types can be found on [SLDN](https://softlayer.github.com/reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server) and will typically begin with SoftLayer_Container_Product_Order.

```
$ slcli order place --verify --billing hourly BARE_METAL_SERVER DALLAS13 --preset S1270_32GB_1X1TBSATA_NORAID BANDWIDTH_0_GB_2 1_GBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS REBOOT_KVM_OVER_IP 1_IP_ADDRESS UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT OS_CENTOS_7_X_64_BIT --complex-type SoftLayer_Container_Product_Order_Hardware_Server
:.....................................................:.......................................................:......:
:                       keyName                       :                      description                      : cost :
:.....................................................:.......................................................:......:
:                   BANDWIDTH_0_GB_2                  :                     0 GB Bandwidth                    :  0   :
:        1_GBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS        :        1 Gbps Public & Private Network Uplinks        : .04  :
:                  REBOOT_KVM_OVER_IP                 :                  Reboot / KVM over IP                 :  0   :
:                     1_IP_ADDRESS                    :                      1 IP Address                     :  0   :
: UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT : Unlimited SSL VPN Users & 1 PPTP VPN User per account :  0   :
:                 OS_CENTOS_7_X_64_BIT                :                  CentOS 7.x (64 bit)                  :  0   :
:               DISK_CONTROLLER_NONRAID               :                        Non-RAID                       :  0   :
:              HARD_DRIVE_1_00_TB_SATA_2              :                      1.00 TB SATA                     : .036 :
:             INTEL_SINGLE_XEON_1270_3_50             :    Single Intel Xeon E3-1270 v3 (4 Cores, 3.50 GHz)   : .173 :
:              RAM_32_GB_DDR3_1333_REG_2              :                       32 GB RAM                       : .356 :
:.....................................................:.......................................................:......:
```

The output will show you each item being ordered, along with the cost associated with that item. If the order passes verification, that means there are no conflicting items, and all required categories have an item specified in the order. 


### Step 5: Place the order


The next step is to place the order.

```
$ slcli order place --billing hourly BARE_METAL_SERVER DALLAS13 --preset S1270_32GB_1X1TBSATA_NORAID BANDWIDTH_0_GB_2 1_GBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS REBOOT_KVM_OVER_IP 1_IP_ADDRESS UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT OS_CENTOS_7_X_64_BIT --complex-type SoftLayer_Container_Product_Order_Hardware_Server

This action will incur charges on your account. Continue? [y/N]: y

SoftLayerAPIError(SoftLayer_Exception_Order_InvalidData): Invalid data on the order for property: hardware. Hostname and domain are not set properly.
```

In the order placement, extra data is required based on the complex type. In this case, Bare Metal servers need extra hardware data to specify the hostname and domain of the server. This is specified using the --extras option. Extras are specified as a JSON-encoded string. According to the error message, we need to specify a hardware property in our extras with the hostname and domain of the server. The structure of the JSON will be:

```json
{
    "hardware": [
        {    "hostname": "<yourhostname>",
            "domain": "<yourdomain>"
        }
    ]
}
```
Now we can place the order with the extra data needed.

```
$ slcli order place --billing hourly BARE_METAL_SERVER DALLAS13 \
    --preset S1270_32GB_1X1TBSATA_NORAID BANDWIDTH_0_GB_2 \
    1_GBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS \
    REBOOT_KVM_OVER_IP \
    1_IP_ADDRESS  \
    UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT \
    OS_CENTOS_7_X_64_BIT  \
    --complex-type SoftLayer_Container_Product_Order_Hardware_Server  \
    --extras '{"hardware": [{"hostname": "test-demo", "domain": "softlayer.com"}]}'

This action will incur charges on your account. Continue? [y/N]: y

:.........:...........................:
:    name : value                     :
:.........:...........................:
:      id : 21924753                  :
: created : 2018-01-03T10:08:03-06:00 :
:  status : PENDING_APPROVAL          :
:.........:...........................:
```

We now have ordered a bare metal server!


## [Place an order programmatically with Python](#with_python) {#with_python .anchor-link}

Now that we have used the CLI to build an order with the package and items that we want, we can convert this order to Python code and programmatically place the order.

### Safety of item keynames

Using item keynames is a more hardened way of placing orders. Item IDs may change, and orders placed with hard-coded IDs may not continually work. Keynames will allow orders to consistently work, because price IDs for the order are dynamically retrieved for you. 

_Note_: If an item is removed from the ordering catalog due to deprecation, orders will still need to be updated to use the keyname of a more current item.


### Converting from CLI calls to Python code


If we take our previous example for creating a bare metal server on the CLI, we can very easily convert this over to Python code. As of version 3.4.0 of softlayer-python, functions have been added to the ordering manager for verifying and placing orders.

Here is the place order command from before:
```
$ slcli order place --billing hourly BARE_METAL_SERVER DALLAS13 --preset S1270_32GB_1X1TBSATA_NORAID BANDWIDTH_0_GB_2 1_GBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS REBOOT_KVM_OVER_IP 1_IP_ADDRESS UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT OS_CENTOS_7_X_64_BIT --complex-type SoftLayer_Container_Product_Order_Hardware_Server --extras '{"hardware": [{"hostname": "test-demo", "domain": "softlayer.com"}]}'
```

The function for place_order on the ordering manager has arguments that are like the data given to the place order command:

```python
def place_order(self, package_keyname, location, item_keynames, complex_type=None, hourly=True, preset_keyname=None, extras=None, quantity=1):
```

The Python code for placing the order is similar to the place order command:
import SoftLayer

```python
package = 'BARE_METAL_SERVER'
location = 'DALLAS13'
extras = {'hardware': [{'hostname': 'test-demo',
                        'domain': 'softlayer.com'}]}
preset = 'S1270_32GB_1X1TBSATA_NORAID'
items = ['BANDWIDTH_0_GB_2',
         '1_GBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS',
         'REBOOT_KVM_OVER_IP',
         '1_IP_ADDRESS',
         'UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT',
         'OS_CENTOS_7_X_64_BIT']
complex_type = 'SoftLayer_Container_Product_Order_Hardware_Server'

client = SoftLayer.create_client_from_env()
order_mgr = SoftLayer.OrderingManager(client)
order_mgr.verify_order(package, location, items,
                       hourly=True, preset_keyname=preset,
                       complex_type=complex_type,
                       extras=extras)

```

If you want to programmatically verify your order rather than placing it, substitute verify_order() for place_order(). Both functions use the arguments the same way.


### Converting existing Python code to use keynames


If you already place orders via Python code using hard-coded IDs, you can use this code snippet to do a one-time retrieval of the keynames from the IDs.

```python
import SoftLayer

client = SoftLayer.create_client_from_env()

package_id = 200
keyname_mask = 'mask[keyName]'
package = client['Product_Package'].getObject(id=package_id, mask=keyname_mask)
print("Package:")
print(package['keyName'])
print("\n")


prices = [1800, 274, 906, 21, 420, 44988]
keyname_mask = 'mask[keyName, prices[id]]'
keynames = []
print("Items:")
pkg_items = client['Product_Package'].getItems(id=package_id,
                                               mask=keyname_mask)
for price in prices:
    pkg_item = [i for i in pkg_items
                if price in [p['id'] for p in i['prices']]][0]
    print(pkg_item['keyName'])
```


### How to figure out capacity restrictions.

Some items have a capacity restriction, and you must select the item that matches the capacity of the server. These restrictions will generally be on the `CORE` count of your server, although some can be on the `PROCESSOR` count (number of physical CPUs). Ordering storage will also have its own type, `STORAGE` to watch out for.

#### Example:

In package `SINGLE_E31270_V3_4_DRIVES` (id=253) there are the following [items](/reference/datatypes/SoftLayer_Product_Item/).


+ The Processor

```json
{
    "capacityRestrictedProductFlag": false,
    "description": "Dual Intel Xeon E5-2690 v3 (24 Cores, 2.60 GHz)",
    "id": 6090,
    "keyName": "INTEL_XEON_2690_2_60",
    "totalPhysicalCoreCapacity": 24,
    "totalProcessorCapacity": 2,
    "prices": [
        {
            "id": 47067,
            "locationGroupId": null
        },
    ],
    "itemCategory": {
        "categoryCode": "server",
    }
},
```
Since `capacityRestrictedProductFlag` is `false`  we can select the price from this item for our order.

+ Windows Server
  
```json
{
    "capacityRestrictedProductFlag": true,
    "description": "Windows Server 2019 Standard Edition (64 bit) ",
    "id": 13385,
    "keyName": "OS_WINDOWS_2019_FULL_STD_64_BIT",
    "prices": [
        {
            "capacityRestrictionMaximum": "16",
            "capacityRestrictionMinimum": "6",
            "capacityRestrictionType": "CORE",
            "id": 229001,
            "locationGroupId": null
        },
        {
            "capacityRestrictionMaximum": "20",
            "capacityRestrictionMinimum": "20",
            "capacityRestrictionType": "CORE",
            "id": 229003,
            "locationGroupId": null
        },
        {
            "capacityRestrictionMaximum": "24",
            "capacityRestrictionMinimum": "24",
            "capacityRestrictionType": "CORE",
            "id": 229005,
            "locationGroupId": null
        }
```

Since this item has `capacityRestrictedProductFlag`, we need to check each price to see if its Minimum and Maximum are valid for the server we are ordering. The `capacityRestrictionType` is `CORE` here, so we check against the `totalPhysicalCoreCapacity` of our SERVER item. In this case we would pick price id `229005`.


+ VMware

```json
{
    "capacityRestrictedProductFlag": true,
    "description": "VMware Server Virtualization 6.5",
    "id": 10313,
    "itemCategory": {
        "categoryCode": "os",
        "id": 12,
        "name": "Operating System",
        "quantityLimit": 0,
        "sortOrder": 1
    },
    "keyName": "OS_VMWARE_SERVER_VIRTUALIZATION_6_5",
    "prices": [
        {
            "capacityRestrictionMaximum": "2",
            "capacityRestrictionMinimum": "2",
            "capacityRestrictionType": "PROCESSOR",
            "id": 201161,
            "locationGroupId": null
        }
    ],
    "totalPhysicalCoreCapacity": null,
    "totalProcessorCapacity": null
},
```

Here is an example of a `PROCESSOR` restriction. Here we would match our server item's `totalProcessorCapacity` field.


#### Other example

``` json
[{
	"id": 52227,
	"item": {
		"capacity": "3.5",
		"description": "Single Intel Xeon E3-1270 v3 (4 Cores, 3.50 GHz)",
		"totalPhysicalCoreCapacity": 4
		}
}, {
	"id": 244570,
	"item": {
		"capacity": "3.8",
		"description": "Single Intel Xeon E-2174G (4 Cores, 3.80 GHz)",
		"totalPhysicalCoreCapacity": 4
		}
}, {
    "id": 17275,
    "capacityRestrictionMaximum": "6",
    "capacityRestrictionMinimum": "6",
    "capacityRestrictionType": "CORE",
    "item": {
        "description": "Microsoft SQL Server 2012 Web Edition",
        "capacityRestrictedProductFlag": true
    }    
},
{
   "id": 17291,
   "capacityRestrictionMaximum": "4",
   "capacityRestrictionMinimum": "4",
   "capacityRestrictionType": "CORE",
   "item": {
      "keyName": "DATABASE_MICROSOFT_SQL_SERVER_2012_STANDARD",
      "capacityRestrictedProductFlag": true
         }
    }

]
```

If you select a priceId that has a capacity restriction, but do not select the right price, you will get an error similar to this:

> SoftLayer_Exception_Public: Windows Server 2016 Standard Edition (64 bit) (28 Cores), price ID# 179935, has a Cores capacity restriction that does not match the capacity of Dual Intel Xeon E5-2620 v4 (16 Cores, 2.10 GHz), price ID# 177639



## Various Ordering Examples

Order from package SINGLE_E31270_2_DRIVES, no raid, with a specific backend network vlan.
```
slcli -vvv order place SINGLE_E31270_V3_4_DRIVES DALLAS13 \
INTEL_SINGLE_XEON_1270_3_50 \
RAM_32_GB_DDR3_1333_REG_2 \
OS_RHEL_7_1_64_BIT  \
DISK_CONTROLLER_NONRAID \
HARD_DRIVE_1_00_TB_SATA_2 \
BANDWIDTH_500_GB \
1_GBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS \
1_IP_ADDRESS \
REBOOT_KVM_OVER_IP \
NOTIFICATION_EMAIL_AND_TICKET \
MONITORING_HOST_PING_AND_TCP_SERVICE UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT \
AUTOMATED_NOTIFICATION \
--complex-type SoftLayer_Container_Product_Order_Hardware_Server \
--extras '{"hardware":[{"domain":"test-cgallo.com","hostname":"testOrderCANCEL"},{"primaryBackendNetworkComponent":{"networkVlan":{"id":2257307}}}]}' \
 --billing monthly --verify

```

Turns into:

```
curl -u $SL_USER:$SL_APIKEY -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress" -d '{"parameters": [{"orderContainers": [{"hardware": [{"domain": "test-cgallo.com", "hostname": "testOrderCANCEL"}, {"primaryBackendNetworkComponent": {"networkVlan": {"id": 2257307}}}], "packageId": 257, "quantity": 1, "location": 1854895, "useHourlyPricing": false, "complexType": "SoftLayer_Container_Product_Order_Hardware_Server", "prices": [{"id": 49515}, {"id": 49415}, {"id": 48999}, {"id": 876}, {"id": 49759}, {"id": 50357}, {"id": 274}, {"id": 21}, {"id": 906}, {"id": 418}, {"id": 57}, {"id": 56}, {"id": 420}, {"id": 58}]}]}]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Order/verifyOrder.json'
```


## [Step by Step Example with ibmcloud CLI](#step_by_step) {#step_by_step .anchor-link}
These commands will use the `ibmcloud sl` command, but it works the same way as `slcli`. The only big difference is `ibmcloud` requires Items be a comma seperated list, where `slcli` requires them be space seperated.

Here we want to order a Cascade Lake Dual Xeon server.


#### Get the package.

```
$ ibmcloud sl order package-list | grep -i Cascade
1105   Dual Intel Xeon Processor Cascade Lake Scalable Family (4 Drives)         DUAL_INTEL_XEON_PROCESSOR_CASCADE_LAKE_SCALABLE_FAMILY_4_DRIVES   BARE_METAL_CPU
1107   Dual Intel Xeon Processor Cascade Lake Scalable Family (12 Drives)        DUAL_INTEL_XEON_PROC_CASCADE_LAKE_SCALABLE_FAMILY_12_DRIVES       BARE_METAL_CPU
```

#### Get the Items

```
ibmcloud sl order item-list DUAL_INTEL_XEON_PROCESSOR_CASCADE_LAKE_SCALABLE_FAMILY_4_DRIVES
```

From that list you'll need to select the Processor (`INTEL_XEON_4210_2_20`), RAM (`RAM_32_GB_DDR4_2133_ECC_NON_REG`), OS (`OS_DEBIAN_10_X_BUSTER_MINIMAL_64_BIT`), Port Speed (`1_GBPS_REDUNDANT_PUBLIC_PRIVATE_NETWORK_UPLINKS`, assuming you wanted redundany, but unbonded is an option of too), RAID (`DISK_CONTROLLER_RAID`), DISKS ( 2 of `HARD_DRIVE_2_00_TB_SATA_2` or `HARD_DRIVE_1_9_TB_SSD` if you wanted the SSD drives) and a few other required items (`BANDWIDTH_1000_GB`, `REBOOT_KVM_OVER_IP`, `1_IP_ADDRESS`, `UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT`, `NOTIFICATION_EMAIL_AND_TICKET `, `AUTOMATED_NOTIFICATION`, `MONITORING_HOST_PING`)


#### (Optional) SSH Keys

The `ibmcloud sl` command doesn't have a built in way of showing ssh-keys (The `SLCLI`, which is what the `ibmcloud sl` command is based from, does if that is useful: https://softlayer-python.readthedocs.io/en/latest/cli/sshkey/). However you can still get the ssh key id from the following:

`ibmcloud sl call-api SoftLayer_Account getSshKeys`
you'll need the `id` field that corresponds to the SSH key you want installed on the server.

#### (Optional) Subnets and Vlans

You'll need the subnet and vlan ID for provisioning. 
`ibmcloud sl subnet list`
`ibmcloud sl vlan list`


#### Raid Configuration

To get all the Raid Type options, use the following command:
`ibmcloud sl call-api SoftLayer_Configuration_Storage_Group_Array_Type getAllObjects` 
RAID1 is id=2

To get all the partition templates available, run the following
`ibmcloud sl call-api SoftLayer_Hardware_Component_Partition_OperatingSystem getObject --init 1 --mask="mask[partitionTemplates[data]]"`
Linux basic is id=1 (1G /swap, .25G /boot, / set to 'grow')

#### "Extras"

Extras is a JSON string that corresponds to https://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server/
It is here you will put your SSH keys, post provision scripts, domain/hostname and other bits of information.

```
{
    "hardware":[{
        "hostname":"ordering-test",
        "domain":"ibm.com",
        "primaryBackendNetworkComponent": {"networkVlan": {"primarySubnet":{"id": 1942931}}},
        "primaryNetworkComponent": {"networkVlan": {"id": 2843340}},
    }],
    "storageGroups":[{
        "arrayTypeId": 2,
        "arraySize": 2000,
        "hardDrives": [0,1],
        "partitionTemplateId": 1
    }],
    "sshKeys": [{"sshKeyIds":[87634,92868]}],
    "provisionScripts": ["https://pastebin.com/raw/SCp607Tm"]
}
```


#### Everything Together

```
ibmcloud sl order place DUAL_INTEL_XEON_PROCESSOR_CASCADE_LAKE_SCALABLE_FAMILY_4_DRIVES  DALLAS13  INTEL_XEON_4210_2_20,RAM_32_GB_DDR4_2133_ECC_NON_REG,OS_DEBIAN_10_X_BUSTER_MINIMAL_64_BIT,1_GBPS_REDUNDANT_PUBLIC_PRIVATE_NETWORK_UPLINKS,DISK_CONTROLLER_RAID,HARD_DRIVE_2_00_TB_SATA_2,HARD_DRIVE_2_00_TB_SATA_2,BANDWIDTH_1000_GB,REBOOT_KVM_OVER_IP,1_IP_ADDRESS,UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT,NOTIFICATION_EMAIL_AND_TICKET,MONITORING_HOST_PING,AUTOMATED_NOTIFICATION --complex-type SoftLayer_Container_Product_Order_Hardware_Server --extras '{"hardware":[{"hostname":"cgallo-test","domain":"cgallo.com","primaryBackendNetworkComponent": {"networkVlan": {"primarySubnet":{"id": 1942931}}},"primaryNetworkComponent": {"networkVlan": {"id": 2848660}}}],"storageGroups":[{"arrayTypeId": 2,"arraySize": 2000,"hardDrives": [0,1],"partitionTemplateId": 1}],"sshKeys": [{"sshKeyIds":[87634,92868]}],"provisionScripts": ["https://pastebin.com/raw/SCp607Tm"]}' --billing monthly --verify
```


```
slcli order place DUAL_INTEL_XEON_PROCESSOR_CASCADE_LAKE_SCALABLE_FAMILY_4_DRIVES  DALLAS13  INTEL_XEON_4210_2_20 RAM_32_GB_DDR4_2133_ECC_NON_REG OS_DEBIAN_10_X_BUSTER_MINIMAL_64_BIT 1_GBPS_REDUNDANT_PUBLIC_PRIVATE_NETWORK_UPLINKS DISK_CONTROLLER_RAID HARD_DRIVE_2_00_TB_SATA_2 HARD_DRIVE_2_00_TB_SATA_2 BANDWIDTH_1000_GB REBOOT_KVM_OVER_IP 1_IP_ADDRESS UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT NOTIFICATION_EMAIL_AND_TICKET MONITORING_HOST_PING AUTOMATED_NOTIFICATION --complex-type SoftLayer_Container_Product_Order_Hardware_Server --extras '{"hardware":[{"hostname":"cgallo-test","domain":"cgallo.com","primaryBackendNetworkComponent": {"networkVlan": {"primarySubnet":{"id": 1942931}}},"primaryNetworkComponent": {"networkVlan": {"id": 2848660}}}],"storageGroups":[{"arrayTypeId": 2,"arraySize": 2000,"hardDrives": [0,1],"partitionTemplateId": 1}],"sshKeys": [{"sshKeyIds":[87634,92868]}],"provisionScripts": ["https://pastebin.com/raw/SCp607Tm"]}' --billing monthly --verify
```


## [Portal to CLI](#portal_to_cli) {#portal_to_cli .anchor-link}


Lets say you are ordering a server, and want to automate it. For this example, we will build a server that looks like this:
![2U_QUAD_XEON_PROCESSOR_CASCADE_LAKE_SCALABLE_FAMILY_24_DRIVES](/img/articles/orderExampleCascadeLake.png)

Most of the information you need to build an API order is on the order form already. The only thing you need to know is that the [Intel Xeon 8260](https://www.intel.com/content/www/us/en/products/sku/192474/intel-xeon-platinum-8260-processor-35-75m-cache-2-40-ghz/specifications.html?wapkw=8260) is a Cascade Lake class of processor, so when you look for packages, that is the keyword you will search for.

1. Find the package:
```bash
$> slcli order package-list  | grep -i cascade
 1105     Dual Intel Xeon Processor Cascade Lake Scalable Family (4 Drives)     DUAL_INTEL_XEON_PROCESSOR_CASCADE_LAKE_SCALABLE_FAMILY_4_DRIVES                     BARE_METAL_CPU
 1107    Dual Intel Xeon Processor Cascade Lake Scalable Family (12 Drives)       DUAL_INTEL_XEON_PROC_CASCADE_LAKE_SCALABLE_FAMILY_12_DRIVES                       BARE_METAL_CPU
 1111          Cascade Lake for VMware vSAN QualifiedNode (12 Drives)                    2U_CASCADE_LAKE_FOR_VMWARE_VSAN_QUALIFIEDNODE                              BARE_METAL_CPU
 1113       Quad Xeon Processor Cascade Lake Scalable Family (24 Drives)         2U_QUAD_XEON_PROCESSOR_CASCADE_LAKE_SCALABLE_FAMILY_24_DRIVES                      BARE_METAL_CPU
 2670          Cascade Lake for VMware vSAN QualifiedNode (24 Drives)                             2U_VMWARE_VSAN_QUALIFIEDNODE                                      BARE_METAL_CPU
 2692         Dual Xeon Proc Cascade Lake Multi-GPU Family (24 Drives)              4U_DUAL_XEON_PROC_CASCADE_LAKE_MULTIGPU_FAMILY_24_DRIVES                        BARE_METAL_CPU
 2708  CVAD Dual Intel Xeon Processor Cascade Lake Scalable Family (12 Drives)   CVAD_DUAL_INTEL_XEON_PROCESSOR_CASCADE_LAKE_SCALABLE_12_DRIVES                     BARE_METAL_CPU
 2710  CVAD Dual Intel Xeon Processor Cascade Lake Scalable Family (4 Drives)    CVAD_DUAL_INTEL_XEON_PROCESSOR_CASCADE_LAKE_SCALABLE_4_DRIVES                      BARE_METAL_CPU
 2796           Cascade Lake for VMware vSAN QualifiedNode (4 Drives)                    1U_CASCADE_LAKE_FOR_VMWARE_VSAN_QUALIFIEDNODE                              BARE_METAL_CPU
 2866    Oracle Application Cluster Cascade Lake Scalable Family (4 Drives)     ORACLE_APPLICATION_CLUSTER_CASCADE_LAKE_SCALABLE_FAMILY_4_DRIVES                    BARE_METAL_CPU
 3110            Cascade Lake VMW PMEM Enabled 1.5TB-3TB (12 Drives)                  2U_CASCADE_LAKE_VMW_PMEM_ENABLED_1_5TB_3TB_12_DRIVES                          BARE_METAL_CPU
 3116             Cascade Lake VMW PMEM Enabled 3TB-6TB (24 Drives)                      CASCADE_LAKE_VMW_PMEM_ENABLED_3TB6TB_24_DRIVES                             BARE_METAL_CPU
```

We want the `2U_QUAD_XEON_PROCESSOR_CASCADE_LAKE_SCALABLE_FAMILY_24_DRIVES` package here since it has the `Quad Processor` and `Up to 24 Drives` mentioned on the order form.

2. Find all the items you need.
```bash
$> slcli order item-list 2U_QUAD_XEON_PROCESSOR_CASCADE_LAKE_SCALABLE_FAMILY_24_DRIVES
```

We will need the following to match the order:

| Category | KeyName |
| -------- | ------- |
| bandwidth | BANDWIDTH_20000_GB |
| disk0 | HARD_DRIVE_960GB_SSD_SED_5DWPD |
| disk_controller | DISK_CONTROLLER_NONRAID |
| monitoring | MONITORING_HOST_PING |
| notification | NOTIFICATION_EMAIL_AND_TICKET |
| os | OS_CENTOS_STREAM_9_X_64_BIT |
| port_speed | 100_MBPS_REDUNDANT_PUBLIC_PRIVATE_NETWORK_UPLINKS |
| power_supply | REDUNDANT_POWER_SUPPLY |
| pri_ip_addresses | 1_IP_ADDRESS |
| ram | RAM_384_GB_DDR4_2133_ECC_REG | 
| remote_management | REBOOT_KVM_OVER_IP |
| response  | AUTOMATED_NOTIFICATION |
| server | INTEL_XEON_8260_2_4_96 |
| vpn_management | UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT |

3. Add it all and verify the order

(use `slcli -vvv order place` to see actual API calls this makes)
```bash
$> slcli order place 2U_QUAD_XEON_PROCESSOR_CASCADE_LAKE_SCALABLE_FAMILY_24_DRIVES DALLAS10  BANDWIDTH_20000_GB \
HARD_DRIVE_960GB_SSD_SED_5DWPD DISK_CONTROLLER_NONRAID MONITORING_HOST_PING NOTIFICATION_EMAIL_AND_TICKET \
OS_CENTOS_STREAM_9_X_64_BIT 100_MBPS_REDUNDANT_PUBLIC_PRIVATE_NETWORK_UPLINKS REDUNDANT_POWER_SUPPLY 1_IP_ADDRESS \
RAM_384_GB_DDR4_2133_ECC_REG REBOOT_KVM_OVER_IP AUTOMATED_NOTIFICATION INTEL_XEON_8260_2_4_96 \
UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT \
--verify --quantity 1 --billing monthly  --complex-type SoftLayer_Container_Product_Order_Hardware_Server \
--extras '{"hardware": [{"hostname": "baremetal01", "domain": "ibmcloud.private"}]}'
```

To make this into a pure API call, use the output of `slcli -vvv order place` and the slcli will convert the item keynames into the required priceIds needed for [SoftLayer_Product_Order::placeOrder()](https://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/)

```bash
$> curl -u $SL_USER:$SL_APIKEY -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress" -d '{"parameters": [{"orderContainers": [{"hardware": [{"hostname": "baremetal01", "domain":
"ibmcloud.private"}], "packageId": 1113, "quantity": 1, "location": 1441195, "useHourlyPricing": false, "complexType": "SoftLayer_Container_Product_Order_Hardware_Server", "prices": [{"id": 342}, {"id":
230475}, {"id": 876}, {"id": 55}, {"id": 57}, {"id": 307539}, {"id": 21513}, {"id": 50221}, {"id": 21}, {"id": 165785}, {"id": 906}, {"id": 58}, {"id": 254988}, {"id": 420}]}]}]}'
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Order/placeOrder.json'
```