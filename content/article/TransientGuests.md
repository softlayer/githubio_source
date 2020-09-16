---
title: "Transient Guests"
description: "Examples on how to create Transient guests, and working with web hooks."
date: "2020-01-15"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualguest"
    - "transient"
    - "ordering"
---


# Introduction

If you are not familiar with the basics of Transient Guests, please see the following documentation.

- [Transient virtual servers](https://cloud.ibm.com/docs/vsi?topic=virtual-servers-about-vs-transient)
- [Configuring notifications for reclaims of transient virtual servers](https://cloud.ibm.com/docs/vsi?topic=virtual-servers-configuring-notifications-for-reclaims-of-transient-virtual-servers)

This article will show how to use the SoftLayer-Python library to create a Transient Guest with [SoftLayer_Virtual_Guest::createObject()](https://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject/), set the webhook URI with [SoftLayer_Virtual_Guest::setTransientWebhook()](https://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/setTransientWebhook/), and how to test it with [SoftLayer_Virtual_Guest::sendTestReclaimScheduledAlert()](https://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/sendTestReclaimScheduledAlert/). Not covered is how to do something useful with the data received, that is left as an exercise for the reader.


## Example Setup

To start off, I like to use the following example format. We start with a class, and add methods to it for various actions we need to take. The python file will have a `if __name__ == "__main__":` block so that it can be executed as a shell script for easy testing. At the end of the article will be the full file. Each section will break down what is going on with each function of the class.

```python
import SoftLayer
from pprint import pprint as pp
import random
import string

class transient():

    def __init__(self):
        """Init the SoftLayer Client.
        
        the debugger part lets you easily reproduce the exact API calls made.
        """
        self.client = SoftLayer.Client()
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.client.transport = debugger

    def debug(self):
        for call in self.client.transport.get_last_calls():
            print(self.client.transport.print_reproduceable(call))

    def randomString(self, stringLength=10):
        """Generate a random string of fixed length.
        
        I use this to make random hostnames.
        """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

if __name__ == "__main__":
    main = transient()
    main.debug()
```


# Order Options

This example will showcase how to create a Virtual Guest with the createObject method. For more information on the details about ordering the following might also be helpful [Ordering examples](https://sldn.softlayer.com/tags/ordering/).


The following methods will print out some of the basic options for creating a new transient guest. 

```python
    def printFlavors(self, flavors):
        """Flavors need to have the attribute transientGuestFlag == True"""
        print("====== FLAVORS ======")
        print("Flavor, Hourly Cost")
        for option in flavors:
            if option['template'].get('transientGuestFlag', False):
                flavor = option['flavor']
                print("{}, {}".format(flavor['keyName'], flavor['totalMinimumHourlyFee']))

    def printOS(self, operatingSystems):
        """Only list operating systems billed hourly"""
        print("====== OPERATING SYSTEMS ======")
        print("KeyName, Description, Cost")
        for option in operatingSystems:
            if option['itemPrice'].get('hourlyRecurringFee', False):
                print("{}, {}, {}".format(
                    option['template']['operatingSystemReferenceCode'],
                    option['itemPrice']['item']['description'],
                    option['itemPrice']['hourlyRecurringFee']
                ))

    def printDisk(self, disks):
        """Disks with device == 2 are the ones that can be ordered as additional disks

        disk 0 is primary
        disk 1 is SWAP
        """
        print("====== Disks ======")
        print("Size, Cost")
        for option in disks:
            device = option['template']['blockDevices'][0]['device'] 
            if device == "2" and not option['itemPrice'].get('dedicatedHostInstanceFlag', False):
                print("{}, {}".format(
                    option['itemPrice']['item']['description'], 
                    option['itemPrice']['hourlyRecurringFee']

```


### Output

```text
Calling: SoftLayer_Virtual_Guest::getCreateObjectOptions(id=None, mask='', filter='None', args=(), limit=None, offset=None))
====== OPERATING SYSTEMS ======
KeyName, Description, Cost
CENTOS_LATEST, CentOS - Latest, 0
CENTOS_LATEST_64, CentOS - Latest (64 bit), 0
CENTOS_7_64, CentOS 7.x - Minimal Install (64 bit), 0
====== FLAVORS ======
Flavor, Hourly Cost
B1_1X2X25, 0.0133
B1_1X2X100, 0.0293
B1_1X4X25, 0.0208
====== Disks ======
Size, Cost
10 GB (SAN), .007
20 GB (SAN), .009
25 GB (SAN), .01
```

### REST API Call

```bash
curl -u $SL_USER:$SL_APIKEY  'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/getCreateObjectOptions.json'
```

# Creation
Given how many options there are for creating guests, it is challenging to make an easy to read example, but hopefully this helps. I highly recommend using the build in [VSManager.order_guest()](https://softlayer-python.readthedocs.io/en/latest/api/managers/vs/#SoftLayer.managers.vs.VSManager.order_guest) method as that is a little more flexible. This example does basically the same thing though, just hard-coded a bit to be more readable.

```python
    def createTransient(self, hostname, webhook_uri, secret):
        """Creates a transient guest

        This example directly uses SooftLayer_Virtual_Guest::createObject, but using VSManager.order_guest()
        might be easier for most users.
        https://softlayer-api-python-client.readthedocs.io/en/latest/api/managers/vs/#SoftLayer.managers.vs.VSManager.order_guest
        """

        domain = 'ibm.com' # pick a domain
        datacenter = 'dal13' # pick a dc
        os_keyname = 'UBUNTU_LATEST_64' # from options in printOS
        pub_network_vlan_id = 12345
        pub_subnet_id = 54321
        pri_network_vlan_id = 112233
        pri_subnet_id = 332211
        sg_allow_all_tcp_id = 999999
        sg_allow_all_udp_id = 888888
        post_install_uri = 'https://pastebin.com/raw/62wrEKuW' # needs to be https to be executed
        flavor_keyname = 'C1_1X1X100' # from printFlavors
        ssh_keys = [{'id':7777777}] # ID of sshkey

        # https://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest/
        template = {
            'hostname': hostname,
            'domain': domain,
            'datacenter': {'name':datacenter}, 
            'hourlyBillingFlag': True, # Has to be True for transient
            'operatingSystemReferenceCode': os_keyname,
            'networkComponents': [{'maxSpeed':1000}], # 10, 100, 1000
            'blockDevices': [
                {'device': 2, 'diskImage': {'capacity': 30}} # optional additional disks.
            ],
            'sshKeys': ssh_keys,  # optional
            # https://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_SupplementalCreateObjectOptions/
            'supplementalCreateObjectOptions': {
                'flavorKeyName': flavor_keyname,
                'postInstallScriptUri':  post_install_uri  # optional
            },
            'transientGuestFlag': True,
            'primaryBackendNetworkComponent' : { # optional
                'networkVlan': {'id': pri_network_vlan_id, 'primarySubnet': {'id': pri_subnet_id}}
            },
            'primaryNetworkComponent': { # optional
                'networkVlan': {'id': pub_network_vlan_id, 'primarySubnet': {'id': pub_subnet_id}},
                'securityGroupBindings': [ # optional
                    {'securityGroup': {'id': sg_allow_all_tcp_id}}, {'securityGroup': {'id': sg_allow_all_udp_id}}
                ]
            },
            'userData': [{'value':"Just some random data, you can put anything here you want!"}] # optional
        }

        result = self.client.call('SoftLayer_Virtual_Guest', 'createObject', template)
        pp(result)
        # Webhook HAS to be set AFTER the guest is created.
        self.setWebHook(result['id'], webhook_uri, secret)
        return result
```

### REST API Call

```bash
# Virtual_Guest::createObject
curl -u $SL_USER:$SL_APIKEY -X POST -d \ 
'{"parameters": [{"hostname": "TRXcgezuyxunytl", "domain": "ibm.com", "datacenter": {"name": "dal13"}, "hourlyBillingFlag": true, "operatingSystemReferenceCode": "UBUNTU_LATEST_64", "networkComponents": [{"maxSpeed": 1000}], "blockDevices": [{"device": 2, "diskImage": {"capacity": 30}}], "sshKeys": [{"id": 87634}], "supplementalCreateObjectOptions": {"flavorKeyName": "C1_1X1X100", "postInstallScriptUri": "https://pastebin.com/raw/62wrEKuW"}, "transientGuestFlag": true, "primaryBackendNetworkComponent": {"networkVlan": {"id": 2068355, "primarySubnet": {"id": 1509335}}}, "primaryNetworkComponent": {"networkVlan": {"id": 2068353, "primarySubnet": {"id": 1499537}}, "securityGroupBindings": [{"securityGroup": {"id": 128323}}, {"securityGroup": {"id": 128321}}]}, "userData": [{"value": "Just some random data, you can put anything here you want!"}]}]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/createObject.json'

# Virtual_Guest::setTransientWebhook
curl -u $SL_USER:$SL_APIKEY -X POST -d \
'{"parameters": ["http://169.62.147.163/tesdfdsfst", "MySecret123"]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/95433052/setTransientWebhook.json'
```


# Web Hooks

The webhook has two parts. The URI, and the Secret. The URI is simply the location to send the cancellation notification. The Secret is used to create a Authorization Header hash so you can verify it was IBM Cloud who sent you the notification.


```python
    def setWebHook(self, guest_id, url, secret):
        """Sets the webhook"""
        self.client.call('SoftLayer_Virtual_Guest', 'setTransientWebhook', url, secret, id=guest_id)

    def getWebHook(self, guest_id):
        result = self.client.call('SoftLayer_Virtual_Guest', 'getTransientWebhookURI', id=guest_id)
        pp(result)

    def delWebHook(self, guest_id):
        result = self.client.call('SoftLayer_Virtual_Guest', 'deleteTransientWebhook', id=guest_id)
        pp(result)

    def testWebHook(self, guest_id):
        """Will send a test reclaim message to the TransientWebhookURI

        SoftLayer_Virtual_Guest::sendTestReclaimScheduledAlert return None
        """
        try:
            self.client.call('SoftLayer_Virtual_Guest', 'sendTestReclaimScheduledAlert', id=guest_id)
        except SoftLayer.exceptions.SoftLayerAPIError:
            print("{} doesn't have a webhook set!".format(guest_id))
```

### The Cancellation Notification
When you make an API call to `sendTestReclaimScheduledAlert`, OR the transient Virtual Guest is reclaimed, a HTTP request will get sent to the TransientWebhookURI. That request will look something like this:

Here I'm using [nc](https://en.wikipedia.org/wiki/Netcat) to catch the requests.
```bash
# nc -lk 0.0.0.0 80
POST /tesdfdsfst HTTP/1.1
Host: 169.62.147.163
Content-Type: application/json
User-Agent: IBM Cloud Webhook Service
Authorization: AAAAAAA11111111111111111111111yNzMwNjA4YjAwMjU0MjUzM2MwMGE1MjljOTAxNDlkM2M1NjgyODdkYg==
X-IBM-Nonce: 111111116f3d430799139a0a28450000
Content-Length: 200

{"id":"95430736","serviceName":"SoftLayer_Virtual_Guest","event":"reclaim-scheduled-test","timestamp":1579124035,"link":"https:\/\/api.softlayer.com\/rest\/v3\/SoftLayer_Virtual_Guest\/95430736.json"}
HEAD /robots.txt HTTP/1.0
```

Compared to a REAL reclaim event.
```bash
# nc -lk 0.0.0.0 80
POST /tesdfdsfst HTTP/1.1
Host: 169.62.147.163
Content-Type: application/json
User-Agent: IBM Cloud Webhook Service
Authorization: AAAAAAA11111111111111111111111yNzMwNjA4YjAwMjU0MjUzM2MwMGE1MjljOTAxNDlkM2M1NjgyODdkYg==
X-IBM-Nonce: 111111116f3d430799139a0a28450000
Content-Length: 222

{"id":"95433052","serviceName":"SoftLayer_Virtual_Guest_Citrix_XenServer_Version41","event":"reclaim-scheduled","timestamp":1579127296,"link":"https:\/\/api.softlayer.com\/rest\/v3\/SoftLayer_Virtual_Guest\/95433052.json"}
```


### REST API Calls

```bash
# Virtual_Guest::setTransientWebhook
curl -u $SL_USER:$SL_APIKEY -X POST  -d \
'{"parameters": ["http://169.62.147.163/tesdfdsfst", "MySecret123"]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/95433052/setTransientWebhook.json'

# Virtual_Guest::getTransientWebhookURI
curl -u $SL_USER:$SL_APIKEY \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/95433052/getTransientWebhookURI.json'

# Virtual_Guest::sendTestReclaimScheduledAlert
curl -u $SL_USER:$SL_APIKEY  \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/95433052/sendTestReclaimScheduledAlert.json'

# Virtual_Guest::deleteTransientWebhook
curl -u $SL_USER:$SL_APIKEY \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/95433052/deleteTransientWebhook.json'
```



# Full Example

```python
"""
@package examples 
@author Christopher Gallo

"""
import SoftLayer
from pprint import pprint as pp
import random
import string

class transient():

    def __init__(self):

        self.client = SoftLayer.Client()
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.client.transport = debugger


    def transientOptions(self):
        """
        Formats results from services/SoftLayer_Virtual_Guest::getCreateObjectOptions()
        """

        options = self.client.call('SoftLayer_Virtual_Guest', 'getCreateObjectOptions')
        self.printOS(options.get('operatingSystems'))
        self.printFlavors(options.get('flavors'))
        self.printDisk(options.get('blockDevices'))


    def printFlavors(self, flavors):
        print("====== FLAVORS ======")
        print("Flavor, Hourly Cost")
        for option in flavors:
            if option['template'].get('transientGuestFlag', False):
                flavor = option['flavor']
                print("{}, {}".format(flavor['keyName'], flavor['totalMinimumHourlyFee']))

    def printOS(self, operatingSystems):
        print("====== OPERATING SYSTEMS ======")
        print("KeyName, Description, Cost")
        for option in operatingSystems:
            if option['itemPrice'].get('hourlyRecurringFee', False):
                print("{}, {}, {}".format(
                    option['template']['operatingSystemReferenceCode'],
                    option['itemPrice']['item']['description'],
                    option['itemPrice']['hourlyRecurringFee']
                ))

    def printDisk(self, disks):
        print("====== Disks ======")
        print("Size, Cost")
        for option in disks:
            device = option['template']['blockDevices'][0]['device'] 
            if device == "2" and not option['itemPrice'].get('dedicatedHostInstanceFlag', False):
                print("{}, {}".format(
                    option['itemPrice']['item']['description'], 
                    option['itemPrice']['hourlyRecurringFee']
                ))

    def createTransient(self, hostname, webhook_uri, secret):
        """Creates a transient guest

        This example directly uses SooftLayer_Virtual_Guest::createObject, but using VSManager.order_guest()
        might be easier for most users.
        https://softlayer-api-python-client.readthedocs.io/en/latest/api/managers/vs/#SoftLayer.managers.vs.VSManager.order_guest
        """

        domain = 'ibm.com' # pick a domain
        datacenter = 'dal13' # pick a dc
        os_keyname = 'UBUNTU_LATEST_64' # from options in printOS
        pub_network_vlan_id = 12345
        pub_subnet_id = 54321
        pri_network_vlan_id = 112233
        pri_subnet_id = 332211
        sg_allow_all_tcp_id = 999999
        sg_allow_all_udp_id = 888888
        post_install_uri = 'https://pastebin.com/raw/62wrEKuW' # needs to be https to be executed
        flavor_keyname = 'C1_1X1X100' # from printFlavors
        ssh_keys = [{'id':87634}] # ID of sshkey

        # https://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest/
        template = {
            'hostname': hostname,
            'domain': domain,
            'datacenter': {'name':datacenter}, 
            'hourlyBillingFlag': True, # Has to be True for transient
            'operatingSystemReferenceCode': os_keyname,
            'networkComponents': [{'maxSpeed':1000}], # 10, 100, 1000
            'blockDevices': [
                {'device': 2, 'diskImage': {'capacity': 30}} # optional additional disks.
            ],
            'sshKeys': ssh_keys, 
            # https://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_SupplementalCreateObjectOptions/
            'supplementalCreateObjectOptions': {
                'flavorKeyName': flavor_keyname,
                'postInstallScriptUri':  post_install_uri 
            },
            'transientGuestFlag': True,
            'primaryBackendNetworkComponent' : {
                'networkVlan': {'id': pri_network_vlan_id, 'primarySubnet': {'id': pri_subnet_id}}
            },
            'primaryNetworkComponent': {
                'networkVlan': {'id': pub_network_vlan_id, 'primarySubnet': {'id': pub_subnet_id}},
                'securityGroupBindings': [
                    {'securityGroup': {'id': sg_allow_all_tcp_id}}, {'securityGroup': {'id': sg_allow_all_udp_id}}
                ]
            },
            'userData': [{'value':"Just some random data, you can put anything here you want!"}]
        }

        result = self.client.call('SoftLayer_Virtual_Guest', 'createObject', template)
        pp(result)
        # Webhook HAS to be set AFTER the guest is created.
        self.setWebHook(result['id'], webhook_uri, secret)
        return result
        


    def setWebHook(self, guest_id, url, secret):
        """Sets the webhook"""
        result = self.client.call('SoftLayer_Virtual_Guest', 'setTransientWebhook', url, secret, id=guest_id)
        pp(result)

    def getWebHook(self, guest_id):
        result = self.client.call('SoftLayer_Virtual_Guest', 'getTransientWebhookURI', id=guest_id)
        pp(result)

    def delWebHook(self, guest_id):
        result = self.client.call('SoftLayer_Virtual_Guest', 'deleteTransientWebhook', id=guest_id)
        pp(result)


    def testWebHook(self, guest_id):
        """Will send a test reclaim message to the TransientWebhookURI

        SoftLayer_Virtual_Guest::sendTestReclaimScheduledAlert return None
        """
        try:
            self.client.call('SoftLayer_Virtual_Guest', 'sendTestReclaimScheduledAlert', id=guest_id)
        except SoftLayer.exceptions.SoftLayerAPIError:
            print("{} doesn't have a webhook set!".format(guest_id))


    def debug(self):
        for call in self.client.transport.get_last_calls():
            print(self.client.transport.print_reproduceable(call))

    def randomString(self, stringLength=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

if __name__ == "__main__":
    webhook_uri = 'http://169.62.147.163/tesdfdsfst'
    secret = 'MySecret123'
    hostname = "TRX{}".format(main.randomString(12))
    
    main = transient()
    main.transientOptions()
    
    guest = main.createTransient(hostname, webhook_uri, secret)
    guest_id = guest['id']

    main.setWebHook(guest_id, webhook_uri, secret)
    main.getWebHook(guest_id)
    main.testWebHook(guest_id)
    main.debug()
```
