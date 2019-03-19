---
title: "Various Place Order Examples"
description: "place_order_cdn.py"
date: "2019-03-14"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Network_ContentDelivery_Account"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_ContentDelivery_Account"
tags:
    - "order"
---

*NOTICE:* Be careful using hard coded price IDs, as they can change at any time without notice. For a better way of building orders, see https://softlayer.github.io/article/understanding-ordering/

### CDN

```python
"""
Order a new CDN account

Build a SoftLayer_Container_Product_Order_Network_ContentDelivery_Account
object for a new CDN account order and pass it to the SoftLayer_Product_Order
API service to order it. In this case we'll order a pay as you go bandwidth
and storage CDN account. See below for more details.


"""
import SoftLayer

"""
Build a skeleton SoftLayer_Container_Product_Order_Network_ContentDelivery_Account object
containing the order you wish to place.
"""
orderData = {
    "complexType": "SoftLayer_Container_Product_Order_Network_ContentDelivery_Account",

    "packageId": 208,  # The package id to order Content Delivery Network
    # The prices to order the CDN
    "prices": [
        {
            "complexType": "SoftLayer_Product_Item_Price",
            "id": 1661  # CDN Pay as You Go Bandwidth
        },

        {
            "complexType": "SoftLayer_Product_Item_Price",
            "id": 1670  # CDN No storage (origin pull)
        }
    ],
    "quantity": 1,  # We only want 1 fire-wall
}

# Declare the API client
client = SoftLayer.Client()
productOrderService = client['SoftLayer_Product_Order']

try:
    """
    verifyOrder() will check your order for errors. Replace this with a call to
    placeOrder() when you're ready to order. Both calls return a receipt object
    that you can use for your records.
    """
    response = client['SoftLayer_Product_Order'].verifyOrder(orderData)
    print(response)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to place order faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```


### EVault

```python
"""
Order a Evault

Build a SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault
object for a new Evault order and pass it to the SoftLayer_Product_Order
for more information see below:

"""
import SoftLayer

"""
# Your SoftLayer API username and key.
# Generate an API key at the SoftLayer Customer Portal:
# https://manage.softlayer.com/Administrative/apiKeychain
"""

# Create a SoftLayer API client object
client = SoftLayer.Client()
productOrderService = client['Product_Order']

orderTemplate = {
    "complexType": "SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault",

    # Build a skeleton SoftLayer_Hardware object.
    # The object contains the hardware ID of the
    # Bare Metal server wich will contain the Evault
    # If you want use a Virtual Server instead a
    # Bare Metal server build a skeleton SoftLayer_Virtual_Guest object
    "virtualGuests": [
        {
            "complexType": "SoftLayer_Virtual_Guest",
            "id": 4241550
        }
    ],
    # The location for the Evault
    "location": "DALLAS06",
    "packageId": 0,
    # Build a skeleton SoftLayer_Product_Item_Price object.
    # The object contains the price ID of the Evaul device
    # you wish order.
    "prices": [
        {
            "complexType": "SoftLayer_Product_Item_Price",
            "id": 1045
        }
    ],
    "quantity": 1
}

try:
    """
    # verifyOrder() will check your order for errors. Replace this with a call
    # to placeOrder() when you're ready to order. Both calls return a receipt
    # object that you can use for your records.
    #
    # Once your order is placed it'll go through SoftLayer's approval and
    # provisioning process.
    """
    result = productOrderService.verifyOrder(orderTemplate)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to place order faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```


### NAS

```python
"""
Order a NAS

Build a SoftLayer_Container_Product_Order_Network_Storage_Nas
object for a new CDN account order and pass it to the SoftLayer_Product_Order
API service to order it. In this script we'll order a NAS. See below for more details.

"""
import SoftLayer

USERNAME = 'set me'
# Generate one at https://manage.softlayer.com/Administrative/apiKeychain
API_KEY = 'set me'

"""
Build a skeleton SoftLayer_Container_Product_Order_Network_Storage_Nas object
containing the order you wish to place.
"""
orderData = {
    "complexType": "SoftLayer_Container_Product_Order_Network_Storage_Nas",
    "packageId": 216,  # the package id to order NAS
    "location": "AMSTERDAM",
    # The prices to order the NAS
    "prices": [
        {
            "complexType": "SoftLayer_Product_Item_Price",
            "id": 508  # 20 GB NAS
        }

    ],
    "quantity": 1,
    "privateCloudOrderFlag": False
}

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
productOrderService = client['SoftLayer_Product_Order']

try:
    """
    verifyOrder() will check your order for errors. Replace this with a call to
    placeOrder() when you're ready to order. Both calls return a receipt object
    that you can use for your records.
    """
    response = client['SoftLayer_Product_Order'].verifyOrder(orderData)
    print(response)
except SoftLayer.SoftLayerAPIError as e:
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    print("Unable to place order faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```


