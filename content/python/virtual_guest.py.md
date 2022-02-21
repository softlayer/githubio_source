---
title: "More Virtual Guest Examples"
description: "A few examples on interacting with Virtual Guest"
date: "2020-07-09"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
tags:
    - "vsi"
    - "virtualguest"
---

### Create Virtual Server

Creation of computing instances on an account. 
This method is a simplified alternative to interacting with the ordering system directly.

```python
import SoftLayer
import json

client = SoftLayer.Client()
virtualGuestService = client['SoftLayer_Virtual_Guest']

# The order template for the new virtual guest
# See getCreateObjectOptions for available options
order = {
    "hostname": "dedisim2",
    "domain": "example.com",
    "blockDevices": [
        {
            "device": "0",
            "diskImage": {
                "capacity": 25
            }
        }
    ],
    "hourlyBillingFlag": true,
    "localDiskFlag": false,
    "datacenter": {
        "name": "dal13"
    },
    "dedicatedHost": {
        "id": 9301
    },
    "operatingSystemReferenceCode": "UBUNTU_LATEST",
    "supplementalCreateObjectOptions": {
        "flavorKeyName": "AC1_8X60X25"
    }
}

try:
    response = virtualGuestService.createObject(order)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to place the order. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```

### Create a virtual server and attach Security Groups

Creates a new virtual server (VSI) and attach the public and private interfaces to respective Security Groups.

```python
from __future__ import print_function
import SoftLayer
from SoftLayer.managers.vs import VSManager

def create_vsi():
    client = SoftLayer.Client()
    vsi_mgr = VSManager(client)

   # common values
    datacenter = 'wdc07' 
    domain = 'cde.services' 
    os_code = 'UBUNTU_LATEST_64'
    local_disk = False
    hourly = True 
    dedicated = False 
    nic_speed = 1000 
    private = False 
    ssh_keys = [972047] 
    public_security_groups = [43507]
    private_security_groups = [43511]

    # server properties
    hostname = 'sgvsi'
    flavor = 'BL1_1X2X100'

    result = vsi_mgr.create_instance(hostname=hostname, domain=domain,
                                     flavor=flavor, datacenter=datacenter,
                                     os_code=os_code, local_disk=local_disk,
                                     hourly=hourly, dedicated=dedicated,
                                     disks=disks, nic_speed=nic_speed, private=private,
                                     ssh_keys=ssh_keys, public_security_groups=public_security_groups,
                                     private_security_groups=private_security_groups)
    print(result)

if __name__ == '__main__':
    create_vsi()
```

### Get Virtual Server Details

Retrieve a SoftLayer_Virtual_Guest record.

```python
import SoftLayer

# For nice debug output:
from pprint import pprint as pp

# Set the server id that you wish to get details.
# Call the getVirtualGuests method from SoftLayer_Account
serverId = 35747489

# Retrieve the wanted server information using a mask
mask = "mask[id, fullyQualifiedDomainName, operatingSystem[passwords], networkComponents, datacenter," \
       "billingItem[id, item[id, description], category[name, id],children[id, item[id, description], " \
       "category[name, id]]]]"
       
# Make a connection to the Virtual_Guest service.
client = SoftLayer.Client()

try:
    # Make the call to retrieve the server details.
    virtualGuestDetails = client['Virtual_Guest'].getObject(id=serverId,
                                                    mask=mask)
    pp(virtualGuestDetails)

except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to get the Virtual Guest infomrmation faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))
```

### Month to date cost of a Virtual Server

Determine the month-to-date cost of an hourly Virtual_Guest using getBillingItem.

```python
import SoftLayer
from pprint import pprint as pp

client = SoftLayer.Client()
mask = "mask[createDate,hoursUsed,hourlyRecurringFee,currentHourlyCharge]"

try:
    serverCost = client['SoftLayer_Virtual_Guest'].getBillingItem(mask=mask,id=1234567)
    pp(serverCost)

except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to get the Virtual Guest infomrmation faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```

### Get Virtual Console Virtual Guest

Retrieve the IP, username, and password needed to access the KVM console for a Virtual Guest.

```python
import SoftLayer
from pprint import pprint as pp

client = SoftLayer.Client()

mask = "mask[consoleIpAddressRecord[ipAddress[ipAddress],port],operatingSystem[passwords]]"

getDetails = client['SoftLayer_Virtual_Guest'].getObject(mask=mask,id=31678643)
pp(getDetails)
```

### View Monitoring Closed Alarms

