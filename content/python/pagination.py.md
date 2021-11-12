---
title: "Pagination Examples"
description: "A collection of examples on how to properly get large listings of objects from the SoftLayer API using Pagination,
    Python iterators, and objectFilters."
date: "2021-11-12"
classes: 
    - "SoftLayer_Account"
tags:
    - "pagination"
---

When querying the SoftLayer API and using a resultLimit to paginate your results, you should almost always use an `OrderBy` [objectFilter](/article/object-filters/) to sort your results, as by default most results will not have an order imposed on them by the database. It is fairly common for the database to have differeing orders between queries UNLESS an `OrderBy` filter is used.

The python client itself has a built in function called [`iter_call`](https://softlayer-python.readthedocs.io/en/latest/api/client/#SoftLayer.API.BaseClient.iter_call) which will return a python [generator](https://wiki.python.org/moin/Generators). This generator will only get the next set of results when you need them, which can make doing operations on large datasets feel faster in that you don't have to wait for the entire dataset to be retrieved before obtaining some results.


## [The Setup](#the-setup) {#the-setup .anchor-link}

To avoid having to type the boiler-plate code a lot, assume each of these example function will be a member function of the following `Paginator` class

```python
import SoftLayer

class Paginator():

    def __init__(self):
        self.client = SoftLayer.create_client_from_env()
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.client.transport = debugger
        self.DESC = {
            "operation": "orderBy", 
            "options": [{
                "name": "sort", 
                "value": ["DESC"]
            }]
        }

if __name__ == "__main__":
    paginator = Paginator()
    # Then just call whichever function you want to run like this
    # paginator.list_servers()
```

## [A simple pagination example](#simple-example) {#simple-example .anchor-link}

```python

def list_servers(self):
    orderBy = {"hardware": {"id": self.DESC}}
    objectMask = "mask[id,hostname]"
    servers = self.client.iter_call('SoftLayer_Account', 'getHardware', filter=orderBy, mask=objectMask, limit=10)
    print("Id, Hostname")
    for server in servers:
        print("{}, {}".format(server.get('id'), server.get('hostname')))

```

## [List Users](#list_users) {#list_users .anchor-link}

```python
def list_users(self):
    orderBy = {"users": {"id": self.DESC}}
    objectMask = "mask[id,username]"
    users = self.client.iter_call('SoftLayer_Account', 'getUsers', filter=orderBy, mask=objectMask, limit=10)
    print("Id, Username")
    for user in users:
        print("{}, {}".format(user.get('id'), user.get('username')))
```

## [List Global Ips](#list_gips) {#list_gips .anchor-link}

```python
def list_global_ips(self):
    orderBy = {"globalIpRecords": {"id": self.DESC}}
    objectMask = "mask[ipAddress,destinationIpAddress[ipAddress,hardware[id,hostname], virtualGuest[id,hostname]]]"
    globalIps = self.client.iter_call('SoftLayer_Account', 'getGlobalIpRecords',
                                      filter=orderBy, mask=objectMask, limit=100)
    for globalIp in globalIps:
        ipAddress = globalIp.get('ipAddress', {})
        associatedHostname = ""
        # If the global IP is assigned somewhere, set the hostname its assigned to
        if globalIp.get('destinationIpAddress', None) is not None:
            if 'hardware' in globalIp['destinationIpAddress'].keys():
                associatedHostname = globalIp['destinationIpAddress']['hardware']['hostname']
            elif 'virtualGuest' in globalIp['destinationIpAddress'].keys():
                associatedHostname = globalIp['destinationIpAddress']['virtualGuest']['hostname']
            else:
                associatedHostname = globalIp['destinationIpAddress'].get('ipAddress')
        if associatedHostname != "":
            print("{} is assigned to {}".format(ipAddress.get('ipAddress'), associatedHostname))
        else:
            print("{} is unassigned".format(ipAddress.get('ipAddress')))
```

## [Invoices](#invoices) {#invoices .anchor-link}

```python

def invoices(self):
    """This method will go through ALL invoices on an account.

    The older an account is, the more invoices it will have, so queries like this must be split up. Otherwise
    you will get API errors or timeouts. Once we have the invoice ID, we can get each invoices details seperately
    which will greatly speed up this process
    """
    orderBy = {"invoices": {"id": self.DESC}}

    objectMask = "mask[id, createDate, statusCode]"
    invoices = self.client.iter_call("SoftLayer_Account", "getInvoices", filter=orderBy, mask=objectMask)
    print("Id, Date, Status, Total")
    for invoice in invoices:
        # For more detail about an invoice, you should use getInvoiceTopLevelItems
        invoice_detail = self.client.call("SoftLayer_Billing_Invoice", "getInvoiceTotalAmount",
                                          id=invoice.get('id'))
        date = SoftLayer.utils.clean_time(invoice.get('createDate'))
        print("{}, {}, {}, {}".format(invoice.get('id'), date, invoice.get('statusCode'), invoice_detail))
```

## [List Subnets](#list_subnets) {#list_subnets .anchor-link}

```python
def list_subnets(self):
    """Lists all subnets on an account

    Could also use `getPrivateSubnets` or `getPublicSubnets`
    """
    orderBy = {"subnets": {"id": self.DESC}}
    objectMask = """mask[id,networkIdentifier, cidr, subnetType, networkVlan[vlanNumber],
                         usableIpAddressCount, datacenter[name]]"""
    subnets = self.client.iter_call('SoftLayer_Account', 'getSubnets', filter=orderBy, mask=objectMask, limit=100)
    print("Id, Type, Network, Vlan, Usable IPs, Datacenter")
    for subnet in subnets:
        print("{}, {}, {}/{}, {}, {}, {}".format(
            subnet.get('id'),
            subnet.get('subnetType'),
            subnet.get('networkIdentifier'),
            subnet.get('cidr'),
            SoftLayer.utils.lookup(subnet, 'networkVlan', 'vlanNumber'),
            subnet.get('usableIpAddressCount'),
            SoftLayer.utils.lookup(subnet, 'datacenter', 'name')
        ))        

```