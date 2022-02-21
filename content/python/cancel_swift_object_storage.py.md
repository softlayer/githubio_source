---
title: "Cancel all object storage swift"
description: "Cancel all object storage swift"
date: "2019-05-14"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Network_Storage"
tags:
    - "billing"
    - "account"
    - "objectstorage"
    - "swift"
---

### List, delete, deleteAll Object Storage Swift Volumes 

This script do the following:

List all swift object storage volumes.
Delete an object storage swift.
Delete all object storage swift.

To run this script, you can use any terminal,
Run the following python followed by the file.py:

c:> python cancel_object_storage.py

```python

import SoftLayer
import click
from SoftLayer.CLI import exceptions
from SoftLayer.utils import clean_time
from prettytable import PrettyTable


@click.group()
def cli():
    """Object Storage volumes."""


@cli.command('list', short_help='List all object storage swift volumes')
def list():
    """List all swift object storage volumes."""

    table = PrettyTable(['id', 'username', 'capacityGb', 'createDate', 'ApiType'])
    storage_list = Storage()._list_swift_volumes()

    for data in storage_list:
        table.add_row([
            data['id'],
            data['username'],
            data['capacityGb'],
            clean_time(data['createDate']),
            data['vendorName'],
        ])

    print(table)


@cli.command('delete', short_help='delete an object storage volume')
@click.argument('identifier')
def delete(identifier):
    """Delete a object storage volume."""
    storage_id = Storage().delete_swift_volume(identifier)
    print(storage_id)


@cli.command('deleteAll', short_help='delete all object storage swift volumes')
def delete():
    """Delete all object storage swift volumes."""
    Storage().delete_all_swift_volumes()


class Storage(object):

    def __init__(self):
        client = SoftLayer.create_client_from_env()
        self.account_service = client['SoftLayer_Account']
        self.storage_service = client['SoftLayer_Network_Storage']
        self.billing_service = client['SoftLayer_Billing_Item']

    def _list_swift_volumes(self):
        _filter = {
            'hubNetworkStorage': {'vendorName': {'operation': 'Swift'}},
        }
        mask = 'mask[id,capacityGb,createDate,username,vendorName]'
        response = self.account_service.getHubNetworkStorage(mask=mask, filter=_filter)

        return response

    def delete_swift_volume(self, identifier):

        storage_response = self.storage_service.getObject(mask='mask[id,billingItem[id]]', id=identifier)
        response = self.billing_service.cancelItem(id=storage_response['billingItem']['id'])

        return response

    def delete_all_swift_volumes(self):
        _filter = {
            'hubNetworkStorage': {'vendorName': {'operation': 'Swift'}},
        }
        mask = 'mask[id,capacityGb,createDate,vendorName,billingItem[id]]'
        storage_response = self.account_service.getHubNetworkStorage(mask=mask, filter=_filter)

        for volume in storage_response:
            billing_response = self.billing_service.cancelItem(id=volume['billingItem']['id'])
            if not billing_response:
                raise exceptions.CLIAbort("This object storage was not deleted" + str(volume['billingItem']['id']))

        print("All object storage swift volumes were deleted")


if __name__ == '__main__':
    cli()

```
