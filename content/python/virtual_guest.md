---
title: "Working with Virtual Guests"
description: "A variety of examples on getting information from Virtual Guest Objects"
date: "2020-07-02"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "vsi"
    - "virtualguest"
aliases:
    - /python/create_server_simplified.py
    - /python/create_virtual_guest_with_tags
---



## Example Framework

For these examples, the following class structure will be used. Since most of these examples will share a lot of the initialization code, this class will help reduce the noise level.

All these examples will have a function definition that can simply be added to the `example` class and run with a call from the `if __name__ == "__main__":` block.

```python
import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):
        """Sets up the SoftLayer client, and debugger client"""
        self.client = SoftLayer.Client()
        # Sets up the SoftLayer debugger, allowing for more verbose output.
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.client.transport = debugger

    def main(self, vsi):
        """Gets the vsi Object"""
        vsi = self.client.call('Virtual_Guest', 'getObject', id=vsi)
        pp(vsi)

    def debug(self):
        """Iteratess through all class made in this session"""
        for call in self.client.transport.get_last_calls():
            print(self.client.transport.print_reproduceable(call))

if __name__ == "__main__":
    main = example()
    vsi = 123465
    main.main(vsi)
    # Add any functions you need to call below.

```

## Simple Create
This example calls [SoftLayer_Virtual_Guest::generateOrderTemplate()](/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate/) to ensure the [SoftLayer_Virtual_Guest](/reference/datatypes/SoftLayer_Virtual_Guest/) template object you created is valid.

From there you can pass the same template to [SoftLayer_Virtual_Guest::createObject()](/reference/services/SoftLayer_Virtual_Guest/createObject/) and a new virtual guest will be created. The only limitation here is that some options are not available with [SoftLayer_Virtual_Guest::createObject()](/reference/services/SoftLayer_Virtual_Guest/createObject/), namely adding IPv6 addresses.

To get the options avaliable for Virtual Guest creation, see [SoftLayer_Virtual_Guest::getCreateObjectOptions](/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions/)

When creating a templateObject, don't set `startCpus` and `maxMemory` fields, these are legacy options, use `supplementalCreateObjectOptions->flavorKeyName` to select how much RAM/CPU the new VSI will have.

```python
templateObject = {
    # The name of the server
    "hostname": "host1",  
    # The domain for the server
    "domain": "example.com",  
     # Specifies the billing type for the server.
    "hourlyBillingFlag": True, 
    # An identifier for the operating system to provision the server with.
    "operatingSystemReferenceCode": "UBUNTU_LATEST",  
    # Specifies which datacenter the server is to be provisioned in.
    "datacenter": {"name": "dal10"},
    # Sets metadata, optional.
    "userData": [{"value": "someValue"}],
    "supplementalCreateObjectOptions": {
        "flavorKeyName": "B1_1X2X100" # list from createObjectOptions
    }
}
    def getCreateOptions(self):
        """Prints out the options available for creating virtual guests"""
        create_options = self.client.call('SoftLayer_Virtual_Guest', 'getCreateObjectOptions')
        pp(create_options)

    def verifyObject(self, templateObject):
        """Pass in a templateObject, defined above, to test if it is valid."""
        try:
            receipt = self.client.call(
                'SoftLayer_Virtual_Guest', 'generateOrderTemplate',
                templateObject
            )
            pp(receipt)
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to verify VSI. {} {}".format(e.faultCode, e.faultString))
    def createObject(self, templateObject):
        """Pass in a templateObject, defined above, to actually create a VSI."""
        try:
            receipt = self.client.call(
                'SoftLayer_Virtual_Guest', 'createObject',
                templateObject
            )
            pp(receipt)
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to create VSI. {} {}".format(e.faultCode, e.faultString))
```