Returns closed monitoring alarms for a given time period.

```python
import SoftLayer
import json

vsiIp = "169.45.98.148"

startDate = "2000-01-01"
endDate = "2016-12-22"

client = SoftLayer.Client()
vsiService = client['SoftLayer_Virtual_Guest']

try:
    vsi = vsiService.findByIpAddress(vsiIp)
    if not vsi:
        print("There is no a vsi with the IP address: " + vsiIp)
        exit(1)
    result = vsiService.getMonitoringClosedAlarms(startDate, endDate, id=vsi['id'])
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to view the closed alarms:  faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```

### View Monitoring Active Alarms

Returns open monitoring alarms for a given time period.

```python
import SoftLayer
import json

vsiIp = "169.45.98.148"

startDate = "2000-01-01"
endDate = "2016-12-22"

client = SoftLayer.Client()
vsiService = client['SoftLayer_Virtual_Guest']

try:
    vsi = vsiService.findByIpAddress(vsiIp)
    if not vsi:
        print("There is no a vsi with the IP address: " + vsiIp)
        exit(1)
    result = vsiService.getMonitoringActiveAlarms(startDate, endDate, id=vsi['id'])
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to view the active alarms: faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```

### Reload current OS configuration

Create a transaction to perform an OS reload.

```python
import SoftLayer
from pprint import pprint as pp

# Set the server id that you wish to reload.
serverId = 35747489

# Create a SoftLayer Client.
client = SoftLayer.Client()

# Reload the Virtual Guest
try:
    # Make the call to reload the server.
    result = client['Virtual_Guest'].reloadCurrentOperatingSystemConfiguration(
        id=serverId)
    pp(result)

except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to reload the server faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```

### Set Tags Virtual Server

```python
import SoftLayer

# the virtual guest ID where you wish to add the tags
virtualGuestID = 35747489

# the tags you wish to add
tags = "tag1,tag2,tag3"

client = SoftLayer.Client()
virtualGuestService = client['SoftLayer_Virtual_Guest']

try:
    result = virtualGuestService.setTags(tags, id=virtualGuestID)
    print (result)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to set the tags"
          % (e.faultCode, e.faultString))

```

### Search Virtual Server tag

The script retrieve all the VSIs which contain an arbitrary list of tags.

```python
import SoftLayer.API
from pprint import pprint as pp

# List of tags to look for
tags = ["mytag1", "tag2"]

# Declare the API client
client = SoftLayer.Client()
accountService = client['SoftLayer_Account']

# Declaring an object filter to get only the virtual servers which contain the tags that we are looking for
objectFilter = {'virtualGuests': {'tagReferences': {'tag': {'name': {'operation': 'in', 'options': [{'name': 'data', 'value': tags}]}}}}}

# Send the request to get the virtual guest using the filter
try:
    result = accountService.getVirtualGuests(filter=objectFilter)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the virtual guests faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```

### Retrieve Metadata

Retrieves the user data for the VSIs in the account

The script gets the user metadata for a VSI in the account we make a simple call the getVirtualGuests() in the 
SoftLayer_Virtual_Guest API service and we set an object mask to get the information about the user data.

```python
import SoftLayer

# Declaring the API client
client = SoftLayer.Client()
accountService = client['SoftLayer_Account']

# Adding the object mask to the call to get the information about the user data.
objectMask = "mask[userData]"

try:
    # Retrieving our account's VSI records.
    result = accountService.getVirtualGuests(mask=objectMask)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the tags faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```

### Reboot Virtual Guest

It reboots a SoftLayer Virtual Guest

```python
import SoftLayer
from pprint import pprint as pp

# If you don't know your server id you can call getVirtualGuests() in the
# SoftLayer_Account API service to get a list of Virtual Guests
serverId = 35747489

# Create a connection to API service.
client = SoftLayer.Client()

# Reboot the Virtual Guest
try:

    result = client['Virtual_Guest'].rebootDefault(id=serverId)
    pp(result)

except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to reboot the server faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```

### Get Virtual Server Notes

The script retrieves the notes for an arbitrary VSI, it makes a single call to  SoftLayer_Virtual_Guest::getObject 
method.

```python
import SoftLayer

#Declare variables
virtualGuestId = 35747489

# Declare the API client
client = SoftLayer.Client()
virtualServer = client['SoftLayer_Virtual_Guest']

try:
    result = virtualServer.getObject(id=virtualGuestId)
    print (result['notes'])
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to get the notes. "
          % (e.faultCode, e.faultString))

```
