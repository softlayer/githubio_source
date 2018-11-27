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
    volumes = main.getStorageFromOrder(orderId)
    for storage in volumes:
        main.setStorageNote(storage['id'], 'This is a test note')
        main.getStorageObject(storage['id'])

    main.debug()
```