### Portable Storage

```python
"""
Order a portal storage

The script orders a portal storage device, it makes a single call to
SoftLayer_Product_Order::placeOrder method.
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Declare the API client to use the SoftLayer_Product_Order API service
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
productOrderService = client['SoftLayer_Product_Order']

# Building an skeleton SoftLayer_Container_Product_Order_Virtual_Disk_Image to the order
orderTemplate = {
    "complexType": "SoftLayer_Container_Product_Order_Virtual_Disk_Image",
    "location": "SANJOSE",
    # The package for order portable storage
    "packageId": 198,
    "diskDescription": "test portable storage",
    "prices": [
        {
            # The prices for the portable storage
            # to see the list of prices available for the package
            # use the Softlayer_Product_Package::getItems method (http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItems)
            # e.g.
            # client = SoftLayer::Client.new(:username => user,:api_key => api_key)
            # productPackageService = client.service_named("Softlayer_Product_Package")
            # packageID = 198
            # result = productPackageService.object_with_id(packageID).getItems()
            "id": 21861,
            "complexType": "SoftLayer_Product_Item_Price"
        }
    ]
}

try:
    # Verifies the order when you are ready to create the
    # portal storage replace "verifyOrder" by "placeOrder"
    result = productOrderService.verifyOrder(orderTemplate)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    print("Unable to place the order. "
          % (e.faultCode, e.faultString))

```


#### Snap shot replica

```python
"""
Order snapshot replica.

Build a SoftLayer_Container_Product_Order_Network_Storage_Enterprise
object to order a replica for your endurance object storage.
"""

import SoftLayer

USERNAME = 'set me'
API_KEY = 'set me'

# Builds a skeleton SoftLayer_Container_Product_Order_Network_Storage_Enterprise object
# containing the order you wish to place.
orderData = {
    "complexType": "SoftLayer_Container_Product_Order_Network_Storage_Enterprise",
    "packageId": 240,
    # In order to get the valid locations for the replica
    # call the SoftLayer_Network_Storage::getValidReplicationTargetDatacenterLocations method
    # e.g.
    # client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
    # enduranceStorage = 6548079
    # storageService = client['SoftLayer_Network_Storage']
    # result = storageService.getValidReplicationTargetDatacenterLocations(id=enduranceStorage)
    # print(result)
    "location": "AMSTERDAM03",
    "originVolumeId": 6548079,  # The storage endurance id where you wish to create the replica.
    # This is the origin volume schedule, you can get this id by calling SoftLayer_Network_Storage::getSchedules
    # client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
    # enduranceStorage = 6548079
    # storageService = client['SoftLayer_Network_Storage']
    # result = storageService.getSchedules(id=enduranceStorage)
    # print(result)
    "originVolumeScheduleId": 34247,
    "quantity": 1,
    "prices": [
        {
            "id": 46649  # 20 GB Storage Space (Replication)
        },
        {
            "id": 45098  # Block Storage
        },
        {
            "id": 45068  # 0.25 IOPS per GB
        },
        {
            "id": 144005  # 20 GB Storage Space
        },
        {
            "id": 144255  # 5 GB Storage Space
        },
        {
            "id": 45058  # Endurance Storage
        }
    ],
    "osFormatType": {
        "keyName": "LINUX"
    }
}

# Declares the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
productOrderService = client['SoftLayer_Product_Order']

try:
    # verifyOrder() will check your order for errors. Replace this with a call to
    # placeOrder() when you're ready to order. Both calls return a receipt object
    # that you can use for your records.
    response = productOrderService.verifyOrder(orderData)
    print(response)
except SoftLayer.SoftLayerAPIError as e:
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    print("Unable to place the order faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```


### VSI

