---
title: "Working with Network Storage"
description: "A few examples on interacting with network storage. Ordring volumes and setting notes from that orderId"
date: "2018-11-27"
classes: 
    - "SoftLayer_Network_Storage"
tags:
    - "ordering"
    - "filter"
    - "storage"
---



```python
import SoftLayer
import time
from pprint import pprint as pp

class example():

    def __init__(self):
        self.client = SoftLayer.Client()
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.client.transport = debugger

    def main(self):
        block_manager = SoftLayer.BlockStorageManager(self.client)

        # This block will actually order storage, make sure to uncomment the other order block
        # order = block_manager.order_block_volume(
        #     storage_type="endurance",
        #     location='dal13',
        #     size=100,
        #     tier_level=float(4),
        #     os_type='LINUX',
        #     snapshot_size=None,
        #     service_offering='storage_as_a_service',
        #     hourly_billing_flag=True
        # )

        # Used to test setting a note without actually placing an order
        # This is the basic structure returned from an order
        order = {
            'orderDate': '2018-11-27T12:03:50-06:00',
            'orderId': 31323125,
            'placedOrder': {
                'id': 31323125,
                'items': [
                    {'categoryCode': 'storage_as_a_service',
                     'description': 'Storage as a Service'},
                    {'categoryCode': 'storage_block',
                     'description': 'Block Storage'},
                    {'categoryCode': 'performance_storage_space',
                     'description': '100 GBs'},
                    {'categoryCode': 'storage_tier_level',
                     'description': '4 IOPS per GB'}
                ]
            }
        }
        if 'placedOrder' in order:
            print("OrderID: #{0}".format(order['placedOrder']['id']))
            for item in order['placedOrder']['items']:
                print(" > {0}".format(item['description']))
            return order['placedOrder']['id']

    def getStorageFromOrder(self, orderId):
        """This will get all of the storage volumes that were ordered as part of orderId
        """
        mask = "mask[id, capacityGb, username, notes]"
        _filter =  {
            'networkStorage': {
                'billingItem': {
                    'orderItem': {
                        'order': {
                            'id': {
                                'operation': orderId
                            }
                        }
                    }
                }
            }

        }
        orders = self.client.call('Account', 'getNetworkStorage', filter=_filter, mask=mask)
        return orders

    def setStorageNote(self, storageId, note):
        storage_object = {
            'notes': note
        }
        result = self.client.call('Network_Storage', 'editObject', storage_object, id=storageId)

    def getStorageObject(self, storageId):
        result = self.client.call('Network_Storage', 'getObject', id=storageId)
        print("{0} -> {1}".format(result['username'], result['notes']))

    def debug(self):
        for call in self.client.transport.get_last_calls():
            print(self.client.transport.print_reproduceable(call))

if __name__ == "__main__":
    main = example()
    orderId = main.main()
    print("Sleeping for 60s to wait for volume to be ready")
    time.sleep(60)
    volumes = main.getStorageFromOrder(orderId)
    for storage in volumes:
        main.setStorageNote(storage['id'], 'This is a test note')
        main.getStorageObject(storage['id'])

    main.debug()
```


### Actual API calls

Resolves the DC shortname, `dal13` to its locationId.
```sh
curl -u $SL_USER:$SL_APIKEY -X GET -H  'https://api.softlayer.com/rest/v3.1/SoftLayer_Location_Datacenter/getDatacenters.json?objectMask=mask%5BlongName%2Cid%2Cname%5D'
```

Gets the storage package information used in ordering
```sh
curl -u $SL_USER:$SL_APIKEY -X GET -H   'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Package/getAllObjects.json?objectMask=mask%5Bid%2Cname%2Citems%5Bprices%5Bcategories%5D%2Cattributes%5D%5D&objectFilter=%7B%22categories%22%3A+%7B%22categoryCode%22%3A+%7B%22operation%22%3A+%22_%3D+storage_as_a_service%22%7D%7D%2C+%22statusCode%22%3A+%7B%22operation%22%3A+%22_%3D+ACTIVE%22%7D%7D'
```

Orders the storage volume
```sh
curl -u $SL_USER:$SL_APIKEY -X POST -H -d '{"parameters": [{"complexType": "SoftLayer_Container_Product_Order_Network_Storage_AsAService", "packageId": 759, "prices": [{"id": 189433}, {"id": 189443}, {"id": 194763}, {"id": 194703}], "quantity": 1, "location":1854895, "useHourlyPricing": true, "volumeSize": 100, "osFormatType": {"keyName": "LINUX"}}]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Order/placeOrder.json'
```

Searches network storage volumes for one with a matching orderId. Will return a list of storage volumes. The number of volumes in this list should match how many you requested in the initial order.
```sh
curl -u $SL_USER:$SL_APIKEY -X GET -H  'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getNetworkStorage.json?objectMask=mask%5Bid%2C+capacityGb%2C+username%2C+notes%5D&objectFilter=%7B%22networkStorage%22%3A+%7B%22billingItem%22%3A+%7B%22orderItem%22%3A+%7B%22order%22%3A+%7B%22id%22%3A+%7B%22operation%22%3A+31324259%7D%7D%7D%7D%7D%7D'
```

Sets the notes for the the storage volume 123456789
```sh
curl -u $SL_USER:$SL_APIKEY -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress" -d '{"parameters": [{"notes": "This is a test note"}]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage/123456789/editObject.json'
```

Gets the object for storage volume 123456789
```sh

curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Storage/123456789/getObject.json'
```