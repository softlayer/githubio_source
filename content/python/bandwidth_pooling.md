---
title: "Working with Bandwidth Pools"
description: "A few examples on interacting with Bandwidth Pools"
date: "2021-03-22"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
tags:
    - "bandwidthpools"
---

### Setup
All the functions defined in this article will be part of this `PoolingExample` class. Which only sets up the SoftLayer Client, and configures the debugger, which allows you to see the exact API calls being made.

```python
from pprint import pprint

import SoftLayer
from SoftLayer.CLI import environment
from SoftLayer.CLI import formatting


class PoolingExample:

    def __init__(self):
        self.client = SoftLayer.create_client_from_env()
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.pooling_service = self.client['Network_Bandwidth_Version1_Allotment']
        self.client.transport = debugger
        self.env = environment.Environment()

    def debug(self):
        for call in self.client.transport.get_last_calls():
            pprint(self.client.transport.print_reproduceable(call))

```

## Creating a Bandwidth Pool
To create a Bandwidth Pool needs a name, location group, and account, `list locations(self)` method helps to get the location groups available.

### Python
```python

    def create(self, name, location_group, account):
        templateObject = {
            'accountId': account,
            'bandwidthAllotmentTypeId': 2,  # Type 2 is the Bandwidth pool type
            'name': name,
            'locationGroupId': location_group,
        }
        result = self.pooling_service.createObject(templateObject)
        self.env.fout(formatting.iter_to_table(result))
        return result
    
    def list_locations(self):
        objectFilter = {"locationGroupType": {"name": {"operation": "VDR"}}}
        locations = self.client.call('SoftLayer_Location_Group', 'getAllObjects', filter=objectFilter)
        self.env.fout(formatting.iter_to_table(locations))

```

## Retrieving the valid server list to add to the bandwidth pool
Retrieves all hardware and virtual guests with the location group and virtual rack whose values match the desired bandwidth pool.

### Python
```python

    def list_available_servers(self, pool_identifier):
        group_id = pool.get_pool(pool_identifier).get('locationGroupId')
        virtual_rack_id = pool.get_virtual_rack()[0].get('id')
        hardware = self.list_servers(group_id, virtual_rack_id)
        self.env.fout(formatting.iter_to_table(['Hardware Servers', hardware]))
        self.list_servers(group_id, virtual_rack_id)
        guests = self.list_guest(group_id, virtual_rack_id)
        self.env.fout(formatting.iter_to_table(['Virtual Servers', guests]))

    def list_servers(self, group_id, virtual_rack_id):
        mask = '''mask[
            bandwidthAllocation,
            billingItem[
                hourlyRecurringFee
            ],
            datacenter[
                longName,
                groups[
                    id
                ]
            ],
            hardwareStatus[
                status
            ],
            id,
            fullyQualifiedDomainName,
            primaryIpAddress,
            virtualRackId
        ]'''
        _filter = {
            "hardware": {
                "bandwidthAllocation": {
                    "operation": "> 0"
                },
                "billingItem": {
                    "hourlyRecurringFee": {
                        "operation": "is null"
                    }
                },
                "datacenter": {
                    "groups": {
                        "id": {
                            "operation": group_id
                        }
                    }
                },
                "hardwareStatus": {
                    "status": {
                        "operation": "!= SPARE_POOL"
                    }
                },
                "virtualRackId": {
                    "operation": virtual_rack_id
                }
            }
        }
        result = self.client['Account'].getHardware(mask=mask, filter=_filter)
        return result

    def list_guest(self, group_id, virtual_rack_id):
        mask = '''mask[
            bandwidthAllocation,
            billingItem[
                hourlyRecurringFee
            ],
            datacenter[
                longName,
                groups[
                    id
                ]
            ],
            id,
            fullyQualifiedDomainName,
            primaryIpAddress,
            virtualRackId
        ]'''
        _filter = {
            "virtualGuests": {
                "bandwidthAllocation": {
                    "operation": "> 0"
                },
                "billingItem": {
                    "hourlyRecurringFee": {
                        "operation": "is null"
                    }
                },
                "datacenter": {
                    "groups": {
                        "id": {
                            "operation": group_id  # 2
                        }
                    }
                },
                "virtualRackId": {
                    "operation": virtual_rack_id  # "138442"
                }
            }
        }
        result = self.client['Account'].getVirtualGuests(mask=mask, filter=_filter)
        return result

    def get_virtual_rack(self):
        _filter = {
            "bandwidthAllotments": {
                "bandwidthAllotmentType": {
                    "keyName": {
                        "operation": "VIRTUAL_PRIVATE_RACK"
                    }
                }
            }
        }
        result = self.client['Account'].getBandwidthAllotments(filter=_filter)
        self.env.fout(formatting.iter_to_table(result))
        return result

    def get_pool(self, identifier):
        result = self.pooling_service.getObject(id=identifier)
        return result


```