`getCreateOptions` has a lot of irrelevant output, and trimming that out takes a bit of code to complete that gets in the way of this example. See [SoftLayer/CLI/virt/create_options.py](https://github.com/softlayer/softlayer-python/blob/master/SoftLayer/CLI/virt/create_options.py) for how the SLCLI handles the output.

SLCLI also has this as a command feature. See  [`slcli vs create`](https://softlayer-python.readthedocs.io/en/latest/cli/vs/#virtual-create) and [`slcli vs create-options`](https://softlayer-python.readthedocs.io/en/latest/cli/vs/#virtual-create-options)


## Add tags

Tags cannot be set at create time, they can only be added after a VSI has been provisioned, or at least gotten an `id`.

[SoftLayer_Virtual_Guest::setTags()](/reference/services/SoftLayer_Virtual_Guest/setTags/) will either return `True`, or an `Exception`.

```python

    def tagGuest(self, vsi_id, tags="default, tags, csv formatted"):
        """Adds tags to vsi_id"""
        try:
            self.client.call('SoftLayer_Virtual_Guest', 'setTags',
                             tags, id=vsi_id)
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to tag {}, {} {}".format(e.faultCode, e.faultString))
```


## Edit Details

Occasionally you will want to change some of the details of a server, like its hostname, or notes for example. This can be don with [SoftLayer_Virtual_Guest::editObject()](/reference/services/SoftLayer_Virtual_Guest/editObject/)


```python
# A Virtual_Guest object. Not all fields are changeable.
objectTemplate = {
    'hostname': 'myhostnameEdited',
    'notes': 'edited from api'
}

    def editGuest(self, vsi_id, objectTemplate):
        try:
            result = self.client.call('SoftLayer_Virtual_Guest', 'editObject',
                                      objectTemplate, vsi_id)
            pp(result)
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to edit {}, {} {}".format(vsi_id, e.faultCode, e.faultString))
```

## Set Port Speed

Usually changing the port speed is used to disable or enable an interface.  Speed values can only be 0 (Disconnect), 10, 100, or 1000. The new speed must be equal to or less than the max speed of the interface. If you want to increase the speed to a higher limit than was ordered, that will require an upgrade order for the virtual guest.

[setPublicNetworkInterfaceSpeed](/reference/services/SoftLayer_Virtual_Guest/setPublicNetworkInterfaceSpeed/) and p(/reference/services/SoftLayer_Virtual_Guest/setPrivateNetworkInterfaceSpeed/) both will return `True` on success, or an `Exception` on a failure.

```python
    def setPortSpeed(self, vsi_id, speed=0, public=False, private=False):
        """Sets vsi public and/or private interfaces to speed"""
        if public:
            try:
                self.client.call(
                    'SoftLayer_Virtual_Guest', 'setPublicNetworkInterfaceSpeed',
                    speed, id=vsi_id)
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to set public interface on {} to {}, {} {}".format(
                vsi_id, speed, e.faultCode, e.faultString))            
        if private:
            try:
                self.client.call(
                    'SoftLayer_Virtual_Guest', 'setPrivateNetworkInterfaceSpeed',
                    speed, id=vsi_id)
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to set private interface on {} to {}, {} {}".format(
                vsi_id, speed, e.faultCode, e.faultString))          
```


## Getting all Virtual Guests

This example will get a listing of all the Virtual Guests on your account, with an option to filter that result by hostname.

`iter=True` in the API call will return a python generator, and automatically [paginate](https://softlayer-python.readthedocs.io/en/latest/api/client/#making-api-calls) through the results. Especially useful for accounts with a long list of guests.

```python

    def listGuets(self, hostname='not null'):
        """Gets all virtual guests, with optional hostname filter"""
        filterInstance = {'virtualGuests': {'host':{'operation':hostname}}}
        objectMask = "mask[location]"
        instances = self.client.call('SoftLayer_Account', 'getVirtualGuests', iter=True, filter=filterInstance, mask=objectMask)
        pp(instances)

```


## Find Upgrade Prices

Print out the available upgrades a Virtual Guest can order.

[SoftLayer_Virtual_Guest::getUpgradeItemPrices()](/reference/services/SoftLayer_Virtual_Guest/getUpgradeItemPrices/) This method exclude downgrade item prices by default. You can set the “includeDowngradeItemPrices” parameter to true so that it can include downgrade item prices.

```python
    def getUpgrades(self, vsi_id):
        """Gets available upgrades and downgrades for vsi_id"""
        upgrades = self.client.call('SoftLayer_Virtual_Guest', 'getUpgradeItemPrices', True, id=vsi_id)
        pp(upgrades)
```


## Power Management

The following API calls exist for power management, and they all are called simply by passing in the VSI id you want to deal with. the `Soft` commands will send a signal to the OS to reboot safely. Where the `Hard` command will forcefully shut down the VSI.

- [Power On](/reference/services/SoftLayer_Virtual_Guest/powerOn/)
- [Power Off](/reference/services/SoftLayer_Virtual_Guest/powerOff/)
- [Power Off Soft](/reference/services/SoftLayer_Virtual_Guest/powerOffSoft/)
- [Power Cycle](/reference/services/SoftLayer_Virtual_Guest/powerCycle)
- [Reboot Soft](/reference/services/SoftLayer_Virtual_Guest/rebootSoft/)
- [Reboot Hard](/reference/services/SoftLayer_Virtual_Guest/rebootHard/)
- [Pasue](/reference/services/SoftLayer_Virtual_Guest/pause)
- [Resume](/reference/services/SoftLayer_Virtual_Guest/resume)

These methods will all either return `True`, or an Exception if something prevented a Guest from changing power state. If you get an exception, try with a more forceful command. `RebootHard` instead of `rebootSoft`, or `powerOff` instead of `RebootHard`. If that still doesn't work, a support ticket will need to be created for support to investigate why the Guest is in a stuck state.

```python
    def rebootGuest(self, vsi_id, force=False):
        try:
            if force:
                self.client.call('SoftLayer_Virtual_Guest', 'rebootHard')
            else:
                self.client.call('SoftLayer_Virtual_Guest', 'rebootSoft')
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to reboot {}, {} {}".format(
                vsi_id, e.faultCode, e.faultString))  

    def powerGuest(self, vsi_id, powerOff=False):
        try:
            if powerOff:
                self.client.call('SoftLayer_Virtual_Guest', 'powerOff')
            else:
                self.client.call('SoftLayer_Virtual_Guest', 'powerOn')
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to power  {}, {} {}".format(
                vsi_id, e.faultCode, e.faultString))  
```


## Reload Guest

If you ever need to get the VSI to a clean, newly provisioned state, issue a [OS reload](/reference/services/SoftLayer_Virtual_Guest/reloadCurrentOperatingSystemConfiguration).


```python
    def reloadOS(self, vsi_id):
        """Performs a simple OS reload, no changes"""
        try:
            self.client.call('SoftLayer_Virtual_Guest', 'reloadCurrentOperatingSystemConfiguration', id=vsi_id)
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to reload  {}, {} {}".format(
                vsi_id, e.faultCode, e.faultString))        
```