```python
"""
Order a new VSI.

The script makes a order for a VSI, it uses the SoftLayer_Product_Order::placeOrder method
for more information please see below:
"""
import SoftLayer

# For nice debug output:
from pprint import pprint as pp

"""
Build a skeleton SoftLayer_Container_Product_Order_Virtual_Guest object
containing the order you wish to place.
"""
orderData = {
    # The id of the SoftLayer_Product_Package you wish to order.
    "packageId": 46,
    # Where you'd like your new server provisioned.
    # This can either be the id of the datacenter you wish your new server to be
    # provisioned in or the string 'FIRST_AVAILABLE' if you have no preference
    # where your server is provisioned.
    # Location id 3     = Dallas
    # Location id 18171 = Seattle
    # Location id 37473 = Washington, D.C.
    "location": "AMSTERDAM",
    # Build a skeleton SoftLayer_Product_Item_Price objects. These objects contain
    # much more than ids, but SoftLayer's ordering system only needs the price's id
    # to know what you want to order.

    # Every item in SoftLayer's product catalog is assigned an id. Use these ids
    # to tell the SoftLayer API which options you want in your new server. Use
    # the getActivePackages() method in the SoftLayer_Account API service to get
    # a list of available item and price options per available package.
    "prices":
        [
            {"id": 203965},  # 1 x 2.0 GHz Core
            {"id": 204133},  # 2 GB
            {"id": 45466},  # CentOS 7.x - Minimal Install (64 bit)
            {"id": 2202},  # 25 GB (SAN)
            {"id": 50367},  # 250 GB Bandwidth
            {"id": 273},  # 100 Mbps Public&Private Network Upllinks
            {"id": 55},  # Host Ping
            {"id": 58},  # Automated Notification
            {"id": 420},  # Unlimited SSL VPN Users & 1 PPTP VPN
            {"id": 418},  # Nessus Vulnerability Assessment & Reporting
            {"id": 21},  # 1 IP Address
            {"id": 57},  # Email and Ticket
            {"id": 905}  # Reboot / Remote Console
        ],
    # The number of servers you wish to order in this configuration.
    "quantity": 3,
    # Build a skeleton SoftLayer_Virtual_Guest object to model the hostname,
    # domain and the VLANs we want for our server. If you set quantity greater
    # then 1 then you need to define one hostname/domain pair per server you wish to order.
    # note: if you want order a Bare Metal you need to model a SoftLayer_Hardware_Server
    "virtualGuests":
        [
            {
                "domain": "softlayer.ibm.com",
                "hostname": "VM1",
                # The Backend VLAN for your machine.
                "primaryBackendNetworkComponent": {"id": 465360},
                # The Frontend VLAN for your machine.
                "primaryNetworkComponent": {"id": 360796}
            },
            {
                "domain": "softlayer.ibm.com",
                "hostname": "VM2",
                "primaryBackendNetworkComponent": {"id": 465360},
                "primaryNetworkComponent": {"id": 360796}
            },
            {
                "domain": "softlayer.ibm.com",
                "hostname": "VM3",
                "primaryBackendNetworkComponent": {"id": 465360},
                "primaryNetworkComponent": {"id": 360796}
            }
        ]
        }

# Declare a new API service object
client = SoftLayer.create_client_from_env()


try:
    result = client['Product_Order'].verifyOrder(orderData, False)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to create the order. "
          % (e.faultCode, e.faultString))

```

