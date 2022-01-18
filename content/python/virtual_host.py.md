---
title: "Virtual_host.py"
description: "Working with Virtual Hosts"

date: "2019-07-27"

classes: 
    - "SoftLayer_Virtual_Host"    
    - "SoftLayer_Product_Order"    
tags:
    - "virtual_host"
---

### getAccount

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id variable. 
"""""
id_host="123456"

try:
    response = virtual_service.getAccount(id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
  
```

### getBilledPerMemoryUsageFlag

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id variable. 
"""""
id_host="123456"

try:
    response = virtual_service.getBilledPerMemoryUsageFlag(id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```

### getGuests

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id variable. 
"""""
id_host="123456"

try:
    response = virtual_service.getGuests(id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### getHardware

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id variable. 
"""""
id_host="123456"

try:
    response = virtual_service.getHardware(id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```
### getLiveGuestByUuid

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id and uuid variable. 
"""""
id_host="1001547"
uuid="123456789-bb9a-fe82-7239-4a33077cf32f"
try:
    response = virtual_service.getLiveGuestByUuid(uuid,id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### getLiveGuestList
```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id variable. 
"""""
id_host = "123456"
try:
    response = virtual_service.getLiveGuestList(id=id)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### getLiveGuestRecentMetricData

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id and uuid variable. 
"""""
id_host="1001547"
uuid="123456789-bb9a-fe82-7239-4a33077cf32f"
try:
    response = virtual_service.getLiveGuestRecentMetricData(uuid,id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### getLiveGuestRecentMetricData

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id variable. 
"""""

id_host="123456"

try:
    response = virtual_service.getMetricTrackingObject(id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### getObject

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id variable. 
"""""

id_host="123456"

try:
    response = virtual_service.getObject(id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### getPciDevices

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id variable. 
"""""

id_host="123456"

try:
    response = virtual_service.getPciDevices(id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### pauseLiveGuest

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id and uuid variable. 
"""""
id_host="1001547"
uuid="12345678-bb9a-fe82-7239-4a33077cf32f"

try:
    response = virtual_service.pauseLiveGuest(uuid,id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```


### powerCycleLiveGuest

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id and uuid variable. 
"""""
id_host="1001547"
uuid="12345678-bb9a-fe82-7239-4a33077cf32f"

try:
    response = virtual_service.powerCycleLiveGuest(uuid,id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### powerOffLiveGuest

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id and uuid variable. 
"""""
id_host="1001547"
uuid="12345678-bb9a-fe82-7239-4a33077cf32f"

try:
    response = virtual_service.powerOffLiveGuest(uuid,id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### powerOnLiveGuest

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id and uuid variable. 
"""""
id_host="1001547"
uuid="12345678-bb9a-fe82-7239-4a33077cf32f"

try:
    response = virtual_service.powerOnLiveGuest(uuid,id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### rebootSoftLiveGuest

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id and uuid variable. 
"""""
id_host="1001547"
uuid="12345678-bb9a-fe82-7239-4a33077cf32f"

try:
    response = virtual_service.rebootSoftLiveGuest(uuid,id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```

### resumeLiveGuest

```python
import SoftLayer
import json

client = SoftLayer.create_client_from_env()
virtual_service = client['SoftLayer_Virtual_Host']

""""
Virtual host id and uuid variable. 
"""""
id_host="1001547"
uuid="12345678-bb9a-fe82-7239-4a33077cf32f"

try:
    response = virtual_service.resumeLiveGuest(uuid,id=id_host)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the response for the package: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
```


### Create virtual host

```python
import SoftLayer
from pprint import pprint as pp
from prettytable import PrettyTable


class CreateVirtualHost:

    def __init__(self):
        self.client = SoftLayer.create_client_from_env()

    def main(self, package_id, location_id):
        """
        Places an order for a Virtual Hos Instance
        """

        """These items are required for all servers and have a 0$ cost, some can be upgraded"""
        required_items = [
            'MONITORING_HOST_PING',
            'AUTOMATED_NOTIFICATION',
            'UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT',
            'NOTIFICATION_EMAIL_AND_TICKET',
            'REBOOT_KVM_OVER_IP',
            'VMWARE_VSAN_NODE'

        ]
        """We need bandwidth, at least 1 ip, and the port speed """
        network_items = [
            'BANDWIDTH_500_GB',
            '1_IP_ADDRESS',
            '10_GBPS_DUAL_PUBLIC_PRIVATE_NETWORK_UPLINKS_UNBONDED',
        ]
        """A disk controller, a duplicate entry for each disk you want, in order, ram, OS and processor chip """
        physical_items = [
            'DISK_CONTROLLER_NONRAID',
            'HARD_DRIVE_2_00_TB_SATA_2',
            'HARD_DRIVE_2_00_TB_SATA_2',
            'INTEL_INTEL_XEON_4110_2_10',
            # 'OS_CENTOS_7_X_64_BIT',
            'OS_VMWARE_SERVER_VIRTUALIZATION_6_5',
            'RAM_32_GB_DDR4_2133_ECC_NON_REG',
            'SRIOV_ENABLED',
        ]

        all_items = required_items + network_items + physical_items
        prices = self.gatherPriceIds(package_id, all_items)
        productOrder = {'orderContainers': [
            {'hardware':
                [
                    {
                        'domain': u'virtualHost.com',
                        'hostname': u'vmware-testing01',
                       }
                ],
                'location': location_id,
                'packageId': package_id,
                'prices': prices,
                'quantity': 1
            }
        ]
        }
        pp(productOrder)
        order = self.client['Product_Order'].verifyOrder(productOrder)
        # order = self.client['Product_Order'].placeOrder(productOrder)
        pp(order)
    
    def listRaidArrayTypes(self):
        result = self.client['SoftLayer_Configuration_Storage_Group_Array_Type'].getAllObjects()
        table = PrettyTable()
        table.title = "Raid Array Types"
        table.field_names = ["id", "keyName", "description", "Min", 'Max']
        for raid in result:
            table.add_row([raid['id'],
                           raid['keyName'],
                           raid['description'],
                           raid['minimumDrives'],
                           raid['maximumDrives']]
                          )
        print(table)

    def getServerPrices(self, package_id):
        mask = "mask[regions,items[prices],activeServerItems[prices]]"
        # locations = self.client['Product_Package'].getLocations(id=package_id)
        result = self.client['Product_Package'].getObject(mask=mask, id=package_id)

        table = PrettyTable()
        table.title = "Locations"
        table.field_names = ["Location ID", "Location Name"]
        for location in result['regions']:
            table.add_row([location['location']['location']['id'], location['description']])
        print(table)

        table = PrettyTable()
        table.title = "Items Prices"
        table.field_names = ["Price ID", "description", "cores", "Monthly Fee", "KeyName"]
        for item in result['items']:
            for prices in item['prices']:
                # only print the Default location price.
                # The ordering system will replace the default price id for you if ordering in a non-usa region.
                if prices['locationGroupId'] is None:
                    # Some software has core restrictions that effect prices
                    if 'capacityRestrictionType' in prices:
                        cores = "%s - %s" % (
                            prices['capacityRestrictionMinimum'],
                            prices['capacityRestrictionMaximum'])
                        table.add_row([prices['id'],
                                       str(item['description']).replace(" - ", "\n"),
                                       cores, prices.get('recurringFee', '?'),
                                       item['keyName']])

                    else:
                        table.add_row([prices['id'],
                                       str(item['description']).replace(" - ", "\n"),
                                       "", prices.get('recurringFee', '?'),
                                       item['keyName']])
        print(table)

        # serverItems = self.client['Product_Package'].getActiveServerItems(id=package_id)
        table = PrettyTable()
        table.title = "SERVER ITEMS"
        table.field_names = ["Price ID", "description", "Monthly Fee", "KeyName"]
        for item in result['activeServerItems']:
            for prices in item['prices']:
                # only print the Default location price.
                # The ordering system will replace the default price id for you if ordering in a non-usa region.
                if prices['locationGroupId'] is None:
                    table.add_row([prices['id'],
                                   str(item['description']).replace(" - ", "\n"),
                                   prices.get('recurringFee', '?'),
                                   item['keyName']])
        print(table)

    def gatherPriceIds(self, package_id, keyNames):
        # This will work for prices that have core requirements
        mask = 'mask[id,itemCategory,keyName,prices[categories]]'
        items = self.client['Product_Package'].getItems(mask=mask, id=package_id)
        prices = []
        category_dict = {"gpu0": -1, "pcie_slot0": -1}

        for item_keyname in keyNames:
            try:
                matching_item = [i for i in items if i['keyName'] == item_keyname][0]
            except IndexError:
                raise SoftLayer.SoftLayerError(
                    "Item {} does not exist for package {}".format(item_keyname,
                                                                   package_id))
            item_category = matching_item['itemCategory']['categoryCode']

        for item_keyname in keyNames:
            try:
                matching_item = [i for i in items if i['keyName'] == item_keyname][0]
            except IndexError:
                raise SoftLayer.SoftLayerError(
                    "Item {} does not exist for package {}".format(item_keyname,
                                                                   package_id))

            item_category = matching_item['itemCategory']['categoryCode']

            if item_category not in category_dict:

               price_id = [p['id'] for p in matching_item['prices']
                                if not p['locationGroupId']][0]

            else:
                category_dict[item_category] += 1
                category_code = item_category[:-1] + str(category_dict[item_category])
                price_id = [p['id'] for p in matching_item['prices']
                            if not p['locationGroupId']
                            and p['categories'][0]['categoryCode'] == category_code][0]

            prices.append({"id": price_id})

        return prices


if __name__ == "__main__":
    main = CreateVirtualHost()

    # main.listServerPackages()
    package_id = 1051

    main.getServerPrices(package_id)
    location_id = 448994  # "AMSTERDAM03"

    main.listRaidArrayTypes()
    main.main(package_id, location_id)
```