## Retrieving the Bandwidth Pool Details
The method `list_pools(self)` retrieves all bandwidth pools in the account,  `get_pool_details(self, identifier)` gets the bandwidth pool details from a specific pool as the servers within the bandwidth pool.
### Python
```python

        def get_pool_details(self, identifier):
            detail = self.get_pool(identifier)
            _mask = '''mask[id,
            fullyQualifiedDomainName,
            bandwidthAllocation,          
            outboundPublicBandwidthUsage]
            '''
            detail['Hardware'] = self.pooling_service.getHardware(id=identifier, mask=_mask)
            detail['Virtual Servers'] = self.pooling_service.getVirtualGuests(id=identifier, mask=_mask)
            self.env.fout(formatting.iter_to_table(detail))
        
        
        def list_pools(self):
            result = self.client['Account'].getBandwidthAllotments()
            self.env.fout(formatting.iter_to_table(result))


```

## Editing a Bandwidth Pool
Edit a bandwidth allotment’s local properties. Currently you may only change an allotment’s name.
### Python
```python

    def edit_name(self, identifier, name):
        templateObject = {
            'name': name,
        }
        result = self.pooling_service.editObject(templateObject, id=identifier)
        self.env.fout(formatting.iter_to_table(result))
        return result

```
## Updating a Bandwidth Pool
This will move servers into a bandwidth pool, removing them from their previous bandwidth pool and optionally remove the bandwidth pool on completion.
### Python
```python

    def update(self, identifier,
               add_hardware=None,
               del_hardware=None,
               add_guest=None,
               del_guest=None):
        add_hardware = [{'id': server_id} for server_id in add_hardware]
        del_hardware = [{'id': server_id} for server_id in del_hardware]
        add_guest = [{'id': server_id} for server_id in add_guest]
        del_guest = [{'id': server_id} for server_id in del_guest]
        print(add_guest)

        result = self.client.call('SoftLayer_Network_Bandwidth_Version1_Allotment', 'requestVdrContentUpdates',
                                  add_hardware, del_hardware, add_guest, del_guest, id=identifier)
        self.env.fout(formatting.iter_to_table(result))
        return result

```

## Deleting a Bandwidth Pool
This will remove a bandwidth pooling from a customer’s allotments by cancelling the billing item. All servers in that allotment will get moved to the account’s vpr.
### Python
```python

    def cancel(self, identifier):
        result = self.pooling_service.requestVdrCancellation(id=identifier)
        self.env.fout(formatting.iter_to_table(result))
        return result

```

## Running the Example

### Python
```python

if __name__ == '__main__':
    pool = PoolingExample()
    account_id = 1234
    pool.list_locations()
    location_group_id = 3
    # pool.create('testPooling', location_group_id, account_id)
    pool.list_pools()
    pool_id = 123456
    # pool.edit_name(pool_id, 'PoolUpdateTest')
    pool.get_pool(pool_id)
    # pool.cancel(pool_id)
    pool.list_pool()
    add_servers_ids = [12345] # Hardware Ids to add 
    del_servers_ids = [] # Hardware Ids to remove 
    add_guests_ids = [12345] # Virtual Guest Ids to add 
    del_guests_ids = [] # Virtual Guests Ids to remove

    pool.update(pool_id,
                add_hardware=add_servers_ids,
                del_hardware=del_servers_ids,
                add_guest=add_guests_ids,
                del_guest=del_guests_ids)
    pool.list_available_servers(pool_id)
    pool.get_virtual_rack()
    pool.list_locations()
    pool.get_pool_details(pool_id)
    pool.debug()

```