```python
"""
Order a new VSI with post script and VLAN.

The script makes a order for a VSI, it uses the SoftLayer_Product_Order::placeOrder method
for more information please see below:
"""
import SoftLayer

# For nice debug output:
from pprint import pprint as pp

orderData = {
    "imageTemplateId": "1656107",
    "packageId": 46,
    "location": "AMSTERDAM",
    "prices": [
        {"id": 1962},  # 1 x 2.0 GHz Cores (Dedicated)
        {"id": 1644},  # 1 GB
        {"id": 22267},  # Debian GNU\/Linux 7.x Wheezy\/Stable - Minimal Install (64 bit)
        {"id": 2202},  # 25 GB (SAN)
        {"id": 2255},  # 10 GB (SAN) - GUEST_DISK_10_GB_SAN
        {"id": 905},  # Reboot \/ Remote Console
        {"id": 272},  # 10 Mbps Public & Private Network Uplinks
        {"id": 1800},  # 0 GB Bandwidth
        {"id": 21},  # 1 IP Address
        {"id": 55},  # Host Ping
        {"id": 57},  # Email and Ticket
        {"id": 58},  # Automated Notification
        {"id": 420},  # Unlimited SSL VPN Users & 1 PPTP VPN User per account
        {"id": 418}  # Nessus Vulnerability Assessment & Reporting
               ],
    "quantity": 1,
    "hardware": [
                  {
                    "domain": "softlayer.ibm.com",
                    "hostname": "sptest1",
                    "primaryBackendNetworkComponent": {"networkVlanId": 1084325},
                    "primaryNetworkComponent": {"networkVlanId": 361652}
                  }
              ],
    "provisionScripts": ["https://examples.provisioning.org"]
}


client = SoftLayer.create_client_from_env()

try:
    result = client['Product_Order'].verifyOrder(orderData)
    pp (result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create the order. "  % (e.faultCode, e.faultString))

```


### Storage Space

```python
"""
Order storage space.

The script adds an storage space of 10 GB to an endurance storage.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Enterprise_SnapshotSpace
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer

USERNAME = 'set me'
API_KEY = 'set me'


# Build a skeleton SoftLayer_Container_Product_Order_Network_Storage_Enterprise_SnapshotSpace object
# containing the order you wish to place.
orderData = {
    "complexType": "SoftLayer_Container_Product_Order_Network_Storage_Enterprise_SnapshotSpace",
    "volumeId": 6538873,  # The storage endurance id where you wish to add the storage space.
    "packageId": 240,
    "quantity": 1,
    "prices": [
        {
            "id": 46150  # 10 GB Storage Space.
        }
    ]
}

# Declares the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
productOrderService = client['SoftLayer_Product_Order']

try:
    # verifyOrder() will check your order for errors. Replace this with a call to
    # placeOrder() when you're ready to order. Both calls return a receipt object
    # that you can use for your records.
    response = productOrderService.verifyOrder(orderData)
    print(response)
except SoftLayer.SoftLayerAPIError as e:
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    print("Unable to place the order. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```


### VLAN
*NOTICE:* From March 8, 2019 the VLAN orders with a subnet item specified will begin emitting an error, see [Release Notes](https://sldn.softlayer.com/release_notes/2019/20190308/).

To add subnet/ipaddress to the new vlan, see:

[Order static subnet](/python/order_static_subnet)

[Order portable subnet](/python/order_portable_subnet)


```python
import SoftLayer
from pprint import pprint

class Network:
    def __init__(self):
        self.client = SoftLayer.Client()

    def _get_package_id(self, keyname):
        _filter = {"type":{"keyName":{"operation":keyname}}}
    
        package = self.client['Product_Package'].getAllObjects(filter=_filter)
        return package[0]['id']
        
    def _get_price_id(self, package_id, item_keyname):
        _filter = {"items":{"keyName":{"operation":item_keyname}}}
        
        items = self.client['Product_Package'].getItems(filter=_filter, id=package_id)

        price_id = [p["id"] for p in items[0]["prices"]
                   if not p["locationGroupId"]][0]
        return price_id
    
    def order_vlan(self, package, location, item_keyname, name=None):
        packageId = self._get_package_id(package)
        priceId = self._get_price_id(packageId, item_keyname)

        orderData = {
            "complexType": "SoftLayer_Container_Product_Order_Network_Vlan",
            "packageId": packageId,
            "location": location,
            "prices": [{"id": priceId}],
            "quantity": 1, # for vlans each configuration quantity is restricted to 1
            "name": name
        }

        try:
            return self.client['Product_Order'].placeOrder(orderData)            
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to order: %s - %s" % (e.faultCode, e.faultString))
    
if __name__ == "__main__":
    package = "ADDITIONAL_SERVICES_NETWORK_VLAN"
    location = "AMSTERDAM"
    # set PRIVATE_NETWORK_VLAN if you want a private vlan
    network_type = "PUBLIC_NETWORK_VLAN"
    vlan_name = "Vlan Name"
    
    network = Network()

    # The new Vlan comes with a primary subnet which have 8 ip addresses
    receipt = network.order_vlan(package, location, network_type, name=vlan_name)
    pprint(receipt